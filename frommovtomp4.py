import os
import cv2

def convert_mov_to_mp4(input_dir, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        print(f"Converting {filename} to .mp4...")
        if filename.endswith(".MOV"):
            # Construct full file paths
            mov_file_path = os.path.join(input_dir, filename)
            mp4_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".mp4")

            # Open the .mov file
            cap = cv2.VideoCapture(mov_file_path)
            if not cap.isOpened():
                print(f"Error opening video file: {mov_file_path}")
                continue

            # Get video properties
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            # Create a VideoWriter object to save the .mp4 file
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4
            out = cv2.VideoWriter(mp4_file_path, fourcc, fps, (frame_width, frame_height))

            # Read and write each frame
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

            # Release resources
            cap.release()
            out.release()
            print(f"Conversion successful: {mp4_file_path}")

if __name__ == "__main__":
    # Specify the input and output directories
    input_directory = "ass"
    output_directory = "pes"

    # Convert all .mov files in the input directory
    convert_mov_to_mp4(input_directory, output_directory)