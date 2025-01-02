import os
import subprocess

def reencode_mp4_to_h264(input_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp4"):
            # Construct full file paths
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)

            # Use ffmpeg to re-encode the .mp4 file with H.264
            print(f"Re-encoding {input_file_path} to H.264...")
            try:
                command = [
                    "ffmpeg", "-i", input_file_path, "-c:v", "libx264", "-c:a", "copy", output_file_path
                ]
                subprocess.run(command, check=True)
                print(f"Re-encoding successful: {output_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error re-encoding {input_file_path}: {e}")
            except FileNotFoundError:
                print("ffmpeg not found. Please install ffmpeg and ensure it's in your system PATH.")

if __name__ == "__main__":
    # Specify the input and output directories
    input_directory = "converted"
    output_directory = "convertedass"

    # Re-encode all .mp4 files in the input directory
    reencode_mp4_to_h264(input_directory, output_directory)