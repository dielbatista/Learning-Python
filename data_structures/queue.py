"""A queue is a useful data structure in programming. it is similar to 
the ticket queue outside a cinema hal, where the first person entering
queue is the first person who gets the ticket.

Queue follows the FI-FO rule

!Basic operations of Queue

Enqueue: Add an element to the end of the queue
Dequeue: remove and element from the front of the queue
isEmpty: check if the queue is empty
isFull: Check if the queue is full
Peek: Get the value fo the front of the queue without removing it."""

    #-1   0   1    2    3    4  
    #--------------------------------
    #     1   
    #--------------------------------
    # ENQUEUE FIRST ELEMENT 
    
    
    
    #-1   0   1    2    3    4  
    #--------------------------------
    #                        5
    #--------------------------------
    # DEQUEUE LAST ELEMENT
    
    
    
     #-1   0   1    2    3    4  
    #--------------------------------
    #                        
    #--------------------------------
    # EMPTY QUEUE
    
    
    
    
class Queue():
    
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1
    #Insert an element into the queue
    def enqueue(self, data):
        
        if(self.tail == self.k -1):
            print("The queue is full \n")

        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data
            
        
            
            
    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty \n")
            
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp
        
        
        
        
    def printQueue(self):
        if(self.head == -1):
            print("No element in the queue")
        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

obj = Queue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printQueue()

obj.dequeue()
print("After Removing an element from the queue")
obj.printQueue()