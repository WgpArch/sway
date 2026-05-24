#!/bin/bash
# Check active connection name
CONNECTION=$(nmcli -t -f NAME,TYPE connection show --active | head -n 1 | cut -d: -f1)
if [ -z "$CONNECTION" ]; then
    echo "Disconnected"
else
    echo "📶 $CONNECTION"
fi
