import re

class validateCpf:
    def __init__(self, cpf):
        self.cpf = cpf


    #valida inserção e passa nove digitos para calculo
    def validate(self):
        if not self.cpf:
            return False

        cpf_in_focus = self._calculate_dig(self.cpf[:9])
        cpf_in_focus = self._calculate_dig(cpf_in_focus)

        if cpf_in_focus == self.cpf:
            return True
        return False
    
    #coleta digitos e executa os calculos de validação
    @staticmethod
    def _calculate_dig(slice_cpf):
        if not slice_cpf:
            return False

        sequence = slice_cpf[0] * len(slice_cpf)

        if sequence == slice_cpf:
            return False

        result = 0
        for key, multiplier in enumerate(range(len(slice_cpf)+1, 1, -1)):
            result += int(slice_cpf[key]) * multiplier
        
        checker_dig = 11 - (result%11)
        checker_dig = checker_dig if checker_dig <= 9 else 0
        return slice_cpf + str(checker_dig)

    #metodo get 
    @property
    def cpf(self):
        return self._cpf

    #metodo set 
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._so_numbers(cpf)
    
    #metodo statico para limpar caracteres
    @staticmethod
    def _so_numbers(cpf):
        return re.sub('[^0-9]','', cpf)

