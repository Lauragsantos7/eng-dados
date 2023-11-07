# Redes e sistemas

- Redes são um conjunto de dois ou mais dispositivos eletrônicos conectados entre si, que trocam informações por meio de uma linguagem prś-estabelecida chamada protocolo.

A conexão pode ser por meio físico ou wireless

Origem da redes: Darpa - dpto defesa dos EUA - desenvolveu sist pra melhorar a  comunicação na guerra fria entre EUA e URSS.

Arpanet - (Advanced Research Projects Agency Network, em português, Rede da Agência de Pesquisas em Projetos Avançados) foi a primeira rede de computadores, construída em 1969 como um meio robusto para transmitir dados militares sigilosos e para interligar os departamentos de pesquisa por todo os Estados Unidos. Nos anos 1980, mais precisamente em 1983, a ARPANET trocou o protocolo NCP pelo novo TCP/IP. O IP (internet protocol ou protocolo de internet) tornou-se a espinha dorsal da infraestrutura de informação global. 

##  Infraestrutura

NIC - Network Interface Card - Placa de rede - permite a conexão do PC com o cabo de rede Ethernet ou por wireless. End físico(mac) e lógico(IP)

Hub - conexão entre dispositiovs atravez de cabos de par trançado e conectados entre si. Não gere canais, todo mundo 'conversa' com todo mundo.

Switch - conecta os dispositivos, permite conexão ponta a ponta, sem relação com PCs que não são destinatários da comunicação. 

Roteador - procura as melhores rotas na internet para entregar os pacotes do remetende ao destinatário no menor tempo possível.

Modem - modulação e demodulação do sinal de internet

## Cabeamento

Padrões estabelecidos que definem como serão as organizações do cabos e seus periféricos possibilitando melhor performance na rede. 
Normas: NBR14.565, ANSI/TIA 568, ANSI/TIA 569
Definem quais cabos, velocidade, organização, latência, etc...

Cabo de par trançado: cobre com  fios e cada fio tem uma responsabilidade. UTP - sem isolamento, os fios são diretamente ligados entre sim. Mais interferências. Já o STP, há isolamento entre os fios, e envolto em alumínio para diminuir interf.

Cabo coaxial: cobre com isolamento em silicone e outra cobertura de cobre. Utilizado na conexão com modens, tc a cabo, etc..

Fibra ótica: pedaços de vidro que permitem a propagação do raio de luz, que são conertidos nas extremidades das fibras. Pode ser monomodo ou multimodo

Rack: é um armario para hospedar os equipamentos de hardware como switches, roteadores, modens, fibras óticas e organizar os cabos em patch panels. Essencial em data centers (igual ao do adm)

## Modelo OSI e TCP/IP

Modelo OSI - 7 camadas\  
**Aplicação** - protoc. DNS, SSH, mais próxima do usuário\
**Apresentação** - criptografia\
**Sessão** - como será a comunic. entre origem e destino final.\ 
**Transporte** - o dado chega aqui em forma de segmento. Conexão com  o destinat. final por meio de dos protoc TCP(solicitação de confirm de recebimento ou erro e reenvio, se necessário) ou UDP(não confirma o recebimento, se houver erro não haverá o reenvio - para conexoes rápidas, streams, etc)\
**Rede** - onde acontece o envio dos dados. O dado passa de segmento a pacote a ser enviado ao roteador.\
**Enlace** - fragmenta o pacote em quadros que serão enviados. Consulta o endereço físico para saber pra onde enviar o dado.\
**Física** - os hardwares e periféricos utlizados - cabos, switches...

Modelo TCP - 4 camadas\
**Aplicação** - corresponde a Aplic. Apresent e Sessão\
**Transporte**\
**Internet** - corresp. à Rede\
**Acesso à Rede** - corresp à Enlace e Física

Info saindo do Pc do usuário: de cima para baixo. Resposta recebida pelo PC: de baixo para cima

## Endereços IP

O roteador faz o roteamento dos dados através do endereço IP. Ip é um protocolo responsável por gerar o endereço ao computador, ou qqr servidor, no momento em que ele se conecta à internet.\
IPV4 - 32 bits, divididos em 8 octetos, em que cada octeto vai de 0 a 255. Máximo de 4 bi de dispositivos

NAT - um único IP público e vários IPs locais, que se conectam ao modem para emitir e receber dados.

IPV6 - 128 bits, dividido em 16 pares - 


byte => 8 bits

### Cálculo de sub-redes
A rede principal de uma empresa, por ex., é dividida em sub-redes de acordo com os setores (RH, TI, Vendas..) é haverá comunicação entre elas apenas se houver  uma rota estabelecida.

QOS - cada setor, ou sub-rede tem o recurso de rede apenas de que necessita.

O primeiro octeto varia para saber a qual classe a sub-rede pertence

| Classe | prim. octeto |
| -------|------ |
| A | 0 a 127 |
| B | 128 a 191 |
| C | 192 a 223 |
| D | 224 a 139 |
| E | 240 a 255 |

transformando IP em binário:
192.168.10.1

bit = 8 bites, então eleva-se 2 oito vezes:\
2 ^ 0 = 1
2 ^ 1 = 2
2 ^ 2 = 4
2 ^ 3 = 8
2 ^ 4 = 16
2 ^ 5 = 32
2 ^ 6 = 64
2 ^ 7 = 128

Pega o primeiro octeto e divide pelos resultados da exponenciação:\ 192 / 128 = 1 e sobra 64

6 / 64 = 1 e sobra 0

Não é possível fazer as outras divisões pq não é possivel dividir zero.\
Então fica 11000000

168 / 128 = 1 e sobra 40\
40 / 64 = 0,alguma coisa (não faz o cálculo, so usa o zero)\
10 / 32 = 1 e sobra 8\
8 / 16 = 0\
8 / 8 = 1 e sobra 0\
0 / 4 = 0\
0 / 2 = 0\
0 / 1 = 0

Segundo octeto fica 10101000

Terceiro octeto = 00001010

Quarto octeto = 000000001

=> 3 primeiros octetos não variam, são o endereço de rede\
=> o último octeto varia de acordo com qtos IPS estão disponíveis


## Domínio, DNS e latência

Domínio ->  Servidores raízes recebem a req e passam para os serv responsáveis, os chamdos TLPs - Top Level Domain(.com, .org, .gov)

https://www.umbler.com/br\
https:// - protocolo\
www - subdomínio\
umbler - domínio\
com - TLD\
br - subdiretório\

Latência - tempo de duração da requisição da origem até o destino.


## Segurança da informação

Física: sistema anti-incêndio, backup, acesso biométrico ao datacenter, desabilitar entrada de periféricos, atualização do SO..

Lógica:\
SSO -  Single Sign On: 'entrar com a conta do google',\
Firewall\
VPN\

## Wireless
banda: canal 5.0 Ghz
frequência: faixa (velocidade)

