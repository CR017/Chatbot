import sys
from datetime import datetime
from difflib import get_close_matches

# Closest word match function
def closeMatches(word,patterns):
    #if(any(word.lower() in s.lower() for s in patterns)):
    for p in patterns:
        if(p.lower()== word.lower()):
           return p
    try:
        sw=get_close_matches(word, patterns, n=1)[0]
        write_to_text.write("Chatbot: Do you mean "+ str(sw) +" ?[Yes/No]" + " \n ")
        print("Chatbot: Do you mean "+ str(sw) +" ?[Yes/No]")
        C_input = Check_isEmpty("Chatbot: Do you mean "+ str(sw) +" ?[Yes/No]", input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")
        if(C_input.lower()=="n" or C_input.lower()=="no"):
            return ""
    except IndexError:
        sw=""
    return str(sw)

# Making Time stemped File name
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y_(%H-%M-%S)")
write_to_text=open("CH_"+timestampStr+".txt","w+")
write_to_text.write("Time: "+ timestampStr + " \n ")

#Car brand names
Brands_Name=['Maruthi Suzuki','Honda','Mahindra','Isuzu','Kia','Volvo','Citroen','Land Rover','TATA','Ford']


#Check if the Input is Integer or not
def Ask_Question(Question, C_input):
    global val
    while (True):
        try:
            val = int(C_input)
            break
        except ValueError:
            write_to_text.write(Question + " \n ")
            print(Question)
            C_input = input("Customer: ")
            write_to_text.write("Customer: "+ C_input + " \n ")
            continue
    return val

#if the input is empty ask question again
def Check_isEmpty(Question, C_input):
    while (True):
        if(C_input==""):
            print(Question)
            C_input = input("Customer: ")
        else:
            break
    return C_input

#Getting Information about the Cars and their models
def Cars_Information(Number):
    write_to_text.write("Chatbot: What is the "+Number+" brand Name?" + " \n ")
    print("Chatbot: What is the "+Number+" brand Name?")
    Brand_Name = closeMatches(Check_isEmpty("Chatbot: What is the "+Number+" brand Name?",input("Customer: ")),Brands_Name)
    write_to_text.write("Customer: "+ Brand_Name + " \n ")

    while(len(Brand_Name)==0):
        write_to_text.write("Chatbot: What is the " + Number + " brand Name?[Entered Brand Not Found]" + " \n ")
        print("Chatbot: What is the " + Number + " brand Name?[Entered Brand Not Found]")
        Brand_Name = closeMatches(input("Customer: "),Brands_Name)
        write_to_text.write("Customer: " + Brand_Name + " \n ")

    write_to_text.write("Chatbot: How Many Cars in " + Brand_Name + "? (IN NUMBER)" + " \n ")
    print("Chatbot: How Many Cars in " + Brand_Name + "? (IN NUMBER)")
    C_input = Check_isEmpty("Chatbot: How Many Cars in " + Brand_Name + "? (IN NUMBER)",input("Customer: "))
    write_to_text.write("Customer: " + C_input + " \n ")
    Car_Quantity = Ask_Question("Chatbot: How Many Cars in " + Brand_Name + " (IN NUMBER only)", C_input)

    if(Car_Quantity!=1):
        write_to_text.write("Chatbot: Are They of the same Model?[Yes/No]" + " \n ")
        print("Chatbot: Are They of the same Model?[Yes/No]")
        C_input = Check_isEmpty("Chatbot: Are They of the same Model?[Yes/No]",input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")
    else:
        write_to_text.write("Chatbot: What model is it?" + " \n ")
        print("Chatbot: What model is it?")
        C_input = Check_isEmpty("Chatbot: What model is it?",input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")

        write_to_text.write("Chatbot: What is the engine size of Car?" + " \n ")
        print("Chatbot: What is the engine size of Car?")
        C_input = Check_isEmpty("Chatbot: What is the engine size of Car?", input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")

        write_to_text.write("Chatbot: How many Axles are in this Car?" + " \n ")
        print("Chatbot: How many Axles are in this Car?")
        C_input = Check_isEmpty("Chatbot: How many Axles are in this Car?", input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")

    if ("no" in C_input.lower() or "n" in C_input.lower()):
        j = 1
        while (j <= Car_Quantity):
            if (j == 1):
                write_to_text.write("Chatbot: what is the 1st Car model?" + " \n ")
                print("Chatbot: What is the 1st Car model?")
                C_input =Check_isEmpty("Chatbot: What is the 1st Car model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: What is the engine size of 1st Car?" + " \n ")
                print("Chatbot: What is the engine size of 1st Car?")
                C_input = Check_isEmpty("Chatbot: What is the engine size of 1st Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: How many Axles are in 1st Car?" + " \n ")
                print("Chatbot: How many Axles are in 1st Car?")
                C_input = Check_isEmpty("Chatbot: How many Axles are in 1st Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

            elif (j == 2):
                write_to_text.write("Chatbot: What is the 2nd Car model?" + " \n ")
                print("Chatbot: What is the 2nd Car model?")
                C_input = Check_isEmpty("Chatbot: What is the 2nd Car model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: What is the engine size of 2nd Car?" + " \n ")
                print("Chatbot: What is the engine size of 2nd Car?")
                C_input = Check_isEmpty("Chatbot: What is the engine size of 2nd Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: How many Axles are in 2nd Car?" + " \n ")
                print("Chatbot: How many Axles are in 2nd Car?")
                C_input = Check_isEmpty("Chatbot: How many Axles are in 2nd Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

            elif (j == 3):
                write_to_text.write("Chatbot: What is the 3rd Car model?" + " \n ")
                print("Chatbot: What is the 3nrd Car model?")
                C_input = Check_isEmpty("Chatbot: What is the 3rd Car model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: What is the engine size of 3rd Car?" + " \n ")
                print("Chatbot: What is the engine size of 3rd Car?")
                C_input = Check_isEmpty("Chatbot: What is the engine size of 3rd Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: How many Axles are in 3rd Car?" + " \n ")
                print("Chatbot: How many Axles are in 3rd Car?")
                C_input = Check_isEmpty("Chatbot: How many Axles are in 3rd Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

            elif (i > 3):
                write_to_text.write("Chatbot: What is the " + str(j) + "th Car model?" + " \n ")
                print("Chatbot: What is the " + str(j) + "th Car model?")
                C_input = Check_isEmpty("Chatbot: What is the " + str(j) + "th Car model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: What is the engine size of " + str(j) + "th Car?" + " \n ")
                print("Chatbot: What is the engine size of " + str(j) + "th Car?")
                C_input = Check_isEmpty("Chatbot: What is the engine size of " + str(j) + "th Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

                write_to_text.write("Chatbot: How many Axles are in " + str(j) + "th Car?" + " \n ")
                print("Chatbot: How many Axles are in " + str(j) + "th Car?")
                C_input = Check_isEmpty("Chatbot: How many Axles are in " + str(j) + "th Car?", input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")

            j = j + 1
    elif("yes" in C_input.lower() or "y" in C_input.lower()):
        if(Car_Quantity==1):
            write_to_text.write("Chatbot: What model is it?" + " \n ")
            print("Chatbot: What model is it?")
            C_input = Check_isEmpty("Chatbot: What model is it?",input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

            write_to_text.write("Chatbot: What is the engine size of Car?" + " \n ")
            print("Chatbot: What is the engine size of Car?")
            C_input = Check_isEmpty("Chatbot: What is the engine size of Car?", input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

            write_to_text.write("Chatbot: How many Axles are in this Car?" + " \n ")
            print("Chatbot: How many Axles are in this Car?")
            C_input = Check_isEmpty("Chatbot: How many Axles are in this Car?", input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")
        else:
            write_to_text.write("Chatbot: What model are they?" + " \n ")
            print("Chatbot: What model are they?")
            C_input =Check_isEmpty("Chatbot: What model are they?",input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

            write_to_text.write("Chatbot: What is the engine size of These Car?" + " \n ")
            print("Chatbot: What is the engine size of These Car?")
            C_input = Check_isEmpty("Chatbot: What is the engine size of These Car?", input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

            write_to_text.write("Chatbot: Number of Axles per Car?" + " \n ")
            print("Chatbot: Number of Axles per Car?")
            C_input = Check_isEmpty("Chatbot: Number of Axles per Car?", input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

#Starting Point of the Program
write_to_text.write("Chatbot: Hello, Your Full Name Please " + " \n ")
print("Chatbot: Hello, Your Full Name Please")
Customer_Name =Check_isEmpty( "Chatbot: Hello, Your Full Name Please",input("Customer: "))
write_to_text.write("Customer: " + Customer_Name + " \n ")

write_to_text.write("Chatbot: Hi " + Customer_Name + " What\'s the name of your company?" + " \n ")
print("Chatbot: Hi " + Customer_Name + " What\'s the name of your company?")
C_input = Check_isEmpty("Chatbot: Hi " + Customer_Name + " What\'s the name of your company?",input("Customer: "))
write_to_text.write("Customer: " + C_input + " \n ")

write_to_text.write("Chatbot: Do you own Cars?[Yes/No]" + " \n ")
print("Chatbot: Do you own Cars?[Yes/No]")
C_input = Check_isEmpty("Chatbot: Do you own Cars?[Yes/No]",input("Customer: "))
write_to_text.write("Customer: " + C_input + " \n ")
if("no" in C_input.lower() or "n" in C_input.lower()):
    write_to_text.write("Please contact to one of our Colleague For more information "+ " \n ")
    print('Please contact to one of our colleague for more information ')
    write_to_text.close()
    sys.exit()

write_to_text.write("Chatbot: How many Car's brand do you have? (IN NUMBER)" + " \n ")
print("Chatbot: How many Cars's brand do you have? (IN NUMBER)")
C_input =Check_isEmpty("Chatbot: How many Car's brand do you have? (IN NUMBER)", input("Customer: "))
write_to_text.write("Customer: " + C_input + " \n ")
Brand_Quantity = Ask_Question("Chatbot: How many Car's brand do you have? (IN NUMBER only)", C_input)

i = 1

while i <= Brand_Quantity:
    if (i == 1):
        Cars_Information("1st")
    elif (i == 2):
        Cars_Information("2nd")
    elif (i == 3):
        Cars_Information("3rd")
    elif (i > 3):
        Cars_Information(str(i)+"th")
    i = i + 1

print("Chatbot: Thank you very much for your information \n we are now processing your information and \n we will get back to you soon\n until than have a nice day Bye:) ")
write_to_text.write("Chatbot: Thank you very much for your information \n we are now processing your information and \n we will get back to you soon\n until than have a nice day Bye:)  \n ")
write_to_text.close()
