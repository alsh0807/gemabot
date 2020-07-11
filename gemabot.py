import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("봇활동")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("#실험"):
        await message.channel.send("ok")

    if message.content.startswith("#억울"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("#명령어"):
        await message.channel.send("-명령어 목록-")
        await message.channel.send("*명령어 앞에는 #를 달아줘야 한다")
        await message.channel.send(".")
        await message.channel.send("명령어 - 명령어 목록을 보여준다")
        await message.channel.send(".")
        await message.channel.send("실험 - 실험에 대한 답을 해준다")
        await message.channel.send(".")
        await message.channel.send("억울 697757689031426169 <자기 이름> <자기 할말> - 이장에게 억울함을 호소 할 수 있다")
        await message.channel.send(".")







client.run("NzMxNDg0ODc4ODg0ODMxMzUy.XwmvBA.dWRUHsXN_PqrIn7SQaSLi4FWPbQ")
