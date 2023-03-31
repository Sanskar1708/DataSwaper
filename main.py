def swapFileData():
# Asking the file names
    fileName1 = input("Enter first file name: ")
    fileName2 = input("Enter second file name: ")
# Opening the files with reading mode
    data_a = open(fileName1, 'r')
    print("Opned first file for reading sucessfully")
    data_b = open(fileName2, 'r')
    print("Opned second file for reading sucessfully")
# Reading the file and storing the data
    containData1 = data_a.read()
    print("Copied first file sucessfully")
    containData2 = data_b.read()
    print("Copied second file sucessfully")
# Opening the files with writing mode
    data_a = open(fileName1, 'w')
    print("Opned first file for writing sucessfully")
    data_b = open(fileName2, 'w')
    print("Opned second file for writing sucessfully")
# Swaping the data
    data_a.write(containData2)
    data_b.write(containData1)
swapFileData()
print("Data swap completed")