import time as t

hourly_wage = float(input("Enter your hourly salary: " ))
start_time = input("Enter your start time (XX:XX): ")
end_time = input("Enter your end time (XX:XX): ")
unpaid_breaks = float(input("Enter the total duration of your unpaid breaks (in hours): "))

if input("Are you midway through work? (Y/N): ") == "Y":
    current_time = input("Enter the current time (XX:XX): ")
    current_time = current_time.replace(":","")
    payment = current_time - start_time
else:
    payment = 0



minute_wage = hourly_wage / 60

start_time = float(start_time.replace(":",""))
end_time = float(end_time.replace(":",""))

total_hours_worked = (end_time - start_time - unpaid_breaks) / 100
total_minutes_worked = total_hours_worked * 60
total_wage = total_hours_worked * hourly_wage

print("----------","\nTotal possible earnings: ",total_wage,"\nTotal earnings so far: ", payment)

while total_minutes_worked > 0:
    t.sleep(5)

    payment += minute_wage

    print("----------","\nTotal possible earnings: ",total_wage, "\nTotal earnings so far: ", payment, "\nYou will work for ", total_minutes_worked/60, " more hours")

print("\n----------", "\nYou have made a total of: ", payment)


