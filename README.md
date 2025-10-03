# Hashtag-NEXT

**Descrição:**
Hashtag-NEXT é um jogo da velha desenvolvido em Python utilizando a biblioteca **Pygame** para a interface gráfica. O jogo exibe um tabuleiro interativo, permitindo que os jogadores realizem suas jogadas clicando nas células. O placar é atualizado em tempo real em uma aba lateral, mostrando as vitórias de cada jogador (X e O).

**Recursos principais:**

* Desenho dinâmico do tabuleiro com a função `desenhar_tabu()`.
* Desenho de símbolos X e O com as funções `desenhar_x()` e `desenhar_o()`.
* Placar lateral atualizado automaticamente com `desenhar_score()` e `desenhar_aba_status()`.
* Função `limpar_tabu()` para reiniciar o tabuleiro entre partidas.
* Sistema de logs e histórico de execução com `output()`.
* Função de depuração `debug_funcion()` para auxiliar no desenvolvimento.
* Escolha automática da máquina em modos PvE, com jogadas estratégicas iniciais (`machine_choice()`, `jogada_inicial_estrategica()`).

**Arquitetura e variáveis globais:**

* **Variáveis de estado do jogo:**

  * `jogadas`: lista que mantém o estado do tabuleiro.
  * `vez_de_jogar`: define qual jogador está ativo (1 para X, -1 para O).
  * `win_n_x` / `win_n_o`: mantêm o score atual de X e O.
  * `finalizado`: indica se a partida atual terminou.
* **Combinações de vitória:**

  * `x_win` e `o_win`: listas de tuplas representando posições vencedoras.
* **Configurações de interface:**

  * `tabu_size`, `line_spacing_x`, `line_spacing_y`, `window_status_size` e `line_size` controlam dimensões do tabuleiro e linhas.
  * Cores configuráveis via arquivo `themes.ini`.

**Loop principal:**
O jogo roda em um loop que:

1. Processa eventos do Pygame (cliques, fechamento de janela).
2. Atualiza o tabuleiro e a aba de status.
3. Gerencia a jogada de cada jogador ou da máquina.
4. Verifica vitória, empate ou continuidade da partida.
5. Atualiza o placar e reinicia a partida quando necessário.

**Observação sobre versões:**
A versão anterior do código, sem funcionalidades avançadas, está disponível em `/Basic_Functional_Version`.

## Vídeos

[![Hashtag-NEXT](https://img.youtube.com/vi/lwlirs_dlSI/0.jpg)](https://www.youtube.com/watch?v=lwlirs_dlSI)
[![Hashtag-NEXT](https://img.youtube.com/vi/ow0xaPRF4P4/0.jpg)](https://www.youtube.com/watch?v=ow0xaPRF4P4)
