#!/bin/bash

# LibreELEC Nespi Power Installer

if [[ $EUID -ne 0 ]]; then
   echo "run as root"
   exit 1
fi

# check for raspberry pi tools
if [ ! -d "/storage/.kodi/addons/virtual.rpi-tools" ]; then
    echo "raspberry pi tools addon missing"
    echo "install it from kodi addons then rerun installer"
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

# autostart
mkdir -p /storage/.config

if [ ! -f /storage/.config/autostart.sh ]; then
    echo "#!/bin/sh" > /storage/.config/autostart.sh
    chmod +x /storage/.config/autostart.sh
fi

if ! grep -q "shutdown.py" /storage/.config/autostart.sh; then
    echo "( python3 /storage/scripts/shutdown.py ) &" >> /storage/.config/autostart.sh
fi

echo "install complete rebooting in 3"
sleep 3
reboot
