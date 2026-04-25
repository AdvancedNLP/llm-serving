import ollama

MODEL = 'llama3.2:latest'

if __name__ == '__main__':
    client = ollama.Client(host='http://localhost:11434')

    print("Available models:")
    models = [model.model for model in client.list().models]
    print(models)

    assert MODEL in models, f"{MODEL} not available"

    messages = [
        {
            'role': 'user',
            'content': 'Why is the sky blue? Answer in German',
        },
    ]
    print('Why is the sky blue? Answer in German')
    print('Answer:', end='')
    for chunk in client.chat(MODEL, messages=messages, stream=True):
        print(chunk['message']['content'], end='', flush=True)
