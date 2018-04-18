import random
ret_launch=["Welcome to Monopoly Master","Hey there I'm monopoly master","Hello. You have summoned the monopoly master"]
ask_no_players=["How many players do we have today","How many are in","How many of you are playing today"]







def random_statement(phraselist):
    statement=phraselist[random.randrange(len(phraselist))]
    return statement