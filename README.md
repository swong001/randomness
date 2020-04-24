Python3 Command line Utility to generate QR Codes that can be scanned with your mobile device (laptop, cell phone) to quickly connect to a WIFI network.

QRCodes for Wifi are based on the format: `WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;H:<true|false|>;`
https://en.wikipedia.org/wiki/QR_code#Wi-Fi_network_login

Can also be used to display images on your command-line if using MacOS and iTerm2.

Generates two types of qrcodes, jpg and svg.

The svg image uses `qrcode.constants.ERROR_CORRECT_H` to allow for 30% or less errors to be corrected from the QR Code image (incase of smudging if printed)

Sample QR Codes Generated:

JPEG Image:

![jpeg qrcode](qrcode.jpg)


SVG Image:

![svg qrcode](qrcode.svg)
