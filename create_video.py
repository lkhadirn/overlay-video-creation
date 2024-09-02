import subprocess
import os
from tqdm import tqdm

# First, run the renaming script
subprocess.run(['python', 'rename_images.py'])

# Define the folders
source_folder = './images/source'
target_folder = './images/target'
output_folder = './videos_output'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get the list of renamed source and target images
source_images = sorted([f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])
target_images = sorted([f for f in os.listdir(target_folder) if f.endswith(('.jpg', '.png', '.jpeg'))])

# Determine the number of pairs
num_pairs = min(len(source_images), len(target_images))

# Loop through each pair and create a video
for i in tqdm(range(1, num_pairs + 1), desc="Processing Videos", unit="video"):
    source_image = os.path.join(source_folder, f'image{i}-source.jpg')
    target_image = os.path.join(target_folder, f'image{i}-target.jpg')
    output_video = os.path.join(output_folder, f'video{i}.mp4')

    # Check if both images exist
    if os.path.exists(source_image) and os.path.exists(target_image):
        # Define the FFmpeg command with automatic overwrite
        ffmpeg_command = [
            'ffmpeg',
            '-y',  # Automatically overwrite output files
            '-loglevel', 'error',  # Only show errors
            '-loop', '1',
            '-i', source_image,  # Background image
            '-loop', '1',
            '-i', target_image,  # Foreground image
            '-filter_complex',
            "[1:v]format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='if(gte(X,W*(T/5)),0,255)'[fg];[0:v][fg]overlay=0:0",
            '-t', '5',
            '-c:v', 'libx264',
            '-preset', 'ultrafast',  # Fastest encoding preset
            '-pix_fmt', 'yuv420p',
            output_video
        ]

        # Execute the FFmpeg command
        subprocess.run(ffmpeg_command)

    else:
        print(f"Missing files for pair {i}: {source_image} or {target_image} not found.")

print("Video creation process completed.")
