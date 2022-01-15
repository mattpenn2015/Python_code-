#
#
# This is a command line routine to average a set of FITS file darks
# and output the average to another FITS file
#
# python3 make_avg_dark.py input_file first_dark number_darks output_file
#
# input_file is partial file name without number and without .fits
#
# first_dark is the number of the first dark in the format used in filename
#
# number_darks is the integer number of darks to average, must be consecutive
#
# output_file is the full name of the output FITS file.
#
# MJP 20211224



import sys
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

fits_filename=sys.argv[1]
first_dark=sys.argv[2]
number_darks=int(sys.argv[3])
output_filename=sys.argv[4]

number_first=int(first_dark)
nchar=len(first_dark)

filename=fits_filename+str(first_dark).zfill(nchar)+'.fits'
print('Reading: ' + filename)
img=fits.getdata(filename)
image_data=img.astype(np.float)/float(number_darks)

for i in range(1, number_darks):
    fnum=str(number_first+i).zfill(nchar)
    filename=fits_filename+fnum+'.fits'
    print('Reading: ' + filename)
    print(str(i+1)+' out of '+str(number_darks)+' files')
    img=fits.getdata(filename)
    image_data=image_data+(img.astype(np.float)/float(number_darks))

hdr=fits.Header()
fits.writeto(output_filename,image_data,hdr,overwrite=True)
print('Writing: ' + output_filename)
