# pvlabels_queens
Code for working with the PV segmentation label dataset for Queens, NY

# Contents
- `convert_images.py`
  - Convert the original JPEG2000 imagery from the New York GIS Clearinghouse into a PNG format for training.
- `create_masks.py`
  - Convert the json label files into binary masks representing the pv locations.
- `proj_json_to_shp.py`
  - Convert the json label files into a shapefile for use in GIS software.

# Setup Instructions
Note that conda is preferred for installation due to `openjpeg` availability. Open a terminal and run the following command to install dependencies.
```
conda install --yes --file requirements.txt
```

# Usage
Download and extract the imagery data from the New York GIS Clearinghouse. The labels are based on [2018 Orthoimagery for the Borough of Queens](https://gisdata.ny.gov/ortho/nysdop9/new_york_city/spcs/zips/boro_queens_sp18.zip).

Download the JSON label data from the label Zenodo repository.

Edit the directories listed at the bottom of the desired script to point to the correct directories. Run them from the command prompt, e.g.:
```
python create_masks.py
```

## Creating Tiles
Since the 5000 x 5000 pixel images are too large for most deep learning frameworks, users likely will wish to split them into tiles. There are many ways to do so, but one pre-packaged option is the `split_image` package [Python Package Index](https://pypi.org/project/split-image/). Full details are available on the package site, but to quote their sample usage:

```python
from split_image import split_image

split_image(image_path, rows, cols, should_square, should_cleanup, [output_dir])
# e.g. split_image("bridge.jpg", 2, 2, True, False)
```

In the present case, it would be ideal to use splits that are an even multiple of 5000 pixels, e.g. 1000 x 1000, 625 x 625, 500 x 500 or 250 x 250. The same split parameters should be used for both the imagery and the masks to ensure consistency between the two for training.

# License
Licensed under GPL 3.0. 

Some code within `create_masks.py` is copied in whole or in part from [labelme](https://github.com/wkentaro/labelme), as noted in the function comments. 
