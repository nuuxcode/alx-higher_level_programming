#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
print("------------")
print("-- (1,2), (1,2) : {}".format(add_tuple((1,2), (1,2))))
print("-- (1,), (1,2) : {}".format(add_tuple((1,), (1,2))))
print("-- (), (1,2) : {}".format(add_tuple((), (1,2))))
print("-- (), () : {}".format(add_tuple((), ())))
print("-- (1,), (1,) : {}".format(add_tuple((1,), (1,))))
print("-- (1,2,3), (1,2,3) : {}".format(add_tuple((1,2,3), (1,2,3))))

'''
check len
    0 add 0,0
    1 add 0
    2 good

(1,2)
(1,2)
    (2,4)
(1,)
(1,2)
    (2,2)
()
(1,2)
    (1,2)
()
()
    (0,0)
(1,)
(1,)
    (2,0)
(1,2,3)
(1,2,3)
    (2,4)
'''
