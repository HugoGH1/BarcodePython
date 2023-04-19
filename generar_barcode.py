# import EAN13 from barcode module
from barcode import EAN13
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

def crear_codigo():
    number = 1
    while number <= 700:
        ruta = crear_directorio(number)
        if len(str(number))==1:
            number="00000000000"+str(number)
        elif len(str(number))==2:
            number="0000000000"+str(number)
        elif len(str(number))==3:
            number="000000000"+str(number)
        elif len(str(number))==4:
            number="00000000"+str(number)
        elif len(str(number))==5:
            number="0000000"+str(number)
        elif len(str(number))==6:
            number="000000"+str(number)
        elif len(str(number))==7:
            number="00000"+str(number)
        elif len(str(number))==8:
            number="0000"+str(number)
        elif len(str(number))==9:
            number="000"+str(number)
        elif len(str(number))==10:
            number="00"+str(number)
        elif len(str(number))==11:
            number="0"+str(number)

        my_code = EAN13(number, writer=ImageWriter())
        my_code.save(ruta)
        print("Código generado exitosamente")
        number = int(number)+1


def crear_directorio(number):
    ruta = "./codigos/codigo"+str(number)
    return ruta


if __name__ == "__main__":
    crear_codigo()