import qrcode
import  image

qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr  code high the number bigger the code image and compiled picture
    box_size= 10,
    border = 5
)
data ="https://www.youtube.com/watch?v=JxzZxdht-XY&t=335s"
# As i have given the path of my channel
# if you have don't  want to redirect and create for normal text

qr.add_data(data)
qr.make(fit = True)
img= qr.make_image(fill="black",back_color="white")
img.save("img.png")