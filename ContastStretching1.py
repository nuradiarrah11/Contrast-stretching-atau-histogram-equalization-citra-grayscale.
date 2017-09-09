import scipy.misc

#membuka image baru dan mengkonversinya ke Grayscale
from scipy.misc.pilutil import Image

#Konversi ke Array
var_gambar = Image.open("MyPic1.jpg").convert('L')

var_hasil1 = scipy.misc.fromimage(var_gambar)
#Perlihatkan Nilai Array
#temukan nilai maksimun dan minimun pixel
#Nilai Maksimal Pixel
var_b = var_hasil1.max()

#Nilai Minimum pada Pixel 
var_a = var_hasil1.min()

#konversi hasil1 ke int
var_c = var_hasil1.astype(int)
#transformasi Contrast Stretching
var_hasil2 = (var_c-var_a)*255/(var_b-var_a)
#konversi dari Array ke Image
var_gambar_hasil = scipy.misc.toimage(var_hasil2)
var_gambar_hasil.save("MyPic2.jpg")
print ("nilai hasil1",var_hasil1)
print ("nilai pixel minimum adalah :",var_a)
print ("nilai pixel maximal adalah :",var_b)
print ('nilai c adalah :',var_c)
print (var_hasil2)

