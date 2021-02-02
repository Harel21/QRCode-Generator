import qrcode

print("    _|      _|                  _|                _|               ")       
print("    _|_|  _|_|    _|_|_|    _|_|_|    _|_|        _|_|_|    _|    _|  _| ") 
print("    _|  _|  _|  _|    _|  _|    _|  _|_|_|_|      _|    _|  _|    _|      ")
print("    _|      _|  _|    _|  _|    _|  _|            _|    _|  _|    _|      ")
print("    _|      _|    _|_|_|    _|_|_|    _|_|_|      _|_|_|      _|_|_|  _|  ")
print("                                                                _|      ")
print("                                                            _|_|        \n\n")
                                                                
print("    _|    _|                                _|    _|_|      _|  ")
print("    _|    _|    _|_|_|  _|  _|_|    _|_|    _|  _|    _|  _|_|  ")
print("    _|_|_|_|  _|    _|  _|_|      _|_|_|_|  _|      _|      _|  ")
print("    _|    _|  _|    _|  _|        _|        _|    _|        _|  ")
print("    _|    _|    _|_|_|  _|          _|_|_|  _|  _|_|_|_|    _|  ")

count = 0
while(True):
    FILE = f'QrCode({count}).png'
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=69, border=2)

    link = input("\n\nwhat is the link you want to make a QRcode: ")
    qr.add_data(f'{link}')
    qr.make(fit=True)

    clr = input("What is the fill_color you want: ")
    clr_b = input("What is the back_color you want: ")
    img = qr.make_image(fill_color=clr, back_color=clr_b)
    img.save(FILE)
    count+=1
    
    ans = input("Do you want to stop(y/n)\t")
    if ans == 'y':
        break