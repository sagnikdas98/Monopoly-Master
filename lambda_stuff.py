from return_utterance import *


def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet)

def statement_stop(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
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


def help_intent():

    ret_it = []
    ret_it.append(random_statement(help_utter_1))
    ret_it.append(random_statement(help_utter_2))
    ret_it.append(random_statement(help_utter_3))
    ret_it.append(random_statement(help_utter_4))
    ret_it.append(random_statement(help_utter_5))
    return statement("help", combine_say_it(ret_it))



def cancel_intent():
    pass

