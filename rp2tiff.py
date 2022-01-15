from libtiff import TIFF
from libtiff import libtiff_ctypes
from picamraw import PiRawBayer, PiCameraVersion


raw_bayer = PiRawBayer(
    filepath='test.raw',  # A JPEG+RAW file, e.g. an image captured using raspistill with the "--raw" flag
    camera_version=PiCameraVersion.V2,
    sensor_mode=0
)
data = raw_bayer.bayer_array

tif = TIFF.open('test.raw.tif', mode='w')

width = data.shape[0]
height = data.shape[1]

tif.SetField(libtiff_ctypes.TIFFTAG_IMAGEWIDTH, width)
tif.SetField(libtiff_ctypes.TIFFTAG_IMAGELENGTH, height)
tif.SetField(libtiff_ctypes.TIFFTAG_SAMPLESPERPIXEL, 1)
tif.SetField(libtiff_ctypes.TIFFTAG_BITSPERSAMPLE, 16)

tif.SetField(libtiff_ctypes.TIFFTAG_SAMPLEFORMAT, libtiff_ctypes.SAMPLEFORMAT_UINT)
tif.SetField(libtiff_ctypes.TIFFTAG_ORIENTATION, libtiff_ctypes.ORIENTATION_TOPLEFT)
tif.SetField(libtiff_ctypes.TIFFTAG_PLANARCONFIG, libtiff_ctypes.PLANARCONFIG_CONTIG)
tif.SetField(libtiff_ctypes.TIFFTAG_PHOTOMETRIC, libtiff_ctypes.PHOTOMETRIC_MINISBLACK)
tif.SetField(libtiff_ctypes.TIFFTAG_COMPRESSION, libtiff_ctypes.COMPRESSION_NONE)

# static const short bayerPatternDimensions[] = { 2, 2 };
bayerPatternDimensions = (2,2)
tif.SetField(libtiff_ctypes.TIFFTAG_CFAREPEATPATTERNDIM, bayerPatternDimensions)
tif.SetField(libtiff_ctypes.TIFFTAG_CFAPATTERN, b"\00\01\01\02") # //RGGB


#about the simplest TIFF format to write, one big strip:
# tif.SetField(libtiff_ctypes.TIFFTAG_ROWSPERSTRIP, height);


#import pdb; pdb.set_trace()
tif.write_image(data)
