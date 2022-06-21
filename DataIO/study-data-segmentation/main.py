import os
import json

labels = [
    {
        "category": [["object", "necrosis"]],
        "attributes": [],
        "dicom": {"instanceid": 1},
    },
    {
        "category": [["object", "edema"]],
        "attributes": [],
        "dicom": {"instanceid": 2},
    },
    {
        "category": [["object", "non-enhancing tumor"]],
        "attributes": [],
        "dicom": {"instanceid": 3},
    },
    {
        "category": [["object", "enhancing tumor"]],
        "attributes": [],
        "dicom": {"instanceid": 4},
    },
]


image_dir = "NIFTI_images"
studies = os.listdir(image_dir)
studies = list(
    filter(lambda x: os.path.isdir(os.path.join(image_dir, x)), studies)
)
items = []
for study in studies:
    series = os.listdir(os.path.join(image_dir, study))
    series = list(filter(lambda x: x.endswith("gz"), series))
    items += [
        {
            "items": [
                os.path.join("brain-brats-study", image_dir, study, ser)
                for ser in series
            ],
            "name": study,
        },
    ]

with open("items-study.json", "w+") as file:
    json.dump(items, file, indent=2)
