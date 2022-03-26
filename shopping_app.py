i=j=k=0
user_id=[111]
user_pas=[000]
admin_id=[420]
admin_pas=[888]
e=["MOBILE","SPEAKER","SMART T.V","A.C","GAMING LAPTOP"]
e_prize=[10000,20000,30000,40000,50000]
e_stock=[45,40,30,25,15]
f=["NIGHT WEAR","KIDS WEAR","MENS WEAR","PARTY WEAR","SPORTS WEAR"]
f_prize=[10000,50000,25000,35000,33000]
f_stock=[30,27,45,23,33]
g=["PACKED ITEM","CAKE","CHOCOLATE","WHEAT FLOUER","RICE"]
g_prize=[50000,35000,33000,20000,10000]
g_stock=[10,30,50,11,35]
user_list=[]
user_amount=[]
user_quantity=[]
amount=0
while(1):
    print("------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\twelecom")
    print("------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t 1-electronics\n")
    for i in range(0,(len(e))):
        print("\nITEMS\tCOST\tSTOCK\n",e[i],e_prize[i],e_stock[i])
    print("\t\t\t\t\t\t 2-faishon\n")
    for j in range(0,(len(f))):
        print("\nITEMS\tCOST\tSTOCK\n",f[j],f_prize[j],f_stock[j])
    print("\t\t\t\t\t\t 3-grocery\n")
    for k in range(0,(len(g))):
        print("\nITEMS\tCOST\tSTOCK\n",g[k],g_prize[k],g_stock[k])
    print("enter the choice\n0 for exit\n1 for sign in as user \n2for sign up as user\n3 for sign in as admin\n4 for sign up as admin")
    n=int(input("enter choice"))
    if(n==1):
        a=int(input("enter your id"))
        b=int(input("enter your password if forgetten password then enter your luckey number"))    
        for i1 in range(0,len(user_id)):
            if(a==user_id[i1] and (b==user_pas[i1]or b==6)):
                print("welecom user")
                while(1):
                    print("\t\t\t\t\t\t 1-electronics\n")
                    for i in range(0,(len(e))):
                        print("\nITEMS\tCOST\tSTOCK\n",e[i],e_prize[i],e_stock[i])
                    print("\t\t\t\t\t\t 2-faishon\n")
                    for j in range(0,(len(f))):
                        print("\nITEMS\tCOST\tSTOCK\n",f[j],f_prize[j],f_stock[j])
                    print("\t\t\t\t\t\t 3-grocery\n")
                    for k in range(0,(len(g))):
                        print("\nITEMS\tCOST\tSTOCK\n",g[k],g_prize[k],g_stock[k])
                    c=int(input("enter the category and press 0 to exit"))
                    if(c==1):
                        print("\t\t\t\t\t\t 1-electronics\n")
                        for i in range(0,(len(e))):
                            print("ITEMS\tCOST\tSTOCK\n",i,e[i],e_prize[i],e_stock[i])
                        l=int(input("enter your choice "))
                        q=int(input("enter the quantity"))
                        user_list.append(e[l])
                        user_amount.append(e_prize[l])
                        user_quantity.append(q)
                    elif(c==2):
                        print("\t\t\t\t\t\t 2-faishon\n")
                        for j in range(0,(len(f))):
                            print("\nITEMS\tCOST\tSTOCK\n",j,f[j],f_prize[j],f_stock[j])
                        l=int(input("enter your choice "))
                        user_list.append(f[l])
                        user_amount.append(f_prize[l])
                        user_quantity.append(q)
                    elif(c==3):
                        print("\t\t\t\t\t\t 3-grocery\n")
                        for k in range(0,(len(g))):
                            print("\nITEMS\tCOST\tSTOCK\n",k,g[k],g_prize[k],g_stock[k])
                        l=int(input("enter your choice "))
                        user_list.append(g[l])
                        user_amount.append(g_prize[l])
                        user_quantity.append(q)
                    elif(c==0):
                        print("thankyou for visiting")
                        print("your selected items are")
                        for i in range(0,(len(user_list))):
                            print("ITEMS\tCOST\tSTOCK\n",i,user_list[i],user_amount[i],user_quantity[i])
                            amount=amount+user_amount[i]*user_quantity[i]
                        print("yout bill is",amount)
                        user_amount=[]
                        user_list=[]
                        user_quantity=[]
                        amount=0
                        break
                    else:
                        print("invalid choice")
       
            else:
                print("invalid id")
    elif(n==2):
        a=int(input("enter your new id"))
        b=int(input("enter your new password"))
        user_id.append(a)
        user_pas.append(b)
    elif(n==0):
        print("thank you visit again")
        break
    elif(n==3):
        a=int(input("enter your id"))
        b=int(input("enter your password if forgetten password then enter your luckey number"))    
        for i1 in range(0,len(admin_id)):
            if(a==admin_id[i1] and (b==admin_pas[i1]or b==6)):
                print("welecom admin")
                print("\t\t\t\t\t\t 1-electronics\n")
                for i in range(0,(len(e))):
                    print("\nITEMS\tCOST\tSTOCK\n",e[i],e_prize[i],e_stock[i])
                print("\t\t\t\t\t\t 2-faishon\n")
                for j in range(0,(len(f))):
                    print("\nITEMS\tCOST\tSTOCK\n",f[j],f_prize[j],f_stock[j])
                print("\t\t\t\t\t\t 3-grocery\n")
                for k in range(0,(len(g))):
                    print("\nITEMS\tCOST\tSTOCK\n",g[k],g_prize[k],g_stock[k])
                print("what do you want to do\n 1 to add item\n2 for changing prize\n3 for changing the quantity\n4 for shopping\n0 to exit ")
                ch=int(input("enter the choice"))
                if(ch==1):
                    print("in which category you want to add item \n1 for electronic\n2 for faishon\n3 for grocery")
                    c=int(input("enter the choice"))
                    if(c==1):
                        item=input("enter item name")
                        e.append(item)
                        cost=int(input("enter its cost"))
                        e_prize.append(cost)
                        stock=int(input("enter the stock"))
                        e_stock.append(stock)
                    elif(c==2):
                        item=input("enter item name")
                        f.append(item)
                        cost=int(input("enter its cost"))
                        f_prize.append(cost)
                        stock=int(input("enter the stock"))
                        f_stock.append(stock)
                    elif(c==3):
                        item=input("enter item name")
                        g.append(item)
                        cost=int(input("enter its cost"))
                        g_prize.append(cost)
                        stock=int(input("enter the stock"))
                        g_stock.append(stock)
                    else:
                        print("error:wrong choice")
                elif(ch==2):
                    print("in which category you want to change prize \n1 for electronic\n2 for faishon\n3 for grocery")
                    c=int(input("enter the choice"))
                    if(c==1):
                        n=int(input("enter the number at which item is "))
                        cost=int(input("enter its cost"))
                        e_prize[n-1]=cost
                    elif(c==2):
                        n=int(input("enter the number at which item is "))
                        cost=int(input("enter its cost"))
                        f_prize[n-1]=cost
                    elif(c==3):
                        n=int(input("enter the number at which item is "))
                        cost=int(input("enter its cost"))
                        g_prize[n-1]=cost
                    else:
                        print("invalid number")
                elif(ch==3):
                    print("in which category you want to change quantity\n1 for electronic\n2 for faishon\n3 for grocery")
                    c=int(input("enter the choice"))
                    if(c==1):
                        n=int(input("enter the number at which item is "))
                        stock=int(input("enter its stock"))
                        e_stock[n-1]=stock
                    elif(c==2):
                        n=int(input("enter the number at which item is "))
                        stock=int(input("enter its stock"))
                        f_stock[n-1]=stock
                    elif(c==3):
                        n=int(input("enter the number at which item is "))
                        stock=int(input("enter its stock"))
                        g_stock[n-1]=stock
                    else:
                        print("invalid number")
                elif(ch==4):
                    while(1):
                        print("\t\t\t\t\t\t 1-electronics\n")
                        for i in range(0,(len(e))):
                            print("\nITEMS\tCOST\tSTOCK\n",e[i],e_prize[i],e_stock[i])
                        print("\t\t\t\t\t\t 2-faishon\n")
                        for j in range(0,(len(f))):
                            print("\nITEMS\tCOST\tSTOCK\n",f[j],f_prize[j],f_stock[j])
                        print("\t\t\t\t\t\t 3-grocery\n")
                        for k in range(0,(len(g))):
                            print("\nITEMS\tCOST\tSTOCK\n",g[k],g_prize[k],g_stock[k])
                        c=int(input("enter the category and press 0 to exit"))
                        if(c==1):
                            print("\t\t\t\t\t\t 1-electronics\n")
                            for i in range(0,(len(e))):
                                print("ITEMS\tCOST\tSTOCK\n",i,e[i],e_prize[i],e_stock[i])
                                l=int(input("enter your choice "))
                                q=int(input("enter the quantity"))
                                user_list.append(e[l])
                                user_amount.append(e_prize[l])
                                user_quantity.append(q)
                        elif(c==2):
                            print("\t\t\t\t\t\t 2-faishon\n")
                            for j in range(0,(len(f))):
                                print("\nITEMS\tCOST\tSTOCK\n",j,f[j],f_prize[j],f_stock[j])
                            l=int(input("enter your choice "))
                            q=int(input("enter the quantity"))
                            user_list.append(f[l])
                            user_amount.append(f_prize[l])
                            user_quantity.append(q)
                        elif(c==3):
                            print("\t\t\t\t\t\t 3-grocery\n")
                            for k in range(0,(len(g))):
                                print("\nITEMS\tCOST\tSTOCK\n",k,g[k],g_prize[k],g_stock[k])
                            l=int(input("enter your choice "))
                            q=int(input("enter the quantity"))
                            user_list.append(g[l])
                            user_amount.append(g_prize[l])
                            user_quantity.append(q)
                        elif(c==0):
                            print("thankyou for visiting")
                            print("your selected items are")
                            for i in range(0,(len(user_list))):
                                print("ITEMS\tCOST\tSTOCK\n",i,user_list[i],user_amount[i],user_quantity[i])
                                amount=amount+user_amount[i]*user_quantity[i]
                            print("yout bill is",amount)
                            user_amount=[]
                            user_list=[]
                            user_quantity=[]
                            amount=0
                            break
                        else:
                            print("invalid choice")
                elif(ch==0):
                    print("thank you. visit again")
                    break
                else:
                    print("error")
            else:
                print("invalid id")
    elif(n==4):
        a=int(input("enter your new id"))
        b=int(input("enter your new password"))
        admin_id.append(a)
        admin_pas.append(b)
    else:
        print("invalid number")


    