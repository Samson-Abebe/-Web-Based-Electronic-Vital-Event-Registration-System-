from flask import Flask, request, render_template ,jsonify,Response
from maindb import pull,insert_update_and_DELETE
from datetime import datetime
ACC={"name":"0",
     "id":"0",
     "stu":"0",
     "jn":"0",
     "pw":"0",
      "ACCT":"0"} 
MU={}
mu1={"1"}
ID1=0
ID2=0
TR={"1":"2"}
K=0
jpc=0
TC=[]
FM={"1":"2"}
CM={"1":"2"}
BLU=0
def befr():
  global FM,MU,LT,CM,LG,TB1,TB2,BLU,TR,jpc,ID2
  BLU=0
 
  TR={"1":"2"}
 
  TB1=[0]
  TB2={}
  FM={"1":"2"}
  
  LT={"1":"2"}
  CM={"1":"2"}
  LG="0"
import datetime
def post_get():
 p=9   # Your code that may raise a "Method Not Allowed" error
 if request.method == 'POST':
            # Process GET request
            p=0
            print("SAMSON")
 elif request.method == 'GET':
            p=1  
 return p
def passw1():
  global FM,CM
  FM={
      "insert old pass word":"1",
      "insert new pass word":"1",
      "check pass word":"1"
      
    }
  CM={"Insert the form":" "}
def passw2():
  global CM
  sa = request.form
  print(sa)
  if(sa["insert old pass word"]==ACC["pw"]):
      if(sa["insert new pass word"]==sa["check pass word"]):
        quer="UPDATE emp SET pw = :pw WHERE id = :id"
        dk=[{'pw': sa["insert new pass word"], 'id':ACC["id"]}]
        insert_update_and_DELETE(quer,dk)
        ACC["pw"]= sa["insert new pass word"]
        CM={"Done!":" "}  
      else:
        CM={"The pass woed is not mach":" "}
  else:
      CM={"The pass word is not corect":" "}
def conca(co):
  sam=""
  for x in co:
    print("yadnch",x[0])
    if(x[0]=="ID"):  
      continue
    sam=sam+" "+x[0]
    sam=sam+","
  sam=sam[:-1]
  return sam
def conc(co):
  sam=""
  for x in co:
     if(x[0]=="ID"):  
         continue
     sam=sam+":"+x[0]
     sam=sam+","
  print("samcoc",sam)
  sam=sam[:-1]
  return sam 
  
def Regis(na):
  global FM,CM,TR,TC,jpc
  jp=post_get()
  FM={"resident cellphone":"1"}
  X=()
  if(jp==0):
    if(jpc==0):
      jpc=0
      
      sa = request.form
      quer="SELECT id, fname ,sname FROM emp WHERE  cellphone = '" +str(sa["resident cellphone"]) + "' AND jobid='4'"
      con=pull(quer)
      for x in con:
        print(x)
        X=x
      if len(X) == 0:
           CM={"no resident in this cellphone":" "}
         
      else:
       xp=X
      
       print("xo",xp,X)
       X=()
       quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(na) + "' AND TABLE_SCHEMA = 'wesagn'"      
       co=pull(quer)
       co=co.fetchall()
       kk=conca(co)
       quer="SELECT " +str(kk) + " FROM " +str(na) + " WHERE  userid = '" +str(xp[0]) + "'"
       con=pull(quer)
       for x in con:
        print(x)
        X=x
       if len(X) == 0:
             jpc=xp[0]
             quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(na) + "' AND TABLE_SCHEMA = 'wesagn'"
             CM={"add"+" "+na:" "}
             co=pull(quer)
             co=co.fetchall()
             print("coco",co)
             FM={}
             for x in co:
               if(x[0]=="actuale_birth_date"  or x[0]=="actuale_dath_date" or x[0]=="date_of_Divorcce" or x[0]=="date_of_Mirrage"):
                 FM[x[0]]="2"
               elif(x[0]=="ID" or x[0]=="userid" or x[0] =="datee"):
                     continue
               else:
                 FM[x[0]]="1"
       else:
          quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(na) + "' AND TABLE_SCHEMA = 'wesagn'"
          co=pull(quer)
          co=co.fetchall()
          print("coco",co)
          TR={}
          TC=[]
          T={}
          for x in co:
               if(x[0]=="datee"):
                 TR["Date"]="1"
               elif(x[0]=="ID" or x[0]=="userid" ):
                     continue
               else:
                 TR[x[0]]="1"
          CM={"Have it already":" "}
          C26=1
          print("feeee",X)
          x1=X
            
            
          for ct,cy in TR.items():
               if(ct=="ID" or ct=="userid" ):
                     C26=C26+1
                     continue
               else:
                 T[ct]=x1[C26]
                 C26=C26+1
          TC.append(T)
    else:
      quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(na) + "' AND TABLE_SCHEMA = 'wesagn'"      
      co=pull(quer)
      co=co.fetchall()
      kk=conca(co)
      print("kkcoma",kk)
      k1=conc(co)
      print("k1towdot",k1)
      
      sa = request.form
      print("nulllcar",sa)
      uu=sa
      u1=0
      for key, value in uu.items():
         if key == 'resident cellphone':
            cellphone_number = value
            u1=1
            
            break
      if (u1==1):
        jpc=0
        print("nu;llll")
      else:
       quer="INSERT INTO " +str(na) + " (" +str(kk) + ") VALUES (" +str(k1) + ");"
       tm={}
       for x in co:
              
               if(x[0]=="ID"):  
                     continue
               elif( x[0]=="userid"):
                 tm[x[0]]=jpc
               elif( x[0] =="datee"):
                 tm[x[0]]=datetime.datetime.now().date()
               else:
                 tm[x[0]]=sa[x[0]]
       print("tmm",tm)
       dk=[]
       dk.append(tm)
       jpc=0
       insert_update_and_DELETE(quer,dk)
       CM={"Done!":" "} 
      
def Regi(na):
   global CM
   quer="SELECT * FROM " +str(na) + " WHERE  userid = '" +str(ACC["id"]) + "' "
   con=pull(quer)
   X=()
   for x in con:
        print(x)
        X=x
   if len(X) == 0:
     CM={"you dont have such file":""}
    
     
   else:
     quer="SELECT * FROM requset WHERE  userid = '" +str(ACC["id"]) + "' AND requset_tayp = '" +str(na) + "'"
     con=pull(quer)
     X=()
     for x in con:
        print(x)
        X=x
     if len(X) == 0:
       quer="SELECT cret_empid FROM emp WHERE  id = '" +str(ACC["id"]) + "' "
       con=pull(quer)
       con=con.fetchone()
       CM={"Your request is submitted":""}
       quer="INSERT INTO requset (userid, requset_tayp, stu, kebleid,datee) VALUES (:fname, :sname, :pw, :address,:ddate);"
       dk=[{"fname":ACC["id"],"sname":na,"pw":"0","address":con[0], "ddate":datetime.datetime.now().date()}]
       insert_update_and_DELETE(quer,dk)
     else:
       CM={"you  have request":""}
def resiss(na) :
   global CM,TC,TR
   quer="SELECT * FROM " +str(na) + " WHERE  userid = '" +str(ACC["id"]) + "' "
   con=pull(quer)
   X=()
   for x in con:
        print(x)
        X=x
   if len(X) == 0:
     CM={"you dont have such file":""}
    
     
   else:
          quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(na) + "' AND TABLE_SCHEMA = 'wesagn'"
          co=pull(quer)
          co=co.fetchall()
          print("coco",co)
          TR={}
          TC=[]
          T={}
          for x in co:
               if(x[0]=="datee"):
                 TR["Date"]="1"
               elif(x[0]=="ID" or x[0]=="userid" ):
                     continue
               else:
                 TR[x[0]]="1"
          CM={"Have"+" "+na:" "}
          C26=2
          print("feeee",X)
          x1=X
            
            
          for ct,cy in TR.items():
               if(ct=="ID" or ct=="userid" ):
                     C26=C26+1
                     continue
               else:
                 T[ct]=x1[C26]
                 C26=C26+1
          TC.append(T)

def spel(rom):
  if(rom=="barth"):
    rom="birth"
  if(rom=="deth"):
    rom="death"
  if(rom=="adoption"):
    rom="Adoption"
  if(rom=="merage"):
    rom="mirrage"
  if(rom=="devorce"):
    rom="devorce"
  return rom
def sevak(sals):
  sals=str(sals)
  if(sals=="1"):
    sals="Admin"
  if(sals=="2"):
    sals="City Admin"
  if(sals=="3"):
    sals="keble Manager"
  if(sals=="4"):
    sals="Resident"
  if(sals=="5"):
    sals="Register"
  return sals

###############################  
def admin():
  global MU,FM ,AC,CM,TR,TC,CM
  jp=post_get()
  print("ADMIN1")
  MU={
            "Account":{"Create":"/data/1",
                   "status":"/data/2"},
              "profile":{"change password":"/data/3"}
            }
  if (ID1=="1"):
    print("ADMIN55")
    FM={"Name":"1",
         "sname":"1",
         "Password":"1",
         "job":{"Register":"5",
                "Kebele Manager":"3",
                "city admin":"2"}}
    if(jp==0):
        sa = request.form
        quer="INSERT INTO emp (fname, sname, pw, jobid, stu, cret_empid,datee) VALUES (:fname, :sname, :pw, :address, :statuss, :jop_id,:ddate);"
        dk=[{"fname":sa["Name"],"sname":sa["sname"],"pw":sa["Password"],"address":sa["job"],"statuss":"1","jop_id":"1", "ddate":datetime.datetime.now().date()}]
        insert_update_and_DELETE(quer,dk)
        CM={"Done!":" "} 
  if(ID1=="2"):
    quer="SELECT fname, sname,jobid,id,stu  FROM emp "
    conj=pull(quer)
    TR={"Name":"1",
        "SecondName":"1",
        "job":"1",
         "Status":"2"}
    TC=[]
   
    for c in conj:
      c2=0
      t={}
      for c1,c0 in TR.items():
        tt={}
        if(c0=="2"):
          o=c2+1
          tt[c[c2]]=c[o]
          t[c1]=tt
          c2=c2+1
        else:
           if(c1=="job"):
            t[c1]=sevak(c[c2])
            c2=c2+1
           else: 
            t[c1]=c[c2]
            c2=c2+1
          
       
        print(c[c2],t)
      TC.append(t)
    print(TC[1]['Status'])   
  if(ID1=="3"):
    passw1()
    if(jp==0):
      passw2()     
###############################
def city_admin():
  global MU,FM ,CM,TR,TC,CM,K,d,ID2
  jp=post_get()
  print("ADMIN1")
  MU={
            "kebele":{
                   "Manage":"/data/1",
                   "kebele Manage":"/data/4"},
            "Request":{"Request":"/data/5",
                      },
              "profile":{"change password":"/data/3"}
            }
  if (ID1=="1"):
     
     quer="SELECT Kname,manger_empid,id FROM keble"
     conj=pull(quer)
     TR={
       "kebele name":"1",
       "Name":"1",
         "Edit":"3"}
     TC=[]
   
     for c in conj:
      c2=0
      t={}
      for c1,c0 in TR.items():
        if(c1=="Name"):   
          if(c[1]=="0") :
            t[c1]="Null"
          else:
           quer="SELECT fname,sname FROM emp WHERE  id = '" + str(c[1]) + "'"
           conp=pull(quer)
           conp=conp.fetchone()
           t[c1]=conp[0]+" "+conp[1]
          c2=c2+1  
        else:
            t[c1]=c[c2]
            c2=c2+1
      TC.append(t)        
  if(ID1=="2"): 
    sa = request.form.get('eyob') 
  
    if(sa == None):
       sa = request.form
       quer="UPDATE keble SET manger_empid = :statuss WHERE id = :fname"
       
       print("mmmmmooo",K)
       
       dk=[{'statuss': sa["choose keble manager"], 'fname': K}]
       insert_update_and_DELETE(quer,dk)
    else:
      K=sa
      print("zsse",K)
    quer="SELECT manger_empid,kname FROM keble WHERE  id = '" +str(K) + "' "
    c=pull(quer)
    c=c.fetchone()
    
    TR={"Kebele":"1",
        "manger":"1"}
    TRR={}
    TC=[]
    TRR["Kebele"]=c[1]
    print("eyob",sa)
    FM={}
    ft={}
    CM={"choose keble manager":" "}
    quer="SELECT manger_empid FROM keble"
    conj=pull(quer)
    conj=conj.fetchall()
    quer="SELECT id, fname ,sname FROM emp WHERE  jobid = '3'"
    con=pull(quer)
    for x in con:
      b=0
      print("kkjo",x[0])
      for x1 in conj:
        print("kko",x1[0])
        if(int(x1[0])==int(x[0])):
          print("lllo1")
          if(int(c[0])==int(x[0])):
            print("lllo12")
            TRR["manger"]=x[1]+" "+x[2]
            
            
          
          b=1
          break
      if(b==0):
        ft[x[1]+" "+x[2]]=x[0]
    FM["choose keble manager"] =ft
    TC.append(TRR)  
  if(ID1=="4"):
    ID2=4
    TR={
       "manger name":"1",
       "kebele name":"1",
       
         "Stutes":"2"}
    TC=[]
    TRR1={}
    CM={"keble manager":" "}
    quer="SELECT manger_empid,id,Kname FROM keble"
    conj=pull(quer)
    conj=conj.fetchall()
    quer="SELECT id, fname ,sname FROM emp WHERE  jobid = '3' AND  stu='1' "
    con=pull(quer)
    for x in con:
      b=0
      TRR1 = {}
      print("kkjo",x[0])
      for x1 in conj:
        print("kko",x1[0])
        if(int(x1[0])==int(x[0])):
          print("lllo1") 
          TRR1["manger name"]=x[1]+" "+x[2]
          TRR1["kebele name"]=x1[2]
          t={}
          t[x1[1]]="1"
          TRR1["Stutes"]=t
          b=1
          print(TRR1)
      print(TC,"and",TRR1)      
      TC.append(TRR1)
      print(TC,"and",TRR1)
      if(b==0):
          print("am")
          TRR1["manger name"]=x[1]+" "+x[2]
          TRR1["kebele name"]="Null"
         
          TRR1["Stutes"]={"1":"Null"}
      print("akkknd",TRR1,TC) 
  if(ID1=="5"):
    quer="SELECT requset_tayp ,datee , stu,userid,id FROM requset "
    con=pull(quer)
    ID2=5
    TR={"Name":"1",
        
        "kebele":"1",
        "request tayp":"1",
        "Approvel Status":"2",
        "save":"5"
        
        }
    TC=[]
    
    for x in con:
      Tt={}
      for c1 ,c2 in TR.items():
         quer="SELECT fname ,sname , cret_empid FROM emp WHERE id='" +str(x[3]) + "' "
         con=pull(quer)
         co=con.fetchone()
         if(c1=="Name"):
           Tt[c1]=co[0]+" "+co[1]
         if(c1=="kebele"):
           Tt[c1]=co[2]
         if(c1=="request tayp"):
           Tt[c1]=spel(x[0])
         if(c1=="Approvel Status"):
           dm={}
           dm[x[4]]=x[2]
           Tt[c1]=dm
         if(c1=="save"):
           Tt[c1]={"5":"5"}
      TC.append(Tt)    
  if(ID1=="3"):
    passw1()
    if(jp==0):
      passw2()        
###############################  
def k_manager():
    global MU,FM ,CM,TR,TC,CM
    jp=post_get()
    MU={
            "Resident":{"Create":"/data/1" },
            "Report":{"Generate Report":"/data/2"},
            
              "profile":{"change password":"/data/3"}
            }
    if(ID1=="1"):
      
      FM={"Name":"1",
         "sname":"1",
         "cellphone":"1",
         "Password":"1",
         "job":{"Resident":"4"}}
      
      if(jp==0):
        X=()
        quer="SELECT kname FROM keble WHERE  manger_empid = '" +str(ACC["id"]) + "' "
        conj=pull(quer)
        for x in conj:
          print(x)
          X=x
        if len(X) == 0:
           CM={"your aconnt is not avelebel":" "}
        else:
         sa = request.form
         quer="INSERT INTO emp (fname, sname, pw, jobid, stu, cret_empid,datee,cellphone) VALUES (:fname, :sname, :pw, :address, :statuss, :jop_id,:ddate,:cellphone);"
         dk=[{"fname":sa["Name"],"sname":sa["sname"],"pw":sa["Password"],"address":sa["job"],"statuss":"1","jop_id":X[0],"cellphone":sa["cellphone"],"ddate":datetime.datetime.now().date()}]
         insert_update_and_DELETE(quer,dk)
         CM={"SECCSEFULY!":" "} 
    if(ID1=="2"):
      X=() 
      quer="SELECT id,Kname FROM keble WHERE  manger_empid = '" +str(ACC["id"]) + "' "
      conj=pull(quer)
      for x in conj:
        print(x)
        X=x
      if len(X) == 0:
           CM={"your aconnt is not avelebel":" "}
      else:
        TR={"Name":"1",
          "Second Name":"1",
          "cellphone":"1",
          "kebele Name":"1",
          "Save":"5"}
        TC=[]
       
        quer="SELECT fname,sname,cellphone FROM emp WHERE jobid='4' AND cret_empid = '" +str(X[1]) + "' "
        con=pull(quer)
        for c in con:
         c2=0
         t={}
         for c1,c0 in TR.items(): 
           if(c0=="5"):
             t[c1]={"5":"5"}
             continue
            
           if(c1=="kebele Name"):
             t[c1]=X[1]
             continue
            
           t[c1]=c[c2]
           c2=c2+1
         TC.append(t) 
    if(ID1=="3"):
     passw1()
     if(jp==0):
       passw2()       
def resident() :
    global MU,FM ,CM,TR,TC,CM
    jp=post_get()
    MU={
            "certificate":{"Request":"/data/1",
                           "Approved":"/data/2",},
            "Request":{"Birth":"/data/51",
                    "Death":"/data/61",
                    "Adoption":"/data/71",
                    "Mirrage":"/data/81",
                    "Devorce":"/data/91"
                    },
            "file":{"Birth":"/data/5",
                    "Death":"/data/6",
                    "Adoption":"/data/7",
                    "Mirrage":"/data/8",
                    "Devorce":"/data/9",
                    },
            
              "profile":{"change password":"/data/3"}
            }   
    if(ID1=="1"):
      
      quer="SELECT requset_tayp ,datee , stu FROM requset WHERE  userid = '" +str(ACC["id"]) + "' AND stu='0'"
      con=pull(quer)
      X=()
      
      
      for x in con:
        print(x)
        X=x
      if len(X) == 0:
         CM={"you  have no request":""}
      else:
        
        print("demskosss20",con)
        
        if(X[2]=="0"):
          TR={"request tayp":"1",
              "Date":"1",
              "stage":"1"}
          TC=[]
          quer="SELECT requset_tayp ,datee , stu FROM requset WHERE  userid = '" +str(ACC["id"]) + "' AND stu='0'"
          con=pull(quer)  
          con=con.fetchall()
          for x in con:
            h={}
            print("demskos",x,con)
            d=0
            for v,c in TR.items():
              if(v=="stage"):
                 h[v]="onging"
                 d=d+1
              elif(v=="request tayp"):
                h[v]=spel(x[d])
                d=d+1
              else:
                 h[v]=x[d]
                 d=d+1
            TC.append(h)    
        
    if(ID1=="2"):
      quer="SELECT requset_tayp ,datee , stu FROM requset WHERE  userid = '" +str(ACC["id"]) + "' AND stu='1'"
      con=pull(quer)
      X=()
      
      
      for x in con:
        print(x)
        X=x
      if len(X) == 0:
         CM={"you  have no request":""}
      else:
        if(X[2]=="1"):
          quer="SELECT * FROM " +str(X[0]) + " WHERE  userid = '" +str(ACC["id"]) + "' "
          con=pull(quer)
          X4=()
          for x in con:
            
              X4=x
          quer="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" +str(X[0]) + "' AND TABLE_SCHEMA = 'wesagn'"
          co=pull(quer)
          co=co.fetchall()
          print("coco",co)
          TR={"Save":"5",
              "request tayp":"1"
              }
          TC=[]
          T={}
          for x in co:
               if(x[0]=="datee"):
                 TR["Date"]="1"
               elif(x[0]=="ID" or x[0]=="userid" ):
                     continue
               else:
                 TR[x[0]]="1"
          C26=2
          print("feeee",X)
          x1=X4 
          for ct,cy in TR.items():
               if(ct=="ID" or ct=="userid" ):
                     C26=C26+1
                     continue
               elif(ct=="Save"):
                 T[ct]={"5":"5"}
               elif(ct=="request tayp"):
                 T[ct]=spel(X[0])
               elif(ct=="Date"):
                 T[ct]=x1[C26].isoformat() 
                 C26=C26+1 
               else:
                 T[ct]=x1[C26]
                 C26=C26+1
          TC.append(T)   
    if(ID1=="51"):
      Regi("barth")
    if(ID1=="61"):
      Regi("deth")
    if(ID1=="71"):
      Regi("adoption")
    if(ID1=="81"):
      Regi("merage")
    if(ID1=="91"):
      Regi("devorce")
    if(ID1=="5"):
      resiss("barth")
    if(ID1=="6"):
      resiss("deth")
    if(ID1=="7"):
      resiss("adoption")
    if(ID1=="8"):
      resiss("merage")
    if(ID1=="9"):
      resiss("devorce")
    if(ID1=="3"):
     passw1()
     if(jp==0):
      passw2()
def Registral():
    global MU,FM ,CM,TR,TC,CM
    jp=post_get()
    MU={
            "Registr":{
                   "Birth":"/data/5",
                    "Death":"/data/6",
                    "Adoption":"/data/7",
                    "Mirrage":"/data/8",
                    "Devorce":"/data/9"
                   },
              "profile":{"change password":"/data/3"}
            }
    if(ID1=="5"):
      Regis("barth")
    if(ID1=="6"):
      Regis("deth")
    if(ID1=="7"):
      Regis("adoption")
    if(ID1=="8"):
      Regis("merage")
    if(ID1=="9"):
      Regis("devorce")
    if(ID1=="3"):
     passw1()
     if(jp==0):
      passw2()
      
def log_cont(ID):
   global ID1,MU,FM,CM
   jp=post_get()             
   befr()
   ID1=str(ID)
   
   print("ADMIN0")
   if(ACC["ACCT"]=="1"):
          print("ADMIN")
          admin()
   if(ACC["ACCT"]=="2"):
       city_admin()
      
   if(ACC["ACCT"]=="3"):
       k_manager()
   if(ACC["ACCT"]=="4"):
       resident()
   if(ACC["ACCT"]=="5"):
      Registral()
   ID1="0"
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# @app.route("/",methods=['GET',"POST"])
# def heloo():
  
#   global MU,mu1
#   mu1={"1"}
#   return render_template('admin.html', MU=MU,mu1=mu1 )
@app.route("/", methods=['GET',"POST"])
def heydd():
   return render_template('lands.html')
@app.route("/login12", methods=['GET',"POST"])

def hello_world():
  global LG,CM,TB1,TB2,LT,MU,ID1,mu1
  ID1="0"
  ACC={"name":"0",
     "id":"0",
     "stu":"0",
     "jn":"0",
     "pw":"0",
      "ACCT":"0"}      
  befr()
  mu1={"1"}
  return render_template('log.html')
@app.route('/AC1' , methods=['GET',"POST"])
def helloworld():
 global CM,ACC,MU,FM,TB1,BLU,CM,ID1,ACC
 ID1="0"
 jp=post_get() 
 befr()
 MU={}
  
 TL='admin.html'
 sa = request.form
 print(sa)
 ACC["name"]=sa["User Name"]
 ACC["pw"]=sa["psw"]
 CP="7"
 CM={}
 LG="1"
 X=()
 quer="SELECT id, stu, fname FROM emp WHERE fname = '" + sa["User Name"] + "' AND pw = '" + sa["psw"] + "' AND jobid = '" + sa["Name"] + "' "
 conj=pull(quer)
 for x in conj:
    print(x)
    
    X=x
 if len(X) == 0:
    TL='come.html'
    CM={"incorect pasword or user name ":" "}
    print("List is empty")
 else:
    print("List is not empty")
    print(conj.fetchone())
    ACC["id"]=X[0]
    ACC["stu"]=int(X[1])
    ACC["ACCT"]=sa["Name"]
    ACC["jn"]=sevak(sa["Name"])
    
  
    if ACC["stu"]==0:
      CM={"your aconnt is not avelebel":" "}
      TL='come.html'
    if ACC["stu"]==1:
      print("sura")
      befr()
      P="welcome "+X[2]
      CM={P:" "}
      if(ACC["ACCT"]=="1"):
          admin()
      if(ACC["ACCT"]=="2"):
         city_admin()
      if(ACC["ACCT"]=="3"):
       k_manager()
       
      if(ACC["ACCT"]=="4"):
       resident()
      
       D=0
      if(ACC["ACCT"]=="5"):
       Registral()
       D=0
       f="solmone"
    ID1=0
 return render_template(TL, MU=MU, mu1=mu1,FM=FM,BLU=BLU,CM=CM,ACC=ACC)
@app.route('/data/<A>', methods=['GET',"POST"])
def helow2(A):
  global MU,mu1,ID1,FM,BLU,TR,TC,CM
  print("ADMIN001")
 
  log_cont(A)
  BLU=1
  return render_template('admin.html', MU=MU, mu1=mu1,FM=FM,BLU=BLU,TR=TR,TC=TC,CM=CM,ACC=ACC)
  
@app.route('/<api>/data', methods=['GET',"POST"])
def handle_data(api):
    global MU,mu1,ID1,FM,BLU,TC,TR,CM,ACC
    befr()
    
    
    
    if(1):
     data = str(api)
     print("KKKK")  # Log the received data
     mu1=MU[data]
     print("KKKK",mu1)
    
    return render_template('admin.html', MU=MU, mu1=mu1,FM=FM,BLU=BLU,TR=TR,TC=TC,CM=CM,ACC=ACC)
#if the main is best then the form is in the second 
#the main porpose of that 
def adminrot(data):
    global TC,CM
    print("KKKK",data['X'])  # Log the received data
    if(data['Y']==1):
      pt=0
      for g in TC:
        u=g['Status']
        if(list(g['Status'].keys())[0]==data['X']):
          quer="UPDATE emp SET stu = :statuss WHERE id= :fname"
          dk=[{'statuss': "0", 'fname': list(g['Status'].keys())[0]}]
          insert_update_and_DELETE(quer,dk)
          print(TC[pt]['Status'][data['X']])
      pt=pt+1
    if(data['Y']==0):
      pt=0
      for g in TC:
        u=g['Status']
        
        if(list(g['Status'].keys())[0]==data['X']):
          quer="UPDATE emp SET stu = :statuss WHERE id= :fname"
          dk=[{'statuss': "1", 'fname': list(g['Status'].keys())[0]}]
          insert_update_and_DELETE(quer,dk)
      pt=pt+1
    CM={"DONE!":" "} 
def cadtor(data):
   quer="UPDATE keble SET manger_empid = :statuss WHERE id= :fname"
   dk=[{'statuss': "0", 'fname': data['X']}]
   insert_update_and_DELETE(quer,dk)
def req(data) : 
   if(data['Y']==1):
      quer="UPDATE requset SET stu = :statuss WHERE id= :fname"
      dk=[{'statuss': "0", 'fname': data['X']}]
      insert_update_and_DELETE(quer,dk)
   if(data['Y']==0):
      quer="UPDATE requset SET stu = :statuss WHERE id= :fname"
      dk=[{'statuss': "1", 'fname': data['X']}]
      insert_update_and_DELETE(quer,dk)
@app.route('/api/data/stu', methods=['POST'])
def handle_():
    global ID2
    print("iddd111",ID2)
    data = request.get_json()
    if(ACC["ACCT"]=="1"):
       adminrot(data)
       print("sasa",data)
    if(ACC["ACCT"]=="2"):
      if(ID2==4):
       print("iddd111",ID2)
       cadtor(data)
      if(ID2==5):
       print("iddd111",ID2)
       req(data)
 
    return jsonify(response='Data received!'), 200
import csv
from io import StringIO
@app.route('/download')
def download():
    global TC,TR
    
    tm=[]
    tm2=[]
    t=[]
    tc=0
    
    for x in TC:
      tm=[]
      for m,m1 in x.items():
         if isinstance(m1, dict):
           kakka=0
         else:
           tm.extend([m1])
           if(tc==0):        
            tm2.extend([m])
      if(tc==0):
        t.append(tm2)  
        tc=1   
      t.append(tm)
          
          
    # Create a CSV string in memory
    
    print("t1=",t)
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(t)
    return Response(output.getvalue(),mimetype="text/csv", headers={"Content-disposition": "attachment; filename=data.csv"}),200

@app.route('/down', methods=['POST'])
def down():
    data = request.form.get('eyob') 
    print("lll",data)
    tm=[]
    tm2=[]
    t=[]
    import ast
    data= ast.literal_eval(data)
   
    
    
    for m,m1 in data.items():
         if isinstance(m1, dict):
           kakka=0
         else:
           tm.extend([m1])        
           tm2.extend([m])
      
    t.append(tm2)    
    t.append(tm)
          
          
    # Create a CSV string in memory
    
    print("tsdfsd1=",t)
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(t)
    return Response(output.getvalue(),mimetype="text/csv", headers={"Content-disposition": "attachment; filename=data.csv"}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True) 
