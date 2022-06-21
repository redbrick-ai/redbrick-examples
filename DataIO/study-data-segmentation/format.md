# Mapping file

Maps between NIfTI class ID and RedBrick AI category name

```js
{
    "1": "category-name",
    "2": "category-name-2"
    .
    .
}
```

# Items List

Defines the list of instances/series/studies to upload, along with the corresponding segmentations.

## Semantic Segmentation

```js
[
  // Each entry in this list is a study/task on RedBrick AI
  {
    // Unique identified for the study that is user specified
    "name": "study-1",

    // Each entry here is a single series part of the study
    "items": [
      "path/to/series01.nii",
      "path/to/series02.nii",
      "path/to/series03.nii"
    ],

    // Corresponding segmentation files to the series above
    "segmentations": [
      "path/to/series01_seg.nii",
      "path/to/series02_seg.nii",
      "path/to/series03_seg.nii"
    ]
  }
  .
  .
]
```
