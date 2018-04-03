

class Case:
    Input = ""
    Rules = [Rule(["Default"])]


class Rule:
 
    ActionList = ["Default"]
    def __init__(self, Strings):
        self.ActionList = Strings
    
class Word:
    WordString = ""
    WordSynonyms = [""]


# def ReadStructFile(Name):
