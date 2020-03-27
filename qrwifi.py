#!/usr/bin/env python3
import sys
try:
    import qrcode
    import qrcode.image.svg
    import argparse
    import imgcat
except ImportError as error:
    print(f"{error};\npip3 install {error.name} ")
    sys.exit()


class qrwifi():
    def __init__(self, ssid=None, security=None, password=None, save=None):
        self.ssid=ssid
        self.security=security
        self.password=password
        self.data = f'WIFI:S:{self.ssid};T:{self.security};P:{self.password};;'
        self.create = True if save else False

        self.img()
        self.svg()

    def img(self):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qrcode.make(self.data)
        if self.create: img.save('qrcode.jpg')
        imgcat.imgcat(img.get_image())

    def svg(self):
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(self.data, image_factory = factory)
        if self.create: img.save('qrcode.svg')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate a printable QR code for sharing your wifi with friends.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s','--security', choices=['WEP', 'WPA'], help='Security Protocol', default='WPA')
    parser.add_argument('-i','--ssid',     type=str, help='SSID to join', default='foo')
    parser.add_argument('-p','--password', type=str, help='SSID Password', default='bar')
    parser.add_argument('-c','--create', action='store_true', default=False, help='boolean, save qrcode to disk')
    args = parser.parse_args()

    qrwifi(ssid=args.ssid, security=args.security, password=args.password, save=args.create)
