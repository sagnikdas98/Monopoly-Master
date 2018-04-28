from monopoly_backend import *
from lambda_stuff import *



current_player = None
current_player_index = 0
number = 0
board = None


def lambda_handler(event, context):

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)


def on_launch(event, content):
    return statement("Start,Number of player", combine_statement(random_statement(ret_launch),random_statement(ask_no_players)))


def intent_router(event, context):
    intent = event['request']['intent']['name']

    if intent == "AMAZON.YesIntent":
        return Yes_Intent(event, context)

    if intent == "AMAZON.NoIntent":
        return No_Intent(event, context)

    if intent == "mortgage":
        return statement("mortgage","You cannot mortgage any property right now.")

    if intent == "usejailcards":
        return statement("jail out", combine_say_it(board.get_out_card(current_player)))

    if intent == "usejailmoney":
        return statement ("jail out", combine_say_it(board.get_out_money(current_player)))

    if intent == "numberOfPlayers":
        return numberOfPlayers_intent(event, context)

    if intent == "nextplayer":
        return nextplayer(event, context)

    if intent == "diceroll":
        return diceroll_intent(event, context)

    if intent == "account_balance":
        return accountbalance_intent(event,context)

    if intent == "prop_list":
        return prop_list_intent(event,context)

    if intent == "buy_house":
        return statement("buy house", combine_say_it(board.buy_house(current_player)))

    if intent == "AMAZON.CancelIntent":
        return stop_intent(event, context)

    if intent == "AMAZON.HelpIntent":
        return help_intent ()

    if intent == "AMAZON.StopIntent":
        return stop_intent(event, context)


def Yes_Intent(event,context):

    if board.question_id == "want_to_buy_prop":
        board.bought_prop(current_player)
        return nextplayer(event, context)

    if board.question_id == "want_to_buy_railroad":
        board.bought_railroad(current_player)
        return nextplayer(event, context)

    if board.question_id == "want_to_buy_utility":
        board.bought_utility(current_player)
        return nextplayer(event, context)

    if board.question_id == "jail_card":
        return statement(" jail out", combine_say_it(board.get_out_card(current_player)))

    if board.question_id == "jail_money":
        return statement(" jail out", combine_say_it(board.get_out_money(current_player)))

    if board.question_id == "buy_house":
        board.bought_house(current_player)
        return nextplayer(event, context)

    return statement("not valid", random_statement(not_valid))


def No_Intent(event, context):

    if board.question_id == "want_to_buy_prop":
        return nextplayer(event, context)

    if board.question_id == "want_to_buy_railroad":
        return nextplayer(event, context)

    if board.question_id == "want_to_buy_utility":
        return nextplayer(event, context)

    if board.question_id == "jail_card":
        return nextplayer(event, context)

    if board.question_id == "jail_money":
        return nextplayer(event, context)

    if board.question_id == "":
        return nextplayer(event, context)

    return statement("not valid", random_statement(not_valid))


def numberOfPlayers_intent(event, context):
    dialog_state = event['request']['dialogState']

    global number

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        slots = event['request']['intent']['slots']
        number = int(slots['number']['value'])

        if number in (2, 3, 4):
            global board , current_player
            board = Board(number)
            current_player = board.playerlist[current_player_index]
            return statement("Confirm,Set Board", combine_statement(random_statement(confirmation),
                                                                    format_statement(random_statement(set_board), number),
                                                                    "Its player one's turn. "))
        # prompt user to roll dice

        elif number == 1:
            return statement("Alone,Ask Again", combine_statement(random_statement(alone), random_statement(ask_again)))

        elif number > 4:
            return statement("Too many, Ask Again", combine_statement(random_statement(too_many), random_statement(ask_again)))

        else:
            return statement("Not valid,Ask Again", combine_statement(random_statement(not_valid), random_statement(ask_again)))

    else:
        return statement("Number of players", "I need a head count")


def nextplayer(event,context):
    global current_player, board,current_player_index
    current_player_index += 1
    current_player = board.playerlist[current_player_index % len (board.playerlist)]
    say_curr_player = format_statement(random_statement(next_player_turn),current_player.number)
    if current_player.jailtime > 0:
        ret_sat = board.jail_check(current_player)
        return statement("In jail + curr_ player", combine_statement(say_curr_player,ret_sat))
    return statement("curr_player", say_curr_player)


def diceroll_intent(event, context):

    rN1 = random.randint(1, 6)
    rN2 = random.randint(1, 6)
    return statement ("diceroll intent", combine_statement(
        format_statement_2(random_statement(you_have_rolled),rN1,rN2), combine_say_it(board.playermove (current_player , rN1 + rN2))))


def accountbalance_intent(event,context):
    acc_bal = current_player.money
    return statement("acc bal", format_statement(random_statement(current_balance),acc_bal))


def prop_list_intent(event,context):

    say_list = []

    for color in current_player.proplist:
        for prop in color:
            say_list.append(prop.name)
    for rail in current_player.raillist:
        say_list.append(rail.name)
    for ut in current_player.utlist:
        say_list.append(ut.name)
    return statement("say prop list",combine_say_it(say_list))


def stop_intent(event, context):

    net_worth = 0
    max_net_worth = 0
    player_worth = 0
    say_it = []
    for player_net_worth in board.playerlist:
        for color in player_net_worth.proplist:
            for prop in color:
                net_worth += prop.cost
        for rail in player_net_worth.raillist:
            net_worth += rail.cost
        for ut in player_net_worth.utlist:
            net_worth += ut.cost
        net_worth += player_net_worth.money
        if(net_worth >= max_net_worth):
            max_net_worth = net_worth
            player_worth = player_net_worth.number
        net_worth = 0

    say_it.append(format_statement(random_statement(win),player_worth))
    say_it.append(random_statement(finish))

    return statement_stop("finish", combine_say_it(say_it))
