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

/home/dem/bin/invert-button-and-scroll.sh &
/home/dem/bin/set-wallpaper.sh &

