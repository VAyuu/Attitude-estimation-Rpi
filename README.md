# Attitude-estimation-Rpi

Estimates the euler angles of the mpu9250 sensor. Uses complimentary filter to fuse the accelerometer and gyroscope data to reliably estimate the angles(in degrees).
Pitch is used to further control a servo arm to demonstrate the reliability of the code in real-time applications.

#--Wiring--#

MPU9250--RPi3

SDA--SDA

SCL--SCL

VCC--3V

GND--GND

Servo--RPi3



#--Enable I2C Communication--#

>> Type raspi-config >> Select Advanced options >> Select I2C

#--Download the main.py, imulib module and complimentary module present in the repo. into the RPi in a single folder--#

Execute main.py in the terminal and observe the servo replicating the pitch of the MPU9250 sensor.

