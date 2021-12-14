with open("input.txt", "r") as f:
    initial_seq = f.readline().strip()
    polymer_template = dict()
    for i in f:
        if i != "\n":
            key, value = i.strip().split("->")
            polymer_template[key.strip()] = value.strip()

freq = {i: initial_seq.count(i) for i in polymer_template.keys()}

for i in range(40):
    temp = freq.copy()
    for pair, frequency in freq.items():
        if freq[pair] > 0:
            temp[pair] -= frequency
            temp[pair[0] + polymer_template[pair]] += frequency
            temp[polymer_template[pair] + pair[1]] += frequency
    freq = temp

letters = {x: 0 for x in set(''.join(freq.keys()))}

for pair, frequency in freq.items():
    letters[pair[0]] += frequency/2
    letters[pair[1]] += frequency/2

print(int(max(letters.values()) - min(letters.values()))+1)
