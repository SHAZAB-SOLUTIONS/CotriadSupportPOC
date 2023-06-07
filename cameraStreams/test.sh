#!/usr/bin/bash

# Camera Info
channel=$1
camera_name="STREAM_$channel"
cameraStream="rtsp://admin:Password1!@192.168.1.2:554/cam/realmonitor?channel=$channel&subtype=1"

# Output parameters
output_resolution="640x360"
output_directory="/mnt/e/GIT/CotriadSupportPOC/cameraStreams/recordedStreams"
duration=3600  # Output duration (in seconds) 1 hour

while true; do
    # Generate the output filename with timestamp
    current_time=$(date +"%Y-%m-%d_%H-%M-%S")

    currentTimeForName=$(date +"%Y-%m-%d_%H:%M:%S")
    output_file="$output_directory/$camera_name-$currentTimeForName.mp4"

    # Run ffmpeg command to record the camera stream
    echo "Starting to record camera_$channel"
    ffmpeg -rtsp_transport tcp -i "$cameraStream" -t "$duration" -vf "scale=$output_resolution" "$output_file" # -loglevel debug
    echo "Finished recording camera_$channel"

    break
done
