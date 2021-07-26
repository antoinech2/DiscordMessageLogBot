import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        for channel in guild.channels:
            print(channel, channel.id)
    while True:
        channel = client.get_channel(int(input("Entrez l'id du channel...")))
        print("\n\n===============================================\n\n")
        print("MESSAGES DU SALON", channel.name)
        messages = await channel.history().flatten()
        messages.reverse()
        for mes in messages:
            print("[" + mes.author.name, mes.created_at.strftime("%d/%m/%Y, %H:%M:%S") + "]   ", mes.content)
        print("\n\n===============================================\n\n")


client.run('SECRET-BOT_TOCKEN')
