# libreelec_nespi_power
LibreELEC 12 + RetroFlag Case + Shutdown buttons





Adding the ability of soft shutdown to libreelec and with retroflag pi cases
### How to install

1. Make sure the raspberry pi is connected to the internet.

2. Make sure SSH is enabled in LibreELEC (Config / LibreELEC / Services / SSH Enable is ON).

3. Install Raspberry Pi Tools from repository, LibreELEC Add-ons / Program add-ons / Raspberry Pi Tools

4. ssh into libreelec:

   ```bash
   ssh root@YOUR_LIBRELEC_IP_ADDRESS
   password: libreelec (if unchanged)
   ```

   

5. In the terminal, type the one-line command below(Case sensitive):
   ```
   wget -O - "https://github.com/bearflare20/libreelec_nespi_power/raw/master/install.sh" | bash
   ```
6. Your Raspberry Pi will reboot and you're done!
### Notes
+ tested to work with superpi4 case
   - *fan does stay on in superpi4 case after poweroff*
+ not tested with other retroflag pi cases (nespi+, megapi, nespi4)
   - *could still work, no support provided*
+ will probably not work with gpi cases (gpi case, gpicase2)
   - *uses different system to shutdown*
### Credits
Based off [marcelonovaes lakka nespi script for install.sh](https://github.com/marcelonovaes/lakka_nespi_power) and [RetroFlag RecalBox safe shutdown script](https://github.com/RetroFlag/retroflag-picase/tree/master)





Modified by me (bearflare20) and chatgpt (i cannot be bothered to do it all myself)






