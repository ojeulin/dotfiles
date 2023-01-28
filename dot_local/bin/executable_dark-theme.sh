#!/bin/env zsh
kitty +kitten themes Solarized\ Dark
gsettings set org.gnome.desktop.interface color-scheme prefer-dark

export bat_theme="Solarized (dark)"

# for other scripts (set-wallpaper.sh)
export theme=dark

# rofi
echo '@theme "/usr/share/rofi/themes/multicolor-solarized_dark.rasi"' > "${HOME}/.config/rofi/config.rasi" 

source /home/dem/.oh-my-zsh/custom/aliases.zsh
