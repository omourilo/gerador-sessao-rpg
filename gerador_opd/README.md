# 👁️ Ordo Realitas - Gerador Procedural de Missões

Este é um sistema de Inteligência Artificial baseada em regras e geração procedural, desenvolvido para mestres do sistema de RPG **Ordem Paranormal**. O objetivo é gerar One-Shots (missões curtas) balanceadas para grupos de NEX 10% a 20%, garantindo coesão narrativa entre elementos, locais e reviravoltas.

## 🚀 Funcionalidades
- **Lógica de Elementos:** O sistema garante que ganchos, monstros e locais pertençam ao mesmo domínio elemental (Sangue, Morte, Energia ou Conhecimento).
- **Escada de Perigo:** Gera automaticamente uma sequência de encontros (2 Básicos, 1 Médio e 1 Boss).
- **Sistema de Twists:** Adiciona reviravoltas narrativas baseadas no elemento da missão.
- **Exportação Automática:** Salva cada missão gerada em um arquivo `.txt` formatado para consulta rápida.

## 🛠️ Tecnologias e Conceitos Aplicados
- **Linguagem:** Python 3.10+
- **Arquitetura:** Modular com separação de responsabilidades (Data, Engine, Utils).
- **Engenharia de Dados:** Manipulação de arquivos JSON para armazenamento de ameaças e lógica de jogo.
- **Princípios SOLID:** Baixo acoplamento e alta coesão através de composição de objetos.

## 📂 Estrutura do Projeto
- `data/`: Contém o banco de dados das ameaças e ganchos em JSON.
- `src/engine.py`: O "cérebro" do projeto, contendo a lógica de filtragem e montagem.
- `src/utils.py`: Funções auxiliares para manipulação de arquivos e datas.
- `main.py`: Ponto de entrada da aplicação.

## 📖 Como usar
1. Certifique-se de ter o Python instalado.
2. Clone o repositório.
3. Execute `python main.py`.

---
Desenvolvido por Murilo Arruda - Estudante de Engenharia de Software.