from PIL import Image, ImageFont, ImageDraw, ExifTags
import os
import glob

def read_directory(pathname, file_types):
	files = list()

	for file in glob.glob(os.path.join(pathname, file_types)):
		files.append({
			"name": file.replace(pathname+"/", ""),
			"path": file
		})

	return files


def main():
	input = "./source"
	output = "./output"
	file_type = "jpg"

	pictures = read_directory(input, "*.%s" % file_type)

	for picture in pictures:
		img = Image.open(picture['path'])

		exif = {
		    ExifTags.TAGS[k]: v
		    for k, v in img._getexif().items()
		    if k in ExifTags.TAGS
		}

		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("Courier_Prime.ttf", 128)

		draw.text((0, 0),exif['DateTimeOriginal'],(255,255,0),font=font)

		img.save('%s/%s' % (output,picture['name']))

main()

