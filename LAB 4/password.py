correct_pass = 'aaa'
password = ''
count = 1

while password!=correct_pass:
    if count<=3:
        password = input(f"Enter Your Password ( Try {count} ) : ")
        count+=1
    else:
        print('no more Tries')
        break
else:
    print("====================================")
    print('You Entered The Correct Password ...')