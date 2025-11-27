# libreelec_nespi_power
LibreELEC 12.2.1 + RetroFlag Case + Shutdown buttons
- tested to work with superpi4 case
- not tested with nespi case




Adding the ability of soft shutdown to libreelec and with retroflag cases






Based off [marcelonovaes lakka nespi script](https://github.com/marcelonovaes/lakka_nespi_power)
### How to install

1. Make sure the raspberry pi is connected to the internet.

2. Make sure SSH is enabled in LibreELEC (Config / LibreELEC / Services / SSH Enable is ON).

3. ssh into libreelec:

   ```bash
   ssh root@YOUR_LIBRELEC_IP_ADDRESS
   password: libreelec (if unchanged)
   ```

   

4. In the terminal, type the one-line command below(Case sensitive):

   wget -O - "https://github.com/bearflare20/libreelec_nespi_power/raw/master/install.sh" | bash

5. Your Raspberry Pi will reboot and you're done!







