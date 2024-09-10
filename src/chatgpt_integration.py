import os
import openai


class ChatGPTIntegration:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        openai.api_key = self.api_key
        self.model = None
        self.system_prompt = None

    def get_response(self, prompt):
        if not self.model or not self.system_prompt:
            raise ValueError(
                "Model or system prompt not set. Use set_model() and set_system_prompt() before calling get_response().")

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300  # Ограничиваем длину ответа
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"Ошибка при получении ответа от ChatGPT: {e}")
            return None

    def set_model(self, model):
        self.model = model

    def set_system_prompt(self, prompt):
        self.system_prompt = prompt
