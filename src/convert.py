import os

import pandas as pd
import supervisely as sly
from cv2 import connectedComponents
from tqdm import tqdm


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/almaz/Downloads/malaria_segmentation"
    images_folder = "Giemsa stained images"
    masks_folder = "Ground truth images"
    batch_size = 30
    xlsx_file = "LifeStages.xlsx"

    df = pd.read_excel(os.path.join(dataset_path, xlsx_file))
    df = df[["imageName", "stage"]]
    df = df.set_index("imageName")
    image_names_to_stages_mapping = df.to_dict()["stage"]
    df = None

    def _parse_info_for_tags(image_name):
        trip = image_name.split(" ")[1]
        day = image_name.split(" ")[3]
        stage = image_names_to_stages_mapping[image_name]
        return trip, day, stage

    def _create_ann(image_name):
        labels = []
        file_name_only = os.path.splitext(image_name)[0]
        mask_name = file_name_only + "_GT.png"
        mask_path = os.path.join(dataset_path, masks_folder, mask_name)
        mask = sly.image.read(mask_path)
        height, width = mask.shape[:2]
        if sly.fs.file_exists(mask_path):
            mask_np = sly.imaging.image.read(mask_path)[:, :, 0]
            mask = mask_np == 255
            ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                curr_bitmap = sly.Bitmap(obj_mask)
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        trip, day, stage = _parse_info_for_tags(image_name)
        image_tags = [
            sly.Tag(stage_tag_meta, stage),
            sly.Tag(trip_tag_meta, trip),
            sly.Tag(day_tag_meta, day),
        ]
        return sly.Annotation(img_size=(height, width), labels=labels, img_tags=image_tags)

    obj_class = sly.ObjClass("malaria parasite", sly.Bitmap)

    stage_tag_meta = sly.TagMeta("stage", sly.TagValueType.ANY_STRING)
    trip_tag_meta = sly.TagMeta("trip", sly.TagValueType.ANY_STRING)
    day_tag_meta = sly.TagMeta("day", sly.TagValueType.ANY_STRING)
    tag_metas = [stage_tag_meta, trip_tag_meta, day_tag_meta]

    project_meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=tag_metas)

    project = api.project.create(workspace_id, project_name)
    dataset = api.dataset.create(project.id, "ds0")

    api.project.update_meta(project.id, project_meta.to_json())

    all_images = os.listdir(os.path.join(dataset_path, images_folder))

    pbar = tqdm(total=len(all_images), desc="Processing images")
    for batch_img_names in sly.batched(all_images, batch_size):
        batch_img_paths = [
            os.path.join(dataset_path, images_folder, img_name) for img_name in batch_img_names
        ]
        anns = [_create_ann(img_name) for img_name in batch_img_names]
        img_infos = api.image.upload_paths(dataset.id, batch_img_names, batch_img_paths)
        img_ids = [img_info.id for img_info in img_infos]
        api.annotation.upload_anns(img_ids, anns)

        pbar.update(len(batch_img_names))
    return project
