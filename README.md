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

Now continue with [Step 1](https://github.com/AdvancedNLP/llm-serving/tree/step_01)