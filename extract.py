# usage: python3 extract.py filename
import sys
from pidng.core import RPICAM2DNG
d=RPICAM2DNG()
file=str(sys.argv[1])
d.convert(file)

