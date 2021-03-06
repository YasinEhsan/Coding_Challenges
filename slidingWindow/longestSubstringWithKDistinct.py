
# may 30 20
def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
  # init start vars
  windowStart = 0
  maxLen = 0
  charFreq = {}

  for windowEnd in range(len(str)):
    # get latest var and add to dict
    rightChar = str[windowEnd]
    if rightChar not in charFreq:
      charFreq[rightChar] = 0
    charFreq[rightChar] +=1

    # shrink window if substring has more than k unique chars
    while len(charFreq) > k:
      leftChar = str[windowStart]
      charFreq[leftChar] -=1
      if charFreq[leftChar] == 0:
        del charFreq[leftChar]
      windowStart +=1

    # save max len
    maxLen = max(maxLen, windowEnd - windowStart +1)

  return maxLen

# may 26 20
def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here

  windowStart, maxLen, d = 0,0,{}

  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1

    while len(d) > k:
      leftChar = str[windowStart]
      d[leftChar]-=1
      if d[leftChar] == 0:
        del d[leftChar]
      windowStart +=1
    maxLen = max(maxLen, windowEnd - windowStart +1)
  return maxLen

# time O(n+n) = n | space 0


# 5.21
def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
  windowStart, maxLen, d = 0,0, {}

  for windowEnd in range(len(str)):
    rightChar = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1

    while len(d) > k:
      leftChar = str[windowStart]
      d[leftChar] -=1

      if d[leftChar] == 0:
        del d[leftChar]
      windowStart +=1
    maxLen = max(maxLen, windowEnd - windowStart +1)
  return maxLen



# 5.20 forgot to add max() in maxLen -- returned tuple
def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
  windowStart,  maxLen, d = 0,0, {}

  for windowEnd in range(len(str)):
    rightChar  = str[windowEnd]
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] +=1

    while len(d) > k:
      leftChar = str[windowStart]
      d[leftChar] -=1
      if  d[leftChar] == 0:
        del d[leftChar]
      windowStart +=1

    maxLen = max(maxLen, windowEnd - windowStart + 1)
  return maxLen

# 5.10.20
def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here

  leftChar, maxLen, d = 0,0,{}

  for i, rightChar in list(enumerate(str)):
    if rightChar not in d:
      d[rightChar] = 0
    d[rightChar] += 1

    while len(d) > k:
      d[str[leftChar]] -=1

      if d[str[leftChar]] == 0:
        del d[str[leftChar]]
      leftChar +=1
    maxLen = max(maxLen, i - leftChar + 1 )

  return maxLen


def longest_substring_with_k_distinct(str, k):
  # TODO: Write your code here
    '''
    - have startIndex, currLen, maxLen, d
    '''
    startIndex, currLen, maxLen, d = 0,0,0,{}

    for endIndex in range(len(str)):
        if str[endIndex] not in d:
            d[str[endIndex]] = 0
        d[str[endIndex]] += 1
        currLen+=1

        while len(d) > k:
            d[str[startIndex]]-=1
            if d[str[startIndex]] == 0:
                del d[str[startIndex]]
            currLen -=1
            startIndex +=1

        maxLen = max(maxLen, currLen)
    return maxLen
longest_substring_with_k_distinct("araaci", 2)
