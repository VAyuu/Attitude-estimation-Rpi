import RPi.GPIO as GPIO
import time

from imulib import MPU9250
from complementary import COMPLEMENTARY

# create IMU class to handle raw data
imu = MPU9250()

# initialize IMU
imu.init_imu()

# calibrate IMU
imu.calibrate_gyro()
imu.calibrate_accel()
imu.calibrate_mag()

# complementary filter to fuse data
sensor_fusion = COMPLEMENTARY()

pin = 11
pwm_frequency = 50
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, pwm_frequency)
pwm.start(0)

while True:
    try:

        # check if data is ready
        if imu.is_data_ready():
            # get latest gyro data
            imu.update()
            # use the complementary filter to get euler angles
            sensor_fusion.euler_comp_update(accel_data=imu.accel_data, gyro_data=imu.gyro_data)
            roll = sensor_fusion.euler[0]
            pitch  = sensor_fusion.euler[1]
            yaw = sensor_fusion.euler[2]
            # print outputs
            print(f"Roll: {roll}, Pitch: {pitch}, Yaw: {yaw}")

            #activate the servo motor according to the pitch.
            duty_cycle = pitch*((10 - 5)/180) + 5
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(1)

    except KeyboardInterrupt:
        print("exiting the program!")
        break


pwm.ChangeDutyCycle(5)
time.sleep(1)
GPIO.cleanup()
