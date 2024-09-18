hour = int(input())
minute = int(input())
delivery_time = int(input())
minutes = (minute + (delivery_time % 60))
hours = (hour + (delivery_time // 60) + (minutes // 60)) % 24
print(f'{hours + (minutes // 60):0>2}:{minutes % 60:0>2}')
