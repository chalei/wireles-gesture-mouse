import serial
import keyboard

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = 'COM6'
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 115200


def main():
	ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
	while True:
		baca = ser.readline().decode('utf-8')
		reading = int(baca)
	
		print(reading)
		
		if reading == 1:
			print("atas")
			keyboard.press_and_release('up')
		elif reading == 2:
			keyboard.press_and_release('down')
		
		#keyboard.wait('esc')


if __name__ == "__main__":
    main()
