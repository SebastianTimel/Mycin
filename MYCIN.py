import pymongo

import numpy as np
import matplotlib.pyplot as plt

client = pymongo.MongoClient(
    "mongodb+srv://agudelo:4GtqVE2seziuZaBk@cluster0-wwcjq.mongodb.net/diseases?retryWrites=true&w=majority")
db = client.blanda
consulta = db.consultas
regla = db.reglas
hecho = db.hechos

sintomas = []
tabla = {
    '25': 0,
    '26': 0,
    '27': 0,
    '28': 0,
    '29': 0,
    '30': 0,
}


def tipo(var, dic):
    cont = 0
    consec = var['consecuente']
    ponde = var['ponderacion']

    r = isinstance(consec, list)
    if r == True:
        for i in consec:
            m = str(int(i))
            dic[m] = dic[m]+(1-dic[m])*ponde[cont]
            cont += 1
    else:
        m = str(int(consec))
        dic[m] = dic[m]+(1-dic[m])*ponde


print("\nBIENVENIDO")
print("\nSintomas detectables por el sistema")
cont = 1
for i in hecho.find({'id': {"$lt": 25}}):
    print(str(cont)+". " + i['descripcion'])
    cont += 1	

inp = input("\nDe los anteriores sintomas, por favor ingrese los numeros correspondientes (con una , intermedia) a los sintomas que esta presentando: ")
sintomas = inp.split(",")
for i in sintomas:
    for k in regla.find({"antecedente": float(i)}):
        tipo(k, tabla)

enfermedad = tabla.items()
elec1 = 0  # ponderacion
elec2 = 0  # enfermedad
for num, pon in enfermedad:
    if pon > elec1:
        elec1 = pon
        elec2 = num
for i in hecho.find({"id": float(elec2)}):
    res = i['descripcion']
    print(res)


	

"""
x = np.array(["Dengue", "Bronquitis", "Laringitis",
              "Gripa", "Varicela")
lista = [tabla[key] for key in tabla]
y = np.array(lista)

plt.bar(x, y, align="center")
plt.show()
print("+++")
print(tabla['25'])
print(tabla['26'])
print(tabla['27'])
print(tabla['28'])
print(tabla['29'])
print(tabla['30'])
print("+++")


'''
print('Bienvenido a su diagnosticador medico')
print('Posee usted alguno de estos sintomas?')

print('1.Tos  2.Fiebre  3.Malestar  4.Dolor de cabeza  5.Vomito  6.Dolor estomacal')
print('Si posee uno o mas sintomas, digite sus respectivos numeros')


	

enfermedades(colesterol):-colesterol,!.
enfermedades(diabete):-diabete,!.
enfermedades(gastritis):-gastritis,!.
enfermedades('sin resultado').

colesterol :- tiene_colesterol,
pregunta('tiene inchazon en alguna extremidad del cuerpo?'),
pregunta('tiene perdida de equilibrio'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t').


diabete :- tiene_diabete,
pregunta('padece de orinar con frecuencia'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t').

gastritis :- tiene_gastritis,
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t'),
pregunta('t').


desconocido :- se_deconoce_enfermedad.

tiene_colesterol:- pregunta('t'),!.
tiene_diabete:- pregunta('t'),!.
tiene_gastritis:- pregunta('t'),!.

:-dynamic si/1,no/1.

preguntar(Problema):- new(Di,dialog('exa')),
new(L2,label(texto,'Responde las siguientes preguntas')),
new(La,label(prob,Problema)),

new(B1,button(si,and(message(Di,return,si)))),
new(B2,button(no,and(message(Di,return,no)))),

	send(Di,append(L2)),
send(Di,append(La)),
send(Di,append(B1)),
send(Di,append(B2)),

	send(Di,default_button,si),
send(Di,open_centered),get(Di,confirm,Answer),
write(Answer),send(Di,destroy),

	((Answer==si)->assert(si(Problema));
assert(no(Problema)),fail).
pregunta(S):-(si(S)>true; (no(S)>fail; preguntar(S))).
limpiar :- retract(si(_)),fail.
limpiar :- retract(no(_)),fail.
limpiar.

botones :- lim,
send(@boton,free),
send(@btncarrera,free),
enfermedades(Enfer),
send(@texto, selection('su diagnostico es: ')),

send(@respl, selection(Enfer)),
new(@boton, button('inicia',message(@prolog,botones))),
send(Menu, display,@boton,point(40,50)),
send(Menu, display,@btncarrera,point(20,50)),
limpiar.
lim:- send(@respl, selection('')).

'''