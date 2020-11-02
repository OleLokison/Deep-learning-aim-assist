from PIL import Image
FilePath = r"C:\Users\8holz\Desktop\Dataset_prot\\"
FileName = r"2020-11-02-0.png"

im = Image.open(FilePath+FileName)
im.save(FilePath+"Test.png", dpi=(2560, 1440))