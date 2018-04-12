#def play_game():
easyList = ["Easy", "easy", "EASY"]
intermediateList = ["Intermediate", "INTERMEDIATE", "medium", "Medium", "MEDIUM", "MED", "med", "Med"]
hardList = ["Hard", "hard", "hArd", "hARD", "HARD"]
ultimateList = ["ultimate", "Ultimate", "ULTIMATE"]
yesList = ["yes", "YES", "Yes", "yES", "yEs", "YeS", "yeS", "y", "Y", "yeah", "yah", "ye", "Yeah", "YEAH", "YAH", "YE", "Ye", "Yah"]
noList = ["no", "nO", "No", "NO", "N","n", "nah", "Nah", "NAH", "meh", "MEH", "Meh"]
quiz_entry = {}
quiz_entry['easy_quiz'] = """Naruto graduates the Ninja Academy and joins Team ___1___, along side his rival ___2___, his crush ___3___ and his sensei ___4___."""
quiz_entry['intermediate_quiz'] = """The Akatsuki begin kidnapping the ___1___ to extract their ___2___ and revive the ___3___. With the ___3___ restored, the Akatsuki can cast the ___4___."""
quiz_entry['hard_quiz'] = """Naruto is incapable of performing the basic ___1___ Technique. This leaves him unable to graduate from the Academy, one of his instructors, ___2___, tells Naruto that if he could steal the Scroll of ___3___ and learn one of its secret techniques, Naruto will graduate. After successfully stealing the scroll, ___4___ is caught by another instructor, ___5___."""
quiz_entry['ultimate_quiz'] = """The Hyuga is one of the ___1___ noble clans of Konohagakure. All members born into this clan possess the ___2___, a ___3___ that gives them extended fields of vision and the ability to see through solid objects and even the ___4___ circulatory system, amongst other things. Members of this clan also possess the unique ability to expel ___4___ from any of the ___5___ in their body."""

for key,value in quiz_entry.items():
    print("KEY:")
    print(key)
    print("VALUE:")
    print(value)
    print("")

'''
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
        for level in easyList:
            print(quiz_entry['easy_quiz'])
            if level in intermediateList:
                print(quiz_entry['intermediate_quiz'])
            elif level in hardList:
                print(quiz_entry['hard_quiz'])
            else:
                print(quiz_entry['ultimate_quiz'])
            break
    
    def start_quiz():

        global alive
        alive = True
        print("\n" + "* " * 10)
        print("\nWELCOME TO THE QUIZ TO END ALL QUIZES!\n")
        print("* " * 10)
        welcome()
        level_choice()
        quiz = quiz_entry['level']

    while True:
        start_quiz()

play_game()
'''