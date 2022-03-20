# Read a file and print its contents
strfile = "SampleText.txt"
try:
    fhandlr = open(strfile)
except:
    print("File doesn't exists")
    exit()

for lines in fhandlr:
    print(lines.rstrip())

print("Done")
# -------------------------------------------------------------------------------
