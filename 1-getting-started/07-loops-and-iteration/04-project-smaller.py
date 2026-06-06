smaller = None

for i in [21,32,13,432,44,11,2,1] :

    if smaller is None :
        smaller = i

    elif i < smaller :
        smaller = i

    print(f"{smaller} - {i}")

print(f"o menor é: {smaller}")
