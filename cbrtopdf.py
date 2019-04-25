#!/usr/bin/python

import sys, os
import patoolib
import img2pdf
import shutil

def image_extractor(source, tmp_folder):
    # print("Extracting "+source+" to "+tmp_folder)
    patoolib.extract_archive(source,outdir=tmp_folder)
    # print("Done")

def convert_extension(source):
    raw = os.path.splitext(source)[0]
    return str(raw+".pdf")


def image_to_pdf(image_list_path,output_name,tmp_folder):
    os.chdir(tmp_folder)
    print(output_name)
    with open(output_name, "wb") as f:
        f.write(img2pdf.convert([i for i in image_list_path if i.endswith(".jpg")]))

SOURCE=sys.argv[1]
SOURCE_PATH=os.path.dirname(SOURCE)

if SOURCE_PATH == "":
    SOURCE_PATH = os.getcwd()
    SOURCE= SOURCE_PATH + "/" + sys.argv[1]
    TMP_FOLDER = SOURCE_PATH + "/" + ".tmp_images"

else:
    if SOURCE_PATH != "":
        TMP_FOLDER = SOURCE_PATH + "/" + ".tmp_images"

os.makedirs(TMP_FOLDER)

image_extractor(SOURCE, TMP_FOLDER)

image_list_path=sorted(os.listdir(TMP_FOLDER))

converted_name=convert_extension(SOURCE)

image_to_pdf(image_list_path,converted_name,TMP_FOLDER)

shutil.rmtree(TMP_FOLDER)
