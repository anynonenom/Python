import datetime
import operator as oper
import array

current_date = datetime.date.today().strftime('%Y-%m-%d')
current_date_lst = current_date.split('-')
print(current_date , current_date_lst )
#list
bday_log = [] #, ('Yash' , ('1999' , '04' , '21'))
add = input('To add birthday type y :   ').strip().lower()
if add[:1] == 'y' :
    new = input('Add birthday in format yyyy-mm-dd : ')
    # print(new_lst)
    name=input('Whose bday ? ,  ')
    date = new.split('-')
    bday_log.append((name ,  tuple(date)))
    #print( tuple(date) ,  bday_log)
    for birthday in bday_log:
        if current_date_lst[1] != birthday[1][1] and current_date_lst[2] != birthday[1][1]:
            age = int( oper.__sub__(int(current_date_lst[0]) ,  int(birthday[1][0])))
            ordinal_suffix = {1:'st' , 2:'nd' , 3:'rd' , 11:'th' , 12:'th' , 13:'th'}.get(age % 10 if not 10 < age <= 13 else age % 14 ,'th' )
            print(f"It's {birthday[0]}'s {age}{ordinal_suffix} Birthday")
