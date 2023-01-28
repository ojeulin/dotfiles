#!/bin/bash

# display random images every N minutes
local time=1m
local dir_img=$(readlink -f ~/Images/wallpapers/1920x1200/thème-clair)
while :
do
	feh --quiet --no-fehbg --bg-max --recursive --randomize "$dir_img"
	sleep $time
done

