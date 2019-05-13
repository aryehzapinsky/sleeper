#!/bin/bash

vidArray=()

for file in *.h264; do vidArray=(${vidArray[@]} "-cat $file"); done

fileString=$( IFS=' '; echo "${vidArray[*]}")

echo "#!/bin/bash" > com.sh;
echo "MP4Box ${fileString} -fps 10 ${PWD##*/}.mp4" >> com.sh;
chmod +x com.sh;
./com.sh;
rm com.sh;
