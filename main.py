from DecIntDFA import DecIntDFA
from OctIntDFA import OctIntDFA
from HexIntDFA import HexIntDFA

def main():
    str = input(">>")
    decDFA = DecIntDFA()
    octDFA = OctIntDFA()
    hexDFA = HexIntDFA()   
    decAccepts = decDFA.accepts(str)
    octAccepts = octDFA.accepts(str)
    hexAccepts = hexDFA.accepts(str)
    if(decAccepts):
        print("Decimal Integer Accepted")
    elif(octAccepts):
        print("Octal Integer Accepted")
    elif(hexAccepts):
        print("Hexadecimal Integer Accepted")
    else:
        print("Rejected.")
    

if __name__ == "__main__":
    main()