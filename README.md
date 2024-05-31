# resumo-aulas
Este projeto destina-se a estudantes que desejam gravar e resumir as suas aulas de forma eficiente.
O sistema permite a transcrição do áudio das aulas, gera um resumo conciso e divide o conteúdo por tópicos, proporcionando uma maneira organizada e fácil de estudar.

Funcionalidades
Conversão de Áudio: Converte ficheiros de áudio em formato MP3 para WAV para facilitar a transcrição.
Transcrição de Áudio: Utiliza o Google Speech Recognition para transcrever o áudio da aula para texto.
Resumo de Texto: Gera um resumo conciso do texto transcrito utilizando a API da OpenAI.
Divisão por Tópicos: Divide o texto transcrito em tópicos principais para facilitar a revisão do conteúdo.
Armazenamento de Resultados: Salva a transcrição, o resumo e os tópicos em ficheiros de texto (transcricao.txt, resumo.txt e topicos.txt).
Como Usar
Pré-requisitos:

Python 3.7 ou superior
Instalar as dependências:
sh
pip install openai speechrecognition pydub
FFmpeg instalado e configurado no PATH do sistema.
Configurar a Chave API da OpenAI:

Obtenha a sua chave API da OpenAI e substitua 'a_sua_chave_api_aqui' pela sua chave no código.
Executar o Script:

Altere o caminho do ficheiro de áudio na função main para o ficheiro que deseja transcrever e resumir.
Execute o script:
sh
Copiar código
python resumo_aulas.py
Resultados:

O script gera três ficheiros de texto:
transcricao.txt: Contém o texto transcrito da aula.
resumo.txt: Contém o resumo da aula.
topicos.txt: Contém os tópicos principais da aula.
Exemplos de Utilização
Gravar Aulas: Ideal para estudantes que desejam gravar as suas aulas e obter um resumo organizado por tópicos.
Revisão de Conteúdo: Facilita a revisão do conteúdo da aula através de tópicos bem definidos.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

Licença
Este projeto está licenciado sob a licença MIT. Veja o ficheiro LICENSE para mais detalhes.
