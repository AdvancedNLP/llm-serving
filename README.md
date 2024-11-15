# llm-serving

### Step 4: Interacting with the Model via Open WebUI

Now that the model has been successfully downloaded and tested, it’s time to interact with it through the **Open WebUI** interface. This step will guide you through launching the web interface, creating a local account, and chatting with the model running on **Ollama**.

#### Goal

The goal of this step is to access the **Open WebUI** in your browser, create a user account (locally), and start interacting with the **Llama 3.2** model that is running on **Ollama**.

#### Instructions

1. Ensure the **Ollama** and **Open WebUI** services are still running. If they are not, restart them:

```bash
docker-compose up ollama open-webui
```

2. Open your browser and navigate to the **Open WebUI** at:

```
http://localhost:3000'
```

3. You will be prompted to create an account. **Rest assured, all information you provide remains stored locally on your machine and does not leave your environment**. This ensures your privacy and control over any data you input.

4. Once your account is created, you will be taken to the chat interface, where you can start interacting with the **Llama 3.2** model.

5. Enter a question or prompt in the chat input field, and the model will respond based on the **Ollama** service running in the background. For example, you could ask:

   "What is the capital of France?"

6. The model will process your input and generate a response directly in the chat window.

#### What You’ve Achieved

By completing this step, you have:
- Launched the **Open WebUI** in your browser.
- Created a local account, ensuring that your data remains private and secure.
- Successfully interacted with the **Llama 3.2** model through a user-friendly chat interface.

This step marks the completion of your interactive environment setup, allowing you to continue exploring and experimenting with the language model.

Now continue with the next step. Switch the branch with:

```bash
git switch step_05
```

and continue with [Step 5](https://github.com/AdvancedNLP/llm-serving/tree/step_05)

