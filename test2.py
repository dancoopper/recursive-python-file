
import os
count = 0
print("Test2: hello world")
f = open("test1.py","w")
f.write("count = 1\n" +
    "if count == 1:\n"+
        "\tprint('back to test1')\n"+
        "\texit()\n")
f.close()
os.system("python test1.py")
