echo "MP4Box ${fileString} -fps 10 ${PWD##*/}_120x_60fps.mp4"
'ffmpeg -i  ${PWD##*/}.mp4 -r 60 -filter:v "setpts=0.0083*PTS"  ${PWD##*/}_120x_60fps.mp4 -an'
