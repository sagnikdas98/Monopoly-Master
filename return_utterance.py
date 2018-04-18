import random
ret_launch=["Welcome to Monopoly Master","Hey there I'm monoploy master","Hello. You have summoned the monopoly master"]

def random_statement(phraselist):
    statement=phraselist[random.randrange(len(phraselist))]
    return statement