

class FuncionarioTecnico:
 def __init__(self, status):
  self.status = status
    
nivel = 'Técnico'
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')
 
print(func1.status,":" ,nivel)
print(func2.status)
#print(func1.status)
#print(func2.status)
