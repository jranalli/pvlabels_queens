import os

from PIL import Image
import numpy as np


def zip_to_png(source_dir, out_dir, include_ir=True):
    """
    Convert 4 channel JPEG2000 images from the NYC dataset into PNG images more
    accessible by software tools. Options exist for writing 4 channel RGB+IR
    images or 3 channel RGB images.

    Parameters
    ----------
    source_dir: str
        full path to the unzipped file downloaded from the database
    out_dir: str
        full path output directory for the png images
    include_ir: bool (default True)
        If true, the output images will have 4 channels (RGB+IR), otherwise the
        output images will have 3 channels (RGB).
    """

    # Make sure our output directories exist
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    # Get all jp2 files in the directory
    fns = [f for f in os.listdir(source_dir) if f.endswith(".jp2")]

    for fn in fns:
        fullfn = os.path.join(source_dir, fn)
        print(fn)
        # Read it in as a PIL object
        with (Image.open(fullfn) as pic):

            # Convert to NumPy Array for manipulation
            x, y = pic.size
            a = np.array(pic.getdata()).reshape(x, y, 4)

            if include_ir:
                im = Image.fromarray(a.astype('uint8'))
            else:
                im = Image.fromarray(a[:, :, :-1].astype('uint8'))

            fn_out = os.path.join(out_dir, fn).replace(".jp2", ".png")
            im.save(fn_out)


if __name__ == '__main__':
    indir = r"/path/to/unzipped"
    outdir = r"/path/to/output"

    zip_to_png(indir, outdir, include_ir=True)