def create_phone_number(n):
    n1 = num_to_string(n,0,3)
    n2 = num_to_string(n,3,6)
    n3 = num_to_string(n,6,10)
    return f"({n1}) {n2}-{n3}"

def num_to_string(numbers,start,end):
    return"".join(str(num) for num in numbers[start:end])

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")