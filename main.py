import openai
from googletrans import Translator
import config


openai.api_key = config.api_key
translator = Translator()




while True:
    question = translator.translate(input("Какво искаш да питаш?\n"))

    print("Question in Еnglish: " + question.text)

    model_engine = "text-davinci-002"
    prompt = question.text

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.6,
    )

    message = completion.choices[0].text
    new_answer = translator.translate(message, dest="bg")
    print(new_answer.text)

















