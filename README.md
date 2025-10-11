<div align="center">

# Refatoração de Código e Clean Code

**Projeto A3 - Gestão e Qualidade de Software**

Universidade São Judas Tadeu | São Paulo, 2025  
Professor: Robson Calvetti

---

</div>

## Integrantes

<table>
  <tr>
    <td><b>Andressa Emily Rabêlo Pereira</b><br>RA: 823213904</td>
    <td><b>Júlia Oliveira Rocha</b><br>RA: 823214680</td>
    <td><b>Lucas Marzocca</b><br>RA: 823116813</td>
  </tr>
  <tr>
    <td><b>Marcos V. Santos</b><br>RA: 82327399</td>
    <td><b>Matheus H. F. Guimarães</b><br>RA: 823141914</td>
    <td><b>Mylena Soares Rocha</b><br>RA: 824144075</td>
  </tr>
  <tr>
    <td colspan="3" align="center"><b>Samuel Faustino Gomes da Costa</b><br>RA: 824147380</td>
  </tr>
</table>

<br>

## Sobre o Projeto

<details open>
<summary><b>Qual é o objetivo?</b></summary>
<br>
Transformar um código legado cheio de más práticas em um software limpo, organizado e fácil de manter. Vamos aplicar os princípios do Clean Code para melhorar a qualidade sem quebrar a funcionalidade original.
</details>

<details>
<summary><b>O que vamos refatorar?</b></summary>
<br>
Um sistema simples de cadastro de usuários em Python que apresenta diversos problemas de qualidade. O código funciona, mas está difícil de entender, manter e expandir.
</details>

<details>
<summary><b>Quais problemas identificamos?</b></summary>
<br>

**Problemas no código original:**
- Variáveis globais espalhadas pelo código
- Tratamento de exceções muito genérico
- Mensagens e lógica duplicadas
- Falta de organização em classes
- Não há validação de dados duplicados
- Uso inadequado de estruturas de repetição
- Ausência de testes automatizados

</details>

<br>

## Métricas de Qualidade

<div align="center">

### Comparativo: Antes vs Depois

| Métrica | Código Original | Código Refatorado | Melhoria |
|---------|----------------|-------------------|----------|
| Linhas de código | - | - | - |
| Complexidade ciclomática | - | - | - |
| Cobertura de testes | 0% | - | - |
| Duplicação de código | Alta | Baixa | - |
| Modularização | Nenhuma | Classes + Métodos | - |

*Métricas serão atualizadas conforme o desenvolvimento*

</div>

<br>

## Princípios Aplicados

<table>
<tr>
<td width="25%" align="center">

**SOLID**

Princípios de design orientado a objetos para código mais flexível e manutenível

</td>
<td width="25%" align="center">

**DRY**

Don't Repeat Yourself - eliminação de código duplicado

</td>
<td width="25%" align="center">

**KISS**

Keep It Simple - código simples e direto ao ponto

</td>
<td width="25%" align="center">

**YAGNI**

You Aren't Gonna Need It - sem complexidade desnecessária

</td>
</tr>
</table>

<br>

## Evolução do Projeto

```mermaid
gantt
    title Linha do Tempo da Refatoração
    dateFormat  YYYY-MM-DD
    section Análise
    Identificação de problemas       :done, 2025-09-15, 15d
    section Desenvolvimento
    Refatoração do código            :active, 2025-10-01, 58d
    Implementação de testes          :active, 2025-10-15, 43d
    section Documentação
    Relatório técnico                :2025-11-01, 27d
    Preparação da apresentação       :2025-11-20, 8d
```

<br>

## Atividade dos Contribuidores

<div align="center">

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/SEU-USUARIO/SEU-REPOSITORIO?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/SEU-USUARIO/SEU-REPOSITORIO?style=flat-square)
![GitHub contributors](https://img.shields.io/github/contributors/SEU-USUARIO/SEU-REPOSITORIO?style=flat-square)

*Substitua SEU-USUARIO/SEU-REPOSITORIO pelo nome real do repositório*

</div>

<br>

## Tecnologias

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?style=flat-square&logo=pytest&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?style=flat-square&logo=git&logoColor=white)

</div>

<br>

## Como Contribuir

Cada membro do grupo deve fazer pelo menos um commit. Para contribuir:

1. Clone o repositório
2. Crie uma branch com seu nome: `git checkout -b feature/seu-nome`
3. Faça suas alterações
4. Commit suas mudanças: `git commit -m "Descrição clara do que foi feito"`
5. Push para o GitHub: `git push origin feature/seu-nome`
6. Abra um Pull Request

<br>

---

<div align="center">

**Universidade São Judas Tadeu**  
Gestão e Qualidade de Software - 2025

*"Qualquer tolo consegue escrever código que um computador entende. Bons programadores escrevem código que humanos entendem."* - Martin Fowler

</div>
