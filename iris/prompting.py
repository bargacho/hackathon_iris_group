from iris import MISTRAL_API_KEY
from .database import search_plants

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


CHATBOT = ChatMistralAI(
    model="open-mistral-7b",
    temperature=0.7,
    max_retries=2,
    max_tokens=256,
    api_key=MISTRAL_API_KEY
)


def run_model(input):
    # Cf RAG codée plus haut, pour trouver le produit approprié
    context = search_plants(input)

    # modèle de prompt (`context` est le résultat de la RAG)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an AI assistant trained to recommend plants based on user requirements. "
                "Give recommendations based on these products: {context}"
            ),
            ("human", "{input}"),
        ]
    )
    chain = prompt | CHATBOT

    # TODO: add images + check if user is asking for a recommendation
    return chain.invoke({
        'context': context,
        'input': input,
    })




def test():
    import pandas as pd

    # Fichier contenant les prompts et réponses (générer et corrigé à la main cf autre fichier code)
    data = pd.read_csv("prompts.csv", sep=";")


    # Format des données : [{"prompt": ..., "response": ...}]
    training_data = [
        {
            "input_language": "English",
            "output_language": "English",
            "input": row["Prompt"],
            "expected_output": row["response"],
        }
        for _, row in data.iterrows()
    ]

    # Itérer sur les données d’entraînement
    for example in training_data[:3]:
        input = example["input"]
        response = run_model(input)

        # Afficher la réponse générée par l'IA
        print(f"Prompt: {input}")
        print(f"Expected: {example['expected_output']}")
        print(f"Generated: {response.content}")
        print("----")
