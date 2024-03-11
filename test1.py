# making recursive python file creation and execution
import os

string = r'''
import os
count = 0
print("Test2: hello world")
f = open("test1.py","w")
f.write("count = 1\n" +
    "if count == 1:\n"+
        "\tprint('back to test1')\n"+
        "\texit()\n"        
)
f.close()

os.system("python test1.py")
'''
count = 0
f = open("test2.py", "w")
f.write(string)

f.close()

os.system("python test2.py")
