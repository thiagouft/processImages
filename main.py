from PIL import Image, ImageFilter

if __name__ == '__main__':

	print("Processamento de Imagens.")
	#Read image
	im = Image.open( 'img/dell.jpg')
	#Display image
	im.show()

	#Applying a filter to the image
	im_sharp = im.filter( ImageFilter.SHARPEN )
	#Saving the filtered image to a new file
	im_sharp.save( 'exitImage.jpg', 'JPEG' )

	#Splitting the image into its respective bands, i.e. Red, Green,
	#and Blue for RGB
	r,g,b = im_sharp.split()

	#Viewing EXIF data embedded in image
	exif_data = im._getexif()
	exif_data
