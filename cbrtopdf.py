#!/usr/bin/python

import os
import shutil
import argparse
import patoolib
from PIL import Image
from PyPDF2 import PdfFileMerger


def load_config():
    options = argparse.ArgumentParser()
    options.add_argument("--output", '-o',
            help="Select a destination output file. Default: current directory")
    options.add_argument("--source", '-s',
                         help="Select source file")

    return options.parse_args()


def image_extractor(source, destination_folder):
    patoolib.extract_archive(source, verbosity=-1, outdir=destination_folder)


def convert_extension_to_pdf(source):
    raw = os.path.splitext(source)[0]
    return str(raw + ".pdf")


def image_to_pdf(image_list, tmp_folder, output_name):
    os.chdir(tmp_folder)

    for image in image_list:
        image1 = Image.open(image)
        im1 = image1.convert('RGB')
        im1.save(image + ".pdf")
        os.remove(image)

    pdf_list = sorted(os.listdir(tmp_folder))
    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(open(pdf, 'rb'))

    with open(output_name, "wb") as destination_file:
        merger.write(destination_file)


def main():
    config = load_config()

    filepath = config.source

    if os.path.dirname(filepath) == '' or os.path.dirname(filepath) is None:
        filepath = os.getcwd() + "/" + filepath

    temp_folder_name = ".cbrtopdf_temp_folder"

    temp_folder_path = os.path.dirname(filepath) + "/" + temp_folder_name

    if os.path.exists(temp_folder_path):
        shutil.rmtree(temp_folder_path)

    os.makedirs(temp_folder_path)

    image_extractor(filepath, temp_folder_path)

    image_list = sorted(os.listdir(temp_folder_path))

    if config.output is None:
        destination_file = convert_extension_to_pdf(filepath)
    else:
        destination_file = config.output

    image_to_pdf(image_list, temp_folder_path, destination_file)

    shutil.rmtree(temp_folder_path)


if __name__ == '__main__':
    main()
