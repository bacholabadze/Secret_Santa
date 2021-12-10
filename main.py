import random
import smtplib



people= {
        0:{"Name":"Jemali Beria", "Mail": "test.1804.beria.jemali@gmail.com"},
        1:{"Name":"Nia Nozadze", "Mail": "test.1804.nianozadze7@gmail.com"},
        2:{"Name":"Sandro Dekanoidze", "Mail": "test.1804.sandro.dekanoidze718@ens.tsu.edu.ge"},
        3:{"Name":"Ana Kitesashvili", "Mail": "test.1804.ana.kitesashvili433@ens.tsu.edu.ge"},
        4:{"Name":"Bacho Labadze", "Mail": "test.1804.bachukilabadze@gmail.com"},
        5:{"Name":"Nika Iniashvili", "Mail": "test.1804.nika.iniashvili767@ens.tsu.edu.ge"},
        6:{"Name":"Giorgi arutiniani", "Mail": "test.1804.J3loodf@protonmail.com"},
        7:{"Name":"Ia Manizhashvili", "Mail": "test.1804.ia.manizhashvili@tsu.ge"},
        8:{"Name":"Sabrina Fague", "Mail": "test.1804.sabrina.fague@tsu.ge"}
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
