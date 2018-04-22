from return_utterance2 import *
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

out_of_jail=["You are out of jail now"]

have_to_pass=["You have to pass to the next player as you dont have enough resources to get out of jail. "]

want_to_buy_house=["Do you want to build a house here. "]

house_bought_success=["House has been built. Congratulation. "]

win = ["Player {} wins. Congratulations."]

which_prop_to_mortgage=["Which property do you want to mortgage. "]


turn_player = [ ]


not_owned_property = ["You have no property to mortgage. " ]

mortgage_done=["Your property has been mortgaged. "]

buy_or_not = ["" ]

pay_rent = [ ]

want_to_buy_prop=["Do you wish to buy this property? "]

player_in_jail=["Oops. Looks like you are in jail right now."]

jail_card_or_money=["Do you wish to use jail card or pay 50 dollar to get out of jail or pass to the next player. "]

jail_card=["Do you wish to use you jail card to get out of jail? "]

jail_money=["Do you wish to pay 50 dollars to get out of jail? " ]


def format_statement(phrase,formatlist):
    return phrase.format(formatlist)

def combine_statement(phrase1, phrase2, phrase3 = " "):
    return phrase1 + "   " + phrase2 + "  " + phrase3

def random_statement(phraselist):
    statement = phraselist[random.randrange(len(phraselist))]
    return statement

def combine_say_it(phraselist):
    say = ""
    for i in phraselist:
        say = say + " " + i

    return say
