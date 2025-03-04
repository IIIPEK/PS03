import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import asyncio


def get_english():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        html = response.content
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

    soup = BeautifulSoup(html, "html.parser")
    word = soup.find("div", id="random_word").text.strip()
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")

    word = soup.find("div", id="random_word").text.strip()
    word_definition = soup.find("div", id="random_word_definition").text.strip()
    return word, word_definition


async def translate(text,src='en',dest='ru'):
    translator = Translator()
    translation = await translator.translate(text, dest=dest, src=src)
    return translation.text

def game():
    print("Привет! Это игра 'Угадай слово'.")
    while True:
        word, word_definition = get_english()
        word = asyncio.run(translate(word))
        word_definition = asyncio.run(translate(word_definition))
        print(f"Вот определение слова: {word_definition}")
        user_input = input("Угадай слово: ")
        if user_input.lower() == word.lower():
            print("Правильно!")
        else:
            print(f"Неверно. Было загадано слово: {word}")
        play_again = input("Хочешь сыграть ещё? (д/н): ")
        if play_again.lower() != "д":
            print("Спасибо за игру!")
            break


if __name__ == "__main__": game()
