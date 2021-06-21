import json 
def main():
    print("teste")


d={"Nome":"Michael", "Idade":"23"}
d['cpf']= 1360
print(json.dumps(d))

#for key in d:
    #print (key + " " + d[key])