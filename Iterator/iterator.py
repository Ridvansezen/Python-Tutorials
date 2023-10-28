""""Python da Iterator kavramı."""

my_list = [2,4,5,8,1,21,]

my_iterator = iter(my_list)

for i in my_list:
    try:
        item = next(my_iterator)
        print(item)

    except:
        raise StopIteration