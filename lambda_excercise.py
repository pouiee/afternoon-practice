# Lambda Exercise 1

# Consider the List

prog_lang = [('Python', 3.8),
             ('Java', 13),
             ('JavaScript', 2019),
             ('Scala', 2.13)]

# 1. Sort the list by each language's version in ascending order.
# [('Scala', 2.13), ('Python', 3.8), ('Java', 13), ('JavaScript', 2019)]

prog_lang1 = sorted(prog_lang, key=lambda x: x[1])
print(prog_lang1)

# 2. Sort the list by the length of the name of each language in descending order.
# [('JavaScript', 2019), ('Python', 3.8), ('Scala', 2.13), ('Java', 13)]

prog_lang2 = sorted(prog_lang, key=lambda x: len(x[0]), reverse=True)
print(prog_lang2)

# 3. Filter the list so that it only contains languages with 'a' in it.
# [('Java', 13), ('JavaScript', 2019), ('Scala', 2.13)]

prog_lang3 = list(filter(lambda x: 'a' in x[0], prog_lang))
print(prog_lang3)

# 4. Filter the list so that it only contains languages whose version is in integer form.
# [('Java', 13), ('JavaScript', 2019)]

prog_lang4 = list(filter(lambda x: type(x[1]) == int, prog_lang))
print(prog_lang4)

# 5. Transform the list so that it contains the tuples in the form,
# ("language in all lower case", length of the language string)
# [('python', 6), ('java', 4), ('javascript', 10), ('scala', 5)]

prog_lang5 = list(map(lambda x: (x[0].lower(), len(x[0])), prog_lang))
print(prog_lang5)

# 6. Generate a tuple in the form,
# ("All languages separated by commas","All versions separated by commas")
# ('Python,Java,JavaScript,Scala', '3.8,13,2019,2.13')

languages = ','.join(tuple(map(lambda x: x[0], prog_lang)))
versions = ','.join(tuple(map(lambda x: str(x[1]), prog_lang)))
print(tuple((languages, versions)))
