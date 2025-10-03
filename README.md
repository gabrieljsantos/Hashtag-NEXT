# Hashtag-NEXT

## Visão Geral

*"O código em questão é um jogo da velha feito em Python usando a biblioteca Pygame para a interface gráfica. O jogo é exibido em uma janela, onde o tabuleiro do jogo da velha é desenhado e o usuário pode jogar clicando nas células do tabuleiro. O jogo suporta dois jogadores e o placar é mantido em uma janela lateral que exibe o número de vitórias do jogador 'X' e do jogador 'O'."*

*"O código possui diversas funções que desenham elementos na tela, como a função `desenhar_tabu()`, que desenha as linhas do tabuleiro, e as funções `desenhar_x()` e `desenhar_o()`, que desenham o 'X' e o 'O' nas células do tabuleiro, respectivamente."*

*"O código também possui funções auxiliares, como a função `rgb_color()`, que converte uma tupla de valores RGB em um valor hexadecimal, e a função `limpar_tabu()`, que limpa o tabuleiro e reinicia o jogo. Além disso, há uma função `debug_function()`, que pode ser usada para imprimir informações de depuração."*

*"O jogo é executado em um loop principal, que trata os eventos da interface gráfica e atualiza a tela. Quando o usuário clica em uma célula do tabuleiro, a função `jogada()` é chamada para atualizar o tabuleiro e verificar se houve um vencedor. Se houver um vencedor, o placar é atualizado e o jogo é reiniciado."*

---

## Estrutura de Versões Legadas

### 1. **Versão Básica Funcional** – `/legacy_v1/Basic_Functional_Version`

* Jogo completo em Python/Pygame.
* Suporta dois jogadores.
* Placar e interface gráfica básicos.
* Código simples, funcional, sem análise avançada.

### 2. **Versão de Análise Heurística (AI)** – `/legacy_v1/AI_heuristic_game_analysis_only`

* Estudos de combinações de jogadas até N movimentos para vitória.
* Sem interface de jogo completa.
* Scripts:

  * `AI_hga_data_gerador.py`: gera dados de jogadas.
  * `AI_heuristic_game_analysis.py`: analisa sequências heurísticas.
* Estado do jogo definido manualmente.

### 3. **Rascunho da Versão 2 (não funcional)** – `/legacy_v1/v2_sandbox`

* Experimentos iniciais de refatoração do código.
* Estrutura POO incompleta.
* Pode servir de base para novas implementações.

### 4. **Legacy Version com temas e histórico** – `/legacy_v1/Legacy_Version`

* Jogo completo com suporte a temas visuais, histórico de partidas e configurações antigas.
* Mantém compatibilidade com implementações antigas.
* Serve como referência para desenvolvimento e testes.

---

## Construção da Versão 2 (Atual)

* Refatoração completa usando **Programação Orientada a Objetos (POO)**.
* Estrutura modular:

  * `models/` → classes de entidades (Jogador, Movimento, Game).
  * `views/` → renderização (ShapeRenderer, BoardRenderer, StatusRenderer).
  * `controllers/` → lógica de seleção e controle do jogo.
  * `utils/` → funções auxiliares e helpers.
* Tabuleiro **dinâmico**, suportando diferentes dimensões.
* Preparado para integração futura com AI e análise de jogadas.

---

## Vídeos de Demonstração

[![Hashtag-NEXT](https://img.youtube.com/vi/lwlirs_dlSI/0.jpg)](https://www.youtube.com/watch?v=lwlirs_dlSI)
[![Hashtag-NEXT](https://img.youtube.com/vi/ow0xaPRF4P4/0.jpg)](https://www.youtube.com/watch?v=ow0xaPRF4P4)
