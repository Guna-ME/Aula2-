# Sintaxe de uma lista(array) em python;
minhaLista = ["Maduh", "Vitor", "Hanna"]
print(minhaLista)

# Acesso ao item por posição;
print(minhaLista[0])

# Acesso indexado negativo por posição;
print(minhaLista[-1])

# Intervalo entre itens (não mostra o ultimo item);
print(minhaLista[1:3])
# intervalo sem o item inicial;
print(minhaLista[:2])
# Intervalo sem o item final
print(minhaLista[0:])

# Intervalo de itens indexação negativa;
print(minhaLista[-1:-3])

# Alterar valor de um item na lista;
minhaLista[2] = "Evelyn"
print(minhaLista)

# Percorer lista;
for i in minhaLista: 
    print(i)

# Verificar se o item está na lista;
if "Vitor" in minhaLista:
    print("Sim,está!")
else:
    print("Não está!")

# Ver tamanho/quantidade de itens da lista;
print(len(minhaLista))

# Adiciona item no final da lista;
minhaLista.append("Eduarda")
print(minhaLista)

# Adiciona item na posição escolhida;
minhaLista.insert(1,"Francine")
print(minhaLista)

# Remover item especifico da lista;
minhaLista.remove("Vitor")
print(minhaLista)

# Remove o índice especifico da lista;
minhaLista.pop(0)
print(minhaLista)

# Remove um item da lista(sem o colchetes deleta a lista toda);
del minhaLista[1]

# Esvazia a lista, mas não a exclui;
minhaLista.clear()
print(minhaLista)

# Adiciona novos itens a lista;
minhaLista.insert(0,"Maduh")
minhaLista.insert(1,"Vitor")
minhaLista.insert(2,"Hanna")
minhaLista.insert(3,"Evelyn")
print(minhaLista)

# Copia de uma lista para outra;
minhaSegundaLista = minhaLista.copy()
print(minhaSegundaLista)

minhaTerceiraLista = list(minhaSegundaLista)
print(minhaTerceiraLista)

# Ver quantas vezes um item se repete;
print(minhaTerceiraLista.count("Maduh"))

# Juntar listas com operadores aritimeticos;
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print(minhaQuartaLista)

# Buscar posição por item;
print(minhaQuartaLista.index("Vitor"))