#Write a Python program to remove the nth index character from a nonempty string
def remove(a, n):
      first = a[:n] 
      last = a[n+1:]
      return first + last
print(remove('victor', 0))