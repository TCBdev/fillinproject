easyList = ["easy", "ez"]
intermediateList = ["intermediate", "medium", "med"]
hardList = ["hard"]
ultimateList = ["ultimate"]
yesList = ["yes", "y", "yeah", "yah", "ye"]
noList = ["no", "n", "nah", "meh"]
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]    

easy_quiz = """Naruto graduates the Ninja ___1___ and joins Team ___2___, along side his rival ___3___, his crush ___4___ and his sensei ___5___. Source: Naruto.Wikia"""
intermediate_quiz = """The ___1___ begin kidnapping the ___2___ to extract their ___3___ and revive the ___4___. With the ___4___ restored, the Akatsuki can cast the ___5___ Tsukuyomi. Source: Naruto.Wikia"""
hard_quiz = """Naruto is incapable of performing the basic ___1___ Technique. This leaves him unable to graduate from the Academy, one of his instructors, ___2___, tells Naruto that if he could steal the Scroll of ___3___ and learn one of its secret techniques, Naruto will graduate. After successfully stealing the scroll, ___4___ is caught by another instructor, ___5___. Source: Naruto.Wikia"""
ultimate_quiz = """The Hyuga is one of the ___1___ noble clans of Konohagakure. All members born into this clan possess the ___2___, a ___3___ that gives them extended fields of vision and the ability to see through solid objects and even the ___4___ circulatory system, amongst other things. Members of this clan also possess the unique ability to expel ___4___ from any of the ___5___ in their body. Source: Naruto.Wikia"""

easy_answers = ["academy", "seven" or "7", "sasuke", "sakura", "kakashi"]
intermediate_answers = ["akatsuki", "jinchuriki", "tailed beast", "ten tails" or "ten-Tails", "infinite"]
hard_answers = ["clone", "mizuki", "seals", "naruto", "iruka" or "iruka umino" or "iruka sensei"]
ultimate_answers = ["four" or "4", "byakugan", "kekkei genkai", "chakra", "tenketsu"]

##############  QUIZ DEFINITIONS  ##############

def welcome(): # GOOD TO GO #
    '''Get players name'''
    global player_name
    print("\n" + "* " * 10)
    print("\nWELCOME TO THE QUIZ TO END ALL QUIZES!\n")
    print("* " * 10)
    player_name = input("\n"r"\/\/\/\/\/\/\/\/\/**NARUTO: Still a Genin?! ¯\_(ツ)_/¯ **/\/\/\/\/\/\/\/\/" "\n""\nPlease tell me your name: ")
    print("\nHello " + player_name)
    print("\nLET'S GET STARTED!!")


def level_choice(level): # GOOD TO GO #
    '''Player chooses level. Executed quiz and answers'''
    if level in easyList:
        return easy_quiz, easy_answers
    elif level in intermediateList:
        return intermediate_quiz, intermediate_answers
    elif level in hardList:
        return hard_quiz, hard_answers
    else:
        return ultimate_quiz, ultimate_answers

def advise_guesses():
    '''Player can determine how many guesses they would like per play, once guesses are 0, game restarts.'''
    global guesses
    guesses  = int(input("\nHow many guesses would you like (up to 5)?: "))
    if int(guesses) < 1 or int(guesses) > 5:
        guesses = input("Please enter a number that is greater than 0, but less than or equal to 5:  ")
    #else: ###########  FIX THIS  ###########
    #    print("Invalid entry. Game will reset.")
    #    return start_game
    guesses = int(guesses)
    print("\n", guesses, "guess(es) it is!!")

def all_blanks(word, blanks): # GOOD TO GO #
    '''To single out every blank. 
    Identifies 'blank' in each quiz AND each blank in the 'blanks' list. With correct answer, quiz is returned with 'word'.'''

    for blank in blanks: # For every blank in the blanks array.
        if blank in word: # If blank is in answer.
            return blank
    return None

def replace_blanks(word, replaced, blanks, player_answer, index): 
    """To replace each blank with its correct answer.
    Inputs: 'blanks' list, the replaced paragraph that has the correct answers so far, if applicable,
    the 'player_answer' for that blank, the index number of that 'player_answer' to correctly match that with the right blank to fill in. 
    Outputs: The correctly replaced paragraph."""

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

def retrieve_answers(quiz, blanks, replaced, player_answer, index): # GOOD TO GO #
    '''Replaces each ___#___ with its correct answer.
    Inputs: Player selected quiz, blanks, the quiz with correct replaced answers + remaining unanswered blanks.
    Outputs: The correctly replaced paragraph.'''

    split_quiz = quiz.split()

    if type(replaced) == str:
        replaced = replaced.split()		

    for word in split_quiz:
        replace_blanks(word, replaced, blanks, player_answer, index)
        
    replaced = " ".join(replaced)
    head, sep, tail = replaced.partition("Naruto.Wikia")
    replaced = head + sep
    return replaced

def answer_question(level, quiz, answers): # GOOD TO GO #
    '''To collect the user's answers. 
    Inputs: The level, the selected level, and corresponding level answers.
    Outputs: The quiz with correct answer replaced (CAPS), the index of each answer.'''
    
    replaced = []
    player_answer = ""

    index = 0
    for blank in blanks:
        global guesses
        question = "\nFor " + blank + " "
        print(question)
        player_answer = input("What is your answer?: ")
        player_answer = player_answer.lower()

        while player_answer != answers[index]:
            print("\nIncorrect. Please try again.\n")
            if guesses > 1:
                guesses += -1 
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

        index += 1

    return replaced, index

def winner_winner(): # GOOD TO GO #
    '''
    Allows player to choose bonus content, quit the game, or restart the quiz
    '''
    print("\nWinner Winner Chicken Dinner" "\nCongratulations you won the game!")
    bonus_level = input("\nWould you like to play a bonus level?: ")
    if bonus_level in yesList:  
            return restart_quiz()
    elif bonus_level in noList:
            return restart_quiz()
    else:
        print("I'm sorry, I do not understand your choice.")
        bonus_level = input("\nWould you like to play a bonus level?" "\n Yes or No?: ")
        if bonus_level in yesList:  
            return restart_quiz()
        elif bonus_level in noList:
            return restart_quiz()
        else:
            print("\n" + "* " * 10)
            print("\nGAME OVER\n")
            print("* " * 10)
            print("\nTHANK YOU FOR STOPPING BY!\n")
            print("* " * 10)
            print("\n")
            quit()


def restart_quiz(): # GOOD TO GO #
    '''
    Allow the player to start the game fromthe beginning. Choose a different level.
    '''
    global restart
    restart = input("Would you like to start again?: ")
    if restart in yesList:
        start_game()
    elif restart in noList:
        print("\n" + "* " * 10)
        print("Thank you for participating in my quiz!" "\n GOLD STAR." "\n Come back soon!")
        print("* " * 10)
        quit()
    else:
        print("\n" + "* " * 10)
        print("\nI'm sorry, I do not understand your choice.\n")
        print("* " * 10)
        print("\nWould you like to start again?\n")
        print("* " * 10)
        restart = input("\nYes or No?: ")
        if restart in yesList:
            start_game()
        else:
            print("\n" + "* " * 10)
            print("\nGAME OVER\n")
            print("* " * 10)
            print("\nThank you for participating\n")
            print("* " * 10)
            print("")
            quit()


##############  Starting to actually play the 'game'  ##############

def start_game():
    '''Starts actual game play. Executes entire program.'''

    welcome()
    advise_guesses()
    level = input("\n""\nPlease choose your difficulty level - Easy, Intermediate, Hard, Ultimate: ") 
    print("")

    if level in easyList or level in intermediateList or level in hardList or level in ultimateList:
        quiz, answers = level_choice(level)
        print(quiz)
        replaced = answer_question(level, quiz, answers)
    else:
        print("\nI'm sorry, I do not understand your choice.")
        level = input("Please choose from the following - Easy, Intermediate, Hard, Ultimate: ")
        if level in easyList or level in intermediateList or level in hardList or level in ultimateList:
            quiz, answers = level_choice(level)
            print(quiz)
            replaced = answer_question(level, quiz, answers)
        else: # ADD A TIMER TO DELAY THE RESTART #
            print("\nI'm sorry, I do not understand your choice.")
            print("\nThe game will now restart.")
            start_game()

    return winner_winner()

'''
if __name__ == '__main__':
    ## Test functions
    assert answer_question(player_answer["easy_quiz"][1], 'seven') == True
    assert answer_question(player_answer["easy_quiz"][2], 'sasuke uchiha') == True
    assert answer_question(player_answer["easy_quiz"][3], 'sakura haruno') == True
    assert answer_question(player_answer["easy_quiz"][4], 'kakashi hatake') == True
    assert answer_question(player_answer["easy_quiz"][3], 'sasuke uchiha') == True
    assert answer_question(player_answer['medium'][5], 'space time') == True
    assert answer_question(player_answer['medium'][3], 'time') == False
    assert answer_question(player_answer['hard'][1], 'OSCAR') == True
'''
start_game()
