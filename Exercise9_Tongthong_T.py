username = input('please enter your username:')
password = input('please enter your password:')
Sticky_rice = 20
Papaya_Salad = 55
Pickled_Fish = 40
Tom_Yum = 65
Pad_thai = 60

if username == 'User01' and password == '12345':
    print('Welcome to Siam Restaurant')
    print('This is our menu')
    print('1.Sticky rice  1x   = 20')
    print('2.Papaya Salad 1x   = 55')
    print('3.Pickled Fish 1x   = 40')
    print('4.Tom Yum Soup 1x   = 65')
    print('5.Pad Thai     1x   = 60')
    select = int(input('Please select the menu'))
    quantity = int(input('How many do you want?'))
    if select ==   1:
        print(Sticky_rice*quantity,'THB')
    elif select == 2:
        print(Papaya_Salad*quantity,'THB')
    elif select == 3:
        print(Pickled_Fish*quantity,'THB')
    elif select == 4:
        print(Tom_Yum*quantity,'THB')
    elif select == 5:
        print(Pad_thai*quantity,'THB')

