#!/bin/bash
declare -i Sara=$(w -h | ls /dev/pts/ |wc -l)
if [[ "${Sara}" < 3 ]]
then
    ~/Sara.sh
    Sara=1
fi