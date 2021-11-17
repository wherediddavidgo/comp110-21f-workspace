listylist: list[int] = [4, 7, 21, 8, 0, 321, 45, 1231, 4, 4, 5, 6, 2, 4, 3]

other_listylist: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

print(len(listylist))
print(len(other_listylist))
print(listylist.index(4))

from data_utils import create_filter
from data_utils import filtered
from data_utils import head

filter_list: list[int] = create_filter(listylist, 4)
# print(filter_list)
print(filtered(other_listylist, filter_list))