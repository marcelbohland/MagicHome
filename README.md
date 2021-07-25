# MagicHome
A Python library for MagicHome Wifi RGB controller

[![current version](https://img.shields.io/badge/current%20version-1.0.1-green.svg)](https://github.com/marcelbohland/MagicHome/releases/tag/1.0.1)
[![license](https://img.shields.io/badge/license-Apache%20License%202.0-red.svg)](https://github.com/marcelbohland/MagicHome/blob/main/LICENSE)

1. Download the MagicHome.py and add it to your project.
2. Copy the "Create" part to your project.
3. Change the IP-Address to your IP-Address

Create
````python
import MagicHome

MagicHome.ip = "192.168.0.1"
magicHome = MagicHome.MagicHome()
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

Custom RGB Fade
````python
magicBuild.sleep = 0.1

# Calculates from each RGB value - 100 and + 100
magicBuild.fadeIntense = 100

# disable R,G or B with 0 (This value does not change then)
magicBuild.enableR = 0
magicBuild.enableG = 0
magicBuild.enableB = 0

# RGB Code
magicBuild.fade(100,100,100)
````

send [Turn on]
````python
magicHome.send(0x71, 0x23, 0x0F, 0xA3)
````
