def extract_full_names(people):

    names = [(f"{person['first']} {person['last']}") for person in people]
    print(names)

names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
    ]

extract_full_names(names)
        # ['Ada Lovelace', 'Grace Hopper']
