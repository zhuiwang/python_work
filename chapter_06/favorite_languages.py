favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

name_list = ['jen', 'sarah', 'hes']

for name in name_list:
    if name in favorite_languages.keys():
        print('Thanks for ' + name + ' accept!')
    else:
        print('invite ' + name + ' to have diaocha')
