#!/bin/bash

# LibreELEC NESPi Power Installer with systemd service (fixed for lgpio)

if [[ $EUID -ne 0 ]]; then
   echo "run as root"
   exit 1
fi

# check RPi Tools addon
if [ ! -d "/storage/.kodi/addons/virtual.rpi-tools" ]; then
    echo "Raspberry Pi Tools addon missing"
    echo "Install it from LibreELEC addons then rerun installer"
    exit 1
fi

cd /storage/

echo "Downloading package"
wget -O nespi_power.zip "https://github.com/bearflare20/libreelec_retroflag_safeshutdown/archive/master.zip"

echo "Unpacking"
unzip -o nespi_power.zip
cd libreelec_nespi_power-master/

# copy scripts
mkdir -p /storage/scripts
cp -R scripts/* /storage/scripts/
chmod +x /storage/scripts/*.py

# create lgpio notify dir
mkdir -p /storage/.config/lgpio
chown root:root /storage/.config/lgpio

# create systemd service
mkdir -p /storage/.config/system.d
cat <<EOF > /storage/.config/system.d/nespi-power.service
[Unit]
Description=NESPi Power/Reset Service
After=multi-user.target

[Service]
Type=simple
Environment=LGPIO_NFY_DIR=/storage/.config/lgpio
WorkingDirectory=/storage/scripts
ExecStart=/usr/bin/python3 /storage/scripts/shutdown.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# reload systemd and enable service
systemctl daemon-reload
systemctl enable nespi-power.service

echo "Install complete, rebooting in 3 seconds"
sleep 3
reboot
