"""
Student name: Shivam Patel,
Student ID: 200564889,
Email: 200564889@student.georgianc.on.ca,
Last Modified Date: 2024-03-20 08:23 PM
"""

import random
import discord

# Function to get the bot's response based on the user's message
def get_response(message: str) -> str:
    p_message = message.lower()

    # Check if the message is 'hello'
    if p_message == 'hello':
        return 'Hey there!'

    # Check if the message is 'roll'
    if message == 'roll':
        # Generate a random number between 1 and 6 and return it as a string
        return str(random.randint(1,6))

    # Check if the message is '!help'
    if p_message == '!help':
        # Provide instructions on how to use the currency exchange feature
        return 'I will provide you the exchange rate. You have to ask like this "!currency USD_CAD"'

    # Check if the message starts with '!currency'
    if p_message.startswith('!currency'):
        import requests
        import json

        # Extract the currency pair from the message
        currency = p_message[10:]

        # Construct the API URL for the currency exchange rate
        api_url = f'https://api.api-ninjas.com/v1/exchangerate?pair=' + currency.upper()
        print(api_url)
        # Send a GET request to the API
        response = requests.get(api_url, headers={'X-Api-Key': 'kpafxOX1M8xAoV42Z/TjLw==lIzWnAoJPLuNagWx'})

        if response.status_code == requests.codes.ok:
            json_response = json.loads(response.text)
            Exchange_Details = f"Currency Pair: {json_response['currency_pair']}, \nExchange Rate: {json_response['exchange_rate']}"

            return f'{Exchange_Details}'
        # If the request was not successful, return the currency pair as is
        return f'{currency}'

    # If none of the above conditions are met, return a generic message
    return 'I didn\'t understand what you are saying. Try typing "!help".'