import sys
import os
import shutil
import zipfile
from pathlib import Path
from PIL import Image
from zip_processor import ZipProcessor


class ScaleZip(ZipProcessor):
    def __init__(self, zipname, w_size, h_size):
        super().__init__(zipname)
        # self.zipname = zipname
        self.w_size = w_size
        self.h_size = h_size
        self.temp_directory = Path("unzipped-{}".format(
                zipname[:-4]))


    def process_files(self):
        '''
        Scale each image in the directory to input value.
        '''
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((self.w_size, self.h_size))
            scaled.save(str(filename))
