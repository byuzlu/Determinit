import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()


cur.execute('''SELECT * FROM CriterionList where crName = ?''',("Eş Seçimi",))
criterion = cur.fetchall()
trait_names=[]
for i in criterion:
    trait_names.append(i)
trait_num = -1
for i in trait_names[0][1:7]:
    trait_num+=1
    if i is None:
        break
print(trait_names[0][1:7])