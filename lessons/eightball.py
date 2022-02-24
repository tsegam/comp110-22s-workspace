"""An oracle that predicts the future."""

from random import randint as rand 

input("Ask a yes/no question:")

response: int = rand(0, 3)

if response == 0:
    print("Most definitely")
elif response == 1:
    print("Highl likely")
elif response == 2:
    print("Ask again later")
else:
    print("No way, not a chance")