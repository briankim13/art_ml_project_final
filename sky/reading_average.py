from PIL import Image 

img = Image.open('wave.jpg')
pix = img.load() 

r_total = 0
g_total = 0
b_total = 0 
pix_total = img.size[0]*img.size[1] 
print(pix_total) 

for i in range(img.size[0]):
	for j in range(img.size[1]):
	 	r_total += pix[i,j][0]
	 	g_total += pix[i,j][1]
	 	b_total += pix[i,j][2] 

r_avg = int(r_total / pix_total)
g_avg = int(g_total / pix_total)
b_avg = int(b_total / pix_total) 

print(r_avg, g_avg, b_avg) 
