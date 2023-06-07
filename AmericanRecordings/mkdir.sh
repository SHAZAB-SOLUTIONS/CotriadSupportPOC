#!/usr/bin/bash

output_directory="/mnt/e/GIT/CotriadSupportPOC/cameraStreams/recordedStreams"

channel=$1
camera_name="STREAM_$channel"

currentTimeForName=$(date +"%Y-%m-%d_%H:%M:%S")
mkdir -p $output_directory/$camera_name
output_file="$output_directory/$camera_name/$currentTimeForName.mp4"

echo $output_file
