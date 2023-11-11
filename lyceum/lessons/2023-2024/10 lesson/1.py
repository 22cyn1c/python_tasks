fp = open('input.bmp', 'rb')
sp = fp.read()
fp.close()
sp1 = bytes([255 - int(i) for i in sp[54:]])
sp0 = sp[:54] + sp1
fp = open('res.bmp', 'wb')
fp.write(sp0)
fp.close()