print("\n\n\n")                                                                 #Game Intro Screen
print(r"‾‾|‾‾ ‾‾|‾‾ |\  /| |‾‾‾‾‾     \          / /‾\    |‾‾‾\  |‾‾‾\ ")
print(r"  |     |   | \/ | |___        \        / /   \   |___/  |___/ ")
print(r"  |     |   |    | |            \  /\  / /‾‾‾‾‾\  |   \  |     ")
print(r"  |   __|__ |    | |_____        \/  \/ /       \ |    \ |     ")

ruth = {    #Dictionary will be used to provide 'useful' information to the user in the library
    "Birth Name":"George Herman Ruth",
    "Born":"February 6, 1895 in Baltimore, Maryland", #Answer to the mathematical puzzle
    "Died":"August 16, 1948 in New York, New York",
    "Height":"6 foot, 2 inches",
    "Weight":"215 lbs",
    "Batted":"Left",
    "Threw":"Left",
    "Major League Baseball Debut":"July 11, 1914",
    "Last Major League Baseball Appearance":"May 30, 1935",
    "Hall of Fame":"Elected in 1936 receiving 95.13 percent of the votes" #added this line at the end of program
}
def start(): #function called at line 233
    print("Welcome to TIME WARP!  You are outside the time continuum and can explore the history of the famous athlete")
    print("Babe Ruth like no one has before!")
    part1()
def part1(): #control room on map
    #User can only go RIGHT or FORWARD
    print("\nYou are now in the control room.")
    print("The library is the room in front of you and there is another room to your right that may or may not be useful.") #tavern near by
    print("Where do you want to go? (Right / Forward)" )
    while True:
        choice1 = input().title()
        if choice1 == "Right":
            part2()
        elif choice1 == "Forward":
            part3()
        elif choice1 == "Cheat": #will execute the cheat code for the developer
            developerCheat()
        else:
            print("\nPlease enter a valid answer. (Right / Forward)")
def part2(): #room 1 on map
    #User can only go BACKWARDS or LEFT
    print("\nYou just entered a tavern and discover that Babe Ruth's parents own it.")
    print("You find a yellow handle on the wall and a doorway to your left.") #yellow handle = first ending
    print("What would you like to do?  (Pull handle / Go back / Go left)")
    while True:
        choice2 = input().title()
        if choice2 == "Pull Handle":
            print("\nYou just opened up the back exit.  A group of drunk men violently attacked you.  Game over.")
            exit()
        elif choice2 == "Go Back": #split options -- adds game variety
            part1()
        elif choice2 == "Go Left": #split options -- adds game variety
            part4()
        else:
            print("\nPlease enter a valid answer. (Pull handle / Go back / Go left)")
def part3(): #library on map
    #User can only go FORWARD
    print("\nYou just entered the library which contains information that might come in use later.")
    print("Do you want to store this information? (Yes / No)")
    while True:
        choice3 = input().title()
        if choice3 == "Yes":
            print("\nThe information has been stored.  You can retrieve the information when prompted to.")
            print("You have now entered a house in front of you.")
            part5A()
        elif choice3 == "No":
            clearDictionary() #removes the information so that the user cannot access it
            print("\nThe information is no longer available and you have entered a house in front of you.")
            part5A()
        else:
            print("\nPlease enter a valid answer. (Yes / No)")
def part4(): #room 2 on map
    print("\nYou are now outside on a cold and snowy night.  The tavern is behind you and a house is 50 feet in front of you.")
    print("What would you like to do?  (Go back / Go forward)")
    while True:
        choice4 = input().title()
        if choice4 == "Go Back":
            part2()
        elif choice4 == "Go Forward":
            part5B() #is pretty much the same as 5A -- is a result of the different track
        else:
            print("\nPlease enter a valid answer. (Go back / Go forward)")
def part5A(): #users who enter from the library -- room 3 on map
    print("\nIt turns out the house is a trap and the only way out is to guess the combination.")
    print("The combination is six digits and more information may be useful.")
    print("You can either try attempting the code or solve the puzzle. (Guess the code / Solve the puzzle / Review Information)")
    while True:
        choice5A = input().title()
        if choice5A == "Guess The Code":
            code()
        elif choice5A == "Review Information": #will retrieve the dictionary
            dictionary()
        elif choice5A == "Solve The Puzzle":
            solveThePuzzle()
        else:
            print("\nPlease enter a valid answer. (Guess the code / Solve the puzzle)")
def part5B(): #users who enter from room 2 -- room 3 on map
    print("\nIt turns out the house is a trap and the only way out is to guess the combination.")
    print("The combination is six digits.") #user does not have the option to review information with this track
    print("You can either try attempting the code or solve the puzzle. (Guess the code / Solve the puzzle)")
    while True:
        choice5B = input().title()
        if choice5B == "Guess The Code":
            code()
        elif choice5B == "Solve The Puzzle":
            solveThePuzzle()
        else:
            print("\nPlease enter a valid answer. (Guess the code / Solve the puzzle)")
def part6(): #room 4 on map
    print("\nYou are now in a Catholic orphanage and reformatory.  Ruth's parents sent him here for more discipline.")
    print("You see a monk in the right chamber and the owner of the minor league Baltimore Orioles in the left chamber.")
    print("Where do you want to go?  (Right / Left)") #user can still go back and view the other track if they want
    while True:
        choice6 = input().title()
        if choice6 == "Right":
            part7()
        elif choice6 == "Left":
            part8()
        else:
            print("\nPlease enter a valid answer. (Right / Left)")
def part7(): #room 5 on map
    print("\nThe monk introduces himself to you and his name is Brother Matthias.")
    print("He explains that young Ruth looked up to him and he became a father figure to him.")
    print("Brother Matthias states that him and some of the other monks introduced Babe Ruth to baseball.")
    print("If you want to learn more about Ruth's baseball career you can keep moving forward or go backward for other options.")
    print("Where do you want to go?  (Forward / Backward)") #goes back to room 4
    while True:
        choice7 = input().title()
        if choice7 == "Forward":
            part9()
        elif choice7 == "Backward":
            part6()
        else:
            print("\nPlease enter a valid answer. (Forward / Backward)")
def part8(): #room 6 on map
    print("\nThe owner introduces himself as Jack Dunn.")
    print("He explains that he saw great potential in Ruth and at 19, he became Ruth's legal guardian.")
    print("Dunn did this so he could sign the contract and Ruth could play professionally.")
    print("If you want to learn more about Ruth's baseball career you can keep moving forward or go backward for other options.")
    print("Where do you want to go?  (Forward / Backward)") #goes back to room 4
    while True:
        choice8 = input().title()
        if choice8 == "Forward":
            part9() #leads to two tracks
        elif choice8 == "Backward":
            part6() #gives other options
        else:
            print("\nPlease enter a valid answer. (Forward / Backward)")
def part9(): #room 7 on map
    print("\nRuth was in the club for a short period of time until he was called to join the majors in Boston.")
    print("Throughout his years of baseball, he had many accomplishments.")
    print("There are two paths you can take.  Both are great, but are different.  One is in front of you and the other is to the right.")
    print("Where do you want to go? (Forward / Right)") #Both tracks are similar, but has different info to add game variety
    while True:
        choice9 = input().title()
        if choice9 == "Forward":
            part10()
        elif choice9 == "Right":
            part11()
        else:
            print("\nPlease enter a valid answer. (Forward / Right")
def part10(): #room 8 on map
    print("\nThe accomplishments of Babe Ruth are always worth celebrating.")
    print("Babe Ruth hit three home runs in a single game at Forbes Field on May 25, 1935.")
    print("In 1936, Ruth was one of the first five players inducted into the baseball hall of fame.")
    print("In 1938, he earned the title of coach for the Brooklyn Dodgers.")
    part12() #other track will go here as well
def part11(): #room 9 on map
    print("\nThroughout his career, Babe Ruth broke many of baseball's important records.")
    print("Most years he lead a league in most total bases in a season (457), home runs (12), and")
    print("highest slugging percentage (.847).")
    part12() #other track will go here as well
def part12():
    print("\nIt is evident that Babe Ruth is a staple in baseball history.")
    print("He will forever live on through his fans including you who has successfully.")
    print("made it to the end of this adventure!")
    print("Thank you for playing!")
    exit() #will finish and close the game out -- victory = third ending
def dictionary():
    print("\nINFORMATION ON BABE RUTH")
    for x in ruth:
        print(str(x.title())+": "+str(ruth[x])) #provides a better format for the dictionary to be presented
    part5A()
def clearDictionary():
    ruth.clear() #function is used if the user does not want to save the information
def solveThePuzzle():
    print("\nThe first number is twice the value of one.  Multiply the first number by three to find the second number.")
    print("Do the same thing with the second number to find the third number.")
    print("Once you have the first three numbers, multiply the second number by three and add one to the product.")
    num1 = int(input("Input this answer into the calculator to reveive the fourth number: ")) #19 is the input
    num2 = 5
    answer = num1*num2 #95 will be the answer
    print(answer)
    print("\nNow you can guess the code.  There are no spaces between the numbers.") #gives the user the input format
    code() #function used to allow the user to input the code
def code():
    print("\nEnter your guess:")
    guess = input()
    if guess == "261895": #correct answer
        print("\nYou have guessed correctly.  This combination is the birthdate of Babe Ruth.")
        part6()
    else:
        print("\nYour guess was incorrect.  You could not get out in time.  Game over.") #wrong code = second ending
        exit()
def developerCheat(): #is a way for the developer to check and review his code
    while True:
        cheat = input().title() #developer inputs what part of the game they want to jump to
        if cheat == "Part 1":
            part1()
        elif cheat == "Part 2":
            part2()
        elif cheat == "Part 3":
            part3()
        elif cheat == "Part 4":
            part4()
        elif cheat == "Part 5.1": #has the review information option
            part5A()
        elif cheat == "Part 5.2": #does not have the review information option
            part5B()
        elif cheat == "Part 6":
            part6()
        elif cheat == "Part 7":
            part7()
        elif cheat == "Part 8":
            part8()
        elif cheat == "Part 9":
            part9()
        elif cheat == "Part 10": #track will lead to part 12
            part10()
        elif cheat == "Part 11": #track will lead to part 12
            part11()
        elif cheat == "Part 12":
            part12()
        else:
            print("Please enter in a valid cheat code.")

start() #puts the game in motion
