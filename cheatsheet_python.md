# Python notes

## General
- // is for floor
- return 'T'rue
- multi line comment '''

## Loops
- for i in reversed(range(5))
- for i in range(start,end): COLON VERY IMPORTANT

## Arrays / list
- array [-1] returns the element of last position in array
- arr = [0] * 5 creats array of size five with contents 0
- arr = [0 for x in range(10)] creates [0,0,0,0...]
- arr.sort() VS arr.sort(reverse=True)
- list1.sort(key=sortSecond)  for tuple array sort (better in swift)
- pop() last element rm
- pop(x) element at pos x rm and returns removed ele
- remove(x) first occurence of val x rm
- del arr[x] removes the item (i.e. hash charCount[s] = 0)
- list.reverse() modifies og list...list[::-1] creates new copy reversed

## Deque
- a list or array can work as queue using Pop(0)
- however, queue.popleft() is O(1) while list.pop(0) O(N)
- popleft() leftmost element...pop() rightmost ele as in Stack
- q.appendLeft(item) adds to first position like list.insert(0, item)

## dict
- TBD one line update or add

```python
# classic space and time trade off examples

# if was result.insert(0, tempArr) algo complexity wud be higher bc opration O(n) cost
  result.append(tempArr)

  # I can do return [::-1] O(N) space cost new lsit created
  result.reverse()
```
