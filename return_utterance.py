import random
ret_launch=["Welcome to Monopoly Master","Hey there I'm monopoly master","Hello. You have summoned the monopoly master"]

ask_no_players=["How many players do we have today","How many are in","How many of you are playing today"]

confirmation=["Roger that","okay, got it"]

too_many=["Oops, I cant handle more than four players.", "That's a lot of players for me to handle.",
          "I can only manage two to four players.", "I m sorry. I can only manage two to four players."]

ask_again=["so how many players now?","please consider your players again",]

not_valid=["The answer didn't satisfy my question.", "The wasn't the answer i was looking for"]

alone=["oops, you cannot play this game alone","You look pretty lonely"]

setting_board=["Setting up the board.","Creating your game.","Getting your game ready"]



def random_statement(phraselist):
    statement=phraselist[random.randrange(len(phraselist))]
    return statement