from monopoly_backend import *
from lambda_stuff import *

board = None
current_player = None
number = 0


play_game=1
current_question = 0
setboard_confirm = 0



def lambda_handler(event, context):

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)
    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)


def on_launch(event, content):
    return statement("Start,Number of player",combine_statement(random_statement(ret_launch),random_statement(ask_no_players)))


def intent_router(event, context):
    intent = event['request']['intent']['name']

    if intent == "numberOfPlayers":
        return numberOfPlayers_intent(event, context)
    if intent == "diceroll":
        return diceroll_intent(event, context)


def numberOfPlayers_intent(event, context):
    dialog_state = event['request']['dialogState']

    global number

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        slots = event['request']['intent']['slots']
        number = int(slots['number']['value'])

        if number in (2, 3, 4):
            global setboard_confirm
            setboard_confirm=1
            global board
            board = Board(number)
            return statement("Confirm,Set Board",combine_statement(random_statement(confirmation),
                                                             format_statement(random_statement(set_board), number), "Its player one's turn. "))
        #prompt user to roll dice

        elif number == 1 :
            return statement("Alone,Ask Again",combine_statement(random_statement(alone),random_statement(ask_again)))

        elif number > 4:
            return statement("Too many, Ask Again",combine_statement(random_statement(too_many),random_statement(ask_again)))

        else:
            return statement("Not valid,Ask Again",combine_statement(random_statement(not_valid),random_statement(ask_again)))

    else:
        return statement("Number of players", "I need a head count")



def diceroll_intent(event, context):
    rolledNumber1 = random.randint(1, 6)
    rolledNumber2 = random.randint(1, 6)




def play_board(d1,d2):

    global current_player
    global play_game
    while play_game == 1:
        for player in board.playerlist:
            current_player=player.number


