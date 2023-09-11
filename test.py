import json

id="1234"
username="noah"
mdp="motdepasse"

#with open("user_mdp.json","r") as file:
#    data=json.load(file)
#
#existe=False
#for user in data:
#    if id ==user:
#        existe=True
#with open("user_mdp.json","w") as file:
#    if existe:
#        print("tu as déjà ton compte pour le modifier fait /account edit")
#    else:
#        data[id]={"username":username,"mdp":mdp}
#        print("voila ton compte et créer")
#    file.write(json.dumps(data))


with open("user_mdp.json","r") as file:
    data=json.load(file)

existe=False
for user in data:
    if id ==user:
        existe=True
with open("user_mdp.json","w") as file:
    del data[id]
    print("voila ton compte est modifier")
    file.write(json.dumps(data))