from openai import AzureOpenAI as OAI

from src.config import Config

class OpenAI:
    def __init__(self):
        config = Config()
        api_key = config.get_openai_api_key()
        self.client = OAI(
            api_key=api_key,
            api_version="2023-12-01-preview",
            azure_endpoint="https://<YOUR_AZURE_OPENAI_ENDPOINT>.openai.azure.com/"
        )
        
    def inference(self, model_id: str, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip(),
                }
            ],
            model=model_id,
        )

        return chat_completion.choices[0].message.content
