# llm-serving

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

