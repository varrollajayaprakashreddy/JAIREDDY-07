def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Remove common letters
    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    count = len(name1) + len(name2)
    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames.pop()

    return flames[0]


# User input
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")
git init
git add flames.py
git commit -m "Added FLAMES game script"
git branch -M main
git remote add origin https://github.com/your-username/your-repo.git
git push -u origin main
