class product:
    def __init__(self,name='codetree',code='50'):
        self.name=name
        self.code=code


name,code = input().split()
product1 = product()
print('product '+product1.code+ ' is '+ product1.name)

product1 = product(name,code)

print('product '+product1.code+ ' is '+ product1.name)