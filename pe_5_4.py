def new_password(oldpassword, newpassword):
    returnValue = False
    if oldpassword != newpassword:
        if len(newpassword) >= 6:
            if any(i.isdigit() for i in newpassword):
                returnValue = True
            else:
                print("Error - Does not contain a digit!")

    return returnValue


new_password("lmaotest", "skrrtskrrt1")
