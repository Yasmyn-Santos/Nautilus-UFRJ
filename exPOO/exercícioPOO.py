class AUV:
    def __init__(self, thursters, sensor, ano, nome, software):
        self.thursters = thursters 
        self.sensor = sensor
        self.ano = ano
        self.nome = nome
        self.software = software

    def exibir_tabela(aus):
        print('{:<20} {:<20} {:<40} {:<20} {:<20}'.format('Nome', 'Propulsores', 'Sensor', 'Ano', 'Software'))
        for auv in aus:
            print('{:<20} {:<20} {:<40} {:<20} {:<20}'.format(auv.nome, auv.thursters, auv.sensor, auv.ano, auv.software))

    def exibir_individual(self):
        print('Nome: {}'.format(self.nome))
        print('Propulsores: {}'.format(self.thursters))
        print('Sensor: {}'.format(self.sensor))
        print('Ano: {}'.format(self.ano))
        print('Software: {}'.format(self.software))


    def novo_antigo(aus):
        ordem = sorted(aus, key=lambda x: x.ano, reverse=True)
        for i, auv in enumerate(ordem):
            print("Rank {}: {} ({})".format(i+1, auv.nome, auv.ano))

    def get_thursters(auv):
        return auv.thursters


    def propulsores(aus):
        '''Coloca na ordem de acordo com o número de propulsores de cada auv. Do maior para o menor.'''
        ordem_p = sorted(aus, key=AUV.get_thursters, reverse=True)
        for i, auv in enumerate(ordem_p):
            print("Rank {}: {} ({})".format(i+1, auv.nome, auv.thursters))
            

auv_BrHUE = AUV("6", "IMU e sensor de profundidade", "2020", "BrHUE", "ROS e Linux")
auv_Lua = AUV("8", "DVL, IMU e sensor de profundidade", "2022", "Lua", "ROS e Linux")

AUV.exibir_tabela([auv_BrHUE, auv_Lua])
print("\n\n")
auv_BrHUE.exibir_individual()
print("\n\n")
auv_Lua.exibir_individual()
print("\n\n")
print("Rank do mais novo para o mais antigo\n")
AUV.novo_antigo([auv_BrHUE, auv_Lua])
print("\n\n")
print("Rank do auv que possui uma maior quantidade de propulsores para o que possui a menor quantidade\n")
AUV.propulsores([auv_BrHUE, auv_Lua])

