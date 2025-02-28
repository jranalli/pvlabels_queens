# pvlabels_queens
Code for working with the PV segmentation label dataset for Queens, NY

# Contents
- `create_masks.py`
  - Convert the json label files into binary masks representing the pv locations.
- `proj_json_to_shp.py`
  - Convert the json label files into a shapefile for use in GIS software.

# Setup Instructions
Open a terminal and run the following command to install dependencies.
```
pip install -r requirements.txt
```

# Usage
Download and extract the imagery data from the New York GIS Clearinghouse. The labels are based on [2018 Orthoimagery for the Borough of Queens](https://gisdata.ny.gov/ortho/nysdop9/new_york_city/spcs/zips/boro_queens_sp18.zip).

Download the JSON label data from the label Zenodo repository.

Edit the directories listed at the bottom of `create_masks.py` or `proj_json_to_shp.py` to point to the correct directories. Run them from the command prompt, e.g.:
```
python create_masks.py
```
