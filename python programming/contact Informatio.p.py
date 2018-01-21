'''
Create your own command-line address-book program using which you can browse,
add, modify, delete or search for your contacts such as friends,
family and colleagues and their information such as email address and/or phone number.
Details must be stored for later retrieval.
'''

class address_book:
    all_info=[]
    total=0

    def __init__(self,name,phoneno,email,company):
        self.name=name
        self.phoneno=phoneno
        self.email=email
        self.company=company

    def add(self):
        info ={"Name":self.name,"PhoneNo":self.phoneno,"Email":self.email,"Company":self.company}
        address_book.total +=1
        print(info)
        address_book.all_info.append(info)

    

    
   
       
    def modify(self):
        pass
        

    @classmethod

    def all_information(cls):
        print("Total contact Information: ",address_book.all_info)

    def browse(cls,s_name):
        
        s_name=s_name
        for i in address_book.all_info:
            if s_name in i['name']:
                print("Contact Information for {} : {}".format(self.s_name, i))

  


print("hello")
a1=address_book('kunwar',2345,'singh@','wipro')
a1.add()
a2=address_book('kun',23,'singh@','wipro')
a2.add()
a3=address_book('ku',2345,'singh@','wipro')
a3.add()
call=address_book()
call.browse('kunwar')
#calling class function
address_book.all_information()



