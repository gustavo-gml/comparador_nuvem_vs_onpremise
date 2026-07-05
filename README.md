# Simulador de TCO: On-Premise vs Cloud Computing (AWS e Azure)

## Descrição do Projeto
Este repositório contém uma ferramenta de simulação desenvolvida em Python para calcular e comparar o Custo Total de Propriedade (TCO) de infraestruturas de TI. O algoritmo projeta cenários financeiros de curto, médio e longo prazo (até 10 anos), confrontando um ambiente físico local (*On-Premise*) com soluções de Nuvem Pública (Infraestrutura como Serviço - IaaS) da Amazon Web Services (AWS) e Microsoft Azure.

Este projeto foi desenvolvido como parte integrante de um artigo da disciplina de Metodologia Científica focado na análise de viabilidade financeira e eficiência energética para empresas de médio porte que utilizam o ERP TOTVS Protheus.

## Funcionalidades Principais
* Cálculo de depreciação contábil e obsolescência de hardware (ciclos de 5 anos).
* Projeção de despesas de capital (CapEx) baseada em servidores corporativos.
* Cálculo de despesas operacionais (OpEx) locais, incluindo consumo elétrico tarifado (Enel SP), índice de eficiência PUE e contratos de manutenção.
* Conversão cambial e projeção de custos plurianuais em nuvem utilizando instâncias reservadas (*Savings Plans*).
* Geração de relatórios comparativos evidenciando o ponto de equilíbrio e a disparidade de custos ao longo de uma década.

## Escopo Tecnológico Analisado
Para garantir a paridade técnica, a simulação utiliza o dimensionamento de 32 threads (vCPUs) e 128 GB de memória RAM nos três cenários:

| Cenário | Arquitetura / Instância | Modalidade |
| :--- | :--- | :--- |
| **On-Premise** | Dell PowerEdge R570 (Intel Xeon 6) | Aquisição Física (CapEx + OpEx) |
| **AWS** | EC2 m6i.8xlarge + EBS gp3 | Nuvem (Savings Plan 3 anos - No Upfront) |
| **Azure** | D32s_v6 + Premium SSD v2 | Nuvem (Instância Reservada 3 anos) |

## Pré-requisitos
* Python 3.8 ou superior instalado.
* Bibliotecas padrão do Python (nenhuma dependência externa pesada é estritamente necessária).

## Como Executar
1. Clone este repositório para a sua máquina local.
2. Navegue até o diretório raiz do projeto.
3. Abra o terminal ou prompt de comando.
4. Execute o script principal rodando o comando `python simulador_tco.py`.
5. Os resultados consolidados serão impressos diretamente no console.

## Licença
Este projeto está sob a licença MIT. Sinta-se livre para utilizá-lo e adaptá-lo para os seus próprios estudos de viabilidade.
