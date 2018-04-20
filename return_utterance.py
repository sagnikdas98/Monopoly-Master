import random
ret_launch=["Welcome to Monopoly Master. ","Hey there I'm monopoly master. ","Hello. You have summoned the monopoly master. "]

ask_no_players=["How many players do we have today. ","How many are in. ","How many of you are playing today. "]

confirmation=["Roger that. ","okay, got it. "]

too_many=["Oops, I cant handle more than four players. ", "That's a lot of players for me to handle. ",
          "I can only manage two to four players. ", "I m sorry. I can only manage two to four players. "]

ask_again=["so how many players now? ","please consider your players again. ",]

not_valid=["That answer didn't satisfy my question. ", "The wasn't the answer I was looking for. "]

alone=["Oops, you cannot play this game alone. ", "You look pretty lonely. "]

set_board=["Your virtual board has been set for {} players. ","I created a board for {} player. ","A game for {} players is ready. "]

win=[]

turn_player=[]

def format_statement(phrase,formatlist):
    return phrase.format(formatlist)

def combine_statement(phrase1, phrase2, phrase3 = " "):
    return phrase1 + "   " + phrase2 + "  " + phrase3

def random_statement(phraselist):
    statement = phraselist[random.randrange(len(phraselist))]
    return statement

