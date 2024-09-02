# Overlay Video Creation

This repository contains Python scripts for automating the process of renaming images and creating overlay videos. The scripts are designed to take pairs of images from specified folders, rename them based on a consistent naming convention, and then generate videos where one image gradually overlays or reveals another.

## Features

- **Automatic Image Renaming:** Renames images in `source` and `target` folders according to a specific pattern (e.g., `image1-source.jpg`, `image1-target.jpg`).
- **Video Creation:** Generates videos by overlaying images from the `source` and `target` folders. The videos are saved in the `videos_output` folder.
- **Progress Tracking:** Provides a progress bar to monitor the video creation process.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/overlay-video-creation.git
   cd overlay-video-creation

2. **Install the Required Python Packages:**

   Ensure you have Python installed, and then install the necessary packages:

   ```bash
   pip install tqdm

3. **Install FFmpeg:**

   This project relies on FFmpeg to handle video creation. Make sure FFmpeg is installed and accessible from your command line.

   - [FFmpeg Installation Guide](https://ffmpeg.org/download.html)
  
## Usage

1. **Prepare Your Images:**

   - Place your source images in the `./images/source` folder.
   - Place your target images in the `./images/target` folder.

2. **Run the Video Creation Script:**

   Execute the following command to rename the images and create videos:

   ```bash
   python create_videos.py

The script will:

  - Rename the images in the source and target folders.
  - Create videos where each target image overlays its corresponding source image.
  - Save the videos in the ./videos_output folder.


## File Structure Section

  ```bash
    overlay-video-creation/
    │
    ├── images/
    │   ├── source/               # Folder for source images
    │   └── target/               # Folder for target images
    │
    ├── videos_output/            # Folder where videos will be saved
    │
    ├── rename_images.py          # Script to rename images
    ├── create_videos.py          # Script to create overlay videos
    └── README.md                 # This README file
  ```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have suggestions or improvements.

## Acknowledgments

- [FFmpeg](https://ffmpeg.org) for video processing.
- [tqdm](https://github.com/tqdm/tqdm) for the progress bar.


