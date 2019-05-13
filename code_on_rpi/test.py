#!/usr/bin/env python3

# Starting point: https://raspberrypi.stackexchange.com/questions/26714/can-i-record-a-24-hour-video-on-the-raspberry-pi-with-camera-module
import os
import datetime
import picamera

def create_tonight_folder(directory_path):
	if not os.path.exists(directory_path):
		os.makedirs(directory_path)

def create_outputs(directory_path, hours_int):
	for i in range(hours_int):
		yield "{}/{:02d}.h264".format(directory_path,i)

def capture_night(directory_path, hours_int):
	with picamera.PiCamera() as camera:
		camera.resolution = (360, 640)
		camera.framerate = 24
		for filename in camera.record_sequence(
	       		create_outputs(directory_path, hours_int),
			quality=20, bitrate=750000):
			camera.wait_recording(60 * 30) #60 * 60
	
if __name__ == "__main__":
	storage_s = "/home/pi/sleeper/data/"

	now = datetime.datetime.now()
	night_s = now.strftime("%Y-%m-%d")
	directory_path = os.path.dirname(storage_s + "/" + night_s + "/")
	create_tonight_folder(directory_path)

	hours = 3
	capture_night(directory_path, hours)
