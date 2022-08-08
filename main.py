from pymongo import MongoClient
Client=MongoClient("mongodb://localhost:27017")
db=Client['PFSD']
info=db.PFSD
STUDENT1={'Reg No':'2100031019','Name':'M.siva sankar'}
STUDENT2=[
    {'Reg No':'2100031017','Name':'varun'},
{'Reg No':'21000310137','Name':'varn'},
{'Reg No':'2100031014','Name':'varu'},
{'Reg No':'2100031087','Name':'varn'},
{'Reg No':'2100031016','Name':'varma'}
]
studentData=db.STUDENT
studentData.insert_one(STUDENT1)
studentData.insert_many(STUDENT2)
print(studentData.find_one())
tofind1=STUDENT2
for x in tofind1:
    print(studentData.find_one(tofind1))

#Delete
todelete2={'Reg No':'2100031017','Name':'varun'}
studentData.delete_many(todelete2)

