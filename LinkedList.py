class Node: ## Create a new node
  def __init__(self,value):
    self.value = value  ##Value of the node
    self.next = None    ## Points to next node in the linkedlist


class LinkedList:
  def __init__(self,value):
    new_node = Node(value)  ##Assign new_node with value 
    self.head = new_node    ## head points to new_node
    self.tail = new_node    ## tail points to new_node
    self.length = 1  ## length

  def print_list(self): ## Printing the list
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

  def empty_list(self):
    self.head = None
    self.tail = None
    self.length = 0

    
    

  def append(self,value):  ##Insert node at end
        new_node = Node(value)
        if self.length == 0:
          self.head = new_node
          self.tail = new_node
        else:
          self.tail.next = new_node
          self.tail = new_node
        self.length += 1

        

  def append_at_beginning(self,value): ##Insert node at beginning
    new_node = Node(value)
    current_node = self.head
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.head = new_node
      new_node.next = current_node
      self.length += 1


  def insertAtGivenPosition(self,pos,value):   ##Insert node in middle by position
    if pos > self.length or pos < 0:
      return None
    else:
      if pos == 0:
        self.append_at_beginning(value)
      else:
        if pos == self.length:
          self.append(value)
        else:
          new_node = Node(value)
          current_node = self.head
          prev_node = self.head
          count = 1
          while current_node.next != None:
            if count == pos:
              new_node.next = current_node
              prev_node.next = new_node
            count += 1
            prev_node = current_node
            current_node = current_node.next  




    
      


  def pop(self):  ##Remove node at end
    if self.length == 0:
      self.head = None
      self.tail = None
      self.length = 0
      return 0
    else:
      current_node = self.head
      prev_node = self.head
      while current_node.next != None:
        prev_node = current_node
        current_node = current_node.next
      prev_node.next = None
      self.length -= 1 

  def pre_pop(self):    ##remove node from beginning
    current_node = self.head
    next_node = current_node.next
    self.head = next_node
    current_node.next = None
    self.length -= 1

  def get(self, index):  ##get the element
    current_node = self.head
    count = 0
    if self.length == 0 or index >= self.length:
      return None
    else:
      while(current_node.next is not None):
        if count == index:
          return current_node.value
        count += 1
        current_node = current_node.next
      
      

      
           
        



my_linked_list = LinkedList(10) ##Created a linkedList
# print(my_linked_list.head.value)## printing the value of the linkedList




my_linked_list.append(3)
my_linked_list.append(6)
my_linked_list.append(8)

my_linked_list.print_list()

print("The node at 2: ",my_linked_list.get(2))

# my_linked_list.print_list()

# print("Length of the linkedList", my_linked_list.length)

# my_linked_list.pop()


# print("Length of the linkedList", my_linked_list.length)

# my_linked_list.append_at_beginning(5)

# my_linked_list.print_list()

# print("Length of the linkedList", my_linked_list.length)

# my_linked_list.pre_pop()

# my_linked_list.insertAtGivenPosition(2,9)

# my_linked_list.print_list()
