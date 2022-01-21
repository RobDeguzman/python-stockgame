import string

def newpassword(player_name,newpwd):
    player=['','','','']
    result = ''
    with open("players.txt") as player_file:
        for player_record in player_file:
            num = 0
            player_record = player_record.rstrip()
            for char in string.punctuation:
                player_record = player_record.replace(char,' ')
            record = player_record.split()
    
            for fields in record:
                player[num] = fields
                num = num + 1
            stored_name = player[0]
            stored_name = stored_name.lower()
            pname = player_name.lower()
            
            if stored_name == pname:    
                player[1] = str(newpwd)
                result += str(player) + '\n'
            else:
                result += str(player) + '\n'                

    f = open("players.txt", 'w') 
    f.writelines(result)
    f.close()
    print('Password changed successfully. Your new password is \'',newpwd,'\'.')
