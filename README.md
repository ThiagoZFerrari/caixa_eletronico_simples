# 🏦 Simulador de Caixa Eletrônico (ATM)

Este projeto marca a conclusão da fase de **Lógica Fundamental e Programação Procedural** em Python. O objetivo principal foi criar um sistema robusto que pudesse lidar com o fluxo contínuo de um menu e tratar entradas inválidas, um requisito essencial para qualquer aplicação profissional.

---

## 🎯 Habilidades Demonstradas

Este código prova o domínio dos seguintes conceitos:

1.  **Controle de Fluxo Contínuo:** Uso eficaz do laço `while True` para manter o menu principal ativo e navegável.
2.  **Robustez (Tratamento de Erros):** Implementação aninhada do bloco **`try/except`** em todas as entradas (`opção`, `depósito`, `saque`) para evitar falhas e travas do sistema (abordando o temido `ValueError`).
3.  **Regras de Negócio:** Aplicação de lógica condicional (`if/elif/else`) para:
    * Checagem de Saldo Insuficiente (`saque > saldo_caixa`).
    * Validação de valores positivos (`valor > 0`).
    * Uso do comando `break` para sair do laço de transação após o sucesso.
4.  **UX/Modularidade Básica:** Utilização de `import os` (`os.system`) e `sleep` para criar uma interface de terminal mais limpa e simular o tempo de processamento.

---

## 💡 TRANSFORMAÇÃO PARA POO (Próximo Passo)

Embora este código seja funcionalmente excelente, ele gerencia as variáveis (`saldo_caixa`) e as ações (`depositar`, `sacar`) de forma separada.

* **O Problema Procedural:** Se tivéssemos 100 clientes, precisaríamos de 100 variáveis soltas (`saldo_caixa_1`, `saldo_caixa_2`, etc.).
* **A Solução POO:** A próxima etapa (Programação Orientada a Objetos) resolverá isso: nós criaremos uma **Classe `Conta`** para agrupar o `saldo` (atributo) e as ações (`depositar`, `sacar` - métodos) em um único objeto reutilizável.

**Status:** Concluído (Fase Lógica). Pronto para a transição para POO.


OBS: Utilizei a IA somente para a elaboração do exercício, análise de código e correções de escrita para o Readme.