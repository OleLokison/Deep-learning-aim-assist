import os
dirs = r"C:\Users\8holz\OneDrive\BM\Biologie\Humanbio"

for i in os.listdir(dirs):
	print(i[:-5])