def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def test(c1, c2):
    thirdpair_template = list(set(c1+c2))
    thirdpair_template.remove(find_duplicates(c1+c2)[0])
    return thirdpair_template

print(test([1,7],[7,8]))
