import datetime
birth_day = datetime.date(1983, 11, 3)
today = datetime.date.today()
print('私が生まれてから'+str(today - birth_day)[:-14]+'日経ちました。')