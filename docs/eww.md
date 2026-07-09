# 📊 Eww Bar & Scripts

Sway's native IPC for workspaces can be stubborn with standard Waybars, often struggling to display persistent workspaces or update states cleanly without complex workarounds.

To bypass this, this setup uses a custom **Eww** bar, designed to be lightweight and static, prioritizing stability over complex interactive widgets.

## The Eww Bar Layout

The bar is defined in `~/.config/eww/eww.yuck` and styled with `eww.scss`.

## ⚙️ How to Enable
To use EWW instead of Waybar, open your main Sway `config` file, comment out the Waybar line, and uncomment the EWW line:

```bash
# --- OPTION 1: WAYBAR ---
# exec waybar -c ~/.config/sway/configs/waybar/config.jsonc -s ~/.config/sway/configs/waybar/style.css

# --- OPTION 2: EWW ---
#Start Eww daemon
    #exec --no-startup-id eww daemon

#Open the bar
    #exec --no-startup-id eww open bar

### Left
- **Launcher:** Arch Linux icon (Rofi).
- **Workspaces:** Dynamically generated via a Python script (`workspaces.py`), showing workspace IDs 1-10 with active/focused states.

### Center
- **Date & Time:** Updated every second via `defpoll`.

### Right
- **Weather:** Current conditions via `weather.py`.
- **Network Status:** Connection state via `network.sh`.
- **Battery Percentage:** Via `battery.sh`.
- **RAM & CPU Usage:** Via `memory.sh` and `cpu.sh`.
- **Temperature:** Via `temp.sh`.
- **Power Button:** Launches `wlogout`.

## 🤔 Why No Hover Dropdowns/Players?

While Eww *can* support complex interactive popups (like weather forecasts or media player controls), implementing them requires writing custom Lisp-like logic, CSS popups, and additional daemon scripts. For a system monitor bar, the return on investment just isn't there. This setup intentionally opts for a **clean, static layout** that shows essential system stats at a glance without the overhead.

## 📜 Key Scripts

Located in `~/.config/scripts/system/` (Symlinked from `~/.dotfiles/sway/configs/scripts/system/`):

| Script | Description |
| :--- | :--- |
| `workspaces.py` | Listens to Sway IPC and outputs workspace JSON for the Eww bar. |
| `weather.py` | Fetches weather data for the Eww bar. |
| `cpu.sh` / `memory.sh` | Fetches CPU and RAM usage. |
| `battery.sh` / `network.sh` / `temp.sh` | Fetches battery, network, and temperature stats. |

Located in `~/.config/eww/modules/`:

| Script | Description |
| :--- | :--- |
| `powermenu/eww.yuck` | Eww layout for the centered power menu. |
| `calendar/eww.yuck` | Eww layout for the calendar module. |
