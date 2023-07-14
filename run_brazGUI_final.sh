#!/bin/sh
source /users/joerg/opt/anaconda3/etc/profile.d/conda.sh
conda activate pyside2_dev
pkill -f /Users/joerg/repos/brazGUI/brazGUI_final.py

/Users/joerg/opt/anaconda3/envs/pyside2_dev/bin/python /Users/joerg/repos/brazGUI/brazGUI_final.py