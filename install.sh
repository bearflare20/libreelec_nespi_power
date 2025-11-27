#!/bin/bash

# LibreELEC Nespi Power Installer (checks for Raspberry Pi Tools)

if [[ $EUID -ne 0 ]]; then
   echo "Run as root"
   exit 1
fi

# check for raspberry pi tools addon
if [ ! -d "/storage/.kodi/addons/virtual.rpi-tools" ]; then
    echo "Raspberry Pi Tools addon not installed"
    echo "Install it from Kodi Addons then rerun installer"
    exit 1
fi

cd /storage/

echo "Downloading package..."
wget -O nespi_power.zip "https://github.com/bearflare20/libreelec_nespi_power/archive/master.zip"

echo "Unpacking..."
unzip -o nespi_power.zip
cd libreelec_nespi_power-master/

# copy scripts
mkdir -p /storage/scripts
cp -R scripts/* /storage/scripts/
chmod +x /storage/scripts/*.py

# autostart setup
mkdir -p /storage/.config
if [ ! -f /storage/.config/autostart.sh ]; then
    echo "#!/bin/sh" > /storage/.config/autostart.sh
fi

if ! grep -q "shutdown.py" /storage/.config/autostart.sh; then
    echo "python /storage/scripts/shutdown.py &" >> /storage/.config/autostart.sh
fi

chmod +x /storage/.config/autostart.sh

echo "Install complete rebooting in 3..."
sleep 3
reboot
