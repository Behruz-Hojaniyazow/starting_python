def products():
    fruits = []
    name = input("Please enter your name: ")
    print(f"\n---Welcome {name.title()}!, Enter the fruits which you need---\n")
    while True:
        print("Type 'stop' to finish")
        fruit = input("Enter a fruit: ")
        if fruit.lower() == 'stop':
            break
        fruits.append(fruit)
    if fruits:
        filename = "fruit_data.txt"
        with open(filename, 'w', encoding = 'utf-8') as file:
            file.write("You bought these fruits\n")
            for fruit in fruits:
                file.write(f"{fruit.title()}\n")
        print(f"{len(fruits)} fruits were successfully added to the 'fruit_data.txt' file")
    else:
        print("No info entered")
if __name__ == "__main__":
    products()
    
def component_reader():
    """a function that reads the infos from 'fruit_data.txt' """
    filename = 'fruit_data.txt'
    name = input("Enter your name: ")
    print(f"\n---{name.title()} Welcome!---")
    try:
        with open (filename, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            if lines:
                print(f"{len(lines)} products were found")
                for index, line in enumerate(lines, start=1):
                    clean_line = line.strip()
                    print(f"{index}. {clean_line}")
            else:
                print("The file is empty")
    except FileNotFoundError:
        print(f"The file {filename} was not found, Please run the Writer first")
if __name__ == "__main__":
    component_reader()