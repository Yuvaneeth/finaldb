import pyodbc

print("making connection")
cnxn = pyodbc.connect('DRIVER={MongoDB ODBC Driver};Server=18.218.0.221;Port=3307;User=neel;Password=mongo123', autocommit=True)
print("connection made")
with cnxn.cursor() as cur:
    cur.execute("use ADNI")
    cur.execute("select * from adnimerge limit 5")
    print(cur.fetchall())


    #conf yaml file IP???
    #mongo?ec2? hostname


    
  
