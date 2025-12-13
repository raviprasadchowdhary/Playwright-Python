# While loop

# This is an example of a while loop
# Here we count down from 5 to 1 and print each number
# if the condition is no longer true, the loop exits
# then print a message when the loop is exited
i = 5
while i > 0:
    print(i)
    i -= 1
print("While loop exited")
# Output:
# 5
# 4
# 3
# 2
# 1
# While loop exited
# Note: Be careful with while loops to avoid infinite loops
# An infinite loop occurs when the condition never becomes false
# For example, the following code will create an infinite loop
# Uncomment the code below to see the infinite loop in action
# i = 5
# while i>0:
#     print(i)
# In this case, 'i' is never decremented, so the condition 'i>0' is always true
# To stop an infinite loop, you can usually press Ctrl+C in the terminal or stop the execution in your IDE
# Always ensure that the loop has a way to exit by modifying the condition variable within the loop
# To avoid infinite loops, make sure to update the loop variable appropriately within the loop body
# For example, in the first while loop, we decremented 'i' by 1 in each iteration
# This ensures that eventually 'i' will no longer be greater than 0, and the loop will exit
# Always test your while loops to ensure they behave as expected
# and do not run indefinitely unless that is the intended behavior.
# You can also use break statements to exit a while loop prematurely
# For example:
j = 5
while j > 0:
    print(j)
    if j == 3:
        print("Breaking the loop at j =", j)
        break
    j -= 1
# Output:
# 5
# 4
# 3
# Breaking the loop at j = 3
# In this example, the loop will exit when j equals 3 due to the break statement
# This is another way to control the flow of a while loop
# Remember to always ensure that your while loops have a clear exit strategy to prevent unintended infinite loops in your programs.

# You can also use the 'continue' statement to skip the current iteration and move to the next one
k = 5
while k > 0:
    k -= 1
    if k == 2:
        print("Skipping the number", k)
        continue
    print(k)
# Output:
# 4
# 3
# Skipping the number 2
# 1
# 0
# In this example, when k equals 2, the continue statement is executed
# This causes the loop to skip the print statement for that iteration
# and move to the next iteration of the loop
# This is useful when you want to skip certain values or conditions within a loop
# Always use while loops judiciously and ensure they have a clear purpose in your code
# They are powerful tools for repeating actions until a certain condition is met.
# Practice using while loops to become more comfortable with their syntax and behavior
# Experiment with different conditions and loop bodies to see how they affect the flow of your program
