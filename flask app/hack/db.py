# from app import db, create_db
# from dump import mainstreet, dawntown, superkicks, crepdog
# from hack.models import Sneaker, Company, Size, Price
import sqlite3
# from functools import reduce

conn = sqlite3.connect('hack/sneaker_db.sqlite')
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
    
cur.execute("SELECT * FROM sneaker \
               GROUP BY name \
               HAVING COUNT(*) > 1;")
 
# fetch duplicate rows and display them
print('Duplicate Rows:')              
for i in cur.fetchall():
   print(i)
# terminate connection

    