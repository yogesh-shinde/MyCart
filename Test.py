# Test Module

from MyCart import *
import sys

class Test:
    try:
        op=MyCart()
        while(True):
            print('\n1: Admin Register \t2: User Register \t3: Add Category \t4: Add Product \n5: Add Cart \t\t6: Bill \t\t7: Exit()')
            ch=int(input('\nEnter valid chooise :'))

            if(ch == 1):
                op.admin_register()
            elif(ch == 2):
                    op.user_register()
            elif(ch==3):
                op.add_category()
            elif(ch==4):
                op.add_product()
            elif(ch==5):
                op.add_to_cart()
            elif(ch==6):
                op.total_bill()
            elif(ch==7):
                sys.exit()
            else:
                print("Enter valid number....")
    except ValueError as e:
        print("Please add valid input...")
##    except Exception as e:
##        print(e)      

Test()
