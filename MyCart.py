# MyCart Module

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy.sql import func

class MyCart:

    db_url='mysql://root:root@localhost:3306/project'
    engine=create_engine(db_url)
    Base=declarative_base()

    class User(Base):
        __tablename__='user'
        id=Column('uid',Integer,primary_key=True)
        uname=Column('uname',String(35))
        password=Column('password',String(35))
        cart=relationship('Cart',uselist=False)


    class Admin(Base):
        __tablename__='admin'
        id=Column('aid',Integer,primary_key=True)
        uname=Column('uname',String(35))
        password=Column('password',String(35))
        cate=relationship('Category',uselist=False)
        prod=relationship('Product',uselist=False)

    class Category(Base):
        __tablename__='category'
        id=Column('cid',Integer,primary_key=True)
        cname=Column('cname',String(35))
        admin=Column(Integer,ForeignKey('admin.aid'))

    class Product(Base):
        __tablename__='product'
        id=Column('pid',Integer,primary_key=True)
        pname=Column('pname',String(35))
        amount=Column('amount',Integer())
        description=Column('description',String(35))
        admin=Column(Integer,ForeignKey('admin.aid'))



    class Cart(Base):
        __tablename__='cart'
        user=Column(Integer,ForeignKey('user.uid'))
        id=Column('cartid',Integer,primary_key=True)
        pname=Column('pname',String(35))
        amount=Column('amount',Integer())


    Base.metadata.create_all(engine)

    Session=sessionmaker(bind=engine)
    session=Session()

          

    def user_register(self):
        try:

            # Insert  
            uid=int(input('Enter user id :'))
            uname=input('Enter user username :')
            pwd=input('Enter user password :')

            insData=self.User(id=uid,uname=uname,password=pwd)
            
            self.session.add(insData)
            self.session.commit()
            print('\nUser record is inserted...')
        except ValueError as e:
            print('\nPlease enter only number...')
        except Exception as e:
            print(e)
        finally:
            self.session.close()
            
    def admin_register(self):
        try:

            # Insert  
            uid=int(input('Enter admin id :'))
            uname=input('Enter admin username :')
            pwd=input('Enter admin password :')
            
            insData=self.Admin(id=uid,uname=uname,password=pwd)
            
            self.session.add(insData)
            self.session.commit()
            print('\nAdmin record is inserted...')
        except ValueError as e:
            print('\nPlease enter only number...')
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def add_category(self):
        try:
            
            disData=self.session.query(self.Category).all()
            category_list=[]
            for data in disData:
                category_list.append(data.cname)
                
            print('Category List :',category_list,'\n')

            # Insert  
            cid=int(input('Enter category id :'))
            cname=input('Enter category name :')

            adminData=self.session.query(self.Admin).all()
            
            admin_list=[]
            for data in adminData:
                admin_list.append(data.id)
            print('\nAdmin List :',admin_list,'\n')

            admin=int(input('Select admin :'))
            insData=self.Category(id=cid,cname=cname,admin=admin)
            
            self.session.add(insData)
            self.session.commit()
            print('\nCategory record is inserted...')
            
        except ValueError as e:
            print('\nPlease enter only number...')
        except Exception as e:
            print(e)
        finally:
            self.session.close()


    def add_product(self):
        try:
            
            disData=self.session.query(self.Product).all()
            product_list=[]
            for data in disData:
                product_list.append(data.pname)
                
            print('Product List :',product_list,'\n')

            # Insert  
            pid=int(input('Enter product id :'))
            pname=input('Enter product name :')
            amount=int(input('Enter amount :'))
            desc=input('Enter description :')
            
            adminData=self.session.query(self.Admin).all()
            admin_list=[]
            for data in adminData:
                admin_list.append(data.id)
            print('\nAdmin List :',admin_list,'\n')

            admin=int(input('Select admin id :'))
            insData=self.Product(id=pid,pname=pname,amount=amount,description=desc,admin=admin)
            
            self.session.add(insData)
            self.session.commit()
            print('\nCategory record is inserted...')
            
        except ValueError as e:
            print('\nPlease enter only number...')
        except Exception as e:
            print(e)
        finally:
            self.session.close()



    def add_to_cart(self):
        try:
            

            # Display user
            userData=self.session.query(self.User).all()
            user_list=[]
            for data in userData:
                user_list.append(data.id)
            print('\nUser List :',user_list,'\n')

            user=int(input('Select user id :'))
    
            while True:         
                print('\n1: Add Cart \23: Exit')
                chk=int(input('\nEnter your chooice :'))
                
                if(chk==1):

                    # Insert  
                    cartid=int(input('\nEnter cart id :'))

                    # Cart Name
                    disData=self.session.query(self.Cart).all()
                    cart_list=[]
                    for data in disData:
                        cart_list.append(data.pname)
                        
                    print('Cart List :',cart_list,'\n')



                    # Display product name
                    prodData=self.session.query(self.Product).all()
                    prod_dict={}
                    for data in prodData:
                        prod_dict[data.pname]= data.amount
                    print('\nProduct List :',prod_dict,'\n')
                    
                    pname=input('Enter product name :')

                    amount=int(input('Enter product amount :'))
                    
                    
                    insData=self.Cart(user=user,id=cartid,pname=pname,amount=amount)
                    
                    self.session.add(insData)
                    self.session.commit()
                    print('\n Add into cart...')
                elif(chk==2):
                    sys.exit()
                else:
                    print("Enter valid number....")
        except ValueError as e:
            print('\nPlease enter only number...')
        except Exception as e:
            print(e)
        finally:
            self.session.close()


    def total_bill(self):
        try:

            total_product=self.session.query(self.Cart).count()
            print('Total Product :',total_product)

            total=self.session.query(self.Cart).all()

            bill=0
            for amt in total:
                bill +=amt.amount
                
            print('Total bill is :',bill)
        

            # Truncate table

            self.session.query(self.Cart).delete()
            self.session.commit()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
