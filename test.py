calucation_to_hours = 24
name_of_the_units = "hours"
def days_to_units(num_of_the_day):
     Condictional_check = num_of_the_day > 0
     print(type(Condictional_check))
     #print(Condictional_check)
     return(f"{num_of_the_day} days are {num_of_the_day * calucation_to_hours} {name_of_the_units}")




def validate_and_execute():

   try:
        user_input_number = int(num_of_the_day_element)
        if user_input_number > 0:
            caluclated_date = days_to_units(user_input_number)
            print(caluclated_date)
        elif user_input_number == 0:
            print("user entered zero")

        else:
             print("you entered a negative, please enter a valid number")
   except:
           print("your input is not valid")

user_input = ""
while user_input != "exit":
    user_input = input("enter the days want to find the seconds\n")
    for num_of_the_day_element in user_input.split(","):
        validate_and_execute()



