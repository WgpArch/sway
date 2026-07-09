# Waybar Configuration

Waybar is a lightweight, native Wayland status bar. It is the recommended choice for stability and seamless integration with Sway's workspace system.

## ✨ Features
- **Persistent Workspaces:** Always displays workspaces 1 through 11, even when empty.
- **Darkhighway Theme:** Custom black background with orange borders and light blue text.
- **Weather Integration:** Uses a custom Ruby script with a systemd timer for accurate local forecasts.
- **Dropdown Menus:** Native support for calendar and CPU core tooltips.

## 📁 Configuration Files
All Waybar files are located in `configs/waybar/`:

- `config.jsonc`: Module layout and IPC settings.
- `style.css`: The Darkhighway CSS theme.
- `scripts/`: Custom scripts for weather and player status.

## ️ How to Enable
To use Waybar, open your main Sway `config` file and ensure the Waybar line is uncommented:

```bash
# --- OPTION 1: WAYBAR ---
exec waybar -c ~/.config/sway/configs/waybar/config.jsonc -s ~/.config/sway/configs/waybar/style.css

# --- OPTION 2: EWW ---
#Start Eww daemon
    #exec --no-startup-id eww daemon

#Open the bar
    #exec --no-startup-id eww open bar

