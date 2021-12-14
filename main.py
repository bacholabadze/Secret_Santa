import random
import smtplib



people= {
        0:{"Name":"Jemali Beria", "Mail": "test.jemali@gmail.com"},
        1:{"Name":"Nia Nozadze", "Mail": "test.nia@gmail.com"},
        2:{"Name":"Sandro Dekanoidze", "Mail": "test.sandro@ens.tsu.edu.ge"},
        3:{"Name":"Ana Kitesashvili", "Mail": "test.1ana@ens.tsu.edu.ge"},
        4:{"Name":"Bacho Labadze", "Mail": "test.labadze@gmail.com"},
        5:{"Name":"Nika Iniashvili", "Mail": "test.iniashvili767@ens.tsu.edu.ge"},
        6:{"Name":"Giorgi arutiniani", "Mail": "test.J3loodf@mail.com"},
        7:{"Name":"Ia Manizhashvili", "Mail": "test.manizhashvili@tsu.ge"},
        8:{"Name":"Sabrina Fague", "Mail": "test.fague@tsu.ge"}
        }

used=[]
secretsanta=[]
def match():
    check=False
    for i in range(0,len(people)):
        check=False
        while not check:
            randnum=random.randint(0,len(people)-1)
            #print('randum = ',randnum)
            if randnum not in used and i != randnum:
                secretsanta.append(tuple((i,randnum)))
                used.append(randnum)
                print(used)
                check=True
            
def sendMail():
    sender_email = "fr.tsu.secret.santa@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password = input(str("Enter Your Password : "))
    print("Login Success")
    server.login(sender_email,password)

    for i in range(0,len(people)):
        santa_name = people[i]['Name'].split()[0]
        santa_mail = people[i]['Mail']
        kid_index = secretsanta[i][1]
        kid_name = people[kid_index]['Name']
        #print(f'santa = {santa_name}\nkid = {kid_name}\n\n')        
        message = str("Bonjour "+ santa_name+". Tu es le pere noel secret de "+kid_name)
        server.sendmail(sender_email, santa_mail,message)
        print("Email has been sent to ",santa_mail)


match()

print(secretsanta)
sendMail()
