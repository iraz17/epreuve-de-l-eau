import sys 

print(sys.argv[:0:-1])


if len(sys.argv) < 2:
    print("error")
    sys.exit()
