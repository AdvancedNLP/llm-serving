# llm-serving

### Step 2: Downloading a Large Language Model with Ollama

Now that the **Ollama** service is running, we need to download a large language model (LLM) to use for processing. In this step, we will invoke the **Ollama** command-line interface (CLI) to download a model directly into the runtime environment.

#### Goal

The goal of this step is to pull the latest version of the **Llama 3.2** model into the **Ollama** service. This will allow us to use the model for tasks such as answering questions or generating text through the **Open WebUI**.

#### Instructions

1. Ensure that the **Ollama** and **Open WebUI** services are still running from the previous step. If not, start them again:

```bash
docker-compose up ollama open-webui
```

2. To download the Llama 3.2 model, execute the following command in your terminal:

```bash
docker compose exec ollama ollama pull llama3.2:latest
```

3. This command uses Docker to execute the Ollama CLI inside the running container, telling it to pull the *Llama 3.2* model. The `latest tag ensures that you're pulling the most recent version of the model.

Wait for the download to complete. Depending on your internet connection, this might take some time as the model can be quite large.

#### What You’ve Achieved
By completing this step, you have:

Successfully downloaded the Llama 3.2 model into the Ollama runtime environment.
Prepared the system to handle tasks using this model, either locally or through the Open WebUI interface.

Now continue with [Step 3](https://github.com/AdvancedNLP/llm-serving/tree/step_03)