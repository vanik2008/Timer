t time
def start_stopwatch():
    start_time = time.time()
    input("Stopwatch started. Press enter to stop")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

print("Welcome to this Python Stopwatch")
while True:
    print("\nOption:")
    print("1. Start Stopwatch")
    print("2. Exit")

    choice = input("Enter your choice (1-2):")

    if choice == '1':
        print(f"Elapsed Time: {start_stopwatch()}")
    elif choice == '2':
        print("Exiting the stopwatch. Goodbye!")
        break
    else:
        print("Invalid choice . Please enter 1 or 2")