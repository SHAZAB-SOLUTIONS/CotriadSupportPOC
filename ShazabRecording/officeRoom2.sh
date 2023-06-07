#!/usr/bin/bash

# Set the camera device ID
camera_name="OfficeRoom2"
# echo "Recording $camera_name"
rtsp_url="rtsp://admin:Shazabadmin123@172.16.1.6:554"

# Set the output directory
output_directory="/home/fuzail/Desktop/ShazabInternal/CameraRecording/recordedStreams"

# Set the duration of each recording (in seconds)
duration=900  # 15 minutes

# Set the desired output resolution
output_resolution="640x360"

while true; do
    # Generate the output filename with timestamp
    current_time=$(date +"%Y-%m-%d_%H-%M-%S")

    output_file="$output_directory/$camera_name-$current_time.mp4"

    # Use ffmpeg to record the camera stream
    ffmpeg -rtsp_transport udp -i "$rtsp_url" -t "$duration" -vf "scale=$output_resolution" "$output_file"
done
