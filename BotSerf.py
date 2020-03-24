import random

name = input("Введiть ваше iм'я:  ")

print ("\nОк ", name, " ось команди як ви можете застосувати")

def menu():

    print ("\n\na> Kulkulator < ----- Це звычайний кальлулятор ")

    print ("\n\nb> Random Game < ----- якщо вгадаєш число, ти виграв")

    km = input("\n")

    if km == "a":

        def kulm():



            print("\na> +\nb> -\nc> *\nd> :\n")

            klk = input("")

            if klk == "a":

                def kulmp():

                    pl1 = input("\nВведiть перше число:  ")

                    pl2 = input("\nВведiть друге число:  ")

                    pl = int(pl1) + int(pl2)

                    print("\n", int(pl1), "+", int(pl2), "=", int(pl))

                    print("\n Результат", pl, "\n")

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmpv = input("n/m/r/k:  ")

                    if kulmpv == "r":

                        kulmp()

                    elif kulmpv == "m":

                        menu()

                    elif kulmpv == "k":

                        kulm()

                    else:
                        print ("Goodbuy\n")

                kulmp()

            elif klk == "b":

                def kulmm ():

                    mn1 = input("\nВведiть перше число:  ")

                    mn2 = input("\nВведiть друге число:  ")

                    mn = int(mn1) - int(mn2)

                    print("\n", int(mn1), "-", int(mn2), "=", int(mn))

                    print("\n Результат", mn, "\n")

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmmv = input("n/m/r/k:  ")

                    if kulmmv == "n":

                        print("Goodbuy\n")

                    elif kulmmv == "m":

                        menu()

                    elif kulmmv == "r":

                        kulmm()

                    elif kulmmv == "k":

                        kulm()

                    else:

                        print("\nGoodbuy\n")

                kulmm()

            elif klk == "c":

                def kulmj():

                    mj1 = input("\nВведiть перше число:  ")

                    mj2 = input("\nВведiть друге число:  ")

                    mj = int(mj1) * int(mj2)

                    print("\n", int(mj1), "*", int(mj2), "=", int(mj))

                    print("\n Результат", mj, "\n")

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmjv = input("n/m/r/k:  ")


                    if kulmjv == "n":

                        print("Goodbuy\n")

                    elif kulmjv == "m":

                        menu()

                    elif kulmjv == "r":

                        kulmm()

                    elif kulmjv == "k":

                        kulm()

                    else:

                        print("\nGoodbuy\n")

                kulmj()

            elif klk == "d":

                def kulmd():


                     md1 = input("\nВведiть перше число:  ")

                     md2 = input("\nВведiть друге число:  ")

                     md = int(md1) / int(md2)

                     print("\n", int(md1), ":", int(md2), "=", int(md))

                     print("\n Результат", md, "\n")
                    
                     print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                     kulmdv = input("n/m/r/k:  ")
                
                     if kulmdv == "m":

                         menu()

                     elif kulmdv == "r":

                         kulmd()

                     elif kulmdv == "k":

                         kulm()

                     else:

                         print("\nGoodbuy\n")
                        
                kulmd()
        kulm()


    elif km == "b":

        def rz():

            print("\na> 1-5\nb> 1-10\nc> 1-25\nd> 1-..\n")

            rdz = input("")

            if rdz == "a":

                def rz1():

                   rrd = random.randint(1,5)

                   rnd = input("\nВведiть число вiд 1 до 5:  ")

                   if int(rnd) == int(rrd):

                       print ("\nТи виграв, число справдi було", int(rrd))

                   elif int(rnd) != int(rrd):
                       
                       print("\n Нажаль ти програв, насправдi число було", int(rrd))

                   print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                   kulmdv = input("n/m/r/k:  ")

                   if kulmdv == "m":


                       menu()

                   elif kulmdv == "r":


                       rz1()

                   elif kulmdv == "k":

                       rz()

                   else:

                       print("Goodbuy")
      
                rz1()
    
            elif rdz == "b":

                def rz2():

                    rrd = random.randint(1,1)

                    rnd = input("\nВведiть число вiд 1 до 10:  ")

                    if int(rnd) == int(rrd):

                        print ("\nТи виграв, число справдi було", int(rrd))

                    elif int(rnd) != int(rrd):
                       
                        print("\nНажаль ти програв, насправдi число було", int(rrd))

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmdv = input("n/m/r/k:  ")

                    if kulmdv == "m":

                        menu()

                    elif kulmdv == "r":


                         rz2()

                    elif kulmdv == "k":

                         rz()

                    else:

                        print("\nGoodbuy\n")

                rz2()

            elif rdz == "c":


                def rz3():


                    rrd = random.randint(1,25)

                    rnd = input("\nВведiть число вiд 1 до 25:  ")

                    if int(rnd) == int(rrd):

                        print ("\nТи виграв, число справдi було", int(rrd))

                    elif int(rnd) != int(rrd):
                       
                        print("\nНажаль ти програв, насправдi число було", int(rrd))

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmdv = input("n/m/r/k:  ")

                    if kulmdv == "m":

                        menu()

                    elif kulmdv == "r":

                        rz3()

                    elif kulmdv == "k":

                        rz()

                    else:

                        print("Goodbuy")

                rz3()      

            elif rdz == "d":

                def rz4():

                    rnum = input("1-")

                    rrd = random.randint(1,int(rnum))

                    rnd = input("\nВведiть число вiд 1 до .. :  ")

                    if int(rnd) == int(rrd):

                        print ("\nТи виграв, число справдi було", int(rrd))

                    elif int(rnd) != int(rrd):
                       
                        print("\nНажаль ти програв, насправдi число було", int(rrd))

                    print("\n\nn> вийти\nm> меню \nr> заново \nk> меню режима \n")

                    kulmdv = input("n/m/r/k:  ")

                    if kulmdv == "m":

                        menu()

                    elif kulmdv == "r":

                        rz4()

                    elif kulmdv == "k":

                        rz()

                    else:

                        print("Goodbuy")

                rz4()
        rz()
menu()  


