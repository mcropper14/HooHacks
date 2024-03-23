import random 
#from art import *
import time 
import pandas as pd
import csv 

class Twamp:

    def __init__(self):
    
        self.happiness = 100
        self.twampness = 0 
        self.d_dollars = 0
        self.clubs = 0
        self.health = 100
        self.hygiene = 0 
        self.name = ""
        self.caffinate = 0 
        self.sleep = 0 
        self.stres = 50 
        self.hours = 1
        self.study = 0
        self.clases = 0
        self.maj = ""
        self.rec = 0
        self.days = 0 

    def set_name(self):
        name = input("Enter a name for your TWAMP: ")
        self.name = name.capitalize()
        output = "Welcome to William and Mary " + self.name + "!"
        print(output)
        print("You Belong Here!")
        print("""
                 o  
                /|\\ 
                / \\
                   
                    """)

    def major(self):
        print('Majors Include: STEM or Not STEM ')
        print("\n")
        self.maj = input('Choose Your Fate Wisely: ' + self.maj)
        print("\n")
        if self.maj.lower() == 'stem':
            self.stres += 20
            print("That's a good choice!")
            print("\n")
            print("""
                *******
                *      *
                * o  o *
                *   v  *
                * \\_/ *
                ******
                """)
            print("\n")
        elif self.maj.lower() == 'not stem':
            self.stres -= 20 
            print("\n")
            print("""
                *******
                *      *
                * o  o *
                *  ^   *
                * / \  *
                ******
                """)
            print("\n")
         
        

    def get_clases(self):
        self.clases = input('Enter number of classes enrolled in: ')
        print('\n')
        print('You are enrolled in ' + self.clases + ' classes.')
        print('\n')
        

    def meal_plan(self):
        print('Meal Plans Available: All Access, Block, Commuter')
        print("\n")
        plan = input('Please enter your chosen meal plan: ')
        print("\n")
        print("You chose " + plan + " as your meal plan.")
        print("\n")
        if plan.lower() == 'all access':
            self.d_dollars = 400
        elif plan.lower() == 'block':
            self.d_dollars = 500
        elif plan.lower() == 'commuter':
            self.d_dollars = 560
        print("You now have " + str(self.d_dollars) + " dining dollars.")
        print("\n")
     

    def club(self):
        self.clubs = int(input("How many clubs do you want to join? "))
        print("\n")
        print("You joined " + str(self.clubs) +" clubs.")
        print("\n")
        for i in range(self.clubs):
            self.stres += i
            self.happiness += 1
        print("Your new stress level is " + str(self.stres))
        print("\n")
        print("Your new happiness level is " +str(self.happiness))
        print("\n")


    def get_status(self):
        print("\n " + " Your name is: " + self.name)
        print("\n " + " Your major is: " + self.maj.upper())
        print("\n " + " Your happiness level is: " + str(self.happiness))
        print("\n " + " Your twampness level is: " + str(self.twampness))
        print("\n " + " You have: " + str(self.d_dollars) + " dining dollars.")
        print("\n " + " You have joined: " + str(self.clubs))
        print("\n " + " Your health is: " + str(self.health))
        print("\n " + " Your hygiene is: " + str(self.hygiene))
        print("\n " + " Your level of caffeine consumption: " + str(self.caffinate))
        print("\n " + " Your hours of sleep: " + str(self.sleep))
        print("\n " + " Your stress level is: " + str(self.stres))


    def get_calc(self):
        total = 100
        for i in range(total):
            progress = (i + 1) / total * 100
            print('[' + '#' * int(progress // 10) + '-' * (10 - int(progress // 10)) + '] ' + str(int(progress)) + '%', end='\r')
            time.sleep(0.1)
        print('\nDone!\n')

    def spend(self):
        choice = input("Where do you want to spend your dining dollars: Caf or Sadler or Aromas? ")
        if self.d_dollars > 0:
            if choice.lower() == "caf":
                self.d_dollars -= 10 
            elif choice.lower() == "sadler":
                self.d_dollars -= 15
            elif choice.lower() == "aromas":
                self.d_dollars -= 5 
        print('You now have ' + str(self.d_dollars) + ' dining dollars.')
     

    def stress(self):
        print('Calculating Stress Levels: ')
        self.get_calc()
        print('Stress level is now: ' + str(self.stres))
        choices = ["study", "procrastinate", "hang out" ]
        choice = random.choice(choices)
        hours = random.randint(1, 5)
        self.hours = hours 
        print("You decide to " + choice + " for " + str(self.hours) + " hours.")
        print("\n")
        if choice == "study":
            print("You decided to ")
            self.happiness -= self.hours * 10 
            self.twampness += 10 
            self.health -= self.hours 
            self.caffinate += self.hours * 100 
            self.sleep -= self.hours 
            self.hygiene -= 10 
            self.stres += self.hours * 10
        elif choice == "procrastinate":
            self.happiness -= 10
            self.twampness -= 10 
            self.health -= self.hours 
            self.sleep += self.hours 
            self.stres += self.hours * 5 
        else:
            self.happiness += self.hours * 10 
            self.hygiene += 10 
            self.sleep += 7 
            self.stres -= self.hours * 5
        
        return self.stres

    def swem(self):
        self.study = random.randint(1, 12)
        print("Going to Swem to study for " + str(self.study) + " hours.")
        print("\n")
        if self.study > 3:
            print("That's awkward, you got kicked out of Swem at midnight.")
            print("Have fun in the 24 hour study room!")
            for hour in range(self.study):
                self.happiness -= 1 
                self.stres += 1 
                self.sleep -= 1 
                self.caffinate += 1 
           

    def gym(self):
        self.rec = random.randint(1, 12)
        print('Going to the rec for ' + str(self.rec) + ' hours.')
        print('\n')
        if self.rec > 5:
            print('Maybe you should be training your brain instead of your muscles.')
        for hour in range(self.rec):
            self.twampness -= 1
            self.health += 1
            self.stres -= 1
      

    def exams(self):
        self.schedule = self.clases
        grades = []
        if self.hours > 2:
            for i in range(int(self.schedule)):
                grade = random.randint(0,100)
                grade += (self.study *5)
                grades.append(grade)
        else:
            for i in range(int(self.schedule)):
                grade = random.randint(0,100)
                grades.append(grade)
        for i in grades:
            print('This is your exam grade for your class: ' + str(i) +"%.")
            print("\n")
            if i < 50 and self.maj == "stem":
                print("That's an A with a curve!")
                print("\n")
                print("You must be in discrete structures!")
                print("\n")
                print("""
                 o  
                \|/
                / \\
                   
                    """)
       

    def disaster(self):
        poss_diss = ['your instgram was hacked', 'The dorm fire alarm went off when there was actually a fire', 'You forgot there was a test']
        diss = random.choice(poss_diss)
        print(diss)
        if diss == poss_diss[0]:
            poss_stole = ['your inside jokes','your dog pictures','your unflattering pictures','pictures of the homework you send to your friend. It\'s okay, you probably failed anyways.','pictures about your embarassing hobby']
            print('the hacker stole ' + random.choice(poss_stole))
            self.happiness -= 20
            print('You are slowly losing you lust for life. Your happiness is now',self.happiness)
        elif diss == poss_diss[1]:
            poss_lost = ['your computer','your textbook','your hopes and dreams']
            print('Your dorm caught on fire. You lost ' + random.choice(poss_lost))
            self.happiness -= 10
            print('You are slowly losing you lust for life. Your happiness is now',self.happiness)
        elif diss == poss_diss[2]:
            print('This is what you get for skipping class to sleep in')
            self.stres += 10
            print('You are stressed and dropping out seems like a better idea everyday. You are slowly losing your youthful optimism. Your stress is now',self.stres)
        

    def game_over(self): 
        choices = ["stress", "disaster", "housing"]
        choice = random.choice(choices)
        print("\n")
        print(" \\  /")
        print("o----")
        print(" /  \\")
      

    def shower(self):
        print(" \n ") 
        print(" \n ")
        print(" \n ")
        print(" \n ")
        print(" \n ")
        print('\n')
        print('\n')
        print('\n')
        rain_chars = ['.', ',', ':', ';', '`']
        for i in range(25):
            col = random.randint(1, 80)
            row = random.randint(10, 20)
            print('\033[{};{}H'.format(row, col), end='')
            print(random.choice(rain_chars), end='')
            time.sleep(0.1)
            print('\n')
        print('\n')
        print('\n')
        print('\n')
        print("Congrats, you decided to take a shower!")
        if self.maj.lower() == "stem":
            print(" \n ")
            print("You broke the stereotype by showering as a STEM major!")
            self.hygiene += 5
            self.health += 2 
        else:
            self.hygiene += 10
            self.health += 2 
        

    def housing_crisis(self):
        print("You got kicked out of GGV for setting the fire alarm off!")
        print("Kathy Rowe says you have to live in a tent.")
        print("This is your new home.")
        print("Welcome to Tent City!")
        print("   /\\")
        print("  /  \\")
        print(" /    \\")
        print("/      \\")
        self.twampness += 10 
        self.health -= 1 
        self.hygiene -= 20 
        self.sleep -= 1 
        

    def main_game(self):
        print('Let\'s get started!')
        self.set_name()
        self.major()
        self.get_clases()
        self.meal_plan()
        self.club()
        print('Calculating:')
        self.get_calc()
        print('Here are your TWAMPS\'s stats: ')
        print('\n')
        self.get_status()

    def choices(self):
        action_count = 0
        for i in range(5):
            options = ["Spend", "Swem", "Shower", "Gym" ]
            for option in options:
                print(" \n "+ option)
            print(" \n ")
            pick = input("Pick an option: ")
            if pick.lower() == "spend":
                self.spend()
                action_count += 1
            elif pick.lower() == "swem":
                self.swem()
                action_count += 1
            elif pick.lower() == "shower":
                self.shower()
                action_count += 1
            elif pick.lower() == "gym":
                self.gym()
                action_count += 1
            else:
                print("Not a valid option")
      

    def new_day(self, days):
        for i in range(days):
            self.days += 1 
            print('\n')
            print("Good Morning! ")
            print("It's a new day")
            print('\n')
            go_to_class = input("Do you want to go to your classes: ")
            if go_to_class.lower() == "yes" or go_to_class.lower() == "y":
                print("Way to be a TWAMP, you decided to go to class!")
                self.twampness += 5 
                self.caffinate += 5
                self.choices()
                self.exams()
            else:
                print('\n')
                print("You've become a hermit. Maybe you'll drop out and become a goat farmer.")
                print(" \n ")
                self.stres += 5
                self.happiness -= 20
                print('\n')
             

            print('\n')
            print("Here are your TWAMPS's stats after day " + str(self.days) + ": ")
            print('\n')
            self.get_status()
            self.save_to_csv()

            if self.days % 7 == 0:
                print(" \n ")
                print("It's the end of the week! Time to reflect on the choices you made.")
                print(" \n ")
                self.game_over()

            if self.days == 30:
                print("Congratulations! You made it through the month!")
                print("You've survived being a TWAMP!")
                break

        print("Thanks for playing!")

  

  

    def save_to_csv(self):
        with open('twamp_data.csv', mode='a', newline='') as file:  
            writer = csv.writer(file)
            if file.tell() == 0:  # Check if the file is empty
                writer.writerow(self.__dict__.keys())  # Write attribute labels only if the file is empty
            writer.writerow([getattr(self, attr) for attr in self.__dict__.keys()])


     

  
        
    
twamp = Twamp()
twamp.main_game()  # Start the game
twamp.new_day(5)  


