import os
from PIL import Image

images = ['img1.jpg','img2.jpg']
for infile in images:
  f, e = os.path.splitext(infile)
  outfile = f + '.png'
  if infile != outfile:
    try:
      with Image.open(infile) as image:
        image.save(outfile, 'PNG')
        print(f'successfully converted {infile} to {outfile}')
    except OSError:
      print(f'conversion failed for {infile}')
