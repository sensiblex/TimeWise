from activity import *
from manage import *
from activities import *

a = Activity('some', 'sport', 1)
a1 = Activity('some active', 'music', 2)
a2 = Activity('active', 'games', 4)

storage = Activities()

storage.add(a)
storage.add(a1)
storage.add(a2)

print(storage)
print('----------------------------------------------')
storage.remove(a)
print(storage)