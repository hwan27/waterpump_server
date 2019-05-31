from django.shortcuts import render
from django.http import HttpResponse
import serial
# Create your views here.

ser = serial.Serial('COM7', 115200, timeout=0,
                    parity=serial.PARITY_EVEN, rtscts=1)


def index(request):
    # ser.write(str.encode('AT\r'))
    ser.write(str.encode("AT*MOREQ=01093439315, hello\r"))
    data = ser.read()
    return HttpResponse(data)
