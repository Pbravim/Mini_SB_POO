#----------------------------FUNÇÕES------------------------------
#=================================================CLIENTE=================================================
class Cliente:
    def __init__(self, nome, cpf, salario, financiamentos):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._financiamentos = financiamentos

    #Get
    @property
    def nome (self):
        return self._nome
        
    @property
    def cpf (self):
        return self._cpf

    @property
    def salario (self):
        return self._salario
            
    @property
    def financiamentos (self):
        return self._financiamentos

    #Set
    @nome.setter
    def nome(self, novo):
        self._nome = novo

    @cpf.setter
    def cpf (self, novo):
        self._cpf = novo

    @salario.setter
    def salario(self, novo):
        self.salario = novo

    @financiamentos.setter
    def financiamentos (self, novo):
        self._financiamentos = novo

    def total_financiado(self):
        if conacesso == conta1._id:
            a=sum(cliente1._financiamentos)
            print(f'\nAqui está a soma de todos os financiamentos: {a}')
        elif conacesso ==conta2._id:
            b=sum(cliente2.financiamentos)
            print(f'\nAqui está a soma de todos os financiamentos: {b}')

    #MÉTODO ADICIONAL 1#
    def comparar_salario(self):
        if cliente1._salario >= cliente2._salario:
            diferenca_salario = cliente1._salario - cliente2._salario
        elif cliente2._salario >= cliente1._salario:
            diferenca_salario = cliente2._salario - cliente1._salario
        print(f'{cliente1._nome} - Conta {conta1._id}: {cliente1._salario}\n{cliente2._nome} - Conta {conta2._id}: {cliente2._salario}\nDiferença do salário: {diferenca_salario}')

#=================================================CONTA=================================================
class Conta:
    def __init__(self, saldo, id, cliente):
        self._saldo = saldo
        self._id = id
        self._cliente = cliente

    #Get
    @property
    def saldo (self):
        return self._saldo
        
    @property
    def id (self):
        return self._id

    @property
    def cliente (self):
        return self._cliente

    #Set
    @saldo.setter
    def saldo (self, novo):
        self._saldo = novo
        
    @id.setter
    def id (self, novo):
        self._id = novo

    @cliente.setter
    def cliente (self, novo):
        self._cliente = novo

    def creditar(self, valor):
        self._saldo += valor
        print(f'Você adicionou {valor}, seu saldo atual é {self._saldo}')
  
    def debitar(self, valor):
        if self._id == conta1._id:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f'Você retirou {valor}, seu saldo atual é {self._saldo}')
                return True

            else:
                print(f"Você não tem saldo o suficiente.")
                return False

        elif self._id == conta2._id:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f'Você retirou {valor}, seu saldo atual é {self._saldo}')
                return True

            else:
                print(f"Você não tem saldo o suficiente.")
                return False
        
    def transferencia(self, valor, outra_conta):
        if self._id == conta1._id:
            if valor <= conta1._saldo:
                conta1.debitar(valor)
                conta2.creditar(valor)
                print(f'Você transferiu {valor} para a Conta {outra_conta}\nSaldo Atual {self._saldo}')
                return True

            else:
                return False
        
        if self._id == conta2._id:
            if valor <= conta2._saldo:
                conta2.debitar(valor)
                conta1.creditar(valor)
                print(f'Você transferiu {valor} para a Conta {outra_conta}\nSaldo Atual {self._saldo}')
                return True

            else:
                return False

#=================================================BANCO=================================================
class Banco:
    def __init__(self, nome_do_banco, contas = [], financiamentos=[]):
        self._nome_do_banco = nome_do_banco
        self._contas = contas
        self._financiamentos = financiamentos
    
    #Get
    @property
    def nome_do_banco (self):
        return self._nome_do_banco
        
    @property
    def contas (self):
        return self._contas

    @property
    def financiamentos (self):
        return self._financiamentos

    #Set
    @nome_do_banco.setter
    def nome_do_banco (self, novo):
        self._nome_do_banco = novo

    @contas.setter
    def contas (self, novo):
        self._contas = novo

    @financiamentos.setter
    def financiamentos (self, novo):
        self._financiamentos = novo

     #TOTAL VALOR CONTAS#
    def total_valor_contas(self):
        saldo_total = conta1._saldo + conta2._saldo
        print(f'Este é o Saldo de todas as contas somadas: {saldo_total}')

    #FINANCIAMENTOS CLIENTE#
    def financiamentos_cliente(self, cpf):
        if _cpf == "10987654321":
            print(cliente1._financiamentos)
        elif _cpf == '12345678910':
            print(cliente2._financiamentos)
        
#=================================================IMOVEL================================================
class Imovel:
    def __init__(self, tipo, valor_imovel, codigo):
        self._tipo = tipo
        self._valor_imovel = valor_imovel
        self._codigo = codigo

    #Get
    @property
    def tipo (self):
        return self._tipo

    @property
    def valor_imovel (self):
        return self._valor_imovel

    @property
    def codigo (self):
        return self._codigo

    #Set
    @tipo.setter
    def tipo (self, novo):
        self._tipo = novo

    @valor_imovel.setter
    def valor_imovel (self, novo):
        self._valor_imovel = novo
    
    @codigo.setter
    def codigo (self, novo):
        self._codigo = novo

    #MÉTODO ADICIONAL 2#
    def comparar_imovel(self):
        if imovel1._valor_imovel >= imovel2._valor_imovel:
            diferenca_imovel = imovel1._valor_imovel - imovel2._valor_imovel
        elif imovel2._valor_imovel >= imovel1._valor_imovel:
            diferenca_imovel = imovel2._valor_imovel- imovel1._valor_imovel

        print(f'{imovel1._tipo} - {imovel1._codigo}: {imovel1._valor_imovel}\n{imovel2._tipo} - {imovel2._codigo}: {imovel2._valor_imovel}\nDiferença do valor do Imóvel: {diferenca_imovel}')

#================================================FINANCIAMENTO==========================================
class Financiamento:
    def __init__(self, cliente, imovel, banco, valor_financiamento, num_aportes):
        self._cliente = Cliente
        self._imovel = Imovel
        self._banco = Banco
        self._valor_financiamento = valor_financiamento
        self._num_aportes = num_aportes

    #Get
    @property
    def cliente (self):
        return self._cliente
    
    @property  
    def imovel (self):
        return self._imovel

    @property  
    def banco (self):
        return self._banco

    @property  
    def valor_financiamento (self):
        return self._valor_financiamento

    @property
    def num_aportes (self):
        return self._num_aportes

    #Set
    @cliente.setter
    def cliente (self, novo):
        self._cliente = novo
        
    @imovel.setter
    def imovel (self, novo):
        self._imovel = novo

    @banco.setter
    def banco (self, novo):
        self._banco = novo

    @valor_financiamento.setter
    def valor_financiamento (self, novo):
        self._valor_financiamento = novo

    @num_aportes.setter
    def num_aportes (self, novo):
            self._num_aportes = novo

  #RECEBER APORTE#
    def receber_aporte(self, valor):
        if conacesso == conta1._id:
            if valor >= financiamento1._valor_financiamento:
                conta1.debitar(valor)
                cashback = valor - financiamento1._valor_financiamento
                conta1.creditar(cashback)
                self._valor_financiamento= 0
                self._num_aportes += 1
                print(f'Você pagou o financiamento do imóvel!')
        
            elif valor < financiamento1._valor_financiamento and valor > 0:
                conta1.debitar(valor)
                novo_financiamento = financiamento1._valor_financiamento - valor
                self._num_aportes += 1
                self._valor_financiamento = novo_financiamento
                print(f'Você pagou {valor} deixando o financiamento por {self._valor_financiamento}\nNúmero de aportes: {self._num_aportes}')
        elif conacesso == conta2._id:
            if valor >= financiamento2._valor_financiamento:
                conta2.debitar(valor)
                cashback = valor - financiamento2._valor_financiamento
                conta2.creditar(cashback)
                self._valor_financiamento= 0
                self._num_aportes += 1
                print(f'Você pagou o financiamento do imóvel!')
        
            elif valor < financiamento2._valor_financiamento and valor > 0:
                conta2.debitar(valor)
                novo_financiamento = financiamento2._valor_financiamento - valor
                self._num_aportes += 1
                self._valor_financiamento = novo_financiamento
                print(f'Você pagou {valor} deixando o financiamento por {self._valor_financiamento}\nNúmero de aportes: {self._num_aportes}')
  
#================================================DADOS===============================================================================
cliente1 = Cliente('Lucas Pessoa', '10987654321', float(1400), [100,200])
cliente2 = Cliente('Pedro Bravim', '12345678910', float(9000), [300,400])
conta1= Conta(float(3500), 1, cliente1) 
conta2= Conta(float(999999), 2, cliente2)
banco1 = Banco('Nubank', [conta1,conta2], [100,200,300,400])
banco2 = Banco('Banco do Brasil', [conta1,conta2], [100,200,300,400])
imovel1 = Imovel('Casa', float(100000), 1234)
imovel2 = Imovel('Apartamento', float(10000), 4321)
financiamento1 = Financiamento(cliente1, imovel2, banco1, 800, 0)
financiamento2 = Financiamento(cliente2, imovel1, banco1, 2000, 0)
#=================================================================MENU================================================================

print("\n----------------------\n"+ str(cliente1._nome),"\n"+"ID da Conta:", conta1._id,"\n"+"Saldo: R${}".format(conta1._saldo),"\n----------------------")
print("\n----------------------\n"+ str(cliente2._nome),"\n"+"ID da Conta:", conta2._id,"\n"+"Saldo: R${}".format(conta2._saldo),"\n----------------------")
conacesso=int(input("Qual conta você deseja acessar ?"))
if conacesso == conta1._id:
    resposta = ''
    lista_resposta = ['CLIENTE','CONTA','BANCO','FINANCIAMENTO','SAIR']

    while (resposta != 'SAIR'):
        resposta = str(input('\nVocê quer acessar o *CLIENTE, a *CONTA, o *BANCO, o IMÓVEL ou o *FINANCIAMENTO? (Para encerrar o programa digite *SAIR) ')).upper()

        if(resposta == 'CLIENTE'):
            print('\n------------Cliente--------------')
            print(f'Nome: {cliente1._nome}\nCPF: {cliente1._cpf}\nSalário: {cliente1._salario}\nFinanciamentos: {cliente1._financiamentos}')
            cliente1.total_financiado()
            print('--------------------------------')

            resposta5 = ''
            lista_resposta5 = ['SIM, NÃO']

            while (resposta5 != 'NÃO'):
                resposta5= str(input('\nVocê quer compararar os salários? (Para *COMPARAR digite *Sim ou *NÃO) ')).upper()
                if resposta5 == 'SIM':
                    cliente1.comparar_salario()

        elif(resposta == 'CONTA'):
            print('------------Conta--------------')
            print(f' Saldo: {conta1._saldo}\n ID: {conta1._id}')
            print('--------------------------------')

            resposta2 = ''
            lista_resposta2 = ['CREDITAR','DEBITAR','TRANSFERÊNCIA','VOLTAR']

            while (resposta2 != 'VOLTAR'):
                resposta2 = str(input('\nVocê quer *CREDITAR, a *DEBITAR, realizar uma *TRANSFERÊNCIA? (Para encerrar o programa digite *Voltar) ')).upper()

                if(resposta2 == 'CREDITAR'):
                    valor= float(input('Insira o valor a ser creditado na sua conta:'))
                    conta1.creditar(valor)

                elif(resposta2 == 'DEBITAR'):
                    valor= float(input('Insira o valor a ser debitado da sua conta:'))
                    conta1.debitar(valor)
                
                elif(resposta2 == 'TRANSFERÊNCIA'):
                    valor= float(input('Insira o valor que deseja transferir:'))
                    outra_conta= int(input(f'Insira conta na qual você deseja transferir: (Contas disponíveis: Conta {conta2._id}[DIGITE O ID])'))
                    conta1.transferencia(valor, outra_conta)
                
                elif(resposta2 not in lista_resposta2):
                    print("\nInsira um resposta válida.")

            print('--------------------------------')

        elif(resposta == "BANCO"):
            print('------------Banco--------------')
            print(f'Nome do Banco: {banco1._nome_do_banco}\nContas do Banco: Conta {conta1._id} - Conta {conta2._id} \nFinanciamentos: {banco1._financiamentos}')
            print('--------------------------------')

            resposta3 = ''
            lista_resposta3 = ['SALDO TOTAL','FINANCIAMENTOS','VOLTAR']

            while (resposta3 != 'VOLTAR'):
                resposta3 = str(input('\nVocê quer ver *SALDO TOTAL, ou ver os *FINANCIAMENTOS? (Para encerrar o programa digite *Voltar) ')).upper()

                if(resposta3 == 'SALDO TOTAL'):
                    banco1.total_valor_contas()
                    
                elif(resposta3 == 'FINANCIAMENTOS'):
                    _cpf=str(input(f'comfirme o seu CPF para ver seus financiamentos: (CPF: {cliente1._cpf} )'))
                    banco1.financiamentos_cliente(_cpf)
        
                    

                elif(resposta3 not in lista_resposta3):
                    print("\nInsira um resposta válida.")

            print('--------------------------------')

        elif(resposta == "IMÓVEL"):
            print('------------Imóvel--------------')
            print(f'Tipo do Imóvel desejado: {imovel2._tipo}\nValor do Imóvel desejado: {imovel2._valor_imovel}\nCódigo do do Imóvel desejado: {imovel2._codigo}')
            print('--------------------------------')

            resposta6 = ''
            lista_resposta6 = ['SIM, NÃO']

            while (resposta6 != 'NÃO'):
                resposta6= str(input('\nVocê quer compararar os Imóveis? (Para *COMPARAR digite *Sim ou *NÃO) ')).upper()
                if resposta6 == 'SIM':
                    imovel2.comparar_imovel()

        elif(resposta == "FINANCIAMENTO"):
            print('------------Financiamento--------------')
            print(f' Valor do Financiamento: {financiamento1._valor_financiamento}\n Número de aportes: {financiamento1._num_aportes}')
            print('---------------------------------------')

            resposta4 = ''
            lista_resposta4 = ['SIM','NÃO']

            while (resposta4 != 'NÃO'):
                resposta4 = str(input('\nVocê quer *RECEBER APORTE? (Digite SIM ou NÃO)')).upper()

                if(resposta4 == 'SIM'):
                    valor=float(input(f'Seu saldo é {conta1._saldo}, o valor do financiamento é {financiamento1._valor_financiamento}, insira o valor para debitar o financiamento do Imóvel desejado:'))
                    if financiamento1._valor_financiamento > 0:
                        financiamento1.receber_aporte(valor)
                    else:
                        print('O Financiamento do imóvel já foi pago.')
                
                elif resposta4 not in lista_resposta4:
                    print("\nInsira um resposta válida.")

        elif(resposta not in lista_resposta):
            print("\nInsira um resposta válida.")

    print('--------------------------------')
elif conacesso == conta2._id:
    resposta = ''
lista_resposta = ['CLIENTE','CONTA','BANCO','FINANCIAMENTO','SAIR']

while (resposta != 'SAIR'):
    resposta = str(input('\nVocê quer acessar o *CLIENTE, a *CONTA, o *BANCO, o IMÓVEL ou o *FINANCIAMENTO? (Para encerrar o programa digite *SAIR) ')).upper()

    if(resposta == 'CLIENTE'):
        print('\n------------Cliente--------------')
        print(f'Nome: {cliente2._nome}\nCPF: {cliente2._cpf}\nSalário: {cliente2._salario}\nFinanciamentos: {cliente2._financiamentos}')
        cliente2.total_financiado()
        print('--------------------------------')

        resposta5 = ''
        lista_resposta5 = ['SIM, NÃO']

        while (resposta5 != 'NÃO'):
            resposta5= str(input('\nVocê quer compararar os salários? (Para *COMPARAR digite *Sim ou *NÃO) ')).upper()
            if resposta5 == 'SIM':
                cliente2.comparar_salario()

    elif(resposta == 'CONTA'):
        print('------------Conta--------------')
        print(f' Saldo: {conta2._saldo}\n ID: {conta2._id}')
        print('--------------------------------')

        resposta2 = ''
        lista_resposta2 = ['CREDITAR','DEBITAR','TRANSFERÊNCIA','VOLTAR']

        while (resposta2 != 'VOLTAR'):
            resposta2 = str(input('\nVocê quer *CREDITAR, a *DEBITAR, realizar uma *TRANSFERÊNCIA? (Para encerrar o programa digite *Voltar) ')).upper()

            if(resposta2 == 'CREDITAR'):
                valor= float(input('Insira o valor a ser creditado na sua conta:'))
                conta2.creditar(valor)

            elif(resposta2 == 'DEBITAR'):
                valor= float(input('Insira o valor a ser debitado da sua conta:'))
                conta2.debitar(valor)
            
            elif(resposta2 == 'TRANSFERÊNCIA'):
                valor= float(input('Insira o valor que deseja transferir:'))
                outra_conta= int(input(f'Insira conta na qual você deseja transferir: (Contas disponíveis: Conta {conta1._id}[DIGITE O ID])'))
                conta2.transferencia(valor, outra_conta)
            
            elif(resposta2 not in lista_resposta2):
                print("\nInsira um resposta válida.")

        print('--------------------------------')

    elif(resposta == "BANCO"):
        print('------------Banco--------------')
        print(f'Nome do Banco: {banco1._nome_do_banco}\nContas do Banco: Conta {conta1._id} - Conta {conta2._id} \nFinanciamentos: {banco1._financiamentos}')
        print('--------------------------------')

        resposta3 = ''
        lista_resposta3 = ['SALDO TOTAL','FINANCIAMENTOS','VOLTAR']

        while (resposta3 != 'VOLTAR'):
            resposta3 = str(input('\nVocê quer ver *SALDO TOTAL, ou ver os *FINANCIAMENTOS? (Para encerrar o programa digite *Voltar) ')).upper()

            if(resposta3 == 'SALDO TOTAL'):
                banco1.total_valor_contas()
                
            elif(resposta3 == 'FINANCIAMENTOS'):
                _cpf=str(input(f'Confirme o seu CPF para ver seus financiamentos: (CPF: {cliente2._cpf})'))
                banco1.financiamentos_cliente(_cpf)
    
            elif(resposta3 not in lista_resposta3):
                print("\nInsira um resposta válida.")

        print('--------------------------------')

    elif(resposta == "IMÓVEL"):
        print('------------Imóvel--------------')
        print(f'Tipo do Imóvel desejado: {imovel1._tipo}\nValor do Imóvel desejado: {imovel1._valor_imovel}\nCódigo do do Imóvel desejado: {imovel1._codigo}')
        print('--------------------------------')

        resposta6 = ''
        lista_resposta6 = ['SIM, NÃO']

        while (resposta6 != 'NÃO'):
            resposta6= str(input('\nVocê quer compararar os Imóveis? (Para *COMPARAR digite *Sim ou *NÃO) ')).upper()
            if resposta6 == 'SIM':
                imovel1.comparar_imovel()

    elif(resposta == "FINANCIAMENTO"):
        print('------------Financiamento--------------')
        print(f' Valor do Financiamento: {financiamento2._valor_financiamento}\n Número de aportes: {financiamento2._num_aportes}')
        print('---------------------------------------')

        resposta4 = ''
        lista_resposta4 = ['SIM','NÃO']

        while (resposta4 != 'NÃO'):
            resposta4 = str(input('\nVocê quer *RECEBER APORTE? (Digite SIM ou NÃO)')).upper()

            if(resposta4 == 'SIM'):
                valor=float(input(f'Seu saldo é {conta2._saldo}, o valor do financiamento é {financiamento2._valor_financiamento}, insira o valor para debitar o financiamento do Imóvel desejado:'))
                if financiamento2._valor_financiamento > 0:
                    financiamento2.receber_aporte(valor)
                else:
                    print('O Financiamento do imóvel já foi pago.')
            
            elif resposta4 not in lista_resposta4:
                print("\nInsira um resposta válida.")

    elif(resposta not in lista_resposta):
        print("\nInsira um resposta válida.")

print('--------------------------------')
