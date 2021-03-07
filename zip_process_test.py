from scale_zip import ScaleZip
from zip_replace import ZipReplace

# ScaleZip
archive_name = input("Enter arcvive name: ")
width = input("Input width: ")
height = input("Input height: ")

#ScaleZip("lab4_1.zip", "C:\\Users\\ihort\\PycharmProjects\\test\\tmp", 1024, 768).process_zip()
if height.isdigit() and width.isdigit():
    width = int(width) # 140-7680
    height = int(height) # 192-4800

    if width in range(140, 7681) and height in range(192, 4801):
        # 'lab4_1.zip'
        ScaleZip(archive_name, width, height).process_zip()
        print("Successfully converted.")
    else:
        print("Height must be in range from 192 to 4800 and width must be from 140 to 7680.")
else:
    print("Input proper value!")


# ZipReplace
archive_name = input("Name of archive: ")
file_name = input("Name of file which you want to change: ")
what_to_change = input("Text, which you want to change: ")
replacement = input("Change text to this: ")
try:
    # 'text.zip' -> 'text.txt' -> 'cats' -> 'dogs'
    ZipReplace(archive_name, file_name, what_to_change, replacement).zip_find_replace()
    print("Successfully changed.")
except Exception:
    print("There are some problems with your input. Try again.")
