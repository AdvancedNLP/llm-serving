# llm-serving

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

2.Ensure that the **Ollama** and **Open WebUI** services are still running from the previous step. If not, start them again:

```bash
docker-compose up ollama open-webui
```

3. Once the dependencies are installed, you can invoke the `check.py` script to interact with the **Llama 3.2** model:

```bash
poetry run python check.py
```

This command will execute the script within the environment managed by **Poetry**.

The `check.py` script should output a response from the model, verifying that everything is working as expected. Depending on how the script is configured, it might prompt the model with a simple question or task.

#### What You’ve Achieved

By completing this step, you have:
- Installed all the necessary Python dependencies using **Poetry**.
- Successfully invoked the **Llama 3.2** model using the `check.py` script.
- Confirmed that the system is correctly set up and ready to handle model interactions.

Now continue with [Step 4](https://github.com/AdvancedNLP/llm-serving/tree/step_04)