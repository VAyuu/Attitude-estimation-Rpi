# Attitude-estimation-Rpi

>>Estimates the euler angles of the mpu9250 sensor. Uses complimentary filter to fuse the accelerometer and gyroscope data to reliably estimate the angles(in degrees).

>>Pitch is used to further control a servo arm to demonstrate the reliability of the code in real-time applications.

# Wiring 

## MPU9250--RPi3

>>SDA--SDA(PIN 3)

>>SCL--SCL(PIN 5)

>>VCC--3V3(PIN 1)

>>GND--GND (PIN 9)

Servo--RPi3

>> BLACK WIRE---GND(PIN 6)

>> RED WIRE---3V3(PIN 17)

>> YELLOW/ORANGE WIRE(SIGNAL)---GPIO 17(PIN 11)


# Enable I2C Communication

>> Type raspi-config >> Select Advanced options >> Select I2C

#--Download the main.py, imulib module and complimentary module present in the repo. into the RPi in a single folder--#

>>Execute main.py in the terminal and observe the servo replicating the pitch of the MPU9250 sensor.

