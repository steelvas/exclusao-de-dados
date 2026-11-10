"""Simulação de estados; não elimina arquivos nem dados reais."""

copias = {"aplicativo": True, "banco_de_dados": True,
          "backup": True, "fornecedor": True}
copias["aplicativo"] = False
pendentes = [local for local, presente in copias.items() if presente]
print("Cópias ainda existentes:", pendentes)
