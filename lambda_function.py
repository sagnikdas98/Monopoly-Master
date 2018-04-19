from monopoly_backend import *
from return_utterance import *

number = 0
current_player=0

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)


def on_launch(event, content):
    statement("Start",random_statement(ret_launch))
    statement("Number of players",random_statement(ask_no_players))
    return



def intent_router(event, context):
    intent = event['request']['intent']['name']


    if intent == "numberOfPlayers":
        return numberOfPlayers_intent(event, context)

    if intent == "diceroll":
        return diceroll_intent(event, context)




def diceroll_intent(event, context):
    rolledNumber1 = random.randint(1, 6)
    rolledNumber2 = random.randint(1, 6)






def numberOfPlayers_intent(event, context):
    dialog_state = event['request']['dialogState']

    global number

    if dialog_state in ("STARTED", "IN_PROGRESS"):
        return continue_dialog()

    elif dialog_state == "COMPLETED":
        slots = event['request']['intent']['slots']

        number = int(slots['number']['value'])

        if number in (2, 3, 4):
            statement("Confirmation", random_statement(confirmation))
            statement("Setting Board",random_statement(setting_board))
            return setboard()

        elif number == 1 :
            statement("Alone",random_statement(alone))
            statement("Ask again",random_statement(ask_again))
            return

        elif number > 4:
            statement("Too many", random_statement(too_many))
            statement("Ask again",random_statement(ask_again))
            return
        else:
            statement("not valid",random_statement(not_valid))
            statement("Ask again",random_statement(ask_again))
            return
    else:
        return statement("Number of players", "I need a head count")







def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet)


def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech


def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response


def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
    return card


def continue_dialog():
    message = {}
    message['shouldEndSession'] = False
    message['directives'] = [{'type': 'Dialog.Delegate'}]
    return build_response(message)

def setboard():
    board = Board(number)
    startgame = 1
    global current_player
    while startgame == 1:
        for player in board.playerlist:
            if len(board.playerlist) == 1:
                current_player =player.number
                statement("win", random_statement(win))
                return #TODO
            current_player=player.number
            statement("turn_player", random_statement(turn_player))










