# ChatBot - Script Base para MeCorrige

Este é um script simples desenvolvido com a API da OpenAI, utilizado como **base de estudo** para a criação do projeto [MeCorrige](https://github.com/david-uzkk/MeCorrige).

## ✨ Sobre

O script roda diretamente no terminal e permite uma conversa contínua com um assistente virtual que responde de maneira descontraída, como um amigo. Ele foi fundamental para entender o funcionamento básico da API da OpenAI e para testar ideias que evoluíram no projeto final.

## 💡 Funcionalidades

- Conecta-se à API da OpenAI (modelo GPT-4o-mini)
- Responde mensagens de forma casual, como um amigo
- Executa loop contínuo de perguntas e respostas
- Permite encerrar a conversa com o comando `sair`

## 🧠 Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale a biblioteca necessária:**
```bash
pip install openai
```

4. **Configure sua chave da API:**
```bash
client = OpenAI(api_key="sua-api-key-aqui")
```

5. **Execute o script:**
```bash
python nome_do_arquivo.py
```