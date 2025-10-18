import ollama

if __name__ == '__main__':
    client = ollama.Client(host='http://localhost:11434')
    print(f'{client.list()=}')

    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue? Answer in German',
        },
    ]
    print('Why is the sky blue? Answer in German')
    print('Answer:', end='')
    for chunk in client.chat('llama3.2:latest', messages=messages, stream=True):
        print(chunk['message']['content'], end='', flush=True)
