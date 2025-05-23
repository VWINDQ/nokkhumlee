file_path = "E:\VSCODE\Python_practice\example.txt"

try:
  file = open(file_path, 'r')
  # Perform operations on the file
finally:
  file.close()
# Reading from a file using read() method
with open('example.txt', 'r') as file:
  content = file.read()
  print(content)