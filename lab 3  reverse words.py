messange = str(input("Введіт текст: "))
n_messange = ""
for i in messange[::-1]:
    n_messange += i
print("Текст навпаки: ", n_messange)
input("\n\nEnter.")