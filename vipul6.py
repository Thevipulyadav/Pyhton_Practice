#else & finally in try except in python

f1 = open("vipul2")


try:
    f = open("vipul2")
except Exception as e:
    print(e)
else:
    print("this will run only if except is not running")
finally:
    print("run this anyway....")
    f1.close()
print("important stuff")
