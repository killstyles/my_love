# input 1`7 print 星期一~日
user = int(input('please input 1~7:'))
week = '星期一星期二星期三星期四星期五星期六星期日'
print(week[3 * user - 3:3 * user])
