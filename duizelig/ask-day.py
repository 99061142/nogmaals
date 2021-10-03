days = ["ma", "di", "wo", "do", "vr", "za", "zo"]


chosen_day = input("kies een dag, er is keuze tussen 'ma', 'di', 'wo', 'do', 'vr', 'za' en 'zo': ")


num = 0


while chosen_day != days[num]:
    print(days[num])
    num += 1
else:
    print(chosen_day)