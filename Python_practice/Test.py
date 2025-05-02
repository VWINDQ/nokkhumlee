import random

lucky_number = random.randint(1, 10)
not_found = True

while not_found:
  for i in range(1, 10):
    if i == lucky_number:
      not_found = False
      break
    else:
      print(i)
print(f"Yay I got my lucky number {lucky_number}! 🍀")
print("I am done with the loop!")
print("Enjoy your day!")