#!/usr/bin/bash

# Set the camera device ID
rtsp_url="rtsp://admin:Shazabadmin123@172.16.1.6:554"

# Set the output directory
output_directory="/home/fuzail/Desktop/ShazabInternal/cameraStreams/recordedStreams"

# Set the duration of each recording (in seconds)
duration=3600  # 1 hour

# Set the desired output resolution
output_resolution="640x360"

while true; do
    # Generate the output filename with timestamp
    current_time=$(date +"%Y-%m-%d_%H-%M-%S")

    output_file="$output_directory/camera_$current_time.mp4"

    # Use ffmpeg to record the camera stream
    ffmpeg -rtsp_transport tcp -i "$rtsp_url" -t "$duration" -vf "scale=$output_resolution" "$output_file"
done
