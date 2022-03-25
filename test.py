from validatecpf import validateCpf

cpf = validateCpf('111-111-111-11')

if cpf.validate():
    print('cpf valido')
else:
    print('cpf invalido')
