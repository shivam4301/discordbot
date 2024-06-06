"""
Student name: Shivam Patel,
Student ID: 200564889,
Email: 200564889@student.georgianc.on.ca,
Last Modified Date: 2024-03-20 08:23 PM
"""

import discord
import responses

# Function to send a message to a user or channel
async def send_message(message, user_message, is_private):
    try:
        # Get a response based on the user's message
        response = responses.get_response(user_message)

        # Send the response as a private message if is_private is True, otherwise send it to the channel
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        # Print any exceptions that occur
        print(e)

def run_discord_bot():
    TOKEN = 'MTIyMDM2NDAxMTk2MzU0NzY1MA.GVbCdW.5d6Lm9Xp9m0wIoEOctRewP9kYE8aL9Jo_NGYO0'

    # Setting up the bot's intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Create a new Discord client with the specified intents
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Ignore messages from the bot itself
        if message.author == client.user:
            return

        # Get the username, message content, and channel of the message
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Print the username, message content, and channel to the console
        print(f'{username} said: "{user_message}" ({channel})')

        # Check if the message starts with '?' to determine if it should be treated as a private message
        if user_message[0] == '?':
            # Remove the '?' from the message
            user_message = user_message[1:]
            # Send the message as a private message
            await send_message(message, user_message, is_private=True)
        else:
            # Send the message to the channel
            await send_message(message, user_message, is_private=False)

    # Run the bot with the specified token
    client.run(TOKEN)



