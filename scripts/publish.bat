@echo off

echo DEBUG LINE: Program works to ffmpeg point

REM Stream source is an 8 seconds long cat feeder camera loop
REM with an overlay image on top left corner of the frame.
REM Audio is boosted by 2, and stream is sent to localhost, 127.0.0.1:1935 (default rtmp)

ffmpeg -stream_loop -1 -re -i "..\resource\video\mewo.mp4" ^
 -loop 1 -i ..\overlay\overlay.png ^
 -filter_complex "[0:a]loudnorm=I=-16:LRA=11:TP=-1.5,volume=2.0[boosted_audio];[0:v][1:v]overlay=10:10[vid]" ^
 -map "[vid]" -map "[boosted_audio]" ^
 -c:v libx264 -preset veryfast -b:v 800k -maxrate 800k -bufsize 1600k ^
 -c:a aac -b:a 128k -ar 44100 -f flv rtmp://127.0.0.1/live/stream