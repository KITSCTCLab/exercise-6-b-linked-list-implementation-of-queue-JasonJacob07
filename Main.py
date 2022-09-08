class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.last = None

#adding items to the queue.
  def enqueue(self, data) -> None:
    if not self.last is None:
      self.last.next = Node(data)
    if self.head is None:
      self.head = Node(data)
    self.last = Node(data)
    
#removing items from the queue
  def dequeue(self) -> None: 
    if self.head == None:
      pass
    else:
      self.head = self.head.next
    
#displaying status of the queue
  def status(self) -> None:
    while self.head != None:
     print(self.head.data, "=>", sep = "", end = "")
     self.head = self.head.next
    print("None")
    
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
