# cbrtopdf
Tool to convert cbr format in pdf format

## Installation 

```pip install -r requirements.txt```

## Usage

```python cbrtopdf.py <file.cbr>```

## How it works

This script takes the cbr file as a command line parameter, the cbr file will be unpacked inside a hidder directory named  ```.tmp_images```.
The folder will be created in the same path of the cbr file and it contains a list of jpg images(the pages of the cbr file).
A pdf file will be created using the jpg images. When the creation is complete the ```.tmp_images``` folder will be erased
