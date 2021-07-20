#Iniciando
Apos a instalação das dependências do projeto (pandas, tkinter), o código deverá ser executado em uma versão python superior a 3.0.
Nenhum parâmetro adicional deverá ser passado junto com a execução do algoritmo.
Se tudo ocorrer bem, a interface da calculadora será exibida, e serão dispostas as caixas para a inserção dos parâmetros Direction data, modulation order, Bandwidht, aggregated carries, MIMO layers, Frame, Spacing Carries e Scaling factor.
Todos os parâmetros acima são parâmetros de entrada. Na parte inferior da interface irão ser impressos os parâmetros de saída, calculados com base nos parâmetros de entrada.
Uma informação de Log nos parâmetros de saída será apresentada sempre que houver uma incoerência nos parâmetros de entrada, como por exemplo usar o FR1 com um espaçamento de 200kHz.
Os parâmetros de saída será o valor do Throughput, numerologia, número de PRBs e Overhead.
O número de PRBs será calculado com base nas tabelas da norma para frames 1 e 2, e serão obtidos a partir da banda e do espaçamento de portadoras.
