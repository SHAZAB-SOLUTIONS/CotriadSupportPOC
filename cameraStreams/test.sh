#!/usr/bin/bash

# Get current date and time


# Set the start time to 5 am
start_time="12:52:00"

# Set the end time to 6 pm
end_time="12:53:00"

cameraStream="rtsp://admin:Shazabadmin123@172.16.1.6:554"

output_directory="/home/fuzail/Desktop/ShazabInternal/cameraStreams/recordedStreams"

camera_name="OF2"

output_resolution="640x360"

# Check if the current time is within the specified range

while true; do
    echo "Checking Time"
    current_time=$(date +%H:%M:%S)
    if [[ "$current_time" > "$start_time" && "$current_time" < "$end_time" ]]; then
        # Calculate the duration between the current time and the end time
        duration=$(($(date -d "$end_time" +%s) - $(date -d "$current_time" +%s)))

        echo $duration
        currentTime=$(date +"%Y-%m-%d_%H-%M-%S")

        output_file="$output_directory/$camera_name-$currentTime.mp4"
        
        # Run ffmpeg command to record the IP camera stream
        ffmpeg -rtsp_transport tcp -i "$cameraStream" -t "$duration" -vf "scale=$output_resolution" "$output_file" -loglevel debug
        break
    else
        sleep 5
    fi

done