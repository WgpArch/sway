# 🎨 Look & Feel

This Sway config uses the Catppuccin Mocha color palette, featuring generous gaps and rounded window corners.

## General Appearance
- **Gaps (Inner):** 10px
- **Gaps (Outer):** 7px
- **Border Width:** 2px (Pixel style, no title bars).
- **Smart Gaps:** Enabled (Gaps hide automatically if there is only one window).
- **Border Radius:** 30px (Applied via window rules).

## Colors
The Catppuccin Mocha theme is loaded via `include catppuccin-mocha`. 
- **Focused Border:** Mauve (`#c6a0f6`)
- **Inactive Border:** Mantle/Dark grey

## Window Rules
Extensive window rules are configured to automatically manage application behavior:
- **Auto-Floating:** Dialog boxes, pavucontrol, nm-connection-editor, ristretto, and picture-in-picture windows float automatically.
- **Workspace Assignment:** 
  - Google Chrome opens on Workspace 2.
  - Thunar opens on Workspace 3.
  - Telegram opens on Workspace 6.
  - Shotcut opens on Workspace 5.
- **Idle Inhibit:** Google Chrome inhibits screen sleep when fullscreen.

## Input Devices
- **Touchpad:** Tap-to-click, natural scrolling, middle emulation, and drag enabled. Two-finger scroll method.
- **Keyboard:** US layout.

## Autostart
Applications are spawned automatically via `exec` statements in the config:
- **Environment:** dbus and systemd environment imports.
- **Bar:** Eww daemon and bar launch.
- **Utilities:** `swaync`, `nm-applet`, `wl-paste` (cliphist), `mpd` & `mpDris2`.
- **Wallpaper:** Random background script (`bg_random_auto`).
