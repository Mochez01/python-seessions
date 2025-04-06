try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Finally block executed.")
    file.close()
    