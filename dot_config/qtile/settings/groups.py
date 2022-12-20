# Qtile workspaces

import asyncio

from libqtile import hook
from libqtile.command import lazy
from libqtile.config import Group, Key, Match

from .keys import keys, mod

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
groups = (
    Group("1", label="1·"),  # nf-cod-terminal (# nf-dev-terminal)
    Group("2", label="2·", matches=[Match(wm_class=["firefox"])]),  # nf-fa-firefox
    Group("3", label="3·", matches=[Match(wm_class=["code"])]),  # nf-fa-code
    Group("4", label="4·", matches=[Match(wm_class=["spotify"])]),  # nf-fa-music
    Group("5", label="5·", matches=[Match(title=["lazydocker"])]),  # nf-linux-docker,
    Group("6", label="6·", matches=[Match(title=["lazygit"])]),  # nf-dev-git
    Group(
        "7", label="7·", matches=[Match(wm_class=["org.gnome.Nautilus", "thunar"])]
    ),  # folder
    Group("8", label="8·ﴬ"),  # nf-mdi-notebook
    Group("9", label="9·", matches=[Match(wm_class=["keepassxc"])]),  # nf-mdi-layers
    Group(
        "10", label="10·", matches=[Match(wm_class=["transmission-qt"])]
    ),  # nf-fa-cloud_download
)


@hook.subscribe.client_new
async def move_client(client):
    """Spotify's properties are not set when the program is spawned, we must
    wait a few ms to identify it and move it to the expected group.
    """
    await asyncio.sleep(0.01)
    if client.name == "Spotify":
        client.cmd_togroup(group_name="4")


numpad = {
    1: "KP_End",
    2: "KP_Down",
    3: "KP_Next",
    4: "KP_Left",
    5: "KP_Begin",
    6: "KP_Right",
    7: "KP_Home",
    8: "KP_Up",
    9: "KP_Prior",
    10: "KP_Insert",  # the "0" key
}

for i, group in enumerate(groups):
    actual_key = numpad[i + 1]
    keys.extend(
        [
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        ]
    )
