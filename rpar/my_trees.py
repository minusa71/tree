import os


def read_file(path):
    f = open(path, "r")
    # print(f.read())
    f.close()
    os.startfile("apple.jpeg")
    f = open(path, "r")
    text = list()
    for element in f.read().split("\n"):
        text.append(element)
    for index in range(len(text) - 1):
        print(f"{index} - {text[index]}")
    f.close()
    print(f"Number of plants: {len(text) - 1}")


def write_file(path):
    f = open(path, "r")
    text = list()
    for element in f.read():
        text.append(element)
    print("".join(text))
    f.close()
    print("Enter new element:")
    text.append(input())
    text.append("\n")
    f = open(path, "w")
    f.write("".join(map(str, text)))
    f.close()


def search(path):
    f = open(path, "r")
    text = list()
    for element in f.read().split("\n"):
        text.append(element)
    f.close()
    print("Enter element for search:")
    fnd_element = input()
    filtered_text = []
    for el in text:
        if fnd_element in el:
            filtered_text.append(el)
            filtered_text.append("\n")
    print("".join(filtered_text))


print("\n  1 - See content \n  2 - Modify content \n  3 - Search content \n")
print("Enter your choice:", end=" ")
choice = input()
if choice == "1":
    read_file("fruit_tree.txt")
elif choice == "2":
    write_file("fruit_tree.txt")
elif choice == "3":
    search("fruit_tree.txt")
else:
    print("Enter the correct choice!")
