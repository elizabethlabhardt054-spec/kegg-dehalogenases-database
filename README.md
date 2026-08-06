# Catalogação de Deshalogenases: Enzimas, Coculturas e Catalisadores (KEGG Database)

## 📌 Apresentação
Este repositório reúne dados tabulados e extraídos do **KEGG (Kyoto Encyclopedia of Genes and Genomes)** focados no processo de deshalogenação biológica e química de contaminantes organoclorados.

---

## 🧬 1. Enzimas Deshalogenases (Número EC)
Catalogação por código de enzima, vias de reação e micro-organismos associados:
* **EC 3.8.1.5:** Haloalkane dehalogenase
* **EC 3.8.1.2:** (S)-2-haloacid dehalogenase
* **EC 3.8.1.3:** Haloacetate dehalogenase
* **EC 4.5.1.5:** Dichloromethane dehalogenase

---

## 🧫 2. Coculturas e Redes Sintróficas
Estudo da cooperação entre diferentes espécies microbianas para viabilizar a deshalogenação:
* **Sintrofia de Hidrogênio ($H_2$):** Micro-organismos doadores de elétrons (*Geobacter*, *Sulfurospirillum*) em parceria com respiradores de organohaletos (*Dehalococcoides*).
* **Troca Interespécies de Cofatores:** Transferência e suprimento de corrinoides/cobamidas (Vitamina B12) essenciais para a ativação das enzimas.

---

## ⚙️ 3. Catalisadores e Cofatores
Mapeamento dos centros metálicos, cofatores biológicos e mediadores redox:
* **Cofatores Organometálicos:** Cobalaminas (`C00194`), Coenzima F430 (`C01815`).
* **Clusters Metálicos:** Centros de Ferro-Enxofre (`C00023` - [4Fe-4S]).
* **Catalisadores Químicos e Biomiméticos:** Redução catalítica acoplada a metais de transição ($Fe^0$, $Pd$).

---

## 📁 Estrutura de Arquivos
* `data/raw/`: Dados brutos extraídos diretamente das APIs do KEGG.
* `scripts/`: Códigos de automação para extração de dados em Python.
