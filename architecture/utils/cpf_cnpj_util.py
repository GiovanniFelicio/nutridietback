from architecture.exceptions.unprocessable import UnprocessableCPF


class CpfCnpjUtil:

    @staticmethod
    def is_cpf_valid(cpf):
        if not cpf or len(cpf) < 11:
            raise UnprocessableCPF()

        antigo = [int(d) for d in cpf]

        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return True

        raise UnprocessableCPF()
