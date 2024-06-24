def manage_numbers():
    nums = []

    for i in range(3):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)
    
    while nums:
        print(f"Display Numbers: {nums}")
        q = int(input("Is the boss here? Enter 0 if Wala, 1 for Naa: "))

        if q == 0:
            nums.pop()
        elif q == 1:
            nums.pop(0)
        else:
            print("Invalid input!")      
    print("No numbers left.")

manage_numbers()