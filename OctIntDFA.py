class OctIntDFA:
    states = {"q1", "q2", "q3", "q4", "q5", "q6", "q7"} # Set of States of decimal integer DFA
    acceptstates = {"q4"} # Set of accept States of decimal integer DFA
    start_state = "q1" # initial state
    alphabet = {"0", "1", "2", "3", "4", "5", "6", "7", "_", "o", "O"} # alphabet for decimal integer
    octDigits = alphabet - {"o", "O", "_"}
    transition = {}

    def __init__(self):
        self.transition = { # transition function for all states
            "q1": lambda c: "q2" if c == "0" else "q7", 
            "q2": lambda c: "q3" if c == "o" or c =="O" else "q7",
            "q3": lambda c: "q4" if c in self.octDigits else ("q5" if c=="_" else "q7"),
            "q4": lambda c: "q4" if c in self.octDigits else ("q6" if c=="_" else "q7"),
            "q5": lambda c: "q4" if c in self.octDigits else "q7",
            "q6": lambda c: "q4" if c in self.octDigits else "q7",
            "q7": lambda c: "q7"
        }
    
    def accepts(self, str):
        state = self.start_state # set start state
        for char in str: # Step through characters in input
            state = self.transition[state](char) # apply lambda based on state
        if state in self.acceptstates: 
            return True # accept if final state is in accept states
        else:
            return False