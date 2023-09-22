import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number: "))
    
    if predict_number > number:
         print("The number must be smaller")
         
    elif predict_number < number:
        print("Number mus bebigger")
        
    else:
        print(f"You guessed right! The number was {number}, it took you {count} tries")
        break