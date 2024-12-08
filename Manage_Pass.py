def EncPass():
    passwordList = [['moreb','password123','scme.edu.ps'],['ahmad','password2','mail.google.com'],['mdm992002','password2','facebook.com']]
    print (passwordList)
    search = input ("Enter user name to show password... ")
    for i in range(len(passwordList)):
        if passwordList[i][0] == search:
            for j in range(len(passwordList[i])):
                print ( passwordList[i][j])

EncPass()