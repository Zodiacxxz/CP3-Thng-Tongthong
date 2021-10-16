username = input('please enter your username:')
password = input('please enter your password:')
Sticky_rice = 20
Papaya_Salad = 55
Pickled_Fish = 40
Tom_Yum = 65
Pad_thai = 60
Sum_Sticky_rice = 0
Sum_Papaya_Salad = 0
Sum_Pickled_Fish = 0
Sum_Tom_Yum = 0
Sum_Pad_thai = 0
if username == 'User01' and password == '12345':
    print('Welcome to Siam Restaurant')
    print('This is our menu')
    print('1.Sticky rice  1x   = 20')
    print('2.Papaya Salad 1x   = 55')
    print('3.Pickled Fish 1x   = 40')
    print('4.Tom Yum Soup 1x   = 65')
    print('5.Pad Thai     1x   = 60')
    select = int(input('Please select the menu'))
    while select != 0:
        if select == 1:
            quantity = int(input('How many do you want?'))
            Sum_Sticky_rice = Sticky_rice*quantity
            select = int(input('Anything else?'))
        elif select == 2:
            quantity = int(input('How many do you want?'))
            Sum_Papaya_Salad = Papaya_Salad*quantity
            select = int(input('Anything else?'))
        elif select == 3:
            quantity = int(input('How many do you want?'))
            Sum_Pickled_Fish = Pickled_Fish*quantity
            select = int(input('Anything else?'))
        elif select == 4:
            quantity = int(input('How many do you want?'))
            Sum_Tom_Yum = Tom_Yum*quantity
            select = int(input('Anything else?'))
        elif select == 5:
            quantity = int(input('How many do you want?'))
            Sum_Pad_thai = Pad_thai*quantity
            select = int(input('Anything else?'))
    print(Sum_Pad_thai+Sum_Papaya_Salad+Sum_Tom_Yum+Sum_Pickled_Fish+Sum_Sticky_rice)





