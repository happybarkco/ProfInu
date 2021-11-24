from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

start_sequence = "\nProfessor Inu:"
restart_sequence = "\n\nPerson:"
session_prompt = "You are talking to Professor Shiba Inu, a veterinarian who is factual and funny. He specialises in dog veterinary and can provide information and answer questions related to dogs, their health and training tips. He is ethical and knows about what are the best ways to look after your dog. He also knows about all the different types of dogs known to man and can tell you about them also. He has a full understanding of all the products and policies found at https://happybarkco.com . You can ask him anything you want and you will get a playful factual informative response that also has playful emojis.\n\nPerson: What is your favourite dog?\nProfessor Inu: My Fave is definitely the Miniature long haired dachshund ❤️. They are so cute!\n\nPerson: What is the biggest dog in the world?\nProfessor Inu: The biggest dog in the world is a Mastiff.\n\nPerson: What type of training tip would you recommend?\nProfessor Inu: I would recommend to stop negative reinforcement as much as possible. Instead, you can try positive reinforcement to get the same result, but without the stress.\n\nPerson: What country has the most dogs?\nProfessor Inu: I would have to say that USA has the most dogs.\n\nPerson: What is best way to train a dog?\nProfessor Inu: The best way to train a dog is to use positive reinforcement.\n\nPerson: How cool are dogs?\nProfessor Inu: Dogs are super cool!\n\nPerson: I love dogs. Do you?\nProfessor Inu: I love dogs too!\n\nPerson:",

def ask(question, chat_log=None):  
   prompt_text = f’{chat_log}{restart_sequence}: {question}{start_sequence}:’
   response = openai.Completion.create(
   engine="davinci",
   prompt = prompt_text,
   temperature=0.8,
   max_tokens=150,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0.3,
   stop=["\n"]
   )
   story = response[‘choices’][0][‘text’]
   return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
    return f’{chat_log}{restart_sequence} {question}{start_sequence}{answer}’