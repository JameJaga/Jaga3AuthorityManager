import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    guild = message.guild
    send = 0
    status = 0
    getperm = ''
    if message.content.startswith('/amhelp'):
        embed = discord.Embed(title="AuthorityManagerHelp",color=discord.Colour.from_rgb(0,191,255))
        embed.add_field(name="**SetCommands**",value=f'**/ad-admin**でAdmin権限を付与。\n**/ad-assist**でAssistan権限を付与。\n**/rm-admin**でAdmin権限を剥奪。\n**/rm-assist**でAssistant権限を剥奪。**/ad-hr**で人事課権限を付与。\n**/rm-hr**で人事課権限を剥奪。\n\n**/am-reset**で全権剥奪。',inline=False)
        await message.channel.send(embed=embed)
    
    
    if message.content.startswith('/ad-admin'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == 'Admin', member.guild.roles)
            await member.add_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Admin実権', member.guild.roles)
            await member.add_roles(role)
            send = 1
            status = 1
            getperm = 'Admin'
        else:
            await qa_thread(message)
    
    
    if message.content.startswith('/rm-admin'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == 'Admin', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Admin実権', member.guild.roles)
            await member.remove_roles(role)
            send = 1
            getperm = 'Admin'
        else:
            await qa_thread(message)
            
            
    if message.content.startswith('/ad-hr'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == '人事課', member.guild.roles)
            await member.add_roles(role)
            role = discord.utils.find(lambda r: r.name == '人事課実権', member.guild.roles)
            await member.add_roles(role)
            send = 1
            status = 1
            getperm = '人事課'
        else:
            await qa_thread(message)


    if message.content.startswith('/rm-hr'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == '人事課', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == '人事課実権', member.guild.roles)
            await member.remove_roles(role)
            send = 1
            getperm = '人事課'
        else:
            await qa_thread(message)
    
    
    if message.content.startswith('/ad-assis'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == 'Assistant', member.guild.roles)
            await member.add_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Assistant実権', member.guild.roles)
            await member.add_roles(role)
            send = 1
            status = 1
            getperm = 'Assis'
        else:
            await qa_thread(message)
    
    if message.content.startswith('/rm-assis'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == 'Assistant', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Assistant実権', member.guild.roles)
            await member.remove_roles(role)
            send = 1
            getperm = 'Assis'
        else:
            await qa_thread(message)
    if message.content.startswith('/am-reset'):
        member = message.mentions[0]
        if message.author.guild_permissions.administrator:
            role = discord.utils.find(lambda r: r.name == 'Assistant', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Assistant実権', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Admin', member.guild.roles)
            await member.remove_roles(role)
            role = discord.utils.find(lambda r: r.name == 'Admin実権', member.guild.roles)
            await member.remove_roles(role)
            send = 1
            status = 3
        else:
            await qa_thread(message)
    
    if(send == 1):
        channel = client.get_channel(675572910412267540)
        if(status == 1):
            embed = discord.Embed(title="Promoted",description = f'{member.mention}は 運営ランク<<{getperm}>>に昇格しました！！おめでとう！！！！:tada::tada::tada:',color=discord.Colour.from_rgb(0, 255, 255))
            await channel.send(embed=embed)
        elif(status == 0):
            embed = discord.Embed(title="Demoted",description = f'{member.mention}は <<{getperm}>>から降格させられました。元に戻れる日を待ちましょう・・・',color=discord.Colour.from_rgb(255, 0, 0))
            await channel.send(embed=embed)
        elif(status == 3):
            embed = discord.Embed(title="AllAuthorityDeprivationed",description = f'{member.mention}は 運営職をすべて剥奪されました。',color=discord.Colour.from_rgb(255, 0, 0))
            await channel.send(embed=embed)

async def qa_thread(message):
    embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
    await message.channel.send(embed=embed)
    
client.run(TOKEN)
