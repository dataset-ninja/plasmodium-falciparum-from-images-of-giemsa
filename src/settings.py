from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Malaria Segmentation"
PROJECT_NAME_FULL: str = (
    "Malaria Segmentation: A Dataset for Segmentation of Malaria Infected Cells"
)
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2019-11-11"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://data.mendeley.com/datasets/5bf2kmwvfn/1"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2152994
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/malaria-segmentation"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/5bf2kmwvfn-1.zip"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "R": [230, 25, 75],
    "LR-ET": [60, 180, 75],
    "LT": [255, 225, 25],
    "MT": [0, 130, 200],
    "Esch": [245, 130, 48],
    "Lsch": [145, 30, 180],
    "Seg": [70, 240, 240],
    "WBC": [240, 50, 230],
    "Debris": [210, 245, 60],
}

# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://diagnosticpathology.biomedcentral.com/articles/10.1186/s13000-020-01040-9"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {"Kaggle":"https://www.kaggle.com/datasets/niccha/malaria-segmentation"}

CITATION_URL: Optional[str] = "https://data.mendeley.com/datasets/5bf2kmwvfn/1"
AUTHORS: Optional[List[str]] = ["Abbas, Syed Saiden", "M. H. Dijkstra, Tjeerd"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Radboud University Nijmegen, Netherlands",
    "Max Planck Institute for Developmental Biology, Germany",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.ru.nl/icis/",
    "https://www.mpg.de/151769/biology-tuebingen",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
