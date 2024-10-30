from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type,pet_color):
    llm = OpenAI(temperature=0.7)

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type','pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it.it is {pet_color} in color. Suggest me five cool names for my pet"
    )
    prompt = prompt_template_name.format(animal_type=animal_type,pet_color=pet_color)
    response = llm.invoke(prompt)

    return response

if __name__ == '__main__':
    print(generate_pet_name('cow','white'))