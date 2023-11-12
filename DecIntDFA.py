class DecIntDFA:
    states = {"q1", "q2", "q3", "q4", "q5", "q6"} # Set of States of decimal integer DFA
    acceptstates = {"q2", "q3"} # Set of accept States of decimal integer DFA
    start_state = "q1" # initial state
    alphabet = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"}
    digit = alphabet - {"_"}
    nonZeroDigit = digit - {"0"}
    transition = {}

    def __init__(self):
        self.transition = { # transition function for all states
            "q1": lambda c: "q2" if c in self.nonZeroDigit else("q3" if c=="0" else "q6"), 
            "q2": lambda c: "q2" if c in self.digit else("q4" if c=="_" else "q6"),
            "q3": lambda c: "q3" if c == "0" else ("q5" if c=="_" else "q6"),
            "q4": lambda c: "q2" if c in self.digit else "q6",
            "q5": lambda c: "q3" if c == "0" else "q6",
            "q6": lambda c: "q6"
        }
    
    def accepts(self, str):
        state = self.start_state # set start state
        for char in str: # Step through characters in input
            state = self.transition[state](char) # apply lambda based on state
        if state in self.acceptstates: 
            return True # accept if final state is in accept states
        else:
            return False
        