# s = {1,2,3}

# print(s)
# s.add(33)
# s.add(353)
# print(s)

# my_list = [1, 2, 2, 3, 3, 4]
# unique = list(set(my_list))
# print(unique)

# s = {10, 20, 30}
# # print(s[0])  
# # ✅ Hashable types (immutable): int, str, tuple, float
# s = {1, 'hello', (1, 2), 3.14}

# ❌ Unhashable types (mutable): list, dict, set
#s = {[1, 2]}   # TypeError: unhashable type: 'list'

# print(s)

# print(hash(42)) 

# s = set({})
# print(type(s))

# s = {1, 2, 3}
# # s.add(4)   
# # s.update([5, 6, 6])
# # s.remove(32)  
# # s.discard(99) 
# # popped = s.pop()
# # s.clear()  
# print(s)

A = {1, 2, 3}
B = {3, 4, 5}

union_set = A.union(B)

union_set = A | B

union_set = A & B
print(union_set)