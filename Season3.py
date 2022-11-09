print("_________________________________________")
print("_________________________________________")
print("       WORLD HEALTH DAY BY MANASVI       ")
print("_________________________________________")
print("_________________________________________")
print("Did you know that World Health Day is always on April 7th every year!")



options = ["Yoga", "How to stay healthy", "Calorie Calculator", "Exit"]
yogaChoices = ["Steps", "Benefits of Yoga", "How to stay concnetrated"]
yogaConcentrated = ["Set an intention", "Don't compare yourself with others", "Keep mind relaxed", "Just keep Breathing!"]
yogaSteps = ["Salutation Position", "Raised arm position", "Hand to foot position", "Equestrian Position", "Mountain Position", "Eight Limbs position", "Cobra Position", "Mountain Position", "Equestrian Position", "Hand to foot position", "Raised arm position", "Salutation Position"]
yogaHealthy = ["Eat a healthy diet", "Consume less salt or sugar", "Reduce harmul fats", "Be Active", "Check your blood pressure regularly"]


def yoga():
    global yogaChoices
    print("-----------------------------")
    print("Yoga is a spiritual disipline that focuses on bringing harmony between your mind and body.")
    print("-----------------------------")


    yoga = input("If you want to learn more about yoga, type Yes. ")
    if yoga.lower() == "yes":
        print("-----------------------------")
        for i in range(len(yogaChoices)):
            print(i+1, "-", yogaChoices[i])
        print("-----------------------------")
        yogaChoices = int(input("Enter the number you want to learn the most about! "))

def yogaStep():
    print("-----------------------------")
    print("There are a toal of 84 steps/poses in yoga, but there are only 12 most common ones. ")
    print("These are the names of the 12 most common yoga positions - ")
    print("-----------------------------")
    for i in range(len(yogaSteps)):
        print("*", yogaSteps[i])
    print("-----------------------------")

def yogaBenefits():
    print("-----------------------------")
    print("Yoga is a great way to increase your flexibility, athletic performence, strength, even energy, immunity, and helps you with stress!")
    print("-----------------------------")

def yogaConcentrating():
    print("Yoga is very hard to concentrate on mainly because it's hard to maintain flexible and active.")
    print("Some ways to stay concentrated during yoga are -  ")
    print("-----------------------------")
    for i in range(len(yogaConcentrated)):
        print("*", yogaConcentrated[i])
    print("-----------------------------")



def yogaHealthier():
    print("Being healthy is a big deal, but it's really hard to do so. Here are some ways to stay healthy! - ")
    print("-----------------------------")
    for i in range(len(yogaHealthy)):
        print("*", yogaHealthy[i])
    print("-----------------------------")



def calorieCalculator():
    weight = input("Enter you weight in pounds: ")
    if weight.isnumeric():
        weight = int(weight)
    height = input("Enter you height in inches: ")
    if height.isnumeric():
        height = int(height)
    else:
        print("Invalid Input")
    age = input("Enter you age: ")
    if age.isnumeric():
        age = int(age)
    else:
        print("Invalid Input")
    gender = input("Enter you gender. M/F: ")
    activity = input("Enter your daily activity level. Sedentary/light/moderate/very active: ")
    if gender.lower() == "f":
        metabolic_rate = (weight*4.35)+(height*4.7)-(age*4.7)+655
    elif gender.lower() == "m":
        metabolic_rate = (weight*6.23)+(height*12.7)-(age*6.8)+66
    else:
        print("Invalid Input")
    if activity.lower() == "sedentary":
        cal = metabolic_rate*1.2
    elif activity.lower() == "light":
        cal = metabolic_rate*1.375
    elif activity.lower() == "moderate":
        cal = metabolic_rate*1.55
    elif activity.lower() == "very active":
        cal = metabolic_rate*1.725
    else:
        print("Invalid Input")
    print("-----------------------------")
    print("The calories you need to eat each day to maintain your weight is: ", cal)
    print("-----------------------------")




























while True: 
    YN = input("If you want to learn more about World Health Day, type Yes. ")
    if YN.lower() == "yes":
        print("-----------------------------")

        for i in range(len(options)):
            print(i+1, "-", options[i])
        print("-----------------------------")
        choice = input("Enter the number you want to learn the most about! ")
        if choice.isnumeric():
                choice = int(choice)
        elif choice == 0:
            print("Thank You")
            break
        else:
            print("Invalid Input")
            continue
        if choice==1:
            yoga()
            if yogaChoices==1:
                yogaStep()
                if yogaChoices==2:
                    yogaBenefits()
                    if yogaChoices==3:
                        yogaConcentrating()
        if choice==2:
            yogaHealthier()
        if choice==3:
            calorieCalculator()
        if choice==4:
            quit()
        else:
            print("Invalid Input")
            continue
    if YN.lower()=="no":
        print("Thank You")
        break
    else:
        print("Invalid Input")
        continue