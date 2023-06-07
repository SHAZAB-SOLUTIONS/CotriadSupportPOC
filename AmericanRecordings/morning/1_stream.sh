#!/usr/bin/bash

# Set the start time to 9:30 am
startTime="09:30:00"

# Set the end time to 11 am
endTime="11:00:00"

# Camera Info
channel=$1
camera_name="STREAM_$channel"
cameraStream="rtsp://admin:Password1!@192.168.1.2:554/cam/realmonitor?channel=$channel&subtype=1"

# Output parameters
output_resolution="640x360"
output_directory="/home/fueltech/Desktop/ShazabInternal/AmericanRecordings/morning/recordedStreams"

while true; do
    echo "Checking Time" && date +%D_%A_%H:%M:%S
    current_time=$(date +%H:%M:%S)
    if [[ "$current_time" > "$startTime" && "$current_time" < "$endTime" ]]; then
    
        duration=3600 # 1 hour

        currentTimeForName=$(date +"%D_%H:%M:%S")
        output_file="$output_directory/$camera_name-$currentTimeForName.mp4"

        # Run ffmpeg command to record the camera stream
        echo "Starting to record camera_$channel"
        ffmpeg -rtsp_transport tcp -i "$cameraStream" -t "$duration" -vf "scale=$output_resolution" "$output_file" # -loglevel debug
        echo "Finished recording camera_$channel"

        break
    else
        sleep 2
    fi
done
