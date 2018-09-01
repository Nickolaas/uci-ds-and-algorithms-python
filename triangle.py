# name: Nickolas Decker
# email: deckernickolas@gmail.com
# problem: triangle

# define the recursive function triangle after this comment

def triangle(n):
    if n == 1:
        return '*'
    result = triangle(n-1)
    result = result + "\n" + '*'*n
    return result

def main_test():
    tests = [0, '*', '*\n**', '*\n**\n***', '*\n**\n***\n****', '*\n**\n***\n****\n*****',
        '*\n**\n***\n****\n*****\n******', '*\n**\n***\n****\n*****\n******\n*******',
        '*\n**\n***\n****\n*****\n******\n*******\n********',
        '*\n**\n***\n****\n*****\n******\n*******\n********\n*********',
        '*\n**\n***\n****\n*****\n******\n*******\n********\n*********\n**********']
    errors = 0
    for n in range(1,len(tests)):
        student = triangle(n)
        if student[0] == '\n':
            student = student[1:] # trim off starting \n
        correct = tests[n]
        if student != correct:
            print("test n = ", n)
            print("-"*20)
            print(f"FAILED triangle({n})")
            print("Your triangle is:", repr(student))
            print(student)
            print()
            print("Test was expecting:", repr(correct))
            print(correct)
            errors += 1
    if errors == 0:
        print("All Passed")
    else:
        print("-"*20)
        print(f"\n\nFAILED {errors} TESTS")


if __name__ == '__main__':
main_test()