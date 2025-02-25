loan = int(input("How large is the loan? (1-10): "))
credit = int(input("How good is your credit history? (1-10): "))
income = int(input("How high is your income? (1-10): "))
payment = int(input("How large is your down payment? (1-10): "))

do_they_get_the_loan_that_they_want = False

if loan >= 5 :
    if credit >= 7 and income >= 7 : do_they_get_the_loan_that_they_want = True
    if credit >= 7 or income >= 7 :
        if payment >= 5 : do_they_get_the_loan_that_they_want = True
elif loan < 5 :
    if not credit < 4 :
        if income >= 7 or payment >=7 : do_they_get_the_loan_that_they_want = True 
        if income >=4 and payment >=4 : do_they_get_the_loan_that_they_want = True

if do_they_get_the_loan_that_they_want : print("YOU GOT THE LOAN!!!")
else : print("get poor dumby hahahahhahahahha")