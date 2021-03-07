import sys
import os
import shutil
import zipfile
from zip_processor import ZipProcessor


class ZipReplace(ZipProcessor):
    def __init__(self, zipname, filename, search_string, replace_string):
        super().__init__(zipname)
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(
                filename)


    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()


    def find_replace(self):
        for filename in os.listdir(self.temp_directory):
            with open(self._full_filename(filename)) as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)

            with open(self._full_filename(filename), "w") as file:
                file.write(contents)
