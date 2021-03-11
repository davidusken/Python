# Day 9 Project: Credit Card Validator
# Project details found here: https://teclado.com/30-days-of-python/python-30-day-9-project/

print("Welcome to the Credit card validator!")
creditcard = input("Enter card number: ").strip()

print(f"You entered: '{creditcard}'")

# List convert, last digit removal and reverse
creditcardlist = []
for character in creditcard:
    creditcardlist.append(int(character))

slicedcclist = creditcardlist[:-1]
slicedcclist.reverse()

# For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. 
# If any of the results are greater than 9, subtract 9 from those numbers.

results = 0

for index, evenin in enumerate(slicedcclist):
    if index % 2 == 0:
        evenin = int(evenin) * 2
        if evenin > 9:
            evenin = evenin - 9
        slicedcclist[index] = evenin

# Add together all of the results and add the checking digit. If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

if (sum(slicedcclist) + creditcardlist[-1]) % 10 == 0:
     print("Card number is valid.")
else:
     print("Card number is invalid")