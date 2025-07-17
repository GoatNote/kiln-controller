import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering

# Define GPIO pin (change to your desired pin)
SSR_PIN = 26 
LED_PIN = 13

# Setup GPIO pin as output
GPIO.setup(SSR_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    # Turn GPIO on (HIGH)
    print("Turning GPIO ON")
    GPIO.output(SSR_PIN, GPIO.HIGH)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(5)  # Keep on for 2 seconds
    
    # Turn GPIO off (LOW)
    print("Turning GPIO OFF")
    GPIO.output(SSR_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)  # Keep off for 2 seconds
    
    # You can repeat or add more control logic here
    
except KeyboardInterrupt:
    print("\nScript interrupted by user")
    
finally:
    # Clean up GPIO settings
    GPIO.cleanup()
    print("GPIO cleanup completed")
