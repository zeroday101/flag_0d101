import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the video frames
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save each frame as a PNG image
        frame_filename = f"{output_folder}/frame_{frame_count:04d}.png"
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

# Example usage
video_path = 'output.mp4'  # Replace with the path to your video file
output_folder = 'frames_output'  # Replace with the desired output folder

extract_frames(video_path, output_folder)
