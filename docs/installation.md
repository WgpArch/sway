# 🛠️ Installation

This setup uses an Eww bar that relies on custom scripts located in `~/.config/scripts/system/`. Symlinking these directories correctly is crucial.

## Prerequisites

**Core:**
- `sway`
- `eww` (ElKowars wacky widgets)
- `rofi` & `wlogout`
- `swaylock` (Screen locker)
- `swaync` (Notification center)

**Eww Scripts & Utilities:**
- `python3` (For workspace and weather scripts)
- `playerctl` (Media keys)
- `brightnessctl` (Backlight)
- `pamixer` / `pavucontrol` (Audio)
- `grim` & `slurp` (Screenshots)

## Deploying the Config

1. Clone the repository:
        
        git clone https://codeberg.org/WgpArch/sway.git ~/.dotfiles/sway

2. Symlink the Sway configuration:
        
        ln -sf ~/.dotfiles/sway/configs/sway ~/.config/sway

3. Symlink the Eww configuration:
        
        ln -sf ~/.dotfiles/sway/configs/eww ~/.config/eww

4. Symlink the Eww system scripts (Crucial step!):
   The Eww bar looks for scripts in `~/.config/scripts/system/`.
        
        ln -sf ~/.dotfiles/sway/configs/scripts ~/.config/scripts

5. Ensure scripts are executable:
        
        chmod +x ~/.config/sway/scripts/*
        chmod +x ~/.config/scripts/system/*
