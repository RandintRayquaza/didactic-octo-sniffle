# A generator is a special type of iterator which produces values one at a time only when required and it is more memory efficient than iterators because it stores only one element in memory at a time and it generates the next element on the fly when we call next() function


## use case of generator memory efficient => when we have a large data set and we want to process it one at a time without loading the entire data set into memory at once


# useful for large data set => when we have a large data set and we want to process it one at a time without loading the entire data set into memory at once


# values are generated only on demand => when we call next() function it generates the next value on the fly when we call next() function



def demo_generator():
    yield 1
    yield 2
    yield 3

gen = demo_generator()
print(next(gen))
print(next(gen))
print(next(gen))



def demo():
    print('Hello world')
    return 1
    prinr('Good morning')