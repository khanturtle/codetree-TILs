class Code_info:
    def __init__(self,code,color,second):
        self.code=code
        self.color=color
        self.second=second

code,color,second = tuple(input().split())

code_info1 = Code_info(code,color,second)

print('code : '+code_info1.code)
print('color : '+code_info1.color)
print('second : '+code_info1.second)