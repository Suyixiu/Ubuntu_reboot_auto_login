#!/bin/bash
gsettings set org.gnome.system.proxy mode 'none'
time=$(date "+%Y%m%d-%H%M%S")
echo "${time}" > 你下载这个包的路径/test_run.log
/usr/bin/python3.5 你下载这个包的路径/Ubuntu_reboot_auto_login.py 2>你下载这个包的路径/python_run.log
