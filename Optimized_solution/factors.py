def optimal_solution(n):
    result = []
    i = 1
    while i*i <= n:
        print("Starting:", i, i*i)
        if n % i == 0:
            print("The n % i: ", n % i)
            result.append(i)
            if n // i != i:
                print("Multiply wala: ", n//i)
                result.append(n//i)
        i += 1
    result = sorted(result)
    return result

n = 6
print(optimal_solution(n))