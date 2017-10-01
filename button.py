import mraa
import subprocess

print(mraa.getVersion())

bashCommand = "./takePicture"

led  = mraa.Gpio(23)
led.dir(mraa.DIR_OUT)
led.write(0)
        
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

while True:
        touchButton = int(touch.read())
        if(touchButton == 1):
            led.write(1)
            process =  subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        else:
            led.write(0)
            
