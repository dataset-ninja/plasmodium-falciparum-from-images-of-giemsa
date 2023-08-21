# https://www.kaggle.com/datasets/niccha/malaria-segmentation

import csv
import os
from collections import defaultdict

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely.io.fs import get_file_name, get_file_name_with_ext

# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "Malaria Segmentation"
    dataset_path = "APP_DATA/5bf2kmwvfn-1/"
    images_folder_name = "Giemsa stained images"
    masks_folder_name = "Ground truth images"
    ds_name = "ds"
    batch_size = 30
    masks_suffix = "_GT.png"
    data_classes_tags_path = "APP_DATA/5bf2kmwvfn-1/LifeStages.xlsx"
    data_classes_tags_path = "APP_DATA/5bf2kmwvfn-1/please_work.txt"

    def get_points_dist(coords1, coords2):
        return (coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2

    def create_ann(image_path):
        labels = []

        full_image_name = get_file_name_with_ext(image_path)
        classes_data = name_to_data[full_image_name]

        image_name = get_file_name(image_path)
        mask_path = os.path.join(masks_pathes, image_name + masks_suffix)
        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]
        img_height = ann_np.shape[0]
        img_wight = ann_np.shape[1]
        mask = ann_np != 0
        ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
        for i in range(1, ret):
            obj_mask = curr_mask == i
            curr_bitmap = sly.Bitmap(obj_mask)
            rect_to_centr = curr_bitmap.to_bbox()
            y = rect_to_centr.center.row  # error in SL lib...
            x = rect_to_centr.center.col
            distances = []
            for curr_data in classes_data:
                ann_x = int(curr_data[1])
                ann_y = int(curr_data[2])
                distances.append(get_points_dist((x, y), (ann_x, ann_y)))
            if len(distances) > 0:
                min_index = distances.index(min(distances))
                real_data = classes_data.pop(min_index)
                class_name = real_data[0]
                if class_name == "DEBRIS":
                    class_name = "Debris"
                if class_name == "Gam":  # bad authors data...
                    continue
                obj_class = meta.get_obj_class(class_name)
                curr_label = sly.Label(curr_bitmap, obj_class)
                labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class_r = sly.ObjClass("R", sly.Bitmap)
    obj_class_lr_et = sly.ObjClass("LR-ET", sly.Bitmap)
    obj_class_lt = sly.ObjClass("LT", sly.Bitmap)
    obj_class_mt = sly.ObjClass("MT", sly.Bitmap)
    obj_class_esch = sly.ObjClass("Esch", sly.Bitmap)
    obj_class_lsch = sly.ObjClass("Lsch", sly.Bitmap)
    obj_class_seg = sly.ObjClass("Seg", sly.Bitmap)
    obj_class_wbc = sly.ObjClass("WBC", sly.Bitmap)
    obj_class_debris = sly.ObjClass("Debris", sly.Bitmap)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[
            obj_class_r,
            obj_class_lr_et,
            obj_class_lt,
            obj_class_mt,
            obj_class_esch,
            obj_class_lsch,
            obj_class_seg,
            obj_class_wbc,
            obj_class_debris,
        ]
    )
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_pathes = os.path.join(dataset_path, images_folder_name)
    masks_pathes = os.path.join(dataset_path, masks_folder_name)
    images_names = os.listdir(images_pathes)

    name_to_data = defaultdict(list)
    with open(data_classes_tags_path) as f:
        content = f.read().split("\n")
        for curr_data in content:
            curr_data = curr_data.split("\t")
            name_to_data[curr_data[0]].append(curr_data[1:])

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [
            os.path.join(images_pathes, image_path) for image_path in img_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))
    return project
