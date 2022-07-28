# This algorithm helps us find the majority element in an array in O(n) time and O(1) space
# this is rare, as it doesn't involve using a hashmap
# A majority element is an element repeated more than n/2 times in an array of len N

# Intuition ->
# If we had some way of counting instances of the majority element as +1+1 and instances of any other element as -1−1,
# summing them would make it obvious that the majority element is indeed the majority element.

# Algorithm Essentially, what Boyer-Moore does is look for a suffix suf of nums where suf[0] is the majority
# element in that suffix. To do this, we maintain a count, which is incremented whenever we see an instance of our
# current candidate for majority element and decremented whenever we see anything else. Whenever count equals 0,
# we effectively forget about everything in nums up to the current index and consider the current number as the
# candidate for majority element.

# [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
# Here, the 7 at index 0 is selected to be the first candidate for majority element.
# count will eventually reach 0 after index 5 is processed, so the 5 at index 6 will be the next candidate.
# In this case, 7 is the true majority element, so by disregarding this prefix,
# we are ignoring an equal number of majority and minority elements,
# therefore, 7 will still be the majority element in the suffix formed by throwing away the first prefix.

# [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

# Now, the majority element is 5 (we changed the last run of the array from 7s to 5s),
# but our first candidate is still 7.
# In this case, our candidate is not the true majority element,
# but we still cannot discard more majority elements than minority elements
# (this would imply that count could reach -1 before we reassign candidate, which is obviously false).


# Algorithm
Arr = [2,2,1,1,1,2,2]
count = 1
key = Arr[0]
for i in range(1, len(Arr)):
    if count == 0: key = Arr[i]
    if Arr[i] == key: count += 1
    else: count -= 1
print(key)



