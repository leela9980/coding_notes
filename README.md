# python notes
Python coding Interview quick tips

#### Declaration
 ```python
    #list size 10 and zeros
     my_list = [0]*10
    # Set
     my_set = set()
    # Dict
     my_dict = {}
   # find a value in list, set, dict
   if v in set:
 ```

#### FOR
```python
  # for loop with a list
  for v in list:
  #skip first value
  for v in list[1:]:
  # i is index
  for i in range(0, len(list)):
  #reverse
  for i in range(len(list)-1, -1, -1):
  #both index, value in the loop
  for i, v in enumerate(my_list):
  #dict
  my_dict = {'a': 1, 'b': 2, 'c': 3}
  for k,v in my_dict.items():
  # only keys
  for k in my_dict:
  #only values
  for v in my_dict.values():
  # iterate matrix r,c indexes
  for r in range(len(matrix)):
      for c in range(len(matrix[0])):
  #iterate matrix to get value
  for row in matrix:
    for element in row:
```
#### MIN,MAX,SUM
```python
   # min find min in a list or two values
      min(5,6)  or min([1,2,3,4,5])
   # max same as above
   # sum find sum of list of values
      sum([1,2,3,4,5])
```
#### DIVISION
```python
  print(10 / 3)  # Output: 3.3333
  print(10 // 3)  # Output: 3
  /  # true division
  // # floor division
```
#### STACK
```python
 # no stack in python so need to use list as a makeshift stack
 stack = []
 stack.append([1,2,3,4])
 stack.pop() # output: 4
 stack[-1] # output 3 , top value
```

#### QUEUE
```python
 queue = []
 queue.append([1,2,3,4])
 queue.pop(0) # output: 1
 queue[0] # output 2 , fist value
```
#### Dictionary (map)
 ```python
   # get a value no default value
   my_dict.get('blah') or my_dict['blah']
   # with a default value
   my_dict.get('blah', 'not found')
   #Get a list corresponding to a key in a dict or create a new one if not present
   my_dict.setdefault('blah', list()).add(2)
   #equivalent to
   my_dict['blah'] = my_dict.get('blah', [])
   my_dict['blah'].add(2)
 ```
#### Sort
```python
   my_list.sort()
   # Sort in descending
   my_list.sort(reverse=True)
   # Sort with custom comparator
   my_list.sort(key=lambda x: x[0])
```
  
#### HEAP
```python
Import heapq
heap = []
# min heap
heapq.heappush(heap, item)
heapq.heappop(heap)
heap[0] //top

# max heap (no max heap in python so we have to negate the value before inserting)
 heapq.heappush(heap, -item)
-heapq.heappop(heap)
-heap[0]
```
#### HELPER FUNC
```python
# Many coding problems need helper function especially in recurssive problems, it can be written like this
  def lowestCommonAncestor(...) 
        def findLCA(...)
            .....
            return findLCA(...)
        return findLCA(root)
```
