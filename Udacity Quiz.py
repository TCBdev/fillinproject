# -*- coding: utf-8 -*- 
import time

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
    score = 0
    time.sleep(1) #delay next function by (#) seconds
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL!")
    time.sleep(1)
    print("\nThis next section will have three (3) multiple choice questions.")
    time.sleep(1)
    print("\nWhat is the name of Tsunade's summoning animal?: \n\n     (A) Manda\n     (B) Katsuyu\n     (C) Jiraya\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'B' or answer == 'b':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nWhat's the name of the Cursed Seal given to both Sasuke Uchiha and Anko Mitarashi?: \n\n     (A) Heaven Cursed Seal\n     (B) Mud Wall Seal\n     (C) Reaper's Death Seal\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'A' or answer == 'a':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)
    
    time.sleep(2)
    print("\nWho was Naruto Uzumaki's father?: \n\n     (A) Sasuke Uchiha\n     (B) Minato Namikaze \n     (C) Orochimaru\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'B' or answer == 'b':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," You're AMAZING!!\n")
        return restart_quiz()
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," Fantastic!!\n")
        return restart_quiz()

def med_bonus():
    score = 0
    time.sleep(1)
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL!")
    time.sleep(1)
    print("\nThis next section will have three (3) multiple choice questions.")
    time.sleep(1)
    print("\nThe quiz will begin shortly.")
    time.sleep(2)
    print("\nThe Village Hidden in the Leaves can be found in what country?: \n\n     (A) The Land of Fire\n     (B) The Land of Lightning\n     (C) The Land of Earth\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'A' or answer == 'a':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nFILL IN THE BLANK.\nGaara is the _____ Kazakagae: \n\n     (A) First\n     (B) Fifth\n     (C) Forth\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'B' or answer == 'b':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nHow many tails does the tailed beast (biju) Son Gokū have?: \n\n     (A) Three (3)\n     (B) Ten (10)\n     (C) Four (4)\n\n") 
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'C' or answer == 'c':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," You're AMAZING!!\n")
        return restart_quiz()
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," Fantastic!!\n")
        return restart_quiz()

def hard_bonus():
    score = 0
    time.sleep(1)
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL!")
    time.sleep(1)
    print("\nThis next section will have three (3) multiple choice questions.")
    time.sleep(1)
    print("\nWho was Tsunade's fiancée?: \n\n     (A) Dan\n     (B) Jiraiya\n     (C) Minato\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'A' or answer == 'a':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nNagato is a member of which clan?: \n\n     (A) Uzumaki\n     (B) Hyuga\n     (C) Akatsuki\n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'A' or answer == 'a':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nWho was Naruto's teacher at the ninja academy?: \n\n     (A) Iruka\n     (B) Kakashi\n     (C) Hiruzen \n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'A' or answer == 'a':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," You're AMAZING!!\n")
        return restart_quiz()
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," Fantastic!!\n")
        return restart_quiz()

def ultimate_bonus():
    score = 0
    time.sleep(1)
    print("\nCONGRATULATIONS ON MAKING IT TO THE BONUS LEVEL!\n\n  M  E  M  E     E  X  T  R  E  M  E  !")
    time.sleep(1)
    print("\nThis next section will have three (3) multiple choice questions.")
    time.sleep(1)
    print("\nWho was Naruto's first kiss with?: \n\n     (A) Sakura\n     (B) Hinata \n     (C) Sasuke \n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'C' or answer == 'c':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nWho is the child of Sasuke and Sakura?: \n\n     (A) Hinata\n     (B) Sarada\n     (C) Salad \n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'C' or answer == 'c':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)

    time.sleep(2)
    print("\nWho is the male parental figure for Himawari?: \n\n     (A) Naruto\n     (B) Boruto's Dad\n     (C) Sasuke \n\n")
    time.sleep(2)
    answer = input("Your Answer?: ")
    if answer == 'B' or answer == 'b':
        print("CORRECT!!")
        score = score + 1
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," You're AMAZING!!\n")
        return restart_quiz()
    else:
        print("Incorrect")
        time.sleep(1)
        print(r":'(")
        time.sleep(1)
        print("Bonus Score: ", score)
        print("\nYou have completed the bonus level!\n")
        print("You're Bonus Score is", score," Fantastic!!\n")
        return restart_quiz()

def welcome(): 
    '''Get players name'''
    print("\n" + "* " * 10)
    time.sleep(1)
    print("\nWELCOME TO THE QUIZ TO END ALL QUIZES!\n")
    time.sleep(1)
    print("* " * 10)
    time.sleep(1)
    print("\n"r"\/\/\/\/\/\/\/\/\/**NARUTO: Still a Genin?! ¯\_(ツ)_/¯ **/\/\/\/\/\/\/\/\/")
    time.sleep(1)
    player_name = input("\nPlease tell me your name: ")
    time.sleep(1)
    print("\nHello " + player_name)
    time.sleep(1)
    print("\nLET'S GET STARTED!!")
    time.sleep(1)

def level_choice(level): 
    '''Player chooses level. Executed quiz and answers
    Inputs: Current level.  
	Outputs: The specific quiz and its answers associated with that level.'''
    if level == "easy" or level == "Easy" or level == "EASY" or level == "ez" or level == "EZ" or level == "E" or level == "e":
        return easy_quiz, easy_answers
    elif level == "intermediate" or level == "Intermediate" or level == "INTERMEDIATE" or level == "I" or level == "i" or level == "medium" or level == "Medium" or level == "MEDIUM" or level == "med" or level == "Med" or level == "MED" or level == "M" or level == "m":
        return intermediate_quiz, intermediate_answers
    elif level == "HARD" or level == "hard" or level == "Hard" or level == "H" or level == "h":
        return hard_quiz, hard_answers
    elif level == "ultimate" or level == "Ultimate" or level == "ULTIMATE" or level == "U" or level == "u":
        return ultimate_quiz, ultimate_answers

def advise_guesses():
    '''Player can determine how many guesses they would like. Allows to choose between 1 and 5 guesses'''
    global guesses
    global min_guess
    min_guess = 1
    global max_guess
    max_guess = 5
    try:
        guesses  = int(input("\nHow many guesses would you like (up to 5)?: "))
        while int(guesses) < min_guess or int(guesses) > max_guess:
            time.sleep(1)
            guesses = input("Please enter a number that is greater than 0, but less than or equal to 5:  ")
    except:
        time.sleep(1)
        print("\nInvalid entry.\n")
        time.sleep(1)
        try:
            guesses  = int(input("\nHow many guesses would you like (up to 5)?: "))
            while int(guesses) < min_guess or int(guesses) > max_guess:
                time.sleep(1)
                guesses = input("Please enter a number that is greater than 0, but less than or equal to 5:  ")
        except:
            time.sleep(1)
            print("\nInvalid entry.\n")
            time.sleep(1)
            print("\nGame will reset.\n")
            time.sleep(2)
            return start_game()
    guesses = int(guesses)
    time.sleep(1)
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
                time.sleep(1)
                print(guesses, "guess(es) remaining")
                time.sleep(1)
                player_answer = input("\nWhat is your answer for " + blank + "?: ")
                player_answer = player_answer.lower()
            else:
                print("\n" + "* " * 10)
                time.sleep(1)
                print("\nGAME OVER\n")
                time.sleep(1)
                print("* " * 10)
                time.sleep(1)
                print("\nYOU LOSE\n")
                time.sleep(1)
                print("* " * 10)
                time.sleep(1)
                print("\n")
                return restart_quiz()

        time.sleep(1)
        print("\nCORRECT!!\n")
        time.sleep(1)
									
        replaced = retrieve_answers(quiz, blanks, replaced, player_answer, index)
        print(replaced)			

        index += 1

    return replaced, index

def bonus_level():
    '''Program checks player original selected level, returns appropriate bonus level/answers
    Inputs:  level selected by the user.  
	Outputs: The specific bonus quiz.'''
    if level == "easy" or level == "Easy" or level == "EASY" or level == "ez" or level == "EZ":
        return easy_bonus()
    elif level == "intermediate" or level == "Intermediate" or level == "INTERMEDIATE" or level == "I" or level == "i" or level == "medium" or level == "Medium" or level == "MEDIUM" or level == "med" or level == "Med" or level == "MED" or level == "M" or level == "m":
        return med_bonus()
    elif level == "HARD" or level == "hard" or level == "Hard" or level == "H" or level == "h":
        return hard_bonus()
    elif level == "ultimate" or level == "Ultimate" or level == "ULTIMATE" or level == "U" or level == "u":
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
            game_over()

def restart_quiz():
    '''Allow the player to start the game from the beginning. Choose a new level. Outputs: Entire game.'''
    global restart
    restart = input("Would you like to start again?: ")
    if restart in yesList:
        start_game()
    elif restart in noList:
        return game_over()
    else:
        time.sleep(1)
        print("\nI'm sorry, I do not understand your choice.\n")
        time.sleep(1)
        restart = ("\nWould you like to start again?\nYes or No?: ")
        time.sleep(1)
        if restart in yesList:
            start_game()
        else:
            game_over()

def game_over():
    print("\n" + "* " * 10)
    time.sleep(1)
    print("\nGAME OVER\n")
    time.sleep(1)
    print("* " * 10)
    time.sleep(1)
    print("\nTHANK YOU FOR STOPPING BY!\n")
    time.sleep(1)
    print("* " * 10)
    time.sleep(1)
    print("\n")
    time.sleep(5)
    quit()

##############  Starting to actually play the 'game'  ##############

def start_game():
    '''Starts actual game play. Outputs: Entire program.'''

    welcome()
    advise_guesses()
    global level
    time.sleep(1)
    level = input("\n""\nPlease choose your difficulty level - Easy, Medium, Hard, Ultimate: ") 
    print("")

    if level in levelList:
        quiz, answers = level_choice(level)
        print(quiz)
        replaced = answer_question(level, quiz, answers)
    else:
        time.sleep(1)
        print("\nI'm sorry, I do not understand your choice.")
        time.sleep(1)
        level = input("Please choose from the following - Easy, Medium, Hard, Ultimate: ")
        if level in levelList:
            quiz, answers = level_choice(level)
            print(quiz)
            replaced = answer_question(level, quiz, answers)
        else: 
            time.sleep(1)
            print("\nI'm sorry, I do not understand your choice.")
            time.sleep(1)
            print("\nThe game will now restart.")
            time.sleep(1)
            start_game()

    return winner_winner()

start_game()
