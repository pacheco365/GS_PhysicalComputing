# 📌 Projeto - Sistema de Avaliação de Agachamentos com MediaPipe

## 🚩 Descrição do Problema

Durante treinos realizados sem supervisão profissional, muitos indivíduos realizam exercícios de maneira incorreta, podendo levar a eventuais lesões ou baixo desempenho. O agachamento é um dos exercícios mais comuns onde a má execução pode prejudicar significativamente o praticante.

## 🔧 Visão Geral da Solução

Este projeto propõe um sistema automatizado, utilizando Python e MediaPipe, para analisar vídeos de exercícios físicos, verificando se a execução do movimento está correta e realizando a contagem das repetições automaticamente. No caso específico deste projeto, focamos na execução de agachamentos.

## ⚙️ Como Funciona

* **Configuração do MediaPipe**:

  * Utilizamos o MediaPipe Pose para capturar pontos anatômicos chave do corpo humano.
* **Cálculo do Ângulo**:

  * Calculamos ângulos entre três pontos para identificar o grau correto das articulações (por exemplo, o joelho).
* **Definição das Posições do Corpo**:

  * Identificamos pontos específicos como quadris, joelhos e tornozelos para realizar a análise.
* **Verificação da Execução**:

  * O movimento é considerado correto se o ângulo do joelho estiver abaixo de 90 graus durante a fase baixa do agachamento.
* **Função para Contagem de Repetições**:

  * Dentro desta função, são feitas verificações constantes para assegurar que cada repetição contada tenha sido corretamente executada.

## 🎯 Objetivo

* Permitir que usuários realizem treinos sozinhos, garantindo que executem movimentos corretamente.
* Evitar eventuais lesões causadas pela execução incorreta.
* Oferecer uma contagem automática e precisa das repetições feitas durante o exercício.
* Auxiliar na manutenção de uma boa performance em exercícios físicos.

## 📽️ Vídeo Demonstrativo

[Vídeo]

## 💻 Código Fonte

O código completo está disponível neste repositório GitHub.

## 🧑‍🤝‍🧑 Integrantes

* Danilo Urze Aldred - RM: 99465
* Gabriel Pacheco - RM: 550191
* Pedro Henrique Oliveira Ananias - RM:550689
