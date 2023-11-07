# Docker

Usa-se containers para isolar e otimizar aplicações e serviços. 
Encapsula e compartilha os recursos.

## Dockerfile
FROM - Base de SO que pode ser customizado. Servirá de base para as demais config.\
WORKDIR - Acessa um diretório\
ENV - Adiciona variáveis de ambiente\
RUN - Roda comando em tempo de execução\
CMD - Roda comando após o início do container, permitindo que o processo seja prioritáio(caso seja usada a instrução ENTRYPOINT, a prioridade será dele e CMD será usado como argumento)\
LABEL - versão da aplicação

## Imagens

Imutabilidade - o conteúdo da imagem docker deve ser o mesmo, para que, o projeto rode em qqr máquina, independendo do SO.

no mesmo nível do arquivo dockerfile:
docker build -t nomeImage .

