#!/bin/bash

# Script que manipula um arquivo de texto
# Funções:
#			Inserir usuário
#			Remover Usuário
#			Mostrar usuário

# O arquivo é separado por dois pontos, então temos
# uma variável que define o separador
sep=:

# um arquivo temporário será utilizado para operação de apagar registro
temp=temp.$$

# o arquivo do banco deve está definido
[ "$banco" ] || {
	echo "A base de dados não foi encontrada."
	echo "Defina utilizando a variável banco."
	return 1
}

# o nome de usuário é único (chave), temos que ter uma função para
# verificar se o nome de usuário já existe
existe_nome() {
	# utilizamos o grep que tenta encontrar um nome de usuário
	# o -i ignora case-sensitive, ou seja, marcos e MARCOS é a mesma coisa
	# o -q faz uma pesquisa silenciosa no banco
	# o circunflexo indica para casar algo que comece com $1$sep
	# $1 é o argumento passado e $sep é o separador definido no começo do script
	# exemplo: que comece (^) com "marcos:"
	# a pesquisa é feita no arquivo que foi definido na variável $banco
	grep -i -q "^$1$sep" "$banco"
}

# função para inserir um usuário, insere registro $* no banco
inserir_usuario() {
	# redireciona a saída do echo para o comando cut
	# o echo tem como entrada $1 que são os dados do usuário
	# exemplo de dados: joao:joao@gmail.com:python
	# o cut separa esss dados pelo separados ($sep) pegando apenas o primeiro campo
	# o primeiro campo é o nome de usuário para testarmos se já existe
	local nome=$(echo "$1" | cut -d $sep -f1)

	# verifica se o nome já existe
	if existe_nome "$nome"; then
		echo "O nome de usuário \"$nome\" já existe..."
		return 1
	else
		# se não existe, então grava no banco
		# >> adiciona ao final
		echo "$*" >> "$banco"
		echo "Usuário \"$nome\" cadastrado com sucesso!"
	fi
	return 0
}

# função para apagar um usuário
# apaga passando o nome de usuário (chave) contido em $1
apagar_usuario() {
	# verifica se existe o nome de usuário passado
	existe_nome "$1" || return

	# se chegou aqui é porque existe o nome

	# o grep com -v pega tudo exceto o que casou
	# redireciona os dados para um arquivo temporário
	grep -i -v "^$1$sep" "$banco" > "$temp"
	# depois que apagou, basta mover para regravar
	mv "$temp" "$banco"
	echo "Usuário \"$1\" removido com sucesso!"
}


# função para obter os nomes de cada campo
obter_campos() {
	# os nomes dos campos estão na primeira linha,
	# por isso é utilizado o "head - n 1" para pegar
	# a primeira linha do arquivo, a saída é redirecionada
	# para o comando "tr" que substitui o separador ($sep)
	# por um "\n" (nova linha) para mostrar um campo em cada linha
	head -n 1 "$banco" | tr $sep \\n
}

# função para mostrar os dados de um determinado usuário
# pelo nome de usuário que está contido em $1
mostrar_usuario() {
	# pega os dados de um determinado usuário
	# -i ignora o case-sensitive
	local usuario=$(grep -i "^$1$sep" "$banco")

	# verifica se achou algo
	[ "$usuario" ] || return

	# se chegou aqui é porque existe o usuario

	# variável que representa o índice de cada campo
	local i=0

	# loop para mostrar os dados de cada campo
	obter_campos | while read campo; do
		i=$((i+1)) # incrementa o índice do campo

		# mostra o nome do campo, -n evita de pular uma linha
		echo -n "$campo: "

		# mostra o conteúdo de cada campo
		# o delimitador do "cut" é o $sep
		# -f serve para mostrar um determinado camppo
		# o índice do campo que irá ser exibido está definido em $i
		echo "$usuario" | cut -d $sep -f $i
	done


}