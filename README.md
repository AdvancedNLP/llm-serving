# llm-serving

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

Here you find the [complete](https://github.com/AdvancedNLP/llm-serving/tree/complete) lab resources

Switch the branch with:

```bash
git switch complete
```