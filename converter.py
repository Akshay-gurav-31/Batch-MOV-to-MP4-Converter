import os
import subprocess
import sys

def convert_videos():
    # Folder paths
    input_folder = 'video'
    output_folder = 'output'

    # Ensure folders exist
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"Created '{input_folder}' folder. Please add your .mov files there and run the script again.")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of .mov files
    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.mov')]

    if not video_files:
        print(f"No .mov files found in '{input_folder}' folder.")
        return

    print(f"Found {len(video_files)} video(s) to convert.")

    for filename in video_files:
        input_path = os.path.join(input_folder, filename)
        # Create output filename by replacing extension
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"{base_name}.mp4")

        print(f"\nConverting: {filename} -> {base_name}.mp4")

        # Command for FFmpeg
        # -y: Overwrite output files
        # -i: Input file
        # -c:v libx264: Video codec H.264
        # -crf 18: Constant Rate Factor (18 is nearly visually lossless, lower is better quality)
        # -preset slow: Better compression (smaller file size for same quality)
        # -c:a aac: Audio codec AAC
        # -b:a 192k: Audio bitrate
        command = [
            'ffmpeg',
            '-y',
            '-i', input_path,
            '-c:v', 'libx264',
            '-crf', '18',
            '-preset', 'slow',
            '-c:a', 'aac',
            '-b:a', '192k',
            output_path
        ]

        try:
            # Run FFmpeg command
            subprocess.run(command, check=True)
            print(f"Successfully converted: {base_name}.mp4")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {filename}: {e}")
        except FileNotFoundError:
            print("Error: FFmpeg not found. Please make sure FFmpeg is installed and added to PATH.")
            break

    print("\nBatch conversion process completed.")

if __name__ == "__main__":
    convert_videos()
