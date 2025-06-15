from activity import *
from manage import *

a = Activity('some active', 'sport', 2)
print(a)

ManageActivity.rename(a, '123')

print(a)