import sys

# enter code here
def method(arg1, arg2) -> list[int]:
    return []



def main():
    args = []
    for arg in sys.argv[1:]:
        # detect integeter
        if arg[0] == '[' and arg[-1] == ']':
            args.append([int(x) for x in arg[1:len(arg)-1].split(',')]) 
        elif type(arg[0]) == int:
            print("int")
            args.append(int(arg))
        # detect string
        elif type(arg[0]) == str:
            args.append(arg)
        # detect array
        
    # call methods here
    print(method(args[0], args[1]))
     
if __name__ == "__main__":
    main()