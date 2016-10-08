import sys

def print_arguments(arglist = [], *args):
    length = len(arglist)
    text=""
    for i in range( 1, length ):
        text = text + arglist[i] + " "
    print("Hello", text, "!")

def main():
    if len(sys.argv) > 1:
        print_arguments(sys.argv)
    else:
        print("Hello World !")
      

if __name__ == "__main__":
    main()
