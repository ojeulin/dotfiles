#!/bin/bash

# display random images every N minutes
interval=1m
if [[ $theme = "dark" ]];then
	wallpaper_theme=vert
else
	wallpaper_theme=clair
fi
dir_img=$(readlink -f ~/Images/wallpapers/1920x1200/thème-clair)
while :
do
	feh --quiet --no-fehbg --bg-max --recursive --randomize "$dir_img"
	sleep $interval
done

