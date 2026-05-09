#!/usr/bin/env python3

import subprocess
import json
import time
import sys

def get_workspaces():
    try:
        # 1. Ask Sway for the current state of all workspaces
        cmd = ["swaymsg", "-t", "get_workspaces"]
        output = subprocess.check_output(cmd).decode()
        sway_data = json.loads(output)
        
        # 2. Find out which one is currently focused
        focused_num = -1
        active_nums = []
        
        for ws in sway_data:
            if ws['focused']:
                focused_num = ws['num']
            active_nums.append(ws['num'])
        
        # 3. Build our fixed list of 11 workspaces
        final_list = []
        for i in range(1, 12): # 1 to 11
            is_active = i in active_nums
            is_focused = (i == focused_num)
            
            final_list.append({
                "id": i,
                "active": is_active,
                "focused": is_focused
            })
        
        # 4. Print the JSON list for Eww
        print(json.dumps(final_list))
        sys.stdout.flush()
        
    except Exception as e:
        print("[]") # Print empty list on error so Eww doesn't crash
        sys.stdout.flush()

# Initial run
get_workspaces()

# Loop forever (Polling)
while True:
    time.sleep(0.5) # Check every 0.5 seconds
    get_workspaces()
