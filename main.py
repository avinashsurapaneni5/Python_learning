calucalationtoseconds = 24*60*60





def days_to_seconds(days):
 
 #x = days * calucalationtoseconds

 return(f"days are in days{days * calucalationtoseconds}seconds")


user_input = int(input("enter the days want to find the seconds\n"))

my_var = days_to_seconds(user_input)

print(my_var)



