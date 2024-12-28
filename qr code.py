import qrcode

#taking UPI ID as a input
upi_id = input("enter your UPI ID =")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=Currency&tn=MESSAGE

#DEfining the payment URL based on the UPI ID nd the payment app
#You can modify these URLs based on the payment apps and want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr codes or each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
                       
#save the qr code to image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display the qrcode (you need to install PIl/PILLOW)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

