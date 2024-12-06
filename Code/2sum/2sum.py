import sys
 
def twoSum(arg1: list[int], arg2: int) -> list[int]:
    # implement 2 sum, assume theres will be exactly one solution, don't same element twice
    
    # solved using hash, add each element to hash as key value pair
    # key will be the value of the element, value will be target - value
    # check if target - value is in the array (assume there's no duplicate, but also can't use same element twice)
    
    twoSumDict = {}
    # set up the dictinary with { number: index }
    # if we get a duplicate variable, that is fine since we would have last occurrence of the element saved and ideally the program would terminate before then
    for i in range(len(arg1)):
        twoSumDict[arg1[i]] = i
    for i in range(len(arg1)):
        diff = int(arg2) - arg1[i]
        if diff in twoSumDict and twoSumDict[diff] != i:
            return [i, twoSumDict[arg2 - arg1[i]]]
    return []





def firstPass(arg1: list[int], arg2: int) -> list[int]:
    # First attempt on doing 2sum, code is a bit hard to read because I did not think of the case when array has duplicate elements, so I had to do array slicing 
    twoSumDict = {}
    for i in range(len(arg1)):
        if arg1[i] not in twoSumDict:
            diff = int(arg2) - int(arg1[i])
            twoSumDict[arg1[i]] = diff
            if diff in arg1[i+1:]:
                return [i, arg1[i+1:].index(twoSumDict[arg1[i]])+i+1]
    return []



def main():
    args = []
    for arg in sys.argv[1:]:
        # detect integeter
        if arg[0] == '[' and arg[-1] == ']':
            args.append([int(x) for x in arg[1:len(arg)-1].split(',')]) 
        elif arg[0].isdigit():
            args.append(int(arg))
        # detect string
        elif type(arg[0]) == str:
            args.append(arg)
        # detect array
        
    # call twoSum
    print(twoSum(args[0], args[1]))
     
if __name__ == "__main__":
    main()