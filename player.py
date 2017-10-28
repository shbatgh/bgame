import random
import time

tmoney = 50000

first_name = [
    'Sophia', 'Jackson', 'Emma', 'Aiden', 'Olivia', 'Lucas', 'Ava', 'Liam', 'Mia', 'Noah', 'Isabella', 'Ethan',
    'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Grayson', 'Layla',
    'Jacob',
    'Amelia', 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 'Aubrey', 'James', 'Adalyn', 'Jayden',
    'Madison',
    'Logan', 'Chloe', 'Alexander'
]
first_name = random.choice(first_name)
last_name = random.choice(first_name)
full_name = '{} {}'.format(first_name, last_name)
person = first_name + " Xiong"
person1 = first_name + " Lee"
person2 = first_name + " Greene"
person3 = first_name + " Henwich"
person4 = first_name + " Smith"
global myteam
myteam = [
    person,
    person1,
    person2,
    person3,
    person4
]
def run():
    skill = 10 + random.randint(10, 90)
    if __name__ == '__main__':
        teamy = Team(skill)
        teamy.make_teams()
        teamy.bet()
        run()


def play():
    play_game = input("Write Play to play a match ")
    if play_game == "Play" or "play" or "p" or "P":
          pass


class Team():
    def __init__(self, skill):
        self.skill = skill

    def bet(self):
        tmoney = 50000
        time.sleep(0.1)
        betting = input("Do you want to bet ")
        if betting != "yes" or "Yes":
            play()
        elif betting == "yes" or "Yes":
            global mbet
            mbet = float(input("How much do you want to bet "))
            tmoney = 50000
            tmoney = tmoney - mbet

        mbet = float(input("How much do you want to bet "))
        if mbet > tmoney:
            print("You can't bet more than you have")
            bets()
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
        if tskill > oskill:
            x = random.randint(1, 10)
            print(x)
            if x == 1 or 2:
                print("You lose")
                tmoney = tmoney - (mbet * 3)
                print("You now have " + str(tmoney))
            if x == 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
                print("You win")
                tmoney = tmoney + mbet * 5
                print("you now have " + str(tmoney))
        elif tskill == oskill:
            x = random.randint(1, 10)
            if x == 1 or 2 or 3 or 4 or 5:
                print("You win")
            else:
                print("You lose")

        if tmoney >= 100000000000000:
            print("You won the game")
            con = input("Do you want to continue the game ")
            if con != "no" or "No":
                run()
            else:
                quit()

        time.sleep(0.1)

    def make_teams(self):
        global tmoney
        first_name = [
            'Sophia', 'Jackson', 'Emma', 'Aiden', 'Olivia', 'Lucas', 'Ava', 'Liam', 'Mia', 'Noah', 'Isabella', 'Ethan',
            'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Grayson', 'Layla',
            'Jacob',
            'Amelia', 'Michael', 'Emily', 'Benjamin', 'Madelyn', 'Carter', 'Aubrey', 'James', 'Adalyn', 'Jayden',
            'Madison',
            'Logan', 'Chloe', 'Alexander'
        ]
        first_name = random.choice(first_name)
        last_name = random.choice(first_name)
        full_name = '{} {}'.format(first_name, last_name)
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
        print("Your team's total skill is " + str(tskill))
        global person, person1, person2, person3, person4
        def store():
            person = first_name + " Xiong"
            person1 = first_name + " Lee"
            person2 = first_name + " Greene"
            person3 = first_name + " Henwich"
            person4 = first_name + " Smith"
            global myteam
            myteam = [
                person,
                person1,
                person2,
                person3,
                person4
            ]
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
                play()
            elif buyM != "yes" or "Yes":
                def play_again():
                    play_game = input("Write Play to play a match ")
                    if play_game == "Play" or "play" or "p" or "P":
                        pass

            print(str(myteam))
            upgrade = input("Type the first letter of your troops to upgrade their skill, which makes you win more ")
            firstc, firstc1, firstc2, firstc3, firstc4 = person[0][0], person1[0][0], person2[0][0], person3[0][0], person4[0][0]
            time.sleep(0.3)
            tskill = 50000
            if upgrade == firstc or firstc1 or firstc2 or firstc3 or firstc4:
                supgrade = tskill + tskill/250
                if upgrade == firstc:
                    print("To upgrade " + person + " press u, it will upgrade it's skill will become " + str(supgrade) + "this will cost you $4,500")
                    global u
                    u = input("Are you sure you want spend $4500 to upgrade " + person + " skill to " + str(supgrade + tskill))
                    if u == "u" or "U":
                        tmoney = tmoney - 4500
                        tskill = tskill + tskill
                if upgrade == firstc1:
                    print("To upgrade " + person1 + " press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
                    if u == "u" or "U":
                        tmoney = tmoney - 4500
                        tskill = tskill + tskill
                if upgrade == firstc2:
                    print("To upgrade " + person2 + "press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
                    if u == "u" or "U":
                        tmoney = tmoney - 4500
                        tskill = tskill + tskill
                if upgrade == firstc3:
                    print("To upgrade " + person3 + " press u, it will upgrade it's skill will become " + str(supgrade) + " this will cost you $4,500")
                    if u == "u" or "U":
                        tmoney = tmoney - 4500
                        tskill = tskill + tskill
                if upgrade == firstc4:
                    print("To upgrade " + person4 + " press u, it will upgrade it's skill will become " + str(supgrade) + "this will cost you $4,500")
                    if u == "u" or "U":
                        tmoney = tmoney - 4500
                        tskill = tskill + supgrade
                        print(tskill)

skill = 10 + random.randint(10, 90)
if __name__ == '__main__':
    teamy = Team(skill)
    teamy.make_teams()
    teamy.bet()
