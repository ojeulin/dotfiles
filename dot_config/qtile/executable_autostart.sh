#!/bin/bash

# compositor (visual effects for windows, transparency)
picom &
# notifications
dunst &
dropbox-cli start &
# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
copyq &
keepassxc &
/usr/lib/nordtray/nordtray &

# playerctl daemon keeps track of media player activity.
# When playerctld is running, playerctl commands will act on the media player
# with the most recent activity.
playerctld daemon &

/home/dem/.local/bin/invert-button-and-scroll.sh &

# display random images every N minutes
set_wallpaper () {
	local dir_img=$(readlink -f ~/Images/fonds\ d\'écran)
	while :
	do
		feh --quiet --no-fehbg --bg-max --recursive --randomize "$dir_img"
		sleep 1m
	done
}
set_wallpaper &
