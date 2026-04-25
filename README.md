# llm-serving

### Step 3: Invoking the Model with the `check.py` Script

Now that the **Llama 3.2** model has been successfully downloaded, it’s time to test the model by invoking it through the provided `check.py` script. This script will use the **Ollama** service to interact with the model.

Before running the script, we need to have **uv** available. No separate install step is required — `uv` will handle dependencies on the fly.

#### Installing uv

If you don't have **uv** installed yet, choose one of the following methods:

**Option A — recommended installer (macOS/Linux):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Option B — via pip:**

```bash
pip install uv
```

#### Goal

The goal of this step is to run the `check.py` script using **uv** to make a request to the model, validating that the system is set up correctly.

#### Instructions

1. Ensure that the **Ollama** and **Open WebUI** services are still running from the previous step. If not, start them again:

```bash
docker compose up ollama open-webui
```

2. Run the `check.py` script using **uv**, which will automatically fetch the `ollama` dependency:

```bash
uv run --with ollama check.py
```

This command will execute the script, automatically installing the required `ollama` package if not already available.

The `check.py` script should output a response from the model, verifying that everything is working as expected. Depending on how the script is configured, it might prompt the model with a simple question or task.

#### What You've Achieved

By completing this step, you have:
- Successfully invoked the **Llama 3.2** model using the `check.py` script.
- Confirmed that the system is correctly set up and ready to handle model interactions.

Now continue with the next step. Switch the branch with:

```bash
git switch step_04
```

and continue with [Step 4](https://github.com/AdvancedNLP/llm-serving/tree/step_04)