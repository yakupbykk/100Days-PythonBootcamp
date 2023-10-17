import pyqrcode

url= input("Qr olusturmak icin url girin: ")

qr_code = pyqrcode.create(url)
qr_code.svg("qrcode.svg",scale=10)

