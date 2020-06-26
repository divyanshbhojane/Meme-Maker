from PIL import Image, ImageDraw, ImageFont
import textwrap

def addtext(im):
	top_text=input("Enter top text : ")
	bottom_text=input("Enter bottom text : ")

	font_path='./fonts/impact/impact.ttf'
	font_size=8
	newim=im.copy()
	draw = ImageDraw.Draw(newim)
	image_width, image_height = newim.size
	
	# load font
	font = ImageFont.truetype(font=font_path, size=int(image_height*font_size)//100)

	# convert text to uppercase
	top_text = top_text.upper()
	bottom_text = bottom_text.upper()

	# text wrapping
	char_width, char_height = font.getsize('A')
	chars_per_line = image_width // char_width
	top_lines = textwrap.wrap(top_text, width=chars_per_line)
	bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

	# draw top lines
	y = 10
	for line in top_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='black', font=font)
	    y += line_height

	# draw bottom lines
	y = image_height - char_height * len(bottom_lines) - 15
	for line in bottom_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill='white', font=font)
	    y += line_height

	# save meme
	newim.show()
	stack.append(newim)
	return newim
	

def rot(im):
	global stack
	ang=input("Enter angle to rotate :")
	newim=im
	newim.rotate(int(ang)).show()
	print('keep changes? (y/n)')
	if ask():
		newim=newim.rotate(int(ang))
		stack.append(newim)
	return newim

def undo(im):
	global stack
	if len(stack)>1:
		stack.pop()
	return stack[-1]

def savefn(im):
	global stack
	im.save('meme-' + stack[0].filename.split('/')[-1])
	return im	

def cropp(im):
	global stack
	newim=im
	image_width, image_height = newim.size
	x1,y1=map(int,input("Enter space seperated cordinates of top left corner:").split())
	x2,y2=map(int,input("Enter space seperated cordinates of bottom right corner:").split())
	x1=image_width*x1/100
	x2=image_width*x2/100
	y1=image_height*y1/100
	y2=image_height*y2/100
	newim=newim.crop((x1,y1,x2,y2))
	newim.show()
	stack.append(newim)
	return newim

def show(im):
	im.show()
	return im

def ask():
	while True:
		inp=input()
		if inp=='y':
			return True
		if inp=='n':
			return False
		print("Wrong input!! Enter (y/n) again")


if __name__ == '__main__':
	global stack
	stack=[]
	image_path=input("Enter image path :")
	im=Image.open(image_path)
	stack.append(im)
	im.show()
	sw={0:None,1:rot,2:undo,3:addtext,4:cropp,5:savefn,6:show}
	ch=1
	while True:
		ch=input("Opertaions :\n0.quit\n1.Rotate image\n2.Undo\n3.Add text\n4.crop\n5.Save meme\n6.Show meme\nEnter choice: ")
		if ch=='0':
			break
		im=sw[int(ch)](im)

