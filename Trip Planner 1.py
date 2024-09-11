def greeting ():
    print ("Hello. Welcome to the Trip Planner.")
    first_name = input ("Please give me your first name")
    last_name = input ("Please give me your last name")
    print ("Hello",first_name," ",last_name,"")
    destination=input ("Where are you going on your trip?")
    print ("You are going to",destination," That sounds awesome.")

greeting()

def budget ():
    days = input("How many days would you like to travel?")
    int_days=int(days)
    total_budget=input("What is your total budget for the trip? Please answer in U.S. Dollar.")
    fltbudget = float(total_budget)
    print ("Total budget is",total_budget)
    print("Euro=EU,Canada=CAD,Mexico=MEX,Japan=JAP")
    currency_symbol=input ("Please enter the symbol of local currency")
    print(currency_symbol)
    ext_rate=float(input("Please enter the exchange rate for the currency"))
    hours=int_days*24
    minutes=hours*60
    seconds=(minutes*60)
    print("you will be spending ", days," days, ",hours," hours ", minutes," minutes and ", seconds, "seconds on your trip.")
    bperday=fltbudget/int_days
    print("Recommended amount to spend per day",bperday)

budget()

def time_zone ():
    int_hours=int(input("what is the time difference? Please enter plus or minus the number of hours"))
    print(int_hours)
    int_alttime=int(input("how many hours will the destination will be ahead/behind?"))
    print(int_alttime%24,":00")
    print("above is the time in your destination if it is noon at home")
    print(int_alttime%24+12,":00")
    #second "print"only works in forward direction

    print("above is the time in your destination if it is midnight at home.")
time_zone()
#maybe think about if then statement if minus then print "previous day ahead"











