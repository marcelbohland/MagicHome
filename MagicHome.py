import time
import socket
import struct
import threading

ip = "192.168.0.1"

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'



def check_range(number):
    if number < 0:
        return 0
    elif number > 255:
        return 255
    else:
        return number


def checksumme(bytes):
    return sum(bytes) & 0xFF


class MagicHome:
    def __init__(self):
        self.policeMode = 0
        self.fade = 0
        self.pulse = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Open connection...")
            self.s.connect((ip, 5577))
            print("Connection open")
        except socket.error as e:
            print(bcolors.WARNING + "exception socket.error : %s" % e)
            if self.s:
                self.s.close()

    def send(self, *bytes):
        message_length = len(bytes)
        self.s.send(struct.pack("B" * message_length, *bytes))

    def turn_on(self):
        self.send(0x71, 0x23, 0x0F, 0xA3)
        print(bcolors.OKGREEN + "turn_on")

    def turn_off(self):
        self.send(0x71, 0x24, 0x0F, 0xA4)
        print(bcolors.OKGREEN + "turn_off")

    def changeColor(self, r, g, b):
        result_r = check_range(r)
        result_g = check_range(g)
        result_b = check_range(b)
        message = [0x31, result_r, result_g, result_b, 0x00, 0x0f]
        summe = checksumme(message)
        self.send(0x31, result_r, result_g, result_b, 0, 0x00, 0x0f, summe)
        print(bcolors.OKGREEN + "Color Changed to R:" + str(result_r) + " G:" + str(result_g) + " B:" + str(result_b))

    # Effects

    def police(self):
        print("Police Mode:")
        self.policeMode = 1
        while self.policeMode == 1:
            self.changeColor(255, 0, 0)
            time.sleep(0.1)
            self.changeColor(0, 0, 255)
            time.sleep(0.1)

    def stopPolice(self):
        self.policeMode = 0
        print("stop")


    def rgbfade(self):
        print("RGB Fade")
        self.fade = 1
        i = 1
        lab = 1
        r = 255
        g = 0
        b = 0
        while self.fade == 1:
            i += 1
            if i <= 255:
                if lab == 1:
                    g = i
                if lab == 2:
                    r = 255 - i
                if lab == 3:
                    b = i
                if lab == 4:
                    g = 255 - i

            if i > 255:
                lab += 1
                i = 0
                if lab == 5:
                    lab = 1


            self.changeColor(r, g, b)

            time.sleep(0.1)

            if self.fade == 0:
                break

    def stopRgbFade(self):
        self.fade = 0

    def rgbPulse(self):
        print("RGB Fade")
        self.pulse = 1
        i = 1
        lab = 1
        r = 0
        g = 0
        b = 0
        while self.pulse == 1:
            i += 1
            if i <= 255:
                if lab == 1:
                    r = i
                if lab == 2:
                    r = 255 - i
                if lab == 3:
                    g = i
                if lab == 4:
                    g = 255 - i
                if lab == 5:
                    b = i
                if lab == 6:
                    b = 255 - i

            if i > 255:
                lab += 1
                i = 0

                if lab == 7:
                    lab = 1


            self.changeColor(r, g, b)

            time.sleep(0.0001)

            if self.pulse == 0:
                break

    def stopRgbPulse(self):
        self.pulse = 0



#ip = "192.168.0.1"
# Turn on/off
# magicHome.turn_on()
# magicHome.turn_off()



# Change Color
# magicHome.changeColor(0,0,255)


# police
# police = threading.Thread(name='police', target=magicHome.police)
# police.start()
# time.sleep(1)
# magicHome.stopPolice()

# RGB Fade
# rgbFade = threading.Thread(name='rgbfade', target=magicHome.rgbfade)
# rgbFade.start()
# time.sleep(10)
# magicHome.stopRgbFade()

# RGB Pulse
# rgbPulse = threading.Thread(name='rgbPulse', target=magicHome.rgbPulse)
# rgbPulse.start()
# time.sleep(10)
# magicHome.stopRgbPulse()

# send [Turn on]
# magicHome.send(0x71, 0x23, 0x0F, 0xA3)
