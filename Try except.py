while True:
    try:
        number = int(input("Enter a number: "))
        print(number)
        end = input("To quit the program press q, otherwise press any other key : ")
        if end == 'q':
            break
    except ValueError:
        print("Invalid Input")
