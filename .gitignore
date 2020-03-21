import random

name = input ("Введiть ваше iм'я:  ")

print ("\n" + "Ок " + name + " oсь команды якi ви можете застосувати: "  )

print ("\n\n" + "a > Kulkulator < ----- Це звычайний кальлулятор ")

print ("\n\n" + "b > Random Game < ----- якщо вгадаєш числоб, ти виграв\n")


km = input ("")


if km == "a" :
    
    print("\n1> + \n2> - \n3> *\n4> :\n")

    zn = input("")

    if int (zn) == 1:

        num1 = input("\nВведiть перше число:  ")

        num2 = input("\nВведiть друге число:  ")


        rs = int (num1) + int (num2)


        print("\n",int (num1),"+", int (num2) ,"=", rs)

        print ("\n", "Результат", rs, "\n")

       
    elif int(zn) == 2:

        num1a = input("\nВведiть перше число:  ")

        num2a = input("\nВведiть друге число:  ")


        rsa = int (num1a) - int (num2a)


        print("\n",int (num1a),"-", int (num2a) ,"=", rsa)

        print ("\n", "Результат", rsa, "\n")


    elif int(zn) == 3:
        
        num1b = input("\nВведiть перше число:  ")

        num2b = input("\nВведiть друге число:  ")


        rs = int (num1b) * int (num2b)


        print("\n",int (num1b),"*", int (num2b) ,"=", rs)

        print ("\n", "Результат", rs, "\n")


    elif int(zn) == 4:

        num1c = input("\nВведiть перше число:  ")

        num2c = input("\nВведiть друге число:  ")


        rs = int (num1c) / int (num2c)


        print("\n",int (num1c),":", int (num2c) ,"=", rs)

        print ("\n", "Результат", rs, "\n")

    else:
       

        print("\n1> + \n2> - \n3> *\n4> :\n")
        
        zn = input("")


elif km == "b": 

     print("\n\n1> 1-5\n2> 1-10\n3> 1-25\n4> 1-..\n\n")
     
     kmr = input("")

     if int(kmr) == 1:
        nnm = input("\nВведи любе число вiд 1 до 5 \n\n")

        rn = random.randint(1,5)
        
        if rn == int(nnm):

           print("\nТи виграв, число справдi було ", rn)

        elif rn != int(nnm):

           print("\nТи програв, насправдi число було ", rn, "\n")


    
     elif int(kmr) == 2:

        nnm = input("\nВведи любе число вiд 1 до 10 \n\n")

        rn = random.randint(1,10)
        
        if rn == int(nnm):

           print("\nТи виграв, число справдi було ", rn)

        elif rn != int(nnm):

           print("\nТи програв, насправдi число було ", rn, "\n")

     
        
     elif int(kmr) == 3:

        nnm = input("\nВведи любе число вiд 1 до 25 \n\n")

        rn = random.randint(1,25)
        
        if rn == int(nnm):

           print("\nТи виграв, число справдi було ", rn)

        elif rn != int(nnm):

           print("\nТи програв, насправдi число було ", rn, "\n")

   
   

     elif int(kmr) == 4:
         
         nvr = int(input("Виберiть число вiд 1 до 10 000:   1-"))

         nnm = input("\n\nВведи любе число вiд 1 до ... \n\n")

         rn = random.randint(1,nvr)
        
         if rn == int(nnm):

             print("\nТи виграв, число справдi було ", rn)

         elif rn != int(nnm):
             
            print("\nТи програв, насправдi число було ", rn, "\n") 

else:
    print("\n",name, "Такоi команди нема: \n")
