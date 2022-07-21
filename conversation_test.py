import unittest
from answer import Answer
from conversation import Conversation
from goodbye import Goodbye
from question import Question


class TestNext(unittest.TestCase):

    def test_goodbye(self):
        request = {
            "inputs": [
                {
                    "intent": "actions.intent.CANCEL",
                }
            ],
            "conversation": {}
        }
        conv = Conversation(request)
        next = conv.next()
        self.assertTrue(type(next) is Goodbye)

    def test_question(self):
        request = {
            "conversation": {
                "conversationId": "dummy",
                "type": "NEW"
            },
            "inputs": [
                {
                    "intent": "actions.intent.MAIN",
                    "rawInputs": [
                        {
                            "inputType": "VOICE",
                            "query": "Talk to runtimes math"
                        }
                    ]
                }
            ]
        }
        conv = Conversation(request)
        next = conv.next()
        self.assertTrue(type(next) is Question)

    def test_correct_answer(self):
        request = {
            "conversation": {
                "conversationId": "dumy",
                "conversationToken": "{\"x\": 3, \"y\": 3, \"ans\": 6}",
                "type": "ACTIVE"
            },
            "inputs": [
                {
                    "arguments": [
                        {
                            "name": "text",
                            "rawText": "6",
                            "textValue": "6"
                        }
                    ],
                    "intent": "actions.intent.TEXT",
                    "rawInputs": [
                        {
                            "inputType": "VOICE",
                            "query": "6"
                        }
                    ]
                }
            ]
        }
        conv = Conversation(request)
        answer = conv.next()
        self.assertTrue(type(answer) is Answer)
        self.assertTrue(answer.get_json()["expectedInputs"][0]["inputPrompt"]["richInitialPrompt"]["items"][0]["simpleResponse"]["displayText"].
                        startswith("That is correct!")
                        )

    def test_complex_correct_answer(self):
        request = {
            "conversation": {
                "conversationId": "dumy",
                "conversationToken": "{\"x\": 3, \"y\": 3, \"ans\": 6}",
                "type": "ACTIVE"
            },
            "inputs": [
                {
                    "arguments": [
                        {
                            "name": "text",
                            "rawText": "3 + 3 is 6",
                            "textValue": "3 + 3 is 6"
                        }
                    ],
                    "intent": "actions.intent.TEXT",
                    "rawInputs": [
                        {
                            "inputType": "VOICE",
                            "query": "3 + 3 is 6"
                        }
                    ]
                }
            ]
        }
        conv = Conversation(request)
        answer = conv.next()
        self.assertTrue(type(answer) is Answer)
        self.assertTrue(answer.get_json()["expectedInputs"][0]["inputPrompt"]["richInitialPrompt"]["items"][0]["simpleResponse"]["displayText"].
                        startswith("That is correct!")
                        )

    def test_invalid_answer(self):
        request = {
            "conversation": {
                "conversationId": "dumy",
                "conversationToken": "{\"x\": 3, \"y\": 3, \"ans\": 6}",
                "type": "ACTIVE"
            },
            "inputs": [
                {
                    "arguments": [
                        {
                            "name": "text",
                            "rawText": "banana",
                            "textValue": "banana"
                        }
                    ],
                    "intent": "actions.intent.TEXT",
                    "rawInputs": [
                        {
                            "inputType": "VOICE",
                            "query": "banana"
                        }
                    ]
                }
            ]
        }
        conv = Conversation(request)
        answer = conv.next()
        self.assertTrue(type(answer) is Answer)
        self.assertTrue(answer.get_json()["expectedInputs"][0]["inputPrompt"]["richInitialPrompt"]["items"][0]["simpleResponse"]["displayText"].
                        startswith("Sorry I did not understand that.")
                        )

    def test_incorrect_answer(self):
        request = {
            "conversation": {
                "conversationId": "dumy",
                "conversationToken": "{\"x\": 3, \"y\": 2, \"ans\": 5}",
                "type": "ACTIVE"
            },
            "inputs": [
                {
                    "arguments": [
                        {
                            "name": "text",
                            "rawText": "6",
                            "textValue": "6"
                        }
                    ],
                    "intent": "actions.intent.TEXT",
                    "rawInputs": [
                        {
                            "inputType": "VOICE",
                            "query": "6"
                        }
                    ]
                }
            ]
        }
        conv = Conversation(request)
        answer = conv.next()
        self.assertTrue(type(answer) is Answer)
        self.assertTrue(answer.get_json()["expectedInputs"][0]["inputPrompt"]["richInitialPrompt"]["items"][0]["simpleResponse"]["displayText"].
                        startswith("Sorry that is incorrect. What is 3 + 2?")
                        )


if __name__ == '__main__':
    unittest.main()
