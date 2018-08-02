import random
from typing import Any, Union

num = input("Guess the number")
num.strip()
int(num)
random_number: Union[int, Any] = random.randint(1, 10)
if num == random_number:
    print("That is correct.")
else:
    print("That is wrong it was actually %d." % random_number)