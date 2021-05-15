# MagicHome
A Python library for MagicHome Wifi RGB controller

[![current version](https://img.shields.io/badge/current%20version-1.0.0-green.svg)](https://github.com/marcelbohland/MagicHome/releases/tag/1.0.0)

create
````python
controll.ip = "192.168.178.32"
magicHome = controll.MagicHome()
magicHome.turn_off()
````

Turn on/off
````python
magicHome.turn_on()
magicHome.turn_off()
````

Change Color
````python
magicHome.changeColor(0,0,255)
````
Police effect
````python
police = threading.Thread(name='police', target=magicHome.police)
police.start()
magicHome.stopPolice()
````
RGB Fade effect
````python
rgbFade = threading.Thread(name='rgbfade', target=magicHome.rgbfade)
rgbFade.start()
magicHome.stopRgbFade()
````
RGB Pulse effect
````python
rgbPulse = threading.Thread(name='rgbPulse', target=magicHome.rgbPulse)
rgbPulse.start()
magicHome.stopRgbPulse()
````

send [Turn on]
````python
magicHome.send(0x71, 0x23, 0x0F, 0xA3)
````
