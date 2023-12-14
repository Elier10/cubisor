import serial
import time
import struct

def CUBISOR():
    # Puerto
    port = serial.Serial(
        port='COM6',
        baudrate=9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        timeout=1
    )
    # Inicio de la Conexión con el CUBISOR
    Disparo = "@01WR0300000146*\r"
    mensaje_codificado = Disparo.encode('ascii')
    port.write(mensaje_codificado)
    # Respuesta recibida del CUBISOR
    data = port.readline().decode('utf-8').strip()
    #print("Primer respuesta:", data)
    time.sleep(10)
    if data == "@01WR0044*":
        Lectura = "@01RD0200002057*\r"
        mensaje_codificado = Lectura.encode('ascii')
        port.write(mensaje_codificado)
        result = port.readline().decode('utf-8').strip()
        #print("Segunda respuesta:", result)
        if result[0:7] == "@01RD00":
            Num1 = result[11:15] + result[7:11]
            Num2 = result[19:23] + result[15:19]
            Num3 = result[27:31] + result[23:27]
            Num4 = result[35:39] + result[31:35]
            Num5 = result[43:47] + result[39:43]
            Num6 = result[51:55] + result[47:51]
            Num7 = result[59:63] + result[55:59]
            Num8 = result[67:71] + result[63:67]
            Num9 = result[75:79] + result[71:75]
            Num10 = result[83:87] + result[79:83]
            Registros = []
            Registros.append(struct.unpack('!f', bytes.fromhex(Num1))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num2))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num3))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num4))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num5))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num6))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num7))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num8))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num9))[0])
            Registros.append(struct.unpack('!f', bytes.fromhex(Num10))[0])


    #Cierre de la comunicación
    port.close()
    return Registros

