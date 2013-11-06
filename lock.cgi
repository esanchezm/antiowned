#!/bin/bash

source conf.sh

export DISPLAY=$DISPLAY

for device in $DEVICES
do
    /usr/bin/xinput set-int-prop $device "Device Enabled" 8 0
done

sleep $BLOCKING_TIME

for device in $DEVICES
do
    /usr/bin/xinput set-int-prop $device "Device Enabled" 8 1
done

/usr/bin/gnome-screensaver-command -l

echo -e "Content-type: application/javascript\n"
echo '{};'
