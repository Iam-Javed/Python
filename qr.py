import qrcode

img = qrcode.make( 'https://bit.ly/3jkjUo8')

img.save('myQRcode.png')

img.show()
