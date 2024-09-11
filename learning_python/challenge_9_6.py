captains = {}
print(f"1: captains = {captains}")

captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'
print(f"2: captains = {captains}")

if 'Enterprise' in captains:
    print(f"Enterprise is in captains")
else:
    captains['Enterprise'] = 'unknown'

if 'Discovery' in captains:
    print(f"Discovery is in captains")
else:
    captains['Discovery'] = 'unknown'
print(f"3: captains = {captains}")

for key, value in captains.items():
    print(f"The {key} is captained by {value}.")

del captains['Discovery']
print(f"5: captains = {captains}")

contents = (
        ('Enterprise', 'Picard'),
        ('Voyager', 'Janeway'),
        ('Defiant', 'Sisko')
    )
print(f"6: {contents}")
new_captains = dict(contents)
print(f"6: {new_captains}")


