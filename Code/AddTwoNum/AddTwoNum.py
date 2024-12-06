import sys
        
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# some cases to consider
# if there is value at n th index for l1 or l2, add the value to the sum
# if there is carry over, add 1 to the sum
# if the resulting sum is over 10, add 1 to the carry over and get the remainder of sum after dividing by 10

# going to have to create a whole method to immitate linked list

def arrayToList(arr):
    headNode = ListNode(arr[0])
    currentNode = headNode
    for item in arr[1:]:
        currentNode.next = ListNode(item)
        currentNode = currentNode.next
    return headNode
    
def listToArray(node: ListNode) -> list[int]:
    arr = []
    while node != None:
        arr.append(node.val)
        node = node.next
    return arr
    
def prepareAdds(l1,l2) -> list[int]:
    retObject: ListNode = addTwoNumbers(arrayToList(l1), arrayToList(l2), 0)
    return listToArray(retObject)
    

# enter code here
def addTwoNumbers(l1: ListNode, l2: ListNode, carryover) -> ListNode:
    tempNode = ListNode(0)
    sum = 0
    #base case
    if l1 == None and l2 == None and carryover == 0:
        return None
    if l1 != None:
        sum += l1.val
    if l2 != None:
        sum += l2.val
    sum += carryover
    
    tempNode.val = sum % 10
    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next
    tempNode.next = addTwoNumbers(l1, l2, sum//10)
    
    return tempNode



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
    print(prepareAdds(args[0], args[1]))
     
if __name__ == "__main__":
    main()