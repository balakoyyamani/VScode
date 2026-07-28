try:
    file=open("_24_filehandling.txt","x")
    file.close()
except FileExistsError:
    print("File already exists")

file=open("_24_filehandling.txt","w")
file.write("Hello, I am Balachandar from Chennai")
file.close()
file1=open("_24_filehandling.txt","a")
file1.write("\nI am a Python Developer")
file1.close()
file2=open("_24_filehandling.txt","r")
text=file2.read()
print(len(text))
print(file2.read())
print(file2.readlines())
file2.close()