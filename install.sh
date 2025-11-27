#!/bin/bash

# LibreELEC Nespi Power Installer (for RPi.GPIO addon)

if [[ $EUID -ne 0 ]]; then
   echo "Run as root"
   exit 1
fi

cd /storage/

echo "Make sure Raspberry Pi Tools is installed, CTRL+C to cancel installation"
sleep 5

echo "Downloading package..."
wget -O nespi_power.zip "https://github.com/bearflare20/libreelec_nespi_power/archive/master.zip"

echo "Unpacking..."
unzip -o nespi_power.zip
cd libreelec_nespi_power-master/

# Copy scripts from repo
mkdir -p /storage/scripts
cp -R scripts/* /storage/scripts/

# make python scripts executable
chmod +x /storage/scripts/*.py

# ensure autostart exists
mkdir -p /storage/.config
if [ ! -f /storage/.config/autostart.sh ]; then
    echo "#!/bin/sh" > /storage/.config/autostart.sh
fi

# add shutdown script to autostart if missing
if ! grep -q "shutdown.py" /storage/.config/autostart.sh; then
    echo "python /storage/scripts/shutdown.py &" >> /storage/.config/autostart.sh
fi

chmod +x /storage/.config/autostart.sh

echo "Install complete rebooting in 3..."
sleep 3
reboot
