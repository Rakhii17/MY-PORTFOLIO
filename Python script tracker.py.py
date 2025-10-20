''''introduction''' 
    # Author: [Rakhi]
    # Date: 15-10-2025
# Project: Daily Calorie Tracker

print("Welcome to the Daily Calorie Tracker!")
print("Track your daily food intake  and keep  Track of total calories consumed")

#Task2
a = int(input("enter your number of meals: "))
meals = [ ]
calories = [ ]
for i in range(a):
     print("enter meal name")
     meals.append(input())
     print("enter calories")
     calories.append(int(input()))





#Task3
# Calculate total calories using sum()
total_calories = sum(calories)


# average calories
average_calories = total_calories / a

print("Meal information")
print("Total Calories:", total_calories)
print("Average Calories per Meal:", average_calories)


#task4 
#exceed limit warning system

limit = int(input("Enter your daily calorie limit: "))

if total_calories > limit:
    status =print("exceeded calorie limit.")
elif total_calories < limit:
  status=  print(" within your calorie limit.")
else:
    status=print("  success ,exactly your calorie limit!")
    print("status",status)

#task5 - summary table

 # Meal names and calories
meals = ["Breakfast", "Lunch", "Snack", "Total:", "Average:"]
calories = [350, 600, 150, 1100, 366.67]

# Print header
print("Meal Name\tCalories")
print("---------------------------")

#meals and calorie with tabs for alignment
for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")


#task6
#save the report

save = input("Do you want to save the report? (yes or no): ")

if save == "yes":
    file = open("report.txt", "w")
    file.write("Meal: Breakfast  Calories: " + str("Breakfast") + "\n")
    file.write("Meal: Lunch      Calories: " + str("lunch") + "\n")
    file.write("Meal: Dinner     Calories: " + str("dinner") + "\n")
    file.write("Total Calories: " + str("total") + "\n")
    file.write("Average Calories: " + str("average") + "\n")
    file.write("Status: "  + "\n")
    file.close()
    print("Report saved to 'report.txt'")
else:
    print("Report not saved.")