# import EAN13 from barcode module
from barcode import EAN13

# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

# Make sure to pass the number as string
print("Introduce un número:")
number=input()

if len(number)==1:
    number="00000000000"+number
elif len(number)==2:
    number="0000000000"+number
elif len(number)==3:
    number="000000000"+number
elif len(number)==4:
    number="00000000"+number
elif len(number)==5:
    number="0000000"+number
elif len(number)==6:
    number="000000"+number
elif len(number)==7:
    number="00000"+number
elif len(number)==8:
    number="0000"+number
elif len(number)==9:
    number="000"+number
elif len(number)==10:
    number="00"+number
elif len(number)==11:
    number="0"+number



# pass the number with the ImageWriter() as the
# writer
my_code = EAN13(number, writer=ImageWriter())

# Our barcode is ready. Let's save it.
my_code.save("new_code1")
print("Código generado exitosamente")