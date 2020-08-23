requests
json
        
def cnpj():
    print("\n"+17*"="+"CONSULTA CNPJ"+16*"=")
    while True:
        cnpjI = input("\nDigite o cnpj: ")
        local = "https://www.receitaws.com.br/v1/cnpj/"+cnpjI
        obj_url = requests.get(local, headers={"chave-api-dados": "8c2190bf68ad4f00a4bcbf60df1fe44f"})
        cnpj = obj_url.json()
        n = 0
        print (f"""\033[1;32m\nCNPJ CONSULTADO COM SUCESSO!\033[1;97m
    
    Atividade principal:
    
    {cnpj["atividade_principal"][0]["text"]}
    
    Data situação: {cnpj["data_situacao"]}
    Tipo: {cnpj["tipo"]}
    Nome: {cnpj["nome"]}
    Email: {cnpj["email"]}
    
    Atividades secundárias:
        
    """)
        atn = 0
        for at in cnpj["atividades_secundarias"]:
            atn +=1
            print (f"Atividade {atn}: ",at["text"])
        print("\nSócias:\n\n")
        for c in cnpj["qsa"]:
            n += 1
            print( "Sócia:",n,"\nCargo: ",c["qual"])
            print( "Nome: ", c["nome"],"\n")
        print(f'''Situação: {cnpj["situacao"]}
Bairro: {cnpj["bairro"]}
Número: {cnpj["numero"]}
Cep: {cnpj["cep"]}
Município: {cnpj["municipio"]}
Nome fantasia: {cnpj["fantasia"]}
Porte: {cnpj["porte"]}
Abertura: {cnpj["abertura"]}
Natureza jurídica: {cnpj["natureza_juridica"]}
Uf: {cnpj["uf"]}
Cnpj: {cnpj["cnpj"]}
Ultima atualização: {cnpj["ultima_atualizacao"]}
Status: {cnpj["status"]}
Complemento: {cnpj["complemento"]}
Efr: {cnpj["efr"]}
Motivo situação: {cnpj["motivo_situacao"]}
Situação especial: {cnpj["situacao_especial"]}
Data de situação especial: {cnpj["data_situacao_especial"]}
Capital social: {cnpj["capital_social"]}
Extra: {cnpj["extra"]}
Billing: {cnpj["billing"]}''')
