class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None: #adding items to the queue.
    new = Node(data)
    if not self.last is None:
      self.last.next = new
    if self.head is None:
      self.head = new
    self.last = new
    
  def dequeue(self) -> None: #removing items from the queue
    if self.head == None:
      pass
    else:
      self.head = self.head.next
  
  def status(self) -> None:  #displaying status of the queue
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
