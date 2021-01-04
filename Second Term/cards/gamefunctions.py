def ask_yes_no(question) :
    """Ask a yes or no question and get back a yes or no
    answer. to use (answer = ask_yes_no(question)) """
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    return response

def get_good_number(question, low, high):
    while True:
        number = input(question)
        if number.isnumeric() :
            number = int(number)
            if number >=low and number <= high:
                return number
        else:
            print ("not a good number")

class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = Score()
        self.isAlive = True
        self.lives = 3


class Score(object):
    def __init__(self):
        self.score = 0
    def add_to_score(self, points):
        self.score += points
    def take_points(self, points):
        self.score -= points
        if self.score < 0:
            self.score = 0


if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress enter to exit.")

