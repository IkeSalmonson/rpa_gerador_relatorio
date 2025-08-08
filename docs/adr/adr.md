# Architectural Decision Records (ADR) - Gerador de Relatórios de Vendas

Este documento registra as decisões arquiteturais significativas tomadas durante o desenvolvimento do projeto "Gerador de Relatórios de Vendas".

## Índice

1.  [ADR-001: Escolha da Linguagem de Programação](#adr-001-escolha-da-linguagem-de-programação)
2.  [ADR-002: Arquitetura Baseada em Classes e Interfaces](#adr-002-arquitetura-baseada-em-classes-e-interfaces)
3.  [ADR-003: Estrutura do Projeto em Módulos e Pacotes](#adr-003-estrutura-do-projeto-em-módulos-e-pacotes)
4.  [ADR-004: Formato do Arquivo de Configuração](#adr-004-formato-do-arquivo-de-configuração)
5.  [ADR-005: Abstração de Fontes de Dados](#adr-005-abstração-de-fontes-de-dados)
6.  [ADR-006: Tratamento de Cabeçalho em Arquivos de Dados](#adr-006-tratamento-de-cabeçalho-em-arquivos-de-dados)
7.  [ADR-007: Distribuição como Executável](#adr-007-distribuição-como-executável)
8.  [ADR-008: Considerar a migração para Pandas para manipulação de dados](#adr-008-Considerar-a-migração-para-Pandas-para-manipulação-de-dados)
---

## ADR-001: Escolha da Linguagem de Programação

* **Data:** 2024-07-26
* **Status:** Aprovado
* **Contexto:**
    * Precisamos de uma linguagem de programação para desenvolver a POC do gerador de relatórios.
    * A linguagem deve ser adequada para manipulação de dados, fácil de aprender e usar, e ter uma boa biblioteca padrão.
* **Opções Consideradas:**
    * Python:
        * Prós: Sintaxe clara e legível, vasta biblioteca padrão, forte suporte para manipulação de dados, boa comunidade e documentação.
        * Contras: Pode ser mais lento que linguagens compiladas.
    * JavaScript:
        * Prós: Amplamente usado para desenvolvimento web, bom suporte para manipulação de strings e JSON.
        * Contras: Menos adequado para tarefas complexas de manipulação de dados numéricos, pode exigir bibliotecas adicionais.
    * Java:
        * Prós: Forte tipagem, bom desempenho, adequado para aplicações empresariais.
        * Contras: Mais complexo e verboso que Python, curva de aprendizado mais íngreme.
* **Decisão:**
    * Escolhemos Python.
* **Consequências:**
    * O desenvolvimento deve ser mais rápido e fácil devido à sintaxe clara e à vasta biblioteca do Python.
    * Pode haver limitações de desempenho em comparação com linguagens compiladas, mas isso é aceitável para a POC.

---

## ADR-002: Arquitetura Baseada em Classes e Interfaces

* **Data:** 2024-07-26
* **Status:** Aprovado
* **Contexto:**
    * Precisamos definir a arquitetura do sistema para garantir organização, modularidade e extensibilidade.
    * A arquitetura deve facilitar a manutenção e a adição de novas funcionalidades.
* **Opções Consideradas:**
    * Arquitetura Procedural:
        * Prós: Simples para projetos pequenos.
        * Contras: Difícil de manter e estender para projetos maiores.
    * Arquitetura Orientada a Objetos (OO):
        * Prós: Promove modularidade, encapsulamento e reutilização de código, facilita a manutenção e a extensão.
        * Contras: Pode ser mais complexo para projetos muito simples.
* **Decisão:**
    * Escolhemos a Arquitetura Orientada a Objetos.
* **Consequências:**
    * O código será organizado em classes e objetos, facilitando a compreensão e a manutenção.
    * A adição de novas funcionalidades será mais fácil devido à modularidade e ao encapsulamento.
    * Pode haver um aumento na complexidade inicial do código.

---

## ADR-003: Estrutura do Projeto em Módulos e Pacotes

* **Data:** 2024-07-27
* **Status:** Aprovado
* **Contexto:**
    * Precisamos organizar os arquivos do projeto para garantir clareza e facilitar a navegação.
    * A estrutura deve refletir a arquitetura do sistema e agrupar arquivos relacionados.
* **Opções Consideradas:**
    * Estrutura Plana (todos os arquivos no mesmo diretório):
        * Prós: Simples para projetos muito pequenos.
        * Contras: Difícil de manter e navegar para projetos maiores.
    * Estrutura Modular (arquivos agrupados em diretórios/pacotes):
        * Prós: Melhora a organização, facilita a navegação e a manutenção, evita conflitos de nomes.
        * Contras: Adiciona um nível de complexidade à estrutura do projeto.
* **Decisão:**
    * Escolhemos a Estrutura Modular.
* **Consequências:**
    * Os arquivos serão organizados em diretórios (pacotes) que representam os diferentes módulos do sistema (por exemplo, `data_source`, `sales_data`, `sales_report`).
    * Isso tornará o projeto mais fácil de entender, navegar e manter.

---

## ADR-004: Formato do Arquivo de Configuração

* **Data:** 2024-07-27
* **Status:** Aprovado
* **Contexto:**
    * Precisamos de um formato para o arquivo que armazenará as configurações das fontes de dados.
    * O formato deve ser fácil de ler e escrever, tanto para humanos quanto para máquinas.
* **Opções Consideradas:**
    * JSON:
        * Prós: Leve, fácil de ler e escrever, amplamente suportado em Python.
        * Contras: Menos flexível que formatos mais complexos.
    * YAML:
        * Prós: Mais legível para humanos que JSON, permite comentários.
        * Contras: Requer uma biblioteca adicional em Python.
    * INI:
        * Prós: Simples para configurações básicas.
        * Contras: Menos adequado para estruturas de dados complexas.
* **Decisão:**
    * Escolhemos JSON.
* **Consequências:**
    * As configurações serão armazenadas em um arquivo `config.json` fácil de ler e modificar.
    * A biblioteca `json` do Python será usada para ler e escrever o arquivo.

---

## ADR-005: Abstração de Fontes de Dados

* **Data:** 2024-07-28
* **Status:** Aprovado
* **Contexto:**
    * Precisamos de uma forma de lidar com diferentes tipos de fontes de dados (CSV, web, etc.) de forma uniforme.
    * A solução deve permitir a adição de novos tipos de fontes de dados no futuro.
* **Opções Consideradas:**
    * Lógica Específica para Cada Fonte:
        * Prós: Simples para um pequeno número de fontes.
        * Contras: Difícil de manter e estender para muitas fontes, código duplicado.
    * Classe Abstrata `DataSource` com Subclasses:
        * Prós: Permite tratar diferentes fontes de forma uniforme, facilita a adição de novas fontes, promove a reutilização de código.
        * Contras: Adiciona um nível de complexidade ao código.
* **Decisão:**
    * Escolhemos a Classe Abstrata `DataSource` com Subclasses.
* **Consequências:**
    * Será criada uma classe abstrata `DataSource` que define a interface para extrair dados.
    * Classes concretas (`LocalDataSource`, `WebDataSource`) implementarão a interface para cada tipo de fonte de dados.
    * Isso tornará o sistema mais flexível e extensível.

---

## ADR-006: Tratamento de Cabeçalho em Arquivos de Dados

* **Data:** 2024-07-29
* **Status:** Aprovado
* **Contexto:**
    * Precisamos lidar com a possibilidade de os arquivos de dados (especialmente CSV) incluírem uma linha de cabeçalho.
    * O sistema deve ser capaz de detectar e ignorar o cabeçalho para evitar erros na formatação dos relatórios.
* **Opções Consideradas:**
    * Assumir que Sempre Há Cabeçalho:
        * Prós: Simples de implementar.
        * Contras: Falha se o arquivo não tiver cabeçalho.
    * Assumir que Nunca Há Cabeçalho:
        * Prós: Simples de implementar.
        * Contras: Falha se o arquivo tiver cabeçalho.
    * Detectar o Cabeçalho Dinamicamente:
        * Prós: Solução mais robusta, funciona com ou sem cabeçalho.
        * Contras: Mais complexo de implementar.
* **Decisão:**
    * Escolhemos Detectar o Cabeçalho Dinamicamente.
* **Consequências:**
    * As classes formatadoras (`TextReportFormatter`, `HTMLReportFormatter`) implementarão a lógica para detectar o cabeçalho (assumindo que a primeira linha com todos os valores string é o cabeçalho).
    * Isso tornará o sistema mais flexível e tolerante a diferentes formatos de arquivos de dados.

---

## ADR-007: Distribuição como Executável

* **Data:** 2024-07-30
* **Status:** Aprovado
* **Contexto:**
    * Precisamos definir como a aplicação será distribuída para os usuários finais.
    * A distribuição deve ser o mais simples possível para facilitar o uso.
* **Opções Consideradas:**
    * Distribuir o Código-Fonte:
        * Prós: Permite aos usuários modificar o código.
        * Contras: Requer que os usuários instalem o Python e as bibliotecas.
    * Distribuir como Executável (usando PyInstaller):
        * Prós: Simplifica a instalação e o uso, não requer a instalação do Python.
        * Contras: O executável pode ser maior que o código-fonte.
* **Decisão:**
    * Escolhemos Distribuir como Executável (usando PyInstaller).
* **Consequências:**
    * A aplicação será empacotada em um executável usando PyInstaller.
    * Os usuários poderão executar a aplicação sem instalar o Python ou bibliotecas.
    * O tamanho do arquivo de distribuição será maior.


## ADR-008: Considerar a migração para Pandas para manipulação de dados
* **Data:** 2025-08-08
* **Status:** Proposto.
* **Contexto:**
    A arquitetura atual do `rpa_gerador_relatorio` utiliza listas de dicionários e um dicionário de resultados consolidados para manipular os dados extraídos das diversas fontes. Essa abordagem é simples, eficaz e suficiente para conjuntos de dados de pequeno a médio porte, onde o desempenho de manipulação de dados em Python puro é adequado.
* **Decisão:**
    A decisão atual é **manter a implementação baseada em dicionários e listas**. Essa abordagem atende aos requisitos atuais de desempenho e complexidade, mantendo a base de código leve e sem dependências externas adicionais, como o Pandas. A refatoração para uma estrutura de dados mais robusta será considerada como uma melhoria futura, caso os requisitos de desempenho, o volume de dados ou a complexidade das análises aumentem.
* **Consequências:**
    * **Positivas:**
        * Manutenção da simplicidade e leveza do projeto.
        * Não há novas dependências externas.
        * O código é mais direto para quem não tem familiaridade com o ecossistema Pandas.
    * **Negativas:**
        * Pode haver gargalos de desempenho caso o volume de dados cresça significativamente, pois as operações de loop em Python puro são mais lentas que as vetorizadas do Pandas.
        * A implementação de análises estatísticas mais complexas exigirá código manual e verboso.
        * A integração com ferramentas de análise de dados ou visualização será menos direta do que com DataFrames do Pandas.
 