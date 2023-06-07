#!/usr/bin/bash

cameraURL="rtsp://user:password@ipAddress:554"

outputFilename="camVideo_$(date +%Y%m%d%H%M%S).mp4"

duration=10 # 10 seconds

# ffmpeg -rtsp_transport tcp -analyzeduration 30M -probesize 30M -i "$cameraURL" -c copy "$outputFilename"
ffmpeg -rtsp_transport tcp -i "$cameraURL" -t "$duration" "$outputFilename"
