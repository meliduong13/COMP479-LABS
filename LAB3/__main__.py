import glob
import os
from pathlib import Path

from LinkedList import *
from Node import *

id_counter = 0
root_dir = 'C:/Users/melid/shakespeare.mit.edu'

inverted_index = {'Brutus': LinkedList(), 'Caesar': LinkedList(), 'Calpurnia': LinkedList()}

for fullpath in glob.iglob(root_dir + '**/**', recursive=True):
    if os.path.isfile(fullpath):
        filename = Path(fullpath).name
        if 'index.html' not in filename and 'full.html' not in filename and filename.endswith('.html'):
            with open(fullpath, 'r') as file:
                read = file.read()
                for key in inverted_index:
                    if key in read:
                        inverted_index[key].add(Node(filename, id_counter))
                id_counter += 1

# inverted_index['Brutus'].output_list()
# print(inverted_index['Brutus'].list_length())
# print('\n')
# inverted_index['Caesar'].output_list()
# print('\n')
# inverted_index['Calpurnia'].output_list()
# print('\n')

# while current_node is not None:
#     print(current_node.id)

# jump to the linked node
#  current_node = current_node.next


# def list_intersection(list1, list2):
#     current_node_list1= None;
#     current_node_list2= None;
#     if type(list1) is LinkedList and type(list2 is LinkedList):
#         current_node_list1 = list1.head
#         current_node_list2 = list1.head
#         if list1.list_length() is 0 or list2.list_length() is 0:
#             return LinkedList()
#         elif list1.list_length() is not 0 and list2.list_length() is not 0:
#             if current_node_list1.

# inverted_index['Brutus'].intersect_with_another_list(inverted_index['Caesar']).output_list()
inverted_index['Brutus'].union_with_another_list(inverted_index['Caesar']).output_list()

#
#print(inverted_index['Calpurnia'].union_with_another_list(inverted_index['Brutus']).list_length())
# print('abc')

#
# randomList = LinkedList()
# randomList.add(Node('filename1', 1))
# randomList.add(Node('filename2', 2))
# randomList.add(Node('filename3', 3))
#
# randomList2 = LinkedList()
# randomList2.add(Node('filename1', 1))
# randomList2.add(Node('filename3', 8))
# randomList2.add(Node('filename3', 9))
# randomList2.add(Node('filename3', 11))
#
# res = LinkedList()
# res = randomList.union_with_another_list(randomList2)
# res.output_list()
