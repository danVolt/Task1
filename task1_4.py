sample={'physics': 88,  'maths': 75,  'chemistry' : 72,'Basic electrical' : 89}
x=min(sample.values())
y=[key for key in sample if sample[key] == x]
print(str(y))