#!/bin/bash
echo Running Sara ...
cd {__PATH__}
nohup {__PATH__}/.env/bin/python3 Sara.py >/dev/null 2>&1 &
echo Sara is running on :
pgrep python