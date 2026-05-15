from enum import Enum, auto
from tree import *
import re

DT_REGEX_SPLIT = "(\n| |=|<|>|@|;|{|})"

class dt_Token(Enum):
    DT_NODE_NAME = auto()
    DT_NODE_LABEL = auto()
    DT_NODE_ADDRESS = auto()
    DT_PROPERTY_KEYWORD = auto()
    DT_PROPERTY_NAME = auto()
    DT_PROPERTY_VALUE = auto()
    DT_SCOPE_BOUNDARY = auto()
    DT_LINE_BOUNDARY = auto()

class string_line:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.tokens_ptr = 0

    def munch(self) -> (str | None):
        explict_char = None
        if len(self.tokens) > self.tokens_ptr:
            explict_char = self.tokens[self.tokens_ptr]
            self.tokens_ptr += 1
        return explict_char
    
    def push_back(self):
        pass


def lexer(lines: list[str]):
    # Remove whitespace
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    current_line = lines.pop(5)
    for token in current_line:
        print(token, 
            #   end=""
            )
            # match token:
                