class Secret:
    def __init__(self,code,meeting_point,time):
        self.code=code
        self.meeting_point=meeting_point
        self.time=time

input_str = tuple(input().split())
code, meeting_point, time = input_str
secret1 = Secret(code,meeting_point,time)

print('secret code : '+ secret1.code)
print('meeting point : '+ meeting_point)
print('time : '+ time)