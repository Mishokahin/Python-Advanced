def age_assignment(*names, **ages):
    name_ages = {}
    for letter, age in ages.items():
        for name in names:
            if name.startswith(letter):
                name_ages[name] = age

    return "\n".join(f"{n} is {a} years old." for n, a in sorted(name_ages.items(), key=lambda x: (x[0])))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))