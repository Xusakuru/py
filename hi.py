user_time=input("enter seconds?")
hours = int(user_time)//3600
remain_seconds = int(user_time)-3600*hours
minutes = remain_seconds//60
seconds = remain_seconds%60
print("in those seconds there is %d hour(S) %d minute(S) %d second(S)" % (hours, minutes, seconds))


