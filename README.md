# SupportMind AI

Sistema Inteligente de Atendimento e Suporte Técnico com Inteligência Artificial. Criado com objetivo de estudo e prática de programação Full Stack com integração de IA.

## 📖 Visão Geral

O SupportMind AI é uma plataforma que automatiza parte do fluxo de atendimento ao cliente por meio de Inteligência Artificial Generativa e Retrieval-Augmented Generation (RAG).

A solução recebe tickets de suporte, classifica automaticamente o problema, consulta uma base de conhecimento corporativa e sugere respostas para atendentes, aumentando a produtividade das equipes de suporte e melhorando a experiência dos clientes.

---

## 🎯 Problema

Equipes de suporte frequentemente enfrentam:

* Grande volume de tickets
* Respostas repetitivas
* Tempo elevado de resolução
* Dificuldade em encontrar documentação relevante
* Falta de métricas consolidadas sobre atendimento

O SupportMind AI busca reduzir esses problemas utilizando IA aplicada ao fluxo de suporte.

---

## 🚀 Funcionalidades

### Atendimento Inteligente

* Recebimento de tickets
* Classificação automática por categoria
* Priorização de chamados
* Sugestão de respostas com IA

### Base de Conhecimento

* Indexação de documentos
* Busca semântica
* Recuperação contextual de informações
* Sistema RAG (Retrieval-Augmented Generation)

### Painel Gerencial

* Tempo médio de resposta
* Volume de tickets
* Categorias mais frequentes
* Taxa de resolução

---

## 🏗️ Arquitetura

```text
Cliente
   │
   ▼
Frontend (React)
   │
   ▼
FastAPI Backend
   │
   ├── Classificação de Tickets
   ├── Motor RAG
   ├── Sugestão de Respostas
   └── Analytics
   │
   ▼
PostgreSQL
   │
   ▼
Vector Database
(ChromaDB)
   │
   ▼
LLM
(Ollama)
```

---

## 🛠️ Stack Tecnológica

### Backend

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic

### Inteligência Artificial


* Ollama
* Embeddings
* ChromaDB
* RAG

### Frontend

* React
* Tailwind CSS

### DevOps

* Docker

### Testes

* Pytest

---

## 📂 Estrutura do Projeto

```text
supportmind-ai/

├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   └── services
│   │
│   └── main.py
│
├── frontend/
│
├── docs/
│
├── tests/
│
├── alembic/
│   ├── versions/
│   └── env.py
├── alembic.ini
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔄 Fluxo do Sistema

1. Cliente abre um ticket.
2. O ticket é armazenado no banco de dados.
3. A IA classifica automaticamente o assunto.
4. O motor RAG consulta a base de conhecimento.
5. O LLM gera uma sugestão de resposta.
6. O atendente revisa e envia a resposta ao cliente.
7. Os dados são registrados para análise gerencial.

---

## 📌 Roadmap

### Fase 1 — MVP

* [x] Estrutura inicial FastAPI
* [x] PostgreSQL
* [x] SQLAlchemy + Alembic
* [x] Dockerização da aplicação
* [x] CRUD de usuários
* [x] CRUD de tickets e associação ao usuário
* [x] Autenticação e autorização

### Fase 2 — IA

* [ ] Integração com OpenAI/Ollama
* [ ] Classificação automática de tickets
* [ ] Embeddings
* [ ] Busca semântica

### Fase 3 — RAG

* [ ] ChromaDB ou Qdrant
* [ ] Indexação de documentos
* [ ] Recuperação contextual
* [ ] Respostas fundamentadas em documentos

### Fase 4 — Frontend

* [ ] Dashboard React
* [ ] Visualização de tickets
* [ ] Painel de métricas

### Fase 5 — Produção

* [ ] Testes automatizados
* [ ] CI/CD
* [ ] Observabilidade
* [ ] Deploy em nuvem

---

## 🎓 Objetivos de Aprendizado

Este projeto está sendo desenvolvido como estudo prático de:

* Engenharia de Software
* APIs REST
* Inteligência Artificial Generativa
* Engenharia de Prompt
* RAG
* Bancos Vetoriais
* Docker
* Arquitetura de Sistemas
* Desenvolvimento Full Stack

---

## 👨‍💻 Autor

**Itsem Andrade**

Médico Internista em transição para Engenharia de Dados, Inteligência Artificial e Desenvolvimento Full Stack.

Projeto desenvolvido para aprofundar conhecimentos em desenvolvimento de software, sistemas distribuídos e aplicações de IA em cenários reais de negócio.
