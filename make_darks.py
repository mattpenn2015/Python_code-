#
#
# routine for use in Python IDLE
# file names and numeric values are hard coded into this routine
#
#
# MJP 20211214

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

fits_filename='/home/astroberry/Light_20211218/solar_Light_'
first_dark='1601'
number_first=int(first_dark)
number_darks=12
output_filename='/home/astroberry/Desktop/data_dark_20211218.fits'

nchar=len(first_dark)

filename=fits_filename+str(first_dark).zfill(nchar)+'.fits'
img=fits.getdata(filename)
image_data=img.astype(np.float)/float(number_darks)
#plt.plot(image_data[:,600])
#plt.show()


for i in range(1, number_darks):
    fnum=str(number_first+i).zfill(nchar)
    filename='/home/astroberry/Light_20211218/solar_Light_'+fnum+'.fits'
    print(filename)
    img=fits.getdata(filename)
    image_data=image_data+(img.astype(np.float)/float(number_darks))
    print(i+1)

print(type(image_data))
print(image_data.shape)
#plt.imshow(image_data,cmap='gray')
#plt.colorbar()
plt.plot(image_data[:,600])
plt.show()

hdr=fits.Header()
fits.writeto(output_filename,image_data,hdr,overwrite=True)
