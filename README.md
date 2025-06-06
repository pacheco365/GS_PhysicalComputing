# 📌 Sistema de Avaliação de Agachamentos com MediaPipe

---

## 📝 Descrição do Problema

Durante treinos realizados **sem supervisão profissional**, muitos indivíduos realizam exercícios de maneira incorreta, podendo levar a **eventuais lesões** ou **baixo desempenho**. O agachamento é um dos exercícios mais comuns onde a má execução pode prejudicar significativamente o praticante.

---

## 🚀 Visão Geral da Solução

Este projeto propõe um sistema automatizado, utilizando **Python** e **MediaPipe**, para analisar vídeos de exercícios físicos, **verificando se a execução do movimento está correta** e realizando a **contagem das repetições automaticamente**.  
No caso específico deste projeto, focamos na execução de **agachamentos**.

---

## ⚙️ Como Funciona

- **Configuração do MediaPipe**
  - Utilizamos o MediaPipe Pose para capturar pontos anatômicos chave do corpo humano.
- **Cálculo do Ângulo**
  - Calculamos ângulos entre três pontos para identificar o grau correto das articulações (por exemplo, o joelho).
- **Definição das Posições do Corpo**
  - Identificamos pontos como quadris, joelhos e tornozelos para realizar a análise.
- **Verificação da Execução**
  - O movimento é considerado correto se o ângulo do joelho estiver abaixo de 90 graus durante a fase baixa do agachamento.
- **Função para Contagem de Repetições**
  - Dentro desta função, são feitas verificações constantes para assegurar que cada repetição contada tenha sido corretamente executada.

---

## 🎯 Objetivo

> Garantir a **correta execução** do exercício agachamento em treinos autônomos, proporcionando:
>
> - **Evitar lesões**
> - **Contagem automática de repetições**
> - **Feedback visual sobre execução**
> - **Auxílio à boa performance em exercícios físicos**

---

## 🎥 Vídeo Demonstrativo

<p align="center">
  <a href="COLE_AQUI_O_LINK_DO_VIDEO">
    <img src="https://img.youtube.com/vi/ID_DO_VIDEO_AQUI/0.jpg" alt="Vídeo demonstrativo" width="400"/>
  </a>
</p>

> [Clique aqui para assistir ao vídeo demonstrativo](COLE_AQUI_O_LINK_DO_VIDEO)

---

## 💻 Código Fonte

O código completo está disponível neste repositório.

---

## 👨‍💻 Integrantes

| Nome                            | RM      |
|---------------------------------|---------|
| Danilo Urze Aldred              | 99465   |
| Gabriel Pacheco                 | 550191  |
| Pedro Henrique Oliveira Ananias | 550689  |

---
