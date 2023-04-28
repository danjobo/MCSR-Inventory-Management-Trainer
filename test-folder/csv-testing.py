# https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/


import csv
  
# op = open("AllDetails.csv", "r")
# dt = csv.DictReader(op)
# print(dt)
# up_dt = []
# for r in dt:
#     print(r)
#     row = {'Sno': r['Sno'],
#            'Registration Number': r['Registration Number'],
#            'Name': r['Name'],
#            'RollNo': r['RollNo'],
#            'Status': 'P'}
#     up_dt.append(row)
# print(up_dt)
# op.close()


# op = open('test-csv.csv','r')
# dt = csv.DictReader(op)
# print(dt)
# up_dt = []
# for r in dt:
#     print(r)
# op.close()

csv_list_storage = []
op = open('assets/csv-files/test-inv.csv','r')

dt = csv.reader(op)
for row in dt:
    print(row)
    csv_list_storage.append(row)
print(dt)
print('\n\n\n')
print(csv_list_storage)
csv_list_storage[0][8] = 'white_bed'
op.close()


op = open('assets/csv-files/test-inv.csv','w', newline='')
dt = csv.writer(op)
dt.writerows(csv_list_storage)
op.close()


# op = open("AllDetails.csv", "w", newline='')
# headers = ['Sno', 'Registration Number', 'Name', 'RollNo', 'Status']
# data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
# data.writerow(dict((heads, heads) for heads in headers))
# data.writerows(up_dt)
# op.close()