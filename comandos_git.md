# Inicializando o Git e Criando uma Branch para Refatoração

A ideia é:

- Salvar o estado atual do projeto funcionando
- Criar uma branch separada para a nova arquitetura MVC
- Trabalhar com segurança sem quebrar a versão original

## 1. Entrar na pasta do projeto

```bash
cd caminho/do/projeto
```

## 2. Inicializar o Git

```bash
git init
```

Isso cria um repositório Git local dentro da raiz do projeto.

## 3. Adicionar todos os arquivos

```bash
git add .
```

## 4. Criar o primeiro commit

```bash
git commit -m "Estado inicial do projeto"
```

Esse commit representa a versão atual funcionando.

## 5. Renomear a branch principal para `main`

```bash
git branch -M main
```

## 6. Criar a branch da nova arquitetura

```bash
git checkout -b feature/mvc-architecture
```

Agora você estará dentro da nova branch.

# Estrutura Final

Você terá:

```text
main
└── versão original estável

feature/mvc-architecture
└── nova arquitetura/refatoração
```

# Como trocar entre branches

Ir para a versão estável:

```bash
git checkout main
```

Ir para a branch da refatoração:

```bash
git checkout feature/mvc-architecture
```

# Fluxo Profissional de Refatoração

Esse é um workflow muito usado em projetos reais:

- `main` fica protegida e estável
- Features grandes são feitas em branches separadas
- Você pode testar, quebrar, reorganizar e experimentar sem risco
- Depois pode juntar tudo usando merge ou pull request

# Exemplo Completo

```bash
cd caminho/do/projeto

git init

git add .

git commit -m "Estado inicial do projeto"

git branch -M main

git checkout -b feature/mvc-architecture
```