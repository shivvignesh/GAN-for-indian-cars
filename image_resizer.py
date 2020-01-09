from PIL import Image
import os,sys
import cv2

path="C:/EVA 2.0/session 19/indian cars dataset"

j = 0

for i,item in enumerate(os.listdir(path)):
	
	img_path=os.path.join(path+"/"+item)
	print(img_path)
	im=Image.open(img_path)
	f,e=os.path.splitext(img_path)
	if e == '.png' or e == '.webp':
		continue
	newim = im.resize((64,64),Image.ANTIALIAS)
	# im.thumbnail((400,400))
	if j in range(0,10):
		newim.save('C:/EVA 2.0/session 19/resized_images'+'/'+'img_00'+str(j+1)+'.jpg','JPEG',quality=90)
	elif j in range(10,100) :
		newim.save('C:/EVA 2.0/session 19/resized_images'+'/'+'img_0'+str(j)+'.jpg','JPEG',quality=90)
	else:
		newim.save('C:/EVA 2.0/session 19/resized_images'+'/'+'img_'+str(j)+'.jpg','JPEG',quality=90)	

	j += 1	