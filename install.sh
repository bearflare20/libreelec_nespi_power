#!/bin/bash

# LibreELEC Nespi Power Installer (bearflare20 fork)
# -----------------------------------------------------

if [[ $EUID -ne 0 ]]; then
   echo "Run as root"
   exit 1
fi

cd /storage/

echo "Downloading package..."
wget -O nespi_power.zip "https://github.com/bearflare20/libreelec_nespi_power/archive/master.zip"

echo "Unpacking..."
unzip -o nespi_power.zip
cd libreelec_nespi_power-master/

# Copy libs + scripts directly from repo
mkdir -p /storage/lib
cp -R lib/* /storage/lib/

mkdir -p /storage/scripts
cp -R scripts/* /storage/scripts/

# Make sure python files are executable
chmod +x /storage/scripts/*.py

# Ensure autostart exists
mkdir -p /storage/.config
if [ ! -f /storage/.config/autostart.sh ]; then
    echo "#!/bin/sh" > /storage/.config/autostart.sh
fi

# Add python boot line if missing
if ! grep -q "shutdown.py" /storage/.config/autostart.sh; then
    echo "python /storage/scripts/shutdown.py &" >> /storage/.config/autostart.sh
fi

chmod +x /storage/.config/autostart.sh

echo "Install complete rebooting in 3..."
sleep 3
reboot
