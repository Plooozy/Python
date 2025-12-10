def search(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

def answer(result):
    if result == -1:
        print("Number does not exist")
    else:
        print(f"Number's index is - {result}")

def input_x():
    while True:
        user_input = input("Enter an integer: ")
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    x = input_x()
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    result = search(arr, x)
    answer(result)

if __name__ == "__main__":
    main()