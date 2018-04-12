#TODO: Move global variables to __main__
#from question import Question
def play_game():
    easyList = ["Easy", "easy", "EASY"]
    intermediateList = ["Intermediate", "INTERMEDIATE", "medium", "Medium", "MEDIUM", "MED", "med", "Med"]
    hardList = ["Hard", "hard", "hArd", "hARD", "HARD"]
    ultimateList = ["ultimate", "Ultimate", "ULTIMATE"]
    yesList = ["yes", "YES", "Yes", "yES", "yEs", "YeS", "yeS", "y", "Y", "yeah", "yah", "ye", "Yeah", "YEAH", "YAH", "YE", "Ye", "Yah"]
    noList = ["no", "nO", "No", "NO", "N","n", "nah", "Nah", "NAH", "meh", "MEH", "Meh"]
    #blanks = ["___1___", "___2___", "___3___", "___4___", "___5___"]    
    
    quiz_entry = {}
    quiz_entry['easy_quiz'] = """Naruto graduates the Ninja Academy and joins Team ___1___, along side his rival ___2___, his crush ___3___ and his sensei ___4___."""
    quiz_entry['intermediate_quiz'] = """The Akatsuki begin kidnapping the ___1___ to extract their ___2___ and revive the ___3___. With the ___3___ restored, the Akatsuki can cast the ___4___."""
    quiz_entry['hard_quiz'] = """Naruto is incapable of performing the basic ___1___ Technique. This leaves him unable to graduate from the Academy, one of his instructors, ___2___, tells Naruto that if he could steal the Scroll of ___3___ and learn one of its secret techniques, Naruto will graduate. After successfully stealing the scroll, ___4___ is caught by another instructor, ___5___."""
    quiz_entry['ultimate_quiz'] = """The Hyuga is one of the ___1___ noble clans of Konohagakure. All members born into this clan possess the ___2___, a ___3___ that gives them extended fields of vision and the ability to see through solid objects and even the ___4___ circulatory system, amongst other things. Members of this clan also possess the unique ability to expel ___4___ from any of the ___5___ in their body."""
    
    quiz_answers = {
            'easy_answers': [["seven", "Seven", "7"],
                ["Sasuke", "sasuke", "Sasuke Uchiha", "sasuke uchiha"],
                ["Sakura Harano", "sakura haruno", "Sakura", "sakura"],
                ["Kakashi", "kakashi", "Kakashi Hatake", "kakashi hatake"]],
            'intermediate_answers': [["Jinchuriki", "jinchuriki"],
                ["tailed beast", "Tailed beast", "Tailed Beast"],
                ["ten tails", "Ten-Tails", "Ten Tails", "Ten tails"],
                ["Infinite Tsukuyomi", "infinite tsukuyomi"]],
            'hard_answers': [["Clone", "clone"],
                ["Mizuki", "mizuki"],
                ["Seals", "seals", "Seal", "seal"],
                ["Naruto", "naruto"],
                ["Iruka Umino", "iruka umino", "Iruka", "iruka", "Iruka Sensei","iruka sensei","Iruka sensei"]],
            'ultimate_answers': [["Four", "four", "4"],
                ["Byakugan", "byakugan"],
                ["kekkei genkai", "Kekkei genkai", "Kekkei Genkai"],
                ["chakra", "Chakra"],
                ["tenketsu", "Tenketsu"]]}
    
    alive = True
    guesses, level = 1, quiz_entry
    
    def welcome():
        player_name = input("\n"r"\/\/\/\/\/\/\/\/\/**NARUTO: Still a Genin?! ¯\_(ツ)_/¯ **/\/\/\/\/\/\/\/\/" "\n""\nPlease tell me your name: ")
        print("\nHello " + player_name)
        begin = input("\nTo begin the quiz, type 'YES': ")
        while begin not in yesList and noList:
            begin = input("\nI'm sorry, I do not understand your choice. Would you like to begin the quiz - 'Yes' or 'No': ")
            if begin in noList:
                print("Thank you for stopping by!")
                quit()
            elif begin in yesList:
                print("\n""\nGREAT! " + player_name + " Let's get started!")
            else:
                break
    
    def level_choice():
        global level
        level = input("\n""\nPlease choose your difficulty level - Easy, Intermediate, Hard, Ultimate: ") 
        while level not in easyList and intermediateList and hardList and ultimateList:
            level = input("\nI'm sorry, I do not understand your choice. Please choose from the following - Easy, Intermediate, Hard, Ultimate: ")
            break
        if level in easyList:
            print(quiz_entry['easy_quiz'])
        elif level in intermediateList:
            print(quiz_entry['intermediate_quiz'])
        elif level in hardList:
            print(quiz_entry['hard_quiz'])
        else:
            print(quiz_entry['ultimate_quiz'])

        #print(quiz_entry[level])
            #return level

    def check_answer(possible, guesses):

        for answer in possible:
            if guesses.lower() == answer.lower():
                print("Correct! Keep up the good work!") or ("Correct! You're doing amazing!")
            else: 
                print("Incorrect. Please try again. " + str (guesses) + " guesses left!")

    def restart_quiz():
        global restart
        restart = input("Would you like to start again?: ")
        if restart not in yesList:
            restart = input("I'm sorry, I do not understand your choice." "\nWould you like to start again?" "\nYes or No?: ")
        elif restart in yesList:
            play_game()
        elif restart in noList:
            print("Thank you for participating in my quiz!" "\n GOLD STAR." "\n Come back soon!")
            quit()
    '''
    def bonus_quiz():
        if level in easyList:
            return quiz_entry[level]['bonus_easy_quiz']
        elif level in intermediateList:
            return quiz_entry[level]['bonus_intermediate_quiz']
        elif level in hardList:
            return quiz_entry[level]['bonus_hard_quiz']
        else:
            return quiz_entry[level]['bonus_ultimate_quiz']
    '''
    def winner_winner():
        bonus_level = input("Winner Winner Chicken Dinner" "\nCongratulations you won the game!" "\nWould you like to play a bonus level?: ")
        while bonus_level not in yesList:
            bonus_level = input("I'm sorry, I do not understand your choice." "\nWould you like to play a bonus level?" "\n Yes or No?: ")
            if bonus_level in yesList:  
                return restart_quiz
            else:
                return restart_quiz            

    def game_over():
        print("GAME OVER" "\nYOU LOSE" "\nI'm sorry, you failed to obtain a score of 2 or more")
        return restart

    def answer_question(index, level):
        ''' 
        Gets the player's input for blank number ``index``.
        Sets the global variable ``alive`` to False if the player
        has used all their chances.
        Returns:
        string: Quiz updated with player's answer.
        '''
        global guesses
        guesses = 3
        answer = quiz_answers.items()

        while guesses > 0:
            guess = input("What is your answer for ___%s___: " % str(index))
            if check_answer(answer, guess):
                print("CORRECT!! Way to go! \n")
                print('-' * 20)
                level = level.replace('___%s___' % str(index), guess)
                print(level)
                print('-' * 20 + '\n')
                break
            elif guesses > 1:
                print("Incorrect. Please try again. " +guesses + " guesses left!")
                guesses += -1
                print(guesses, "guess(es) left. \n")
            else:
                guesses = False
                return game_over
        return level

    '''
    def answer_bonus(index, quiz):
        answer = quiz_answers[level][index]
    '''

    def start_quiz():
        '''   
        Shows the quiz and asks the user for answers.
        Returns:
            bool: True if the user completes the quiz, ``False`` if they use
            too many guesses.
        '''
        global alive
        alive = True
        print("\n" + "* " * 10)
        print("\nWELCOME TO THE QUIZ TO END ALL QUIZES!\n")
        print("* " * 10)
        welcome()
        level_choice()
        quiz = frozenset(quiz_entry.items())

        for key, elem in (quiz_answers.items()):
            quiz = answer_question(elem, quiz)
            if not alive: break

        if alive:
            return winner_winner
        else:
            return game_over

        return alive

    '''
    Main
    while True:
    '''
    start_quiz()
          

play_game() 