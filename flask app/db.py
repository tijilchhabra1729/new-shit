from app import db, create_db
from dump import mainstreet, dawntown, superkicks, crepdog
from hack.models import Sneaker, Size
import sqlite3
from functools import reduce

conn = sqlite3.connect('sneaker_db.sqlite')
cur = conn.cursor()    
# cur.execute('SELECT name FROM sneaker')
# all_sneakers = list(dict.fromkeys(cur.fetchall()))

def convert_tuple(t):
    s = ''
    for i in t:
        s = s+i
    return s

# # for i in range(len(all_sneakers)):
# #     x = convert_tuple(all_sneakers[i])
# #     y = convert_tuple(all_sneakers[i+1])
# #     if x.find(y) != -1 or y.find(x) != -1:
# #         print('aaa')

# # for i in range(len(all_sneakers)):
# #     for j in range(i + 1, len(all_sneakers)):
# #         if convert_tuple(all_sneakers[j]).find(convert_tuple(all_sneakers[i])) != -1 or convert_tuple(all_sneakers[i]).find(convert_tuple(all_sneakers[j])) != -1:
# #             print(convert_tuple(all_sneakers[j]))
# #             print(convert_tuple(all_sneakers[i]) + '\n')


# for i in range(len(all_sneakers)):
#         for j in range(i + 1, len(all_sneakers)):
#             for k in range(j+1, len(all_sneakers)):
#                 if convert_tuple(all_sneakers[j]).find(convert_tuple(all_sneakers[i])) != -1 or convert_tuple(all_sneakers[i]).find(convert_tuple(all_sneakers[j])) != -1:
#                     print(convert_tuple(all_sneakers[j]))
#                     print(convert_tuple(all_sneakers
            
        
# # reduce(all_sneakers)
    
cur.execute('''SELECT * FROM sneaker WHERE name LIKE "%chicago lost & found%"''')
 
# fetch duplicate rows and display them
alike_sneakers = []
# query = 'chicago lost and found'
# cur.execute('SELECT * FROM sneaker')
# snkrs = cur.fetchall()
# for i in range(len(snkrs)):
#     for j in range(i+1, len(snkrs)):
#         print(snkrs[i][1], snkrs[j][1])

fetched = cur.fetchall()
for i in fetched:
   alike_sneakers.append(i)

print(alike_sneakers)
print(len(alike_sneakers))
# cur.executemany("DELETE FROM sneaker WHERE name = '?'",)


    