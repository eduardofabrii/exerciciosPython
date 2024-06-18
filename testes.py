strings = []
filtered_strings = []

n = int(input("Quantas strings você deseja inserir? "))

for i in range(n):
    string = input("Digite a string: ")
    strings.append(string)

for string in strings:
    if len(string) < 5:
        filtered_strings.append(string)

print(filtered_strings)
