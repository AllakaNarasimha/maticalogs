from maticalgos.historical import historical

def login(mail, passwored):
    ma = historical('simha.happy@gmail.com')
    #ma.reset_password() 
    ## New Password will be sent to your registered email ID
    ma.login("491358") ##Password as sent on email
    return ma
if __name__ == "__login__":
    login()