#!/bin/bash
# Get used RAM percentage
free | awk '/Mem/{printf "%.0f%", $3/$2*100}'
