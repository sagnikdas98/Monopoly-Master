from data import *

number = 0


def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)


def on_launch(event, content):
    return statement("Launch", "Welcome to Monopoly Master! How many players do we have today?")


def intent_router(event, context):
    intent = event['request']['intent']['name']
    if intent == "numberOfPlayers":
        return numberOfPlayers_intent(event, context)
    if intent == "returnNumber":
        return statement("Number", "%d" % number)
    if intent == "startGame":
        return startGame_intent(event, context)


def startGame_intent(event, context):
    rolledNumber = random.randint(1, 6)


def numberOfPlayers_intent(event, context):
    slots = event['request']['intent']['slots']
    global number
    number = int(slots['number']['value'])
    return statement("Confirmation", "Okay, got it.")


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




