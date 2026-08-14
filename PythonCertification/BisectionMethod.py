def square_root_bisection(number, tolerance = 1e-5, maximum = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    else:
        low = 0
        if number > 1:
            high = number
        else:
            high = 1
        count = 0
        while low <= high and count <= maximum:
            mid = (high - low) / 2
            root = (high + low ) / 2
            if mid <= tolerance:
                print(f"The square root of {number} is approximately {root}")
                return root
            elif root**2 > number:
                high = root
            elif root**2 < number:
                low = root
            count += 1
    if mid == root:
        print(f"The square root of {number} is approximately {root}")
        return root
    print(f"Failed to converge within {maximum} iterations")
    return None

