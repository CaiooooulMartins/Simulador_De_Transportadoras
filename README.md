# 🚚 **Simulador de Transportadoras**

## 📜 Descrição

O **Simulador de Transportadoras** é uma aplicação desenvolvida em **Python** utilizando a biblioteca **CustomTkinter** para criar uma interface gráfica moderna e intuitiva. O objetivo é calcular o custo de transporte de mercadorias com base no **valor da Nota Fiscal (NF)** e na **quantidade de pallets**, considerando as regras de cálculo de diferentes transportadoras.

## 🛠️ **Estrutura do Projeto**

### 1. 📚 **Bibliotecas Utilizadas**

- **customtkinter**: Para criar a interface gráfica estilizada e moderna.
- **tkinter.messagebox**: Para exibir mensagens de erro ou informações ao usuário.

### 2. ⚙️ **Configuração Inicial**

O tema da interface gráfica é configurado para o **modo escuro**, com um esquema de cores azul escuro para um visual agradável.

---

## 🏷️ **Classes e Funções**

### 1. 🚛 **Classe Transportadora**

A **Classe Transportadora** armazena as informações de cada transportadora, como:

- **Nome** da transportadora
- **Tipo de veículo** utilizado
- **Custo total** do frete
- **Detalhes do cálculo** do frete

### 2. 🔢 **Função calculo_Transportadora_n1**

Calcula o custo do frete para a **Transportadora N1**, levando em conta as seguintes regras:

- **Veículo**: Determinado pela quantidade de pallets.
- **Frete peso**: Valor fixo baseado no veículo.
- **Advalorem**: Percentual aplicado sobre o valor da NF.
- **ICMS**: Imposto sobre o frete.
- **Escolta**: Adicionada se o valor da NF for superior a R$3.500.000.

O resultado é retornado como um objeto da classe **Transportadora**.

### 3. 🔢 **Função calculo_Transportadora_n2**

Similar à função anterior, mas com regras específicas para a **Transportadora N2**, incluindo valores diferentes para o **frete peso** e o percentual de **Advalorem**.

### 4. ⚡ **Função calcular**

Função principal que:

- Obtém os valores de entrada:
  - **Valor da NF** e **Quantidade de pallets**.
- **Valida os dados** inseridos.
- **Realiza os cálculos** para cada transportadora.
- **Exibe os resultados** e destaca a melhor opção com base no custo total.

### 5. 🖥️ **Interface Gráfica**

A interface gráfica é criada com o **CustomTkinter** e inclui:

- **Janela Principal**: Configurada com título e tamanho fixo.
- **Campos de Entrada**: Para o valor da NF e a quantidade de pallets.
- **Botão de Cálculo**: Aciona a função **calcular**.
- **Janela de Resultados**: Exibe os detalhes do cálculo, incluindo o custo total e a melhor opção destacada.

---

## 🏁 **Passo a Passo do Funcionamento**

1. **Início**: O usuário insere o **valor da NF** e a **quantidade de pallets**.
   
2. **Validação**: O programa verifica se os valores são válidos. Caso contrário, uma mensagem de erro é exibida.
   
3. **Cálculo**: O programa chama as funções para calcular os custos para cada transportadora.

4. **Exibição dos Resultados**: Os detalhes do cálculo são mostrados, destacando a melhor opção de transportadora.

---

## 📊 **Exemplo de Uso**

### Entrada:
- **Valor da NF**: 4.000.000
- **Quantidade de Pallets**: 15

### Saída:
**Transportadora N1**:
- 🚚 **Veículo**: Truck
- 💰 **Frete peso**: R$4.945,24
- 💸 **Advalorem**: 0.07% (R$2.800,00)
- 🏷️ **ICMS**: 12%
- 🛡️ **Escolta**: R$2.900,00 (obrigatório)
- **Total**: R$10.645,24

**Transportadora N2**:
- 🚚 **Veículo**: Truck
- 💰 **Frete peso**: R$4.350,00
- 💸 **Advalorem**: 0.10% (R$4.000,00)
- 🏷️ **ICMS**: 12%
- 🛡️ **Escolta**: R$2.900,00 (obrigatório)
- **Total**: R$11.250,00

**Melhor Opção**: **Transportadora N1** - R$10.645,24

---

## ⚠️ **Possíveis Erros e Soluções**

1. **Erro: "Valor da NF inválido"**
   - **Causa**: O valor inserido não está no formato correto.
   - **Solução**: Insira o valor sem letras ou caracteres especiais, apenas números, pontos e vírgulas.

2. **Erro: "Nenhuma transportadora suporta essa quantidade de pallets"**
   - **Causa**: A quantidade de pallets está fora do intervalo suportado.
   - **Solução**: Insira um valor entre 1 e 27 pallets.

---

## 🏆 **Conclusão**

O **Simulador de Transportadoras** é uma ferramenta prática para calcular os custos de transporte com base em regras específicas. Ele oferece uma interface amigável, valida os dados inseridos e apresenta os resultados de forma clara e detalhada. Uma excelente solução para quem precisa calcular fretes de forma rápida e eficiente! 🚚💨

