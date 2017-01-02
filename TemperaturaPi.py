import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT)

def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return round(float(cpu_temp)/1000)

def get_gpu_temp():
    RetornoSistema = os.popen('vcgencmd measure_temp | cut -d= -f2 | cut -d. -f1')
    Resultado = RetornoSistema.read()
    RetornoSistema.close()
    return int(Resultado.replace("\n", ""))

def main():
    if get_cpu_temp() > 55 or get_gpu_temp() > 55:
        print ("Cooler Ligado!")
        GPIO.output(40, GPIO.HIGH)
    else:
        print("Cooler Desligado!")
        GPIO.output(40, GPIO.LOW)
    print ("GPU = ", get_gpu_temp())
    print ("CPU = ", get_cpu_temp())
    
if __name__ == '__main__':
    while True:    
        main()
        time.sleep(60)
    GPIO.cleanup()
