#!/bin/env zsh
kitty +kitten themes Solarized\ Light
gsettings set org.gnome.desktop.interface color-scheme prefer-light

export bat_theme="Solarized (light)"

# for other scripts (set-wallpaper.sh)
export theme=light

# rofi
echo '@theme "/usr/share/rofi/themes/multicolor-solarized_light.rasi"' > "${HOME}/.config/rofi/config.rasi" 

source /home/dem/.oh-my-zsh/custom/aliases.zsh
