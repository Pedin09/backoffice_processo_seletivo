import json, requests
from validacpf import ValidaCpf

link = 'https://storage.googleapis.com/raccoon-humane/psel.json'
res = requests.get(url=link)
print(res)
resdt = json.loads(res.text)
arquivo = open ('dados.json', 'w', encoding='utf8')

def validadados(resdt):
    resdtmod = resdt
    for i in resdtmod: 
        cpf = ValidaCpf(i['cpf'])
        resdtmod = resdt
        cargo = i['cargo']
        salario = i['salario']
    
        if cpf.valida():
            i['cpf_validado'] = True 

        else: 
            i['cpf_validado'] = False     
             
        if cargo == 'Assassin':
            i['adicional_insalubridade'] = round(salario*0.5,2)
        elif cargo == 'Batman':
            i['adicional_insalubridade'] = round(salario*0.10,2) 
        elif cargo == 'Butler':
            i['adicional_insalubridade'] = round(salario*0,2) 
        elif cargo == 'Side Kick':
            i['adicional_insalubridade'] = round(salario*0.15,2) 
        elif cargo == 'The Chief Demon':
            i['adicional_insalubridade'] = round(salario*0.125,2) 
        
    resdtmod.extend(i)
    return resdtmod


            
resdtmod = validadados(resdt)

json.dump(resdtmod, arquivo, ensure_ascii=False, indent= 6)

print(resdtmod) 
