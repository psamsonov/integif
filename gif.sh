#! /bin/bash

outfile=`date +%s`


ffmpeg -f video4linux2 -i /dev/video0 -vf fps=6 -vframes 30 output%04d.jpg
ffmpeg -f image2 -i output%*.jpg "gif.gif" -y
