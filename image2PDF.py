import os
from PIL import Image
import sys
import time

def get_input():
	logo = """

	░░▀░░█▀▀█░█▀▀▀░█░░█
	░░█▀░░▒▀▄░█░▀▄░█▄▄█
	░▀▀▀░█▄▄█░▀▀▀▀░▄▄▄▀

Easily convert your images to pdf for free!

	"""
	sys.stdout.write(logo)
	given_path = input("\r[+] Enter path to images: ").strip()
	destination_file = input("[+] Enter destination file: ").strip()
	
	try:
		#change the path to the given directory
		os.chdir(given_path)
		# check if provided destination ends with pdf extension
		if len(destination_file) > 0 and destination_file[:-4] != ".pdf":
			destination_file = destination_file + ".pdf"
		else:
			# if no destination is provided use a default one
			# get current time and replace spaces and colons with underscores
			current_time = time.ctime(time.time()).replace(":", " ")
			destination_file = "data_" + "_".join(current_time.split()) + ".pdf"
			print("  Changed destination file to {}".format(destination_file))
			
		convert_files(destination=destination_file)

	except FileNotFoundError:
		print("[-] Unable to change directory, please try again!")
		get_input()
	except OSError:
		print("[-] Unable to change directory, please try again!")
		get_input()
	except:
		print("[-] An error occurred, please try again!")
		get_input()

def convert_files(destination):
	#grab all images in the directory with png or jpg extensions
	image_files = [file for file in os.listdir() if file.endswith(".jpg") or file.endswith(".png")]

	if len(image_files) > 0:
		try:
			#open the images and convert them to RGB format
			opened_images = [Image.open(file).convert("RGB") for file in image_files]

			#save images to pdf format
			#start from the 2nd image to avoid saving the first image twice
			opened_images[0].save(destination, save_all=True, append_images=opened_images[1:])
			
		except Exception as e:
			print(e)
		print("  Done! Th@nk you for using i3 :)")
	else:
		print("[-] No images detected in directory! ")
		os.abort()

if __name__ == '__main__':
	get_input()