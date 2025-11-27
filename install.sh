#!/bin/bash

# LibreELEC NESPi Power Installer with systemd service

if [[ $EUID -ne 0 ]]; then
   echo "run as root"
   exit 1
fi

# check RPi Tools addon
if [ ! -d "/storage/.kodi/addons/virtual.rpi-tools" ]; then
    echo "Raspberry Pi Tools addon missing"
    echo "install it from Kodi addons then rerun installer"
    exit 1
fi

cd /storage/

echo "downloading package"
wget -O nespi_power.zip "https://github.com/bearflare20/libreelec_nespi_power/archive/master.zip"

echo "unpacking"
unzip -o nespi_power.zip
cd libreelec_nespi_power-master/

# copy scripts
mkdir -p /storage/scripts
cp -R scripts/* /storage/scripts/
chmod +x /storage/scripts/*.py

# create systemd service
mkdir -p /storage/.config/system.d
cat <<EOF > /storage/.config/system.d/nespi-power.service
[Unit]
Description=NESPi Power/Reset Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /storage/scripts/shutdown.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# enable service
systemctl enable /storage/.config/system.d/nespi-power.service

echo "install complete rebooting in 3"
sleep 3
reboot
