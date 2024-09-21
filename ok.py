# Write code here
chemical_map = defaultdict(int)

for chemical in input2:
    if isinstance(chemical, str):
        sorted_chemical = ''.join(sorted(chemical))
    chemical_map[sorted_chemical] += 1

explosive_pairs = 0
for count in chemical_map.values():
    if count > 1:
        explosive_pairs += (count * (count - 1)) // 2
        return explosive_pairs


