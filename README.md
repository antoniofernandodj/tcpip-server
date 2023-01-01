# tcpip-server

Este projeto teve como objetivo exercitar os conceitos de programação orientada a objetos desenvolvidos com a leitura do livro 'Python 3 Object Oriented Programming' do autor 'Dusty Philips' da PACKT PUBLISHING.

O projeto foi desenhado para a usabilidade ser parecida com o Flask, e consiste num servidor TCP/IP. Em que o uso se dá da seguinte forma:

1. Instancia-se a classe Server principal com app = Server().
A classe Server está em server.py
1. Cadastram-se ações com @app.register_action, similar a como no Flask se cadastram rotas.
3. Após o cadastro das ações, ele escuta numa dada porta com app.listen(port).
4. Quando um cliente se conecta na mesma porta da aplicação de servidor,
ele recebe um menu com a lista das ações cadastradas e seus respectivos atributos.
O exemplo de aplicação cliente está em client.py
5. Ao digitar via linha de comando qual ação se quer usar e quais atributos, o servidor executa tal ação remotamente.
6. Este projeto é executado usando python puro, e nenhuma dependencia externa.
Nenhuma instalação se faz necessário
