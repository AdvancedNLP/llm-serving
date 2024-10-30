# llm-serving

### Introduction

Welcome to this hands-on exercise! In this repository, you will find everything you need to set up a multi-service environment using **Docker Compose**. The goal of this exercise is to help you deploy a system that allows for running, interacting, and integrating large language models (LLMs) through a seamless setup.

You will be working with three services:
1. **Ollama**: A runtime environment to execute LLMs locally.
2. **Open WebUI**: A user-friendly web interface for interacting with models in a chat-based environment.
3. **Lite-LLM**: A proxy that connects to cloud-based models, allowing for hybrid model integration.

By the end of this exercise, you will have a fully functional environment where you can run models locally, interact with them through a web-based interface, and use cloud-based models as well.

#### Prerequisites

Before you start, make sure you have the following installed on your machine:
1. **Docker**: You can install it by following the official [Docker installation guide](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Docker Compose is usually included with Docker Desktop, but you can check your installation by running `docker-compose --version`.
3. **Git**: If you don’t already have Git installed, you can download it from the [Git website](https://git-scm.com/).
4. **Python** and **Poetry**: You can install it by following the official [Poetry installation guide](https://python-poetry.org/docs/#installation).

Once the prerequisites are met, you are ready to clone the repository and start working through the setup.

```bash
# Clone this repository to get started
git clone https://github.com/AdvancedNLP/llm-serving.git
cd llm-serving
```

In this repository, you will find all the necessary files that we will use to set up each of the services. Let’s dive into the setup process step by step!


### Step 1: Starting Ollama and Open WebUI Services

In this step, we will use Docker Compose to start two services:
1. **Ollama**: This will serve as the runtime environment for running large language models locally.
2. **Open WebUI**: This will provide a chat-based web interface for interacting with the models hosted by Ollama.

#### Goal

The goal of this step is to bring up both the **Ollama** and **Open WebUI** services together using Docker Compose. Once these services are running, you will be able to interact with the local models through a web interface.

#### Instructions

1. Ensure you are in the root directory of the repository (where the `docker-compose.yaml` file is located).
   
2. Run the following command to bring up the services:

```bash
docker-compose up ollama open-webui
```

This command tells Docker Compose to start both the Ollama and Open WebUI services by referencing the appropriate configurations from the `docker-compose.yaml file.

Wait for the services to start. Once completed, you will see log outputs for both services.

Open your browser and navigate to the following URL to access the ollama interface:

```
http://localhost:11434
```

The ollama interface should load, and you should see a welcome message.

#### What You’ve Achieved
By completing this step, you have:

Successfully started the Ollama service, enabling the local execution of large language models.
Launched the Open WebUI service, which provides a web interface for interacting with these models.
Verified that both services are up and running by accessing the Open WebUI in your browser.


### Optional Step: Relaunching Ollama with GPU Support

If you have an NVIDIA GPU available on your machine and you want to leverage GPU acceleration for running large language models, you can relaunch the **Ollama** service with GPU support. This step is optional and only applicable to students with compatible hardware.

#### Goal

The goal of this step is to relaunch the **Ollama** service using your NVIDIA GPU to improve model performance, especially when dealing with larger models. We'll use a separate `docker-compose-gpu.yaml` file in conjunction with the original `docker-compose.yaml` to enable GPU acceleration.

#### Prerequisites

Before proceeding, ensure that:
1. You have a compatible **NVIDIA GPU** installed on your machine.
2. **NVIDIA Docker** is properly configured. You can follow the official [NVIDIA Docker installation guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) to set it up.
3. Your GPU drivers are up to date.

#### Instructions

1. Make sure you have stopped the previous services, if they are still running:

```bash
docker-compose down
```

2. To relaunch Ollama with GPU support, use the `docker-compose-gpu.yaml file in addition to the standard docker-compose.yaml by running:

```bash
docker-compose -f docker-compose.yaml -f docker-compose-gpu.yaml up ollama open-webui
```


This command tells Docker Compose to combine the configurations from both files, applying GPU-specific settings from docker-compose-gpu.yaml while maintaining the rest of the setup.

3. Once the services are up, you can verify that the Ollama service is utilizing the GPU by checking the logs. If the GPU is successfully detected, you should see references to the GPU in the Ollama logs.


#### What You’ve Achieved
By completing this optional step, you have:

- Relaunched the Ollama service with GPU support, enabling faster and more efficient model execution (assuming GPU compatibility).

Verified that Docker is leveraging your NVIDIA GPU for running the models.


If you do not have an NVIDIA GPU or don’t want to use GPU support, you can continue with the previous CPU-based setup without any issues.

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

### Step 3: Invoking the Model with the `check.py` Script

Now that the **Llama 3.2** model has been successfully downloaded, it’s time to test the model by invoking it through the provided `check.py` script. This script will use the **Ollama** service to interact with the model.

Before running the script, we need to install the dependencies using **Poetry**.

#### Goal

The goal of this step is to install the necessary dependencies using **Poetry** and then run the `check.py` script to make a request to the model, validating that the system is set up correctly.

#### Instructions

1. Install the required Python dependencies using **Poetry**. Run the following command in the root directory of the repository:

```bash
poetry install
```

This will install all the dependencies specified in the `pyproject.toml` file.

2. Once the dependencies are installed, you can invoke the `check.py` script to interact with the **Llama 3.2** model:

```bash
poetry run python check.py
```

This command will execute the script within the environment managed by **Poetry**.

3. The `check.py` script should output a response from the model, verifying that everything is working as expected. Depending on how the script is configured, it might prompt the model with a simple question or task.

#### What You’ve Achieved

By completing this step, you have:
- Installed all the necessary Python dependencies using **Poetry**.
- Successfully invoked the **Llama 3.2** model using the `check.py` script.
- Confirmed that the system is correctly set up and ready to handle model interactions.

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

This step marks the completion of your interactive environment setup, allowing you to continue exploring and experimenting with the language model!

### Step 5: Setting up the LiteLLM Proxy for GPT-4o Integration

In this step, we’ll configure the **LiteLLM** proxy service to allow for interaction with the **GPT-4o** model. This setup supports **GPT-4o** through either OpenAI's API or Azure's deployment.

#### Goal

The goal of this step is to set up **LiteLLM** as a proxy service, allowing the system to route requests to **GPT-4o** models, whether through **OpenAI** or **Azure**. Once configured, this will enable hybrid interactions with both local and cloud-based models.

#### Instructions

1. **Choose your GPT-4o Model Provider**
   
   - **For OpenAI GPT-4o**: 
     - Go to [OpenAI's API Key settings](https://platform.openai.com/settings/organization/api-keys).
     - Create a new API key and copy it.
     - Paste the API key into the `.env` file in the repository directory with the following format:
       ```
       OPENAI_API_KEY=your_openai_api_key_here
       ```

   - **For Azure GPT-4o**:
     - Deploy a **GPT-4o** model on your **Azure** account.
     - Copy the API key and deployment URL for your Azure model.
     - Update the `.env` file with both the API key and the deployment URL as follows:
       ```
       AZURE_API_KEY=your_azure_api_key_here
       AZURE_DEPLOYMENT_URL=your_azure_deployment_url_here
       ```

2. **Start the LiteLLM Proxy Service**

   Once the `.env` file is configured, you can start the **LiteLLM** proxy service by combining the primary Docker Compose file with the `docker-compose.proxy.yaml` file:

   ```bash
   docker-compose -f docker-compose.yaml -f docker-compose.proxy.yaml up
   ```

   This command will launch the **LiteLLM** service alongside **Ollama** and **Open WebUI**, routing any calls to **GPT-4o** via **LiteLLM**.

3. **Verify the Setup**

   Check the logs to ensure all services are running smoothly and that the **LiteLLM** proxy is ready to handle requests to the cloud-based model.

4. ** Use GPT-4o in the Open WebUI**
   Now that the **LiteLLM** proxy is set up, you can use the **Open WebUI** to interact with the **GPT-4o** model. Launch the **Open WebUI** and navigate to the chat interface. You should now see a new option for **GPT-4o**.

#### What You’ve Achieved

By completing this step, you have:
- Configured and launched the **LiteLLM** proxy to connect with a cloud-based **GPT-4o** model (OpenAI or Azure).
- Verified that your environment supports hybrid interaction, allowing access to both local models (via **Ollama**) and cloud-based models (via **LiteLLM**).
  
With this setup complete, you now have a flexible and powerful environment for interacting with various types of language models!
