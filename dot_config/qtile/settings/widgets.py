from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg="bg"): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='blue', bg="base02", fontsize=18, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg="emphasized_text"),
            font='Symbols Nerd Font',
            fontsize=16,
            margin_y=3,
            margin_x=1,
            padding_y=1,
            padding_x=1,
            borderwidth=2,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='border',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors["text_secondary"],
            other_current_screen_border=colors["text_secondary"],
            other_screen_border=colors["text_secondary"],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg="yellow"), fontsize=14, padding=5),
        separator(),
    ]


def get_default_interface_linux():
    """Read the default network interface directly from /proc."""
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                # If not default route or not RTF_GATEWAY, skip it
                continue

            return fields[0]


primary_widgets = [
    *workspaces(),

    separator(),

    widget.Prompt(**base(bg="base02"), prompt="", fontsize=16, cursor_color=colors["bg"], ignore_dups_history=True),

    icon(text=''), # Icon: nf-fa-volume_up
    widget.Volume(**base(bg='base02')),

    icon(text=''),
    widget.CPUGraph(**base(bg="base02"), samples=100, border_width=0),
    widget.Memory(**base(bg="base02"), format="{MemUsed: .0f}{mm}", border_width=0),

    icon(text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        **base(bg="base02"),
        colour_have_updates=colors["orange"],
        colour_no_updates=colors["text_secondary"],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    icon(text='בּ'),
    widget.CapsNumLockIndicator(**base(fg="text", bg="base02"), fontsize=12),

    icon(text=''),  # Icon: nf-mdi-ethernet
    #icon(text=''),  # Icon: nf-fa-wifi
    widget.Net(**base(bg="base02"), interface=get_default_interface_linux(), format="{interface} {down} 🠛🠙{up}", prefix='M'),  # U+1F819 U+1F81B

    widget.CurrentLayoutIcon(**base(bg="base02"), scale=0.65),
    widget.CurrentLayout(**base(bg="base02")),

    icon(fontsize=17, text=''), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg="base02"), format='<span weight="bold">%H:%M:%S</span>|%a %d/%m/%Y', fontsize=14),

    #widget.Wallpaper(**base(fg="base02"), directory="/home/dem/Images/fonds d'écran", wallpaper_command=['feh', '--bg-fill', "--recursive"]),

    widget.Systray(background=colors["bg"], padding=3),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    icon(text='בּ'),
    widget.CapsNumLockIndicator(**base(fg="text", bg="base02"), fontsize=12),

    widget.CurrentLayoutIcon(**base(bg="base02"), scale=0.65),
    widget.CurrentLayout(**base(bg="base02"), padding=5),
    
    icon(fontsize=17, text=''), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg="base02"), format='<span weight="bold">%H:%M:%S</span>|%a %d/%m/%Y', fontsize=14),
]

widget_defaults = {
    'font': 'Symbols Nerd Font',
    'fontsize': 13,
    'padding': 2,
}
extension_defaults = widget_defaults.copy()
