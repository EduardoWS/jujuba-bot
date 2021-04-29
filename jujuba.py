import discord
import random


intents = discord.Intents.default()
intents.members = True



client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('A JUJUBA TA ON!')


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention = message.author.mention


    #previnir erro
    if author == 'Jujuba':
        return
 

    elif content == 'bom dia, jujuba':  
        await channel.send(f'Bom dia, {mention}!!')

    #FRASES JUJUBA:
    elif content == '-jujuba':
        rodar = random.randint(1, 20)
        if rodar == 1:
            await channel.send(f'As pessoas são feitas de modos diferente. \nNós não precisamos saber o porquê, apenas precisamos respeitar.')
        
        elif rodar == 2:
            await channel.send(f'Fala, meu compatriota')
        
        elif rodar == 3:
            await channel.send(f'Deves prometer como promessa real que não deixarás nenhum zumbi entrar!!')
        
        elif rodar == 4:
            await channel.send(f'Não sei se te dou um tiro ou uns beijos.')

        elif rodar == 5:
            await channel.send(f'Você tem cheirinho de amor da minha vida :3')

        elif rodar == 6:
            await channel.send('Tem gente que é igual a nuvem... às vezes eu olho e vejo um animal')
        
        elif rodar == 7:
            await channel.send('Primeiramente, tô com fome. \nSegundamente, primeiramente!!')
        elif rodar == 8:
            await channel.send('Te amo com toda a minha barriga! \nEu ia falar coração mas minha barriga é maior.')
        elif rodar == 9:
            await channel.send('Nossa que dia lindo, parece eu hehehe')
        elif rodar == 10:
            await channel.send('Me faltou com respeito? Meus guardas irão cortar sua cabeça!! Brincadeirinha hahaha... \nou não')
        elif rodar == 11:
            await channel.send('Sou tão meiga quanto um tijolo')
        elif rodar == 12:
            await channel.send('Dica do dia: não me irrita')
        elif rodar == 13:
            await channel.send('É proibido comer os doces que andam!!')
        elif rodar == 14:
            await channel.send('As pessoas dizem que a coisa mais bela do universo são as galáxias, isso porque não conhecem você.')
        elif rodar == 15:
            await channel.send('A lua prometeu brilhar até que o sol se apagasse. Então eu prometo viver até que você dê seu último suspiro.')
        elif rodar == 16:
            await channel.send('Está vendo as estrelas do céu? Cada uma delas é equivalente as vezes que eu pensei em você antes de dormir.')
        elif rodar == 17:
            await channel.send('Minha filha vc não é bonita, vc é gostosa, linda, gata, cremosa, magnífica, esplêndida, atraente, calorosa, deslumbrante, iluminada, cheirosa, encantadora, simpática, querida, talentosa, seduzente, perfeita, estudiosa, amorosa, atenciosa, empenhada, reluzente, fofa e pudinzinho.')
        elif rodar == 18:
            await channel.send('Nossa que tipo de obra renascentista é você? A beleza do seu realismo e o poder dramático dos seus traços te transformam em uma arte tão magnífica, que mesmo se fosse estudada por milhares de críticos e acadêmicos, nunca seria compreendida! Pois é espetacular demais para esse mundo')
        elif rodar == 19:
            await channel.send('No seu olhar eu vejo as estrelas que Van Gogh tanto falava.')
        elif rodar == 20:
            await channel.send('Você está cheia de beleza cósmica que transcende todo o tempo. Nenhum conhecimento de astrofísica seria capaz de explicar o raro fenômeno que você é.')
    
    
    

    #HELP COMANDOS:
    elif content == '-comandos':

        await channel.send('Em qualquer outro canal digite esses comandos: `-jujuba`, `bom dia, jujuba` ')
    


@client.event
async def on_member_join(member):
    channel = client.get_channel(831000889178849313)   #id do canal
    await channel.send(f'Bem-vindo, {member.mention}!')




client.run(' ') #token
