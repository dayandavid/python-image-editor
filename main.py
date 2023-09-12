import image_tools

exit = False
while not exit:
    options = ("1. Converter", "2. Compress", "3. Resize")

    [print(item) for item in options]

    selection = int(input("Choose an option: "))

    print(f"{options[selection]} selected!")
