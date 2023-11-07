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

## Volumes
 **Docker volume** - monta o diretório dentro do container\
 **Docekr Bind** - Forma mais antiga de armazenar conteúdo. Mais limitado, faz um link entre o local e o container, criando o caminho ansoluto dele, enquanto o volume cria um novo diretório no caminho de armazenamento do Docker\
 **Tmpfs** - Armazenamento temporário para recursos como dados sensíveis. Só eiste enquanto o container estiver ativo

## Redes de containers

O Docker possui um enderçamento de IP pŕoprio e, portanto, possui uma rede que pode se comunicar entre si, sem rpecisar ser exposta para a internet. É possível criar redes próprias tbm, caso necessário.

**Tipos de redes**

*Bridge:* plugin default de rede. Cria a comunicação entre os containers de forma que eles possam se comunciar dentro de ecossistemas isolados. Cria resolução DNS, em que se pode dar nomes aos containers e conecar usando esses nomes\
*Host:* usa a rede do host e a compartilha. O que fo r válido como rede para a máquina em que o Docer está rodando, será válido para o container tbm.\
*Overlay:* qdo se tem host distribuídos, utiliza-se o formato overlay, que permtie a comunicação segura entre diversos componentes, como serviços em máquinas diferentes

## Docker compose 
auxilia a criar stacks completas, utilizando componentes do Docker como imagens, variáveis de ambiente, protas, etc..

## Orquestradores 
Ajudam a usar containers de forma prática e efetiva, garantindo controle, estado e saúde das apps, mesmo que haja centenas de containers; permite o uso de health checks, segmentação de apps em contextos, armazenamento de dados sensíveis, etc..
O mais famoso é o Kubernetes.
