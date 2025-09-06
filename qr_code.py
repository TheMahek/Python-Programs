import qrcode

website_link = 'https://youtu.be/xVVHZ_CJllg?si=Q1QPSaNIfzwPoiOp'

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('youtube_qr.png')

