def validEmailList(emailList):
    emails = []  
    for mail in emailList:
        if isEmailValid(mail):
            emails.append(mail)
    return emails

def isEmailValid(mail):
    if (' ') in mail:return False
    if mail.count('@') != 1:return False

    local_part, domain_part = mail.split('@')
    if ('.') not in domain_part:
        return False
    if local_part == (''):
        return False
    return True
