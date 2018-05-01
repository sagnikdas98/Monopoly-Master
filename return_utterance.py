import random

your_card = ["You card says {}"]

you_have_rolled=[" You have rolled a {} and a {} . ", " Its a {} and a {}", "You have got {} and {}"]

ret_launch=["Welcome to Monopoly Master. ","Hey there I'm monopoly master. ", "Hello. You have summoned the monopoly master."]

ask_no_players=["How many players do we have today. ", "How many are in. ", "How many of you are playing today. "]

confirmation=["Roger that. ","Okay, got it. ", " Affirmative."]

too_many=["Oops, I cant handle more than four players. ", "That's a lot of players for me to handle. ",
          "I can only manage two to four players. ", "I m sorry. I can only manage two to four players. "]

ask_again=["So how many players now? ", "Please reconsider your players. ", "Please limit the players from 2 to 4. "]

not_valid=["That answer didn't satisfy my question. ", "That wasn't the answer I was looking for. ", "Please reconsider your response."]

alone=["Oops, you cannot play this game alone. ", "You look pretty lonely. ", " You need atleast 2 players to play this game."]

set_board=["Your virtual board has been set for {} players. ","I created a board for {} player. ", "A game for {} players is ready. "]

out_of_jail=["You are out of jail now.", "Alas you are out of jail", ""]

have_to_pass=["You have to pass to the next player as you dont have enough resources to get out of jail. "]

want_to_buy_house=["Do you want to build a house here. "]

house_bought_success=["House has been built. Congratulation. "]

win = ["Player {} wins. Congratulations."]

finish = ["The game ends."]

which_prop_to_mortgage=["Which property do you want to mortgage. "]

not_owned_property = ["You have no property to mortgage. " ]

mortgage_done=["Your property has been mortgaged. "]

want_to_buy_prop=["Do you wish to buy this property? "]

player_in_jail=["Oops. Looks like you are in jail right now."]

jail_card_or_money=["Do you wish to use jail card or pay 50 dollar to get out of jail or pass to the next player. "]

jail_card=["Do you wish to use you jail card to get out of jail? "]

jail_money=["Do you wish to pay 50 dollars to get out of jail? " ]


want_to_buy_railroad = ["Do you want to buy this rail road? "]

want_to_buy_utility = ["Do you want to buy this utility? "]

property_landed = ["You have landed on {}. "]

owned_property = ["The property has been added to your empire. "]

tax_fail = ["Due to insufficient balance you have failed to pay the tax. You lose."]

tax_pass = ["{} dollars has been deducted from your account. "]

landed_on_free_space = ["You have landed on free space. "]  # not required

insufficient_balance = ["Due to insufficient balance you lose."]

already_owned_by_you = ["You already own this property."]

already_owned_by_you_railroad = ["You already own this railroad."]

already_owned_by_you_utility = ["You already own this utility."]


next_player_turn=["Now its Player {}'s turn. "]

you_have_paid_rent_to = ["You have paid rent of {} dollars to {} . "]

insufficient_balance_rent = ["Due to insufficient balance for rent you lose."]

current_balance = ["You currently have {} dollars in your account. "]

out_of_jail_now = ["You are out of jail now. you can roll the dice"]

finish_no_start = ["I hope you play the next time.", "Please play the next time.", "Everybody wins this game.", "We don't have a winner for this game."]

cant_buy_house = "You cannot buy a house right now. "

help_utter_1 = ["Monopoly Master is recast of the original game."]
help_utter_2 = ["Presence of mind is the key to be a true Monopoly Master."]
help_utter_3 = ["Each player can choose to, roll the die, know account balance, know property list, know net worth and mortgage property."]
help_utter_4 = ["Players with insufficient account balance for obligatory transactions will loose."]
help_utter_5 = ["Last player remaining wins. If you wish to end the game at any point then the player with maximum net worth wins."]


def format_statement(phrase,formatlist):
    return phrase.format(formatlist)

def format_statement_2(phrase,for1,for2):
    return phrase.format(for1,for2)

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
