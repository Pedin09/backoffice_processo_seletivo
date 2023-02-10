import re
from typing import Union


class ValidaCpf:
    # Valida CPF
    def __init__(self, cpf: str = '') -> None:
        
        self._validado = False
        
        if cpf:
            self.cpf: str = cpf

    def valida(self) -> bool:
        
        if not self.cpf:
            return False

        qtd_caractere = len(self.cpf)

        # CPF
        if qtd_caractere == 11:
            # Primeiros 9 digitos
            novo_cpf: str = self._calcula_digitos(self.cpf[:9],
                                                       multiplicador_inicial=10)
            # 9 digitos + primeiro digito verificador
            novo_cpf: str = self._calcula_digitos(novo_cpf,
                                                       multiplicador_inicial=11)

            if novo_cpf == self.cpf:
                self._validado = True
                return True
    @property
    def formatado(self):
        if not self._validado:
            if not self.cpf or not self.valida():
                raise ValueError("Enviar o CPF e validar para "
                                 "obter CPF formatado.")

        qtd_caracteres = len(self.cpf)

        if qtd_caracteres == 11:
            cpf = self.cpf

            return '%s.%s.%s-%s' % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:],)

        else:
            
            return False

    @staticmethod
    def _calcula_digitos(
            fatia_cpf: str,
            multiplicador_inicial: int
    ) -> Union[str, bool]:
        if not fatia_cpf:
            return False

        # Evita sequências
        sequencia: str = fatia_cpf[0] * len(fatia_cpf)
        if sequencia == fatia_cpf:
            return False

        soma: int = 0
        for chave, _ in enumerate(range(len(fatia_cpf) + 1, 1, -1)):
            soma += int(fatia_cpf[chave]) * multiplicador_inicial

            if (multiplicador_inicial == 2):
                multiplicador_inicial = 9
            else:
                multiplicador_inicial -= 1

        resto: int = 11 - (soma % 11)
        resto: int = resto if resto <= 9 else 0

        return fatia_cpf + str(resto)

    @property
    def cpf(self) -> str:
        self._validado = False
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str):
        
        self._cpf = self._so_numeros(cpf)

    @staticmethod
    def _so_numeros(cpf: str) -> str:
        
        return re.sub('[^0-9]', '', cpf)