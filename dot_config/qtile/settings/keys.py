# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy
from libqtile.config import EzKey


mod = "mod4"

keys = [
    Key(key[0], key[1], *key[2:])
    if isinstance(key[0], list)
    else EzKey(key[0], key[1], *key[2:])
    for key in [
        # ------------ Window Configs ------------
        # Switch between windows in current stack pane
        ([mod], "s", lazy.layout.down()),
        ([mod], "d", lazy.layout.up()),
        ([mod], "t", lazy.layout.left()),
        ([mod], "r", lazy.layout.right()),
        # Change window sizes (MonadTall)
        ([mod, "shift"], "r", lazy.layout.grow()),
        ([mod, "shift"], "t", lazy.layout.shrink()),
        # Toggle floating
        ([mod, "shift"], "f", lazy.window.toggle_floating()),
        # Move windows up or down in current stack
        ([mod, "shift"], "s", lazy.layout.shuffle_down()),
        ([mod, "shift"], "d", lazy.layout.shuffle_up()),
        # Toggle between different layouts as defined below
        ([mod], "Tab", lazy.next_layout()),
        ([mod, "shift"], "Tab", lazy.prev_layout()),
        # Kill window
        ([mod], "q", lazy.window.kill()),
        # Switch focus of monitors
        # ([mod], "apos", lazy.next_screen()),
        # ([mod], "c", lazy.prev_screen()),
        # Restart Qtile
        ([mod, "control"], "r", lazy.restart()),
        ([mod, "control"], "q", lazy.shutdown()),
        # ------------ App Configs ------------
        # Command widget
        ("M-c", lazy.spawncmd()),
        # Menu
        ([mod], "m", lazy.spawn("rofi -show drun")),
        # Window Nav
        ([mod, "shift"], "m", lazy.spawn("rofi -show")),
        # File Explorer
        ("M-e", lazy.spawn("nautilus")),
        ("M-S-e", lazy.spawn("thunar")),
        # Terminal
        ([mod], "Return", lazy.spawn("kitty")),
        # neovim (hyper+N)
        ("M-A-C-S-n", lazy.spawn("kitty nvim")),
        # calculator
        ("M-A-C-S-g", lazy.spawn("galculator")),
        # Redshift
        ("M-A-r", lazy.spawn("redshift -O 5400")),
        ("M-A-S-r", lazy.spawn("redshift -x")),
        # Screenshot
        # ([mod], "s", lazy.spawn("scrot")),
        # ([mod, "shift"], "s", lazy.spawn("scrot -s")),
        # screen lock
        ("M-l", lazy.spawn("i3lock -i \"/home/dem/Images/fonds d'écran/abstract-minimalism-hd-4k-io-1920x1200.png\"")),
        # ------------ Hardware Configs ------------
        # see "xmodmap -pke" for a list of available keysyms
        # Volume
        (
            [],
            "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        ),
        (
            [],
            "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        ),
        ([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        # Brightness
        ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
        ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
        # Media player controls
        ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        ([], "XF86AudioPause", lazy.spawn("playerctl pause")),
        ([], "XF86AudioNext", lazy.spawn("playerctl next")),
        ([], "XF86AudioPrev", lazy.spawn("playerctl previous ")),
        ([], "XF86AudioRewind", lazy.spawn("playerctl position 30-")),
            ([], "XF86AudioForward", lazy.spawn("playerctl position 30+")),
        ]
]
