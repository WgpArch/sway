<div align="center">
  <img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white" alt="Arch Linux">
  <img src="https://img.shields.io/badge/Wayland-00B4F0?style=for-the-badge&logo=wayland&logoColor=white" alt="Wayland">
  <img src="https://img.shields.io/badge/Sway-00B4F0?style=for-the-badge&logo=sway&logoColor=white" alt="Sway">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
</div>

# 🏠 Welcome to my Sway Config

## 🎛️ Choose Your Bar

This configuration gives you the freedom to choose your preferred status bar. Simply open your main Sway `config` file and comment/uncomment the bar you want to use!

- **Waybar (Recommended):** Lightweight, native Wayland, persistent workspaces 1-11, and the custom Darkhighway theme.
- **EWW (Advanced):** Highly customizable, animated widgets with custom Python workspace integration.

An i3-compatible Wayland compositor setup on Arch Linux, featuring a custom **Eww** bar instead of the standard Waybar, a Catppuccin Mocha theme, and extensive window rules.

![Sway Showcase](screenshots/screenshot_2026-05-24_19-41-50.jpg)

## ✨ Highlights
- **Custom Eww Bar:** Built from scratch using `eww.yuck` and `eww.scss` to bypass Waybar's persistent workspace limitations.
- **Python Workspaces:** A custom `workspaces.py` script dynamically updates the Eww bar with Sway workspace state.
- **Catppuccin Mocha:** Themed with the popular Catppuccin color palette.
- **Extensive Window Rules:** Auto-floating, workspace assignment, and rounded corners for specific applications.
