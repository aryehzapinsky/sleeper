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

def create_photos(directory_path, photos_num, hour_counter):
	for i in range(photos_num):
		yield "{}/{:02d}.jpg".format(directory_path,
						i+(photos_num*hour_counter))

def capture_night(directory_path_v, directory_path_p, hours_int):
	wait_time = 60
	photo_num = int((60*60)/wait_time)
	hour_counter = 0
	with picamera.PiCamera() as camera:
		camera.resolution = (1280, 720)
		camera.hflip = True
		camera.vflip = True
		camera.framerate = 10
		for filename in camera.record_sequence(
	       		create_outputs(directory_path_v, hours_int),
			quality=20, bitrate=750000):
			for photo in create_photos(directory_path_p,
							photo_num,
							hour_counter):
				camera.wait_recording(wait_time) #60 * 60
				camera.capture(photo, use_video_port=True)
			hour_counter += 1
	
if __name__ == "__main__":
	storage_v = "/media/pi/Snorlax/videos"
	storage_p = "/media/pi/Snorlax/photos"

	now = datetime.datetime.now()
	night_s = now.strftime("%Y-%m-%d")
	directory_path_v = os.path.dirname(storage_v + "/" + night_s + "/")
	directory_path_p = os.path.dirname(storage_p + "/" + night_s + "/")
	create_tonight_folder(directory_path_v)
	create_tonight_folder(directory_path_p)

	hours = 6
	capture_night(directory_path_v, directory_path_p, hours)
