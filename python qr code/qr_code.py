import qrcode as qr


img = qr.make("https://www.youtube.com/@karishmaclasses")
img.save("karishma_classes.png")