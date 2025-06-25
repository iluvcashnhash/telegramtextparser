import asyncio
from telethon import TelegramClient
from docx import Document

async def main():
    api_id = int(input("Enter your API ID: "))
    api_hash = input("Enter your API HASH: ")
    channel_url = input("Enter the Telegram channel URL or username: ")

    # Start client session
    async with TelegramClient('session_name', api_id, api_hash) as client:
        # Resolve channel entity
        channel = await client.get_entity(channel_url)

        # Get all messages from channel
        messages = []
        async for message in client.iter_messages(channel, reverse=True):
            text = message.text or ''
            messages.append(text)

        # Save messages to Word document
        doc = Document()
        for text in messages:
            doc.add_paragraph(text)
        doc.save('channel_messages.docx')
        print('Saved', len(messages), 'messages to channel_messages.docx')

if __name__ == '__main__':
    asyncio.run(main())
