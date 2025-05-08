from openai import OpenAI

# insira sua api aqui 
client = OpenAI(api_key="")

# funcao para chamar e receber resposta do chat
def chat(mensagem):
    resposta_chat = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um amigo que vai conversar comigo respondendo de forma descontraída como se fosse um amigo, porem sempre responde meus questionamentos."},
        {"role": "user", "content": mensagem}
    ],
    max_tokens=800
    )
    resposta = resposta_chat.choices[0].message.content
    return resposta

# looping de ficar fazendo as perguntas
while True:
    pergunta = input("Digite sua pergunta (ou digite sair para sair): ")
    if pergunta.lower() == 'sair':
        break
    try:
        print(f"{chat(pergunta)}")
    except ValueError:
        print("Entrada inválida. Por favor, insira dois números inteiros.")