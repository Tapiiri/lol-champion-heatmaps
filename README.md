# League of Legends Movement Project

## Overview
This project utilizes the DeepLeague dataset to generate heatmaps from positional data of champions in League of Legends. It aims to provide insights into player movements and strategies through visual analysis.

## Features
- **Heatmap Generation:** Create heatmaps based on the positional data of League of Legends champions.
- **Data Analysis Tools:** Includes scripts for checking data integrity and preprocessing.

## Getting Started
### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Tapiiri/lol-movement-project.git
   ```
   
### Scripts
### `visualize_centerpoints.py`

The `visualize_centerpoints.py` script in the "lol-movement-project" is used to generate and overlay heatmaps on a map based on the positional data of League of Legends champions. Here's how to use it:

#### Usage
```bash
python visualize_centerpoints.py [-h] [-o OUTPUT_FOLDER] [-f FILE_NAMES [FILE_NAMES ...]] [-c CLASS_NAMES]
```

#### Arguments
- `-h, --help`: Show the help message and exit.
- `-o, --output-folder OUTPUT_FOLDER`: Optional. Specify the output folder for the saved heatmap images. Defaults to "output".
- `-f, --file-names FILE_NAMES`: Required. Provide a list of NPZ filenames or a file containing NPZ filenames.
- `-c, --class-names CLASS_NAMES`: Optional. Specify a file containing a list of NPZ class names in sequential order (e.g., the first class name is for class 0).

#### Description
This script processes NPZ files containing bounding box data to generate heatmaps. These heatmaps are then overlaid on a provided map image. The script allows specifying an output folder for the generated images and supports inputting multiple NPZ files.

---

### `check_npz_data.py`

The `check_npz_data.py` script is designed to load and display bounding boxes from NPZ files, and check if the sizes of these bounding boxes are within a specified tolerance.

#### Usage
```bash
python check_npz_data.py --path PATH
```

#### Arguments
- `--path PATH`: Required. Specify the path to the NPZ file.

#### Description
This script loads bounding boxes from a specified NPZ file and checks if their sizes are consistent. It prints out the bounding boxes and indicates whether their sizes are within a defined tolerance level. This is useful for validating the integrity of the bounding box data in the NPZ files.

---

These scripts are part of the "lol-movement-project" and are essential for processing and visualizing the positional data of League of Legends champions. Make sure to have the necessary NPZ files and dependencies installed before running these scripts.

## Acknowledgements
Thanks for the skeleton ReadMe, ChatGPT!
