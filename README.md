# Batch MOV to MP4 Converter

A clean, open-source Python utility to convert multiple `.mov` files to high-quality `.mp4` videos using FFmpeg.

## Features
- **Batch Processing**: Automatically converts all videos in the input folder.
- **High Quality**: Pre-configured with FFmpeg's visually lossless settings (`CRF 18`).
- **Auto-Setup**: Automatically creates necessary folders if they don't exist.
- **Open Source**: MIT Licensed.

## Prerequisites
- **Python 3.x**
- **FFmpeg** (Must be installed and in your system PATH)

## Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Akshay-gurav-31/Batch-MOV-to-MP4-Converter/
    cd Batch-MOV-to-MP4-Converter
    ```
2.  **Initialize Folders**:
    Run the script once to generate the `video/` folder:
    ```bash
    python converter.py
    ```

## Usage

1.  Place your `.mov` files inside the newly created `video/` folder.
2.  Run the script:
    ```bash
    python converter.py
    ```
3.  Find your converted videos in the `output/` folder.

## Technical Details
- **Video Codec**: H.264 (`libx264`)
- **Quality**: CRF 18 (High fidelity)
- **Audio**: AAC 192kbps

## License
Distributed under the **MIT License**. See `LICENSE` for more information.
