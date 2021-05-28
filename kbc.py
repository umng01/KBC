from questions import QUESTIONS


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''


    return True if question["answer"] == answer\
        else False      #remove this


def lifeLine(a,b,award1):
    if isAnswerCorrect(QUESTIONS[a], int(b)):
        # print the total money won.
        # See if the user has crossed a level, print that if yes
        print('\nCorrect !')
        award1 = award1 + QUESTIONS[a]["money"]
        print("PRIZE WON",award1)
    else:
        # end the game now.
        # also print the correct answer
        print('\nIncorrect !')
        if a < 4:
            award = 0
            print("PRIZE WON",award)
        elif a >= 4 & a < 10:
            award = 10000
            print("PRIZE WON",award)
        elif a >= 10:
            award = 3, 20, 000
            print("PRIZE WON",award)






    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
    print("WELCOME TO KBC")

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    award=0
    w=1
    for i in range(15):
        print(f'\tQuestion {i+1} : {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')

        # check for the input validations
        if ans=="lifeline":
            if w > 0:
                w = 0
                y = QUESTIONS[i]["answer"]
                if y == 4:
                    print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
                    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
                    ans = input('Your choice ( 1-4 ) : ')
                    lifeLine(i, ans, award)
                    if isAnswerCorrect(QUESTIONS[i], int(ans)):
                        continue
                    else:
                        break
                elif y == 3:
                    print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
                    print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
                    ans = input('Your choice ( 1-4 ) : ')
                    lifeLine(i, ans, award)
                    if isAnswerCorrect(QUESTIONS[i], int(ans)):
                        continue
                    else:
                        break
                elif y == 2:
                    print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
                    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
                    ans = input('Your choice ( 1-4 ) : ')
                    lifeLine(i, ans, award)
                    if isAnswerCorrect(QUESTIONS[i], int(ans)):
                        continue
                    else:
                        break
                else:
                    print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
                    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
                    ans = input('Your choice ( 1-4 ) : ')
                    lifeLine(i, ans, award)
                    if isAnswerCorrect(QUESTIONS[i], int(ans)):
                        continue
                    else:
                        break


            else:
                print("LIFELINE AVAILABLE 0")
                ans = input('Your choice ( 1-4 ) : ')
                award = QUESTIONS[i]["money"]
                lifeLine(i, ans, award)
                if isAnswerCorrect(QUESTIONS[i], int(ans)):
                    continue
                else:
                    break




        elif ans=="quit":
            print("PRIZE WON",award)
            break

        elif isAnswerCorrect(QUESTIONS[i],int(ans)):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print('\nCorrect !')
            award = award + QUESTIONS[i]["money"]
            print("PRIZE WON",award)
        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect !')
            if i<4:
                award=0
                print(award)
            if i>=4& i<10:
                award=10000
                print(award)
            if i>=10:
                award=3,20,000
                print(award)

            break












    # print the total money won in the end.


kbc()
