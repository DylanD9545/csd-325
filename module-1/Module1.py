
def countdown_bottles(num_bottles):
    while num_bottles > 0:
        if num_bottles > 1:
            print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
            print("Take one down, pass it around,")
            num_bottles -= 1
            print(f"{num_bottles} bottles of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around,")
            num_bottles -= 1
            print("No more bottles of beer on the wall.\n")

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 100 bottles of beer on the wall.")

def main():
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles < 0:
                print("Please enter a non-negative number.")
            else:
                countdown_bottles(bottles)
                break  # Exit the loop after successful countdown
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()