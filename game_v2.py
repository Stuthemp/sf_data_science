import numpy as np

def random_predict(number: int=1) -> int:
    """Guessing random number

    Args:
        number (int, optional): Target number Defaults to 1.

    Returns:
        int: Number of tries
    """
    
    count = 0
    
    while True:
        count += 1
        predict = np.random.randint(1, 101)
        if number == predict:
            break
    
    return(count)
def score_game(random_predict) -> int:
    """Average tries to guess a random number

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Average number of tries
    """
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    count_ls = list(map(random_predict, random_array))
    res = int(np.mean(count_ls))
    return res
#print(f"Average guesses to guess a number is {score_game(random_predict=random_predict)}")
#print(f"Computer guessed the number in {random_predict(15)} tries")

if __name__ == "__main__":
    score_game(random_predict)