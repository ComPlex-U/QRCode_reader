from pyzbar.pyzbar import decode
from PIL import Image

d=decode(Image.open('#image  address and name'))
print(d[0].data.decode())