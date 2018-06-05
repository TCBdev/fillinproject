# -*- coding: utf-8 -*- 
levelList = ["easy", "Easy", "EASY", "ez", "EZ", "e", "E","intermediate", "Intermediate", "INTERMEDIATE", "I", "i", "medium", "Medium", "MEDIUM", "med", "Med", "MED", "M", "m", "HARD", "hard", "Hard", "h", "H", "ultimate", "Ultimate", "ULTIMATE","u", "U"]
yesList = ["yes", "y", "yeah", "yah", "ye", "YES", "Y","YEAH","YAH", "YE", "Yes", "Yeah", "Yah", "Ye"]
noList = ["no", "n", "nah", "meh", "NO", "N", "NAH", "MEH", "No", "Nah", "Meh"]
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]    

easy_quiz = """Naruto graduates the Ninja ___1___ and joins Team ___2___, along side his rival ___3___, his crush ___4___ and his sensei ___5___. Source: Naruto.Wikia"""
intermediate_quiz = """The ___1___ begin kidnapping the ___2___ to extract their ___3___ and revive the ___4___. With the ___4___ restored, the Akatsuki can cast the ___5___ Tsukuyomi. Source: Naruto.Wikia"""
hard_quiz = """Naruto is incapable of performing the basic ___1___ Technique. This leaves him unable to graduate from the Academy, one of his instructors, ___2___, tells Naruto that if he could steal the Scroll of ___3___ and learn one of its secret techniques, Naruto will graduate. After successfully stealing the scroll, ___4___ is caught by another instructor, ___5___. Source: Naruto.Wikia"""
ultimate_quiz = """The Hyuga is one of the ___1___ noble clans of Konohagakure. All members born into this clan possess the ___2___, a ___3___ that gives them extended fields of vision and the ability to see through solid objects and even the ___4___ circulatory system, amongst other things. Members of this clan also possess the unique ability to expel ___4___ from any of the ___5___ in their body. Source: Naruto.Wikia"""

easy_answers = ["academy", "seven", "sasuke", "sakura", "kakashi"]
intermediate_answers = ["akatsuki", "jinchuriki", "tailed beast", "ten tails", "infinite"]
hard_answers = ["clone", "mizuki", "seals", "naruto", "iruka"]
ultimate_answers = ["four", "byakugan", "kekkei genkai", "chakra", "tenketsu"]

##############  QUIZ DEFINITIONS  ##############

def easy_bonus():
    '''If player chooses to play a bonus level program checks current level and returns the appropriate corresponding level.
    Inputs: Current Level
    Outputs: Bonus questions + Score
    '''
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL! \nThis next section will have three (3) multiple choice questions.")

    bonus_a1 = input("What is the name of Tsunade's summoning animal?: \n\n     1. Manda\n     2. Katsuyu\n     3. Jiraya\n\n Your Answer: ")
    bonus_a2 = input("\nWhat's the name of the Cursed Seal given to both Sasuke Uchiha and Anko Mitarashi?: \n\n     1. Heaven Cursed Seal\n     2. Mud Wall Seal\n     3. Reaper's Death Seal\n\n Your Answer: ")
    bonus_a3 = input("\nWho was Naruto Uzumaki's father?: \n\n     1. Sasuke Uchiha\n     2. Minato Namikaze \n   3. Orochimaru\n\n   Your Answer: ")

    score = 0
    if bonus_a1 == '2':
        score = score + 1
    if bonus_a2 == '1':
        score = score + 1
    if bonus_a3 == '2':
        score = score + 1    

    print('Your score is: {} out of 3'.format(score))
    return restart_quiz()

def med_bonus():
    '''If player chooses to play a bonus level program checks current level and returns the appropriate corresponding level.
    Inputs: Current Level
    Outputs: Bonus questions + Score
    '''
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL! \nThis next section will have three (3) multiple choice questions.")

    bonus_a4 = input("\nThe Village Hidden in the Leaves can be found in what country?: \n\n     1. The Land of Fire\n     2. The Land of Lightning\n     3. The Land of Earth\n\n    Your Answer: ")
    bonus_a5 = input("\nFILL IN THE BLANK.\nGaara is the _____ Kazakagae: \n\n     1. First\n     2. Fifth\n     3. Forth\n\n    Your Answer: ")
    bonus_a6 = input("\nHow many tails does the tailed beast (biju) Son Gokū have?: \n\n     1. Three (3)\n     2. Ten (10)\n     3. Four (4)\n\n Your Answer: ")

    score = 0
    if bonus_a4 == '1':
        score = score + 1
    if bonus_a5 == '2':
        score = score + 1
    if bonus_a6 == '3':
        score = score + 1    

    print('Your score is: {} out of 3'.format(score))
    return restart_quiz()

def hard_bonus():
    '''If player chooses to play a bonus level program checks current level and returns the appropriate corresponding level.
    Inputs: Current Level
    Outputs: Bonus questions + Score
    '''
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL! \nThis next section will have three (3) multiple choice questions.")    

    bonus_a7 = input("\nWho was Tsunade's fiancée?: \n\n     1. Dan\n     2. Jiraiya\n     3. Minato\n\n   Your Answer: ")
    bonus_a8 = input("\nNagato is a member of which clan?: \n\n     1. Uzumaki\n     2. Hyuga\n     3. Akatsuki\n\n     Your Answer: ")
    bonus_a9 = input("\nWho was Naruto's teacher at the ninja academy?: \n\n     1. Iruka\n     2. Kakashi\n     3. Hiruzen \n\n Your Answer: ")

    score = 0
    if bonus_a7 == '1':
        score = score + 1
    if bonus_a8 == '1':
        score = score + 1
    if bonus_a9 == '1':
        score = score + 1    

    print('Your score is: {} out of 3'.format(score) + 'Great Work!')
    return restart_quiz()

def ultimate_bonus():
    '''If player chooses to play a bonus level program checks current level and returns the appropriate corresponding level.
    Inputs: Current Level
    Outputs: Bonus questions + Score
    '''
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL!\n\n  M    E    M    E        E    X    T    R    E    M    E    ! \n\nThis next section will have three (3) multiple choice questions.")

    bonus_a10 = input("\nWho was Naruto's first kiss with?: \n\n     1. Sakura\n     2. Hinata \n     3. Sasuke \n\n   Your Answer: ")
    bonus_a11 = input("\nWho is the child of Sasuke and Sakura?: \n\n     1. Hinata\n     2. Sarada\n     3. Salad \n\n   Your Answer: ")
    bonus_a12 = input("\nWho is the male parental figure for Himawari?: \n\n     1. Naruto\n     2. Boruto's Dad\n     3. Sasuke \n\n  Your Answer: ")

    score = 0
    if bonus_a10 == '3':
        score = score + 1
    if bonus_a11 == '3':
        score = score + 1
    if bonus_a12 == '2':
        score = score + 1    

    print('Your score is: {} out of 3'.format(score) + 'Great Work!')
    return restart_quiz()

def welcome(): 
    '''Get players name'''
    print("\n" + "* " * 10)
    print("\nWELCOME TO THE QUIZ TO END ALL QUIZES!\n")
    print("* " * 10)
    print("\n"r"\/\/\/\/\/\/\/\/\/**NARUTO: Still a Genin?! ¯\_(ツ)_/¯ **/\/\/\/\/\/\/\/\/")
    player_name = input("\nPlease tell me your name: ")
    print("\nHello " + player_name)
    print("\nLET'S GET STARTED!!")

def level_choice(level): 
    '''Player chooses level. Executed quiz and answers
    Inputs: Current level.  
	Outputs: The specific quiz and its answers associated with that level.'''
    if level.lower() in ['easy', 'ez', 'e']:
        return easy_quiz, easy_answers
    elif level.lower() in ['intermediate', 'i', 'med', 'medium', 'm']:
        return intermediate_quiz, intermediate_answers
    elif level.lower() in ['hard', 'h']:
        return hard_quiz, hard_answers
    elif level.lower() in ['ultimate', 'u']:
        return ultimate_quiz, ultimate_answers

def advise_guesses():
    '''Player can determine how many guesses they would like. Allows to choose between 1 and 5 guesses'''
    global guesses
    global min_guess
    min_guess = 1
    max_guess = 5
    guesses = input("How many guesses would you like (up to 5)?: ")
    while not guesses.isdigit() or int(guesses) < min_guess or int(guesses) > max_guess:
        guesses = input("Please enter a number that is greater than 0, but less than or equal to 5:  ")
    guesses = int(guesses)
    
    print("\n    ", guesses, "guess(es) it is!!")

def all_blanks(word, blanks): 
    '''To single out every blank. Identifies 'blank' in each quiz AND each blank in the 'blanks' list. With correct answer, quiz is returned with 'word'.
    Inputs: 'word' is the each blank in the 'blanks' list. 'blanks' is the list. 
	Outputs: Returns 'word' if that matches up with the current word in the quiz.'''

    for blank in blanks:
        if blank in word:
            return blank
    return None

def replace_blanks(word, replaced, blanks, player_answer, index):
    '''To replace each blank with its correct answer.
    
    Inputs: 'blanks' list, the replaced quiz that has the correct answers so far, if applicable,
	the 'player_answer' for that blank, the index number of that 'player_answer' to correctly match that with the right blank to fill in. 
	Outputs: The correctly replaced quiz.'''

    if all_blanks(word, blanks) == None:
        if word not in replaced:
            replaced.append(word)
    else:
        replacement = all_blanks(word, blanks)
        word = word.replace(replacement, player_answer.upper())

        if replacement == blanks[index]:
            if replacement not in replaced:
                replaced.append(word)
            else:
                position = replaced.index(replacement)
                replaced[position] = word
        else:
            replaced.append(replacement)

    return replaced

def retrieve_answers(quiz, blanks, replaced, player_answer, index): 
    '''Replaces each ___#___ with its correct answer. Based on player answer, blanks are replaced with correct answers + remaining unanswered blanks.
    Outputs: The correctly replaced quiz'''

    split_quiz = quiz.split()

    if type(replaced) == str:
        replaced = replaced.split()
    elif type(replaced) == int:
        replaced = replaced.split()

    for word in split_quiz:
        replace_blanks(word, replaced, blanks, player_answer, index)
        
    replaced = " ".join(replaced)
    head, sep, tail = replaced.partition("Wikia")
    replaced = head + sep
    return replaced

def answer_question(level, quiz, answers): 
    '''Program verifies the selected level, and corresponding level answers to player's answers. Number of guesses reduce with every wrong answer. Once guesses reach 0, player will have ability to restart game or end
    Inputs: The current level, its quiz, and its answers. 
	Outputs: The updated replaced quiz, the index of each answer. Guesses.'''

    replaced = []
    player_answer = ""

    index = 0
    for blank in blanks:
        global guesses
        minus_one = -1
        question = "\nFor " + blank + " "
        print(question)
        player_answer = input("What is your answer?: ")
        player_answer = player_answer.lower()

        while player_answer != answers[index]:
            print("\nIncorrect. Please try again.\n")
            if guesses > min_guess:
                guesses += minus_one
                print(guesses, "guess(es) remaining")
                player_answer = input("\nWhat is your answer for " + blank + "?: ")
                player_answer = player_answer.lower()
            else:
                print("\n" + "* " * 10)
                print("\nGAME OVER\n")
                print("* " * 10)
                print("\nYOU LOSE\n")
                print("* " * 10)
                print("\n")
                return restart_quiz()

        print("\nCORRECT!!\n")        							
        replaced = retrieve_answers(quiz, blanks, replaced, player_answer, index)
        print(replaced)			

        index += min_guess

    return replaced, index

def bonus_level():
    '''Program checks player original selected level, returns appropriate bonus level/answers'''
    if level.lower() in ['easy', 'ez', 'e']:
        return easy_bonus()
    elif level.lower() in ['intermediate', 'i', 'med', 'medium', 'm']:
        return med_bonus()
    elif level.lower() in ['hard', 'h']:
        return hard_bonus()
    elif level.lower() in ['ultimate', 'u']:
        return ultimate_bonus()

def winner_winner(): 
    '''Allows player to choose play a bonus level, quit the game, or restart the quiz.'''

    print("\nWinner Winner Chicken Dinner" "\nCongratulations you won the game!")
    blevel = input("\nWould you like to play a bonus level?: ")
    if blevel in yesList:  
            return bonus_level()
    elif blevel in noList:
            return restart_quiz()
    else:
        print("I'm sorry, I do not understand your choice.")
        blevel = input("\nWould you like to play a bonus level?" "\n Yes or No?: ")
        if blevel in yesList:  
            return bonus_level()
        elif blevel in noList:
            return restart_quiz()
        else:
            print("\n" + "* " * 10)
            print("\nGAME OVER\n")
            print("* " * 10)
            print("\nTHANK YOU FOR STOPPING BY!\n")
            print("* " * 10)
            print("\n")
            quit()

def restart_quiz():
    '''Allow the player to start the game from the beginning. Choose a new level. Outputs: Entire game.'''
    global restart
    restart = input("Would you like to start again?: ")
    if restart in yesList:
        start_game()
    elif restart in noList:
        return game_over()
    else:
        print("\nI'm sorry, I do not understand your choice.\n")
        restart = ("\nWould you like to start again?\nYes or No?: ")
        
        if restart in yesList:
            start_game()
        else:
            game_over()

def game_over():
    print("\n" + "* " * 10)
    print("\nGAME OVER\n")
    print("* " * 10)
    print("\nTHANK YOU FOR STOPPING BY!\n")
    print("* " * 10)
    print("\n")
    quit()

##############  Starting to actually play the 'game'  ##############

def start_game():
    '''Starts actual game play. Outputs: Entire program.'''

    welcome()
    advise_guesses()
    global level
    
    level = input("\n""\nPlease choose your difficulty level - Easy, Medium, Hard, Ultimate: ") 
    print("")

    if level in levelList:
        quiz, answers = level_choice(level)
        print(quiz)
        replaced = answer_question(level, quiz, answers)
    else:
        print("\nI'm sorry, I do not understand your choice.")
        level = input("Please choose from the following - Easy, Medium, Hard, Ultimate: ")
        if level in levelList:
            quiz, answers = level_choice(level)
            print(quiz)
            replaced = answer_question(level, quiz, answers)
        else: 
            print("\nI'm sorry, I do not understand your choice.")
            print("\nThe game will now restart.")
            
            start_game()

    return winner_winner()

start_game()
