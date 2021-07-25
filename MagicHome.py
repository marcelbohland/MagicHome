import time
import socket
import struct
import random

ip = "192.168.0.1"


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[31m'


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
        self.random = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Open connection...")
            self.s.connect((ip, 5577))
            print("Connection open")
        except socket.error as e:
            print(bcolors.ERROR + "exception socket.error : %s" % e)
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

    def rgbfade(self, sleep=0.1):
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

            time.sleep(sleep)

            if self.fade == 0:
                break

    def stopRgbFade(self):
        self.fade = 0

    def rgbPulse(self, sleep=0.0001):
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

            time.sleep(sleep)

            if self.pulse == 0:
                break

    def stopRgbPulse(self):
        self.pulse = 0

    def Random(self, sleep=1):
        print("RGB Random")
        self.random = 1

        while self.random == 1:

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            self.changeColor(r, g, b)

            time.sleep(sleep)

            if self.random == 0:
                break

    def stopRandom(self):
        self.random = 0


class MagicBuild:
    enableR = 1
    enableG = 1
    enableB = 1

    fadeIntense = 1
    sleep = 0.1

    # Create a self designed fade effect
    def fade(self, R, G, B):

        magicHome = MagicHome()

        startR = R - self.fadeIntense
        startG = G - self.fadeIntense
        startB = B - self.fadeIntense

        stopR = R + self.fadeIntense
        stopG = G + self.fadeIntense
        stopB = B + self.fadeIntense

        # check if the values are in the range between 0 and 255
        if startR >= 0 and startR <= 255 and startG >= 0 and startG <= 255 and startB >= 0 and startB <= 255 and stopR <= 255 and stopG <= 255 and stopB <= 255:
            fade = 1

            while fade == 1:
                # Fade +1 if R,G or B is not disabled
                if self.enableR == 1:
                    startR = startR + 1
                    sendR = startR + 1
                else:
                    sendR = R
                if self.enableG == 1:
                    startG = startG + 1
                    sendG = startG + 1
                else:
                    sendG = G
                if self.enableB == 1:
                    startB = startB + 1
                    sendB = startB + 1
                else:
                    sendB = B

                # End the While
                if startR <= stopR and startG <= stopG and startB <= stopB:

                    # End the While
                    if self.enableR == 0 and self.enableG == 0 and self.enableB == 0:
                        break
                    # Change Color
                    magicHome.changeColor(sendR, sendG, sendB)
                    print("R: " + str(sendR) + " G: " + str(sendG) + " B: " + str(sendB))
                else:
                    break

                time.sleep(self.sleep)
        else:
            print(bcolors.ERROR + "Error 0x020203: Only numbers between 0 - 255 and fadeIntense +/- with result min. 0 or max. 255 are allowed")
