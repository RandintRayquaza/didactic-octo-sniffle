# If a class or an object has an __iter__ method then it is called an iterable.


# ls = [1,2,3,4,5]
# print(dir(ls))
# dir(range(10))


# Iterators => if a class and object has both __iter__ and __next__ methods then it is called an iterator.

# Difference between iterables and iterators => iterables are those which have an __iter__ method and iterators are those which have both __iter__ and __next__ methods.



a = [1, 23, 4, 5]
b = [43, 5, 2, 3, 4, 5]
print(list(zip(a, b)))

for i in zip(a, b):
    print(i)


# next() 

print(next(zip(a, b)))
print(next(zip(a, b)))
print(next(zip(a, b)))




# Difference between iterables and iterators

# Iterables => it is an object which has an __iter__ method and it can be converted into an iterator using the iter() function.
# It can be iterated n number of times.
# We can access the elements n number of times.
# For example, multiple value data structures like list, tuple, set, dict, string etc. are iterables.
# When you compare them, it is less memory efficient than iterators because it stores all the elements in memory at a time.
# Converting iterables to iterators => we can convert iterables to iterators using the iter() function.



# Iterators => it is an object which has both __iter__ and __next__ methods and it can be iterated only once.
# Can access elements only once at a time.
# For example, zip, map, filter, range etc. are iterators.

# When we compare them, it is more memory efficient than iterables because it stores only one element in memory at a time and it generates the next element on the fly when we call next() function.







t = (12, 23, 4, 3,)

print(dir(t))
