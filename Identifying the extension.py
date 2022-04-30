What_File= input("Enter the file name\n")

if What_File.endswith(".py"): 
    print ("The extension of the file is : 'Python'")
elif What_File.endswith(".html" or "Html"):
    print ("The extension of the file is : 'Html'")
elif What_File.endswith(".jav"):
    print ("The extension of the file is : 'Java'")
elif What_File.endswith(".php"):
    print ("The extension of the file is : 'Php'")
elif What_File.endswith(".css"): 
    print ("The extension of the file is : 'CSS'")
elif What_File.endswith(".c"):
    print ("The extension of the file is : 'C Language'")
elif What_File.endswith(".c++"):
    print ("The extension of the file is : 'C++ Language'")
else: print("Couldn'textension Identify the given file")