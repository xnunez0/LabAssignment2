"""
satrt the program
get the numbers of sheets
sheets / 5 
round answer to next number 
output the result to the user 
end the program
"""
def calculate(sheet):
    answer = sheet / 5 
    rounded = round(answer)
    print("sheet is : ", sheet)
    print("the answer is: ", answer)
    print("rounded is: ", rounded)
    print("======================================")
    return rounded 

output = calculate(16)

print("the return statement is: ", output)
