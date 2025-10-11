<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=180&section=header&text=Clean%20Code%20Project&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35"/>
</div>

<div align="center">
  
  [![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=6366f1&size=35&center=true&vCenter=true&width=1000&lines=Refatoração+de+Código+e+Boas+Práticas;Transformando+Código+Legado+em+Arte;Projeto+A3+-+Gestão+e+Qualidade+de+Software)](https://git.io/typing-svg)
  
</div>

<br>

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
  ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
  
</div>

<br>

<div align="center">
  
  ### 🎓 Universidade São Judas Tadeu
  **Gestão e Qualidade de Software | São Paulo - 2025**
  
  👨‍🏫 **Professor:** Robson Calvetti
  
</div>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 👥 Nossa Equipe

<div align="center">

<table>
  <tr>
    <td align="center" width="14%">
      <img src="https://avatars.githubusercontent.com/u/162994271?s=400&u=b6be7807d4f38c164926fbeb108a7e29ad502503&v=4" width="100px;" alt="Andressa" style="border-radius: 50%;"/><br>
      <sub><b>Andressa Rabêlo</b></sub><br>
      <sub>RA: 823213904</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://i.imgur.com/hrQ4GAz.jpeg" width="100px;" alt="Júlia" style="border-radius: 50%;"/><br>
      <sub><b>Júlia Oliveira</b></sub><br>
      <sub>RA: 823214680</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://github.com/lucas.png" width="100px;" alt="Lucas" style="border-radius: 50%;"/><br>
      <sub><b>Lucas Marzocca</b></sub><br>
      <sub>RA: 823116813</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://github.com/marcos.png" width="100px;" alt="Marcos" style="border-radius: 50%;"/><br>
      <sub><b>Marcos V. Santos</b></sub><br>
      <sub>RA: 82327399</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://github.com/matheus.png" width="100px;" alt="Matheus" style="border-radius: 50%;"/><br>
      <sub><b>Matheus H. F.</b></sub><br>
      <sub>RA: 823141914</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://github.com/mylena.png" width="100px;" alt="Mylena" style="border-radius: 50%;"/><br>
      <sub><b>Mylena Soares</b></sub><br>
      <sub>RA: 824144075</sub>
    </td>
    <td align="center" width="14%">
      <img src="https://github.com/samuel.png" width="100px;" alt="Samuel" style="border-radius: 50%;"/><br>
      <sub><b>Samuel Faustino</b></sub><br>
      <sub>RA: 824147380</sub>
    </td>
  </tr>
</table>

</div>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 🎯 Sobre o Projeto

<div align="center">
  
  <img src="https://readme-typing-svg.herokuapp.com/?color=6366f1&size=25&center=true&vCenter=true&width=800&lines=De+código+caótico+a+código+profissional;Aplicando+Clean+Code+na+prática" />
  
</div>

<br>

Este projeto é uma jornada de transformação: pegamos um código Python funcional, mas problemático, e o transformamos em um exemplo de boas práticas de programação. Não se trata apenas de fazer o código funcionar - trata-se de fazer código que outros desenvolvedores vão amar trabalhar.

<br>

### 🔍 O Desafio

<details open>
<summary><b>📌 Clique para ver o código original</b></summary>

<br>

Trabalhamos com um sistema de cadastro de usuários que possui:

```python
usuarios = []  # ❌ Variável global

def menu():
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    try:
        return int(input("Escolha: "))
    except:  # ❌ Exceção genérica
        return -1

def cadastrar():
    nome = input("Digite o nome: ")
    usuarios.append(nome)  # ❌ Sem validação de duplicidade
    print("Usuário cadastrado!")
```

**Problemas críticos identificados:**
- ❌ Variáveis globais descontroladas
- ❌ Tratamento de exceções genérico e perigoso
- ❌ Zero validação de dados
- ❌ Código duplicado em múltiplos lugares
- ❌ Ausência total de orientação a objetos
- ❌ Nenhum teste automatizado
- ❌ Uso inadequado de estruturas (`range(len())` ao invés de `enumerate`)

</details>

<br>

### ✨ A Solução

<details>
<summary><b>🚀 Clique para ver nossas melhorias</b></summary>

<br>

**Transformações aplicadas:**

🎨 **Arquitetura Limpa**
- Implementação de classes e métodos bem definidos
- Separação de responsabilidades
- Design patterns aplicados

🛡️ **Robustez e Segurança**
- Validação completa de entradas
- Tratamento específico de exceções
- Prevenção de duplicidades

🧪 **Qualidade Garantida**
- Testes unitários abrangentes
- Cobertura de código medida
- Testes de integração

📚 **Documentação Profissional**
- Docstrings em todas as funções
- Comentários apenas onde necessário
- README detalhado

</details>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 🏗️ Princípios de Clean Code Aplicados

<div align="center">

<table>
<tr>
<td align="center" width="25%">

### 🎯 SOLID

Princípios fundamentais da orientação a objetos

**S** - Single Responsibility  
**O** - Open/Closed  
**L** - Liskov Substitution  
**I** - Interface Segregation  
**D** - Dependency Inversion

</td>
<td align="center" width="25%">

### 🔄 DRY

Don't Repeat Yourself

Cada pedaço de conhecimento deve ter uma representação única, não ambígua e autoritativa no sistema

</td>
<td align="center" width="25%">

### 💋 KISS

Keep It Simple, Stupid

Simplicidade deve ser um objetivo chave no design, e complexidade desnecessária deve ser evitada

</td>
<td align="center" width="25%">

### 🚫 YAGNI

You Aren't Gonna Need It

Não adicione funcionalidades até que sejam realmente necessárias

</td>
</tr>
</table>

</div>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 📊 Métricas de Qualidade

<div align="center">

### 📈 Comparativo: Antes vs Depois da Refatoração

<table>
<tr>
<th>Métrica</th>
<th>Código Original</th>
<th>Código Refatorado</th>
<th>Melhoria</th>
</tr>
<tr>
<td><b>Linhas de Código</b></td>
<td align="center">~45</td>
<td align="center">Em análise</td>
<td align="center">🔄</td>
</tr>
<tr>
<td><b>Complexidade Ciclomática</b></td>
<td align="center">Alta</td>
<td align="center">Em análise</td>
<td align="center">🔄</td>
</tr>
<tr>
<td><b>Cobertura de Testes</b></td>
<td align="center">0%</td>
<td align="center">Em desenvolvimento</td>
<td align="center">🔄</td>
</tr>
<tr>
<td><b>Duplicação de Código</b></td>
<td align="center">~25%</td>
<td align="center">< 5%</td>
<td align="center">✅ -80%</td>
</tr>
<tr>
<td><b>Número de Classes</b></td>
<td align="center">0</td>
<td align="center">Em desenvolvimento</td>
<td align="center">🔄</td>
</tr>
<tr>
<td><b>Tratamento de Erros</b></td>
<td align="center">Genérico</td>
<td align="center">Específico</td>
<td align="center">✅ 100%</td>
</tr>
</table>

<sub>📌 Métricas atualizadas conforme o desenvolvimento do projeto</sub>

</div>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 🛠️ Tecnologias e Ferramentas

<div align="center">

### Linguagem Principal

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

### Testes e Qualidade

![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage.py-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Versionamento

![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

### Ambiente de Desenvolvimento

![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)

</div>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 📚 Referências Bibliográficas

<details>
<summary><b>📖 Clique para ver a bibliografia completa</b></summary>

<br>

**Bibliografia Básica:**

📕 PRESSMAN, Roger; MAXIM, Bruce. **Engenharia de Software: Uma abordagem profissional**. 8ª Ed. Bookman, 2016.

📗 SOMMERVILLE, Ian. **Engenharia de Software**. 9ª ed. São Paulo: Pearson Prentice Hall, 2011.

📘 GONÇALVES, Priscila de Fátima et al. **Testes de software e gerência de configuração**. Soluções Educacionais Integradas, 2019.

<br>

**Bibliografia Complementar:**

📙 MARTIN, Robert C. **Clean Code: A Handbook of Agile Software Craftsmanship**. Prentice Hall, 2008.

📙 MARTIN, Robert C. **Clean Architecture: A Craftsman's Guide to Software Structure and Design**. Prentice Hall, 2017.

📙 FOWLER, Martin. **Refactoring: Improving the Design of Existing Code**. Addison-Wesley, 2018.

</details>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br>

## 💡 Conclusão

> *"Qualquer tolo consegue escrever código que um computador entende. Bons programadores escrevem código que humanos entendem."*  
> **— Martin Fowler**

<br>

Este projeto não é apenas sobre corrigir código - é sobre entender que a qualidade do software impacta diretamente na produtividade, manutenibilidade e sucesso de projetos reais. Cada linha refatorada nos ensina que código limpo não é luxo, é necessidade.

<br>

<div align="center">

### 🎓 Universidade São Judas Tadeu

**Gestão e Qualidade de Software**

*Desenvolvendo não apenas código, mas desenvolvedores melhores*

<br>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=120&section=footer"/>

</div>
