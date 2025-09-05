
from sqlalchemy import create_engine,text

print("horoku and me and ")

cp=20

 
engine = create_engine('mysql://root:@localhost/wesagn')
def tryy():
    global cp
    try:
        connection = engine.connect()
        cp=1
    except Exception as e:
        cp=0    

    

      
dk={
     'fname': "bbeteu",
        'sname': "rdaand",
        'pw': "02124",
        'address': 1004,
        'statuss': 3,
        'jop_id': 3
    }
quer="INSERT INTO employe (fname, sname, pw, address, statuss, jop_id) VALUES (:fname, :sname, :pw, :address, :statuss, :jop_id);"
quer="UPDATE employe SET statuss = :statuss WHERE id = :user_id"
quer="DELETE FROM employe WHERE id= :user_id"
quer="SELECT fname   FROM  emp WHERE id= 1  "
def pull(quer):
    
    with engine.connect() as conn:
        tryy()
        query = text(quer)
        result = conn.execute(query)
        return result
        
    
   
    
    
   
def insert_update_and_DELETE(quer,dk):#to insert valuse
    with engine.connect() as conn:
        tryy()
        query = text(quer)
        conn.execute(query, dk)
        conn.commit()
  






"""
  if(PAA["id"]=="0"):
      CM={"no petionent":""} 
    else:
     quer="SELECT p_id,	lab_stu   FROM work WHERE em_id= '" +str( ACC["id"] )+ "' "
     FM={"petionet":""}
     X2={}
     xf=1
     LT={}
     conj=pull(quer)
     for x in conj:
         quer="SELECT fname,	sname    FROM petionet WHERE id= '" + str(x[0]) + "' "
         con=pull(quer)
         Y=con.fetchone()
         x1=Y[0]+" "+Y[1]
         X4={x1:  x[1]}
         if(x[1]=="2"):
           X4={"Name":x1}
           LT.update(X4)
         if(x[1]=="3"):
            xf=0
            X2.update(X4)
     FM["petionet"]=X2
     if(xf==1):
       FM={"1":"2"}
     AC="/1/10/A"
"""


      
 
