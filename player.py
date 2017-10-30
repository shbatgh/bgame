import random
import time
import select

global tmoney
tmoney = 50000

first_names = [
    'Sophia', 'Jackson', 'Emma', 'Aiden', 'Olivia', 'Lucas', 'Ava', 'Liam', 'Mia', 'Noah', 'Isabella', 'Ethan',
    'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Grayson', 'Layla',
    'Jacob',
    'Amelia', 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 'Aubrey', 'James', 'Adalyn', 'Jayden',
    'Madison',
    'Logan', 'Chloe', 'Alexander'
]
last_names = ["Xiong", "Lee", "Greene", "Henwich", "Smith"]

myteam = ['{} {}'.format(random.choice(first_names), last_name) for last_name in last_names]

print(myteam)



def run():
    # function in case i have to rerun my program
    skill = 10 + random.randint(10, 90)
    if __name__ == '__main__':
        play_and_bet()



def play_and_bet():
    # play a game and see if you win or lose
    play_game = input("Write Play to play a match ")
    tmoney = 50000
    mbet = float(input("How much do you want to bet "))
    if play_game == "Play" or "play" or "p" or "P":
        x = 25
        y = random.randint(10, 90)
        y1 = random.randint(10, 90)
        y2 = random.randint(10, 90)
        y3 = random.randint(10, 90)
        y4 = random.randint(10, 90)
        p1 = x + y
        p2 = x + y1
        p3 = x + y2
        p4 = x + y3
        p5 = x + y4
        tskill = p1 + p2 + p3 + p4 + p5
        oskill = 20
        def idk():
            if tskill > oskill:
                x = random.randint(1, 10)
                tmoney = 50000
                if x == 1 or 2:
                    print("You lose so you now have " + str(tmoney-mbet*3))
                    pass
                if x == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                    print("You win so you now have " + str(tmoney+mbet*5))
                    pass
        if tskill == oskill:
            x = random.randint(1, 10)
            if x == 1 or 2 or 3 or 4 or 5:
                print("You win so you now have " + str(tmoney - mbet*3))
            elif x == 6 or 7 or 8 or 9 or 10:
                print("You lose so you now have " + str(tmoney - mbet*2))

        if tmoney >= 100000000000000:
            print("You won the game")
            con = input("Do you want to continue the game ")
            if con != "no" or "No":
                run()
            else:
                quit()

        time.sleep(0.1)

def bet_again():
    # a function to bet again if something goes wrong with the first bet
    mbet = float(input("How much do you want to bet "))
    tmoney = 50000
    tmoney = tmoney - mbet
    print(tmoney)


class Store():
    def __init__(self, tmoney):
        self.tmoney = tmoney

    def buy_new_cards(self):
        global tmoney
        tmoney = 50000
        goToStore = input("1. Shop ")
        if goToStore == "1":
            print("You are in the store what do you want to buy?")
            print("Press the number next to the thing you want to buy to buy it ")
            print("Micheal Jordan \n Stats: Skill is 95 and salary is $2,000,000 \n You have to have $1,000,000 to buy him ")
        buyM = input("Do you want to buy Michael Jordan ")
        if buyM == "Yes" or "yes" and tmoney >= 1000000:
            print("You purchased Micheal Jordan and he was added to your team")
            tmoney = tmoney - 1000000
            myteam.pop()
            myteam.append('Michael Jordan')
            print("This is your team " + str(myteam))
            print("You have $" + str(tmoney))
        if tmoney < 1000000:
            print("You don't have enough money to buy Micheal Jordan")
            play_and_bet()
        elif buyM != "yes" or "Yes":
            play_and_bet()

    def upgrade(self):
        person = myteam[0]
        person1 = myteam[1]
        person2 = myteam[2]
        person3 = myteam[3]
        person4 = myteam[4]
        firstc = person[0]
        firstc1 = person1[0]
        firstc2 = person2[0]
        firstc3 = person3[0]
        firstc4 = person4[0]
        time.sleep(0.3)
        tskill = 50000
        global supgrade
        supgrade = tskill + tskill / 250
        global u, u1, u2, u3, u4
        u = input("To upgrade " + person + " press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
        u1 = input("To upgrade " + person1 + " press u, it will upgrade it's skill will become " + str(
            supgrade) + " this will cost you $4,500")
        u2 = input("To upgrade " + person2 + " press u, it will upgrade it's skill will become " + str(
            supgrade) + " this will cost you $4,500")
        u3 = input("To upgrade " + person3 + " press u, it will upgrade it's skill will become " + str(
            supgrade) + " this will cost you $4,500")
        u4 = input("To upgrade " + person4 + " press u, it will upgrade it's skill will become " + str(
            supgrade) + " this will cost you $4,500")
        print("Are you sure you want spend $4500 to upgrade " + person + " skill to " + str(supgrade + tskill))
        global tmoney
        tmoney = 50000
        if u == firstc:
            print("To upgrade " + person + " press u, it will upgrade it's skill will become " + str(tskill + supgrade) + "this will cost you $4,500")
            if u == "u" or "U":
                tmoney = tmoney - 4500
                tskill = tskill + supgrade
                print("Your total skill is now " + str(tskill))
                pass
        if u1 == firstc1:
            print("To upgrade " + person1 + " press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
            if u == "u" or "U":
                tmoney = tmoney - 4500
                tskill = tskill + supgrade
                print("Your total skill is now " + str(tskill))
                pass
        if u2 == firstc2:
            print("To upgrade " + person2 + "press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
            if u == "yes" or "Yes":
                tmoney = tmoney - 4500
                tskill = tskill + supgrade
                print("Your total skill is now " + str(tskill))
                pass
        if u3 == firstc3:
            if u1 == "yes" or "Yes":
                tmoney = tmoney - 4500
                tskill = tskill + supgrade
                print("Your total skill is now " + str(tskill))
                pass
        if u4 == firstc4:
            print("To upgrade " + person4 + " press u, it will upgrade it's skill will become " + str(supgrade) + "this will cost you $4,500")
            if u == "yes" or "Yes":
                tmoney = tmoney - 4500
                tskill = tskill + supgrade
                print("Your total skill is now " + str(tskill))
                pass
skill = 10 + random.randint(10, 90)
if __name__ == '__main__':
    play_and_bet()
    storey = Store(tmoney)
    storey.upgrade()
    storey.buy_new_cards()
