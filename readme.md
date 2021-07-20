#Iniciando
Apos a instalação das dependências do projeto (pandas, tkinter), o código deverá ser executado em uma versão python superior a 3.0.
Nenhum parâmetro adicional deverá ser passado junto à execução do algoritmo.
Se tudo ocorrer bem, a interface da calculadora será exibida, e serão dispostas as caixas para a inserção dos parâmetros Direction data, modulation order, Bandwidht, aggregated carries, MIMO layers, Frame, Spacing Carries e Scaling factor.
Todos os parâmetros acima são de entrada. Na parte inferior da interface serão impressos os parâmetros de saída, calculados com base nos parâmetros de entrada.
Um Log será informado junto aos parâmetros de saída sempre que houver uma incoerência com as entradas definidas, por exemplo, usar o FR1 com um espaçamento de 200kHz.
Os parâmetros de saída serão o valor do Throughput, numerologia, número de PRBs e Overhead.
O número de PRBs será calculado com base nas tabelas da norma para o range de frequências 1 e 2, e serão obtidos a partir da banda e do espaçamento de portadoras.
