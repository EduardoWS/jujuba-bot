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
    
    elif content == 'bom dia':   #and channel.name == 'teste-linus'
        await channel.send(f'Bom dia, {mention}!!')
    
    elif content == '-jujuba':
        rodar = random.randint(1, 5)
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
        

    elif content == '-helpideia' and channel.name == '꒰🤖꒱-bots':
        await channel.send('No canal ꒰💡꒱-ideias-desenhos digite os seguintes comandos: \n\n[ -ideia1 ] Fácil \n[ -ideia2 ] Médio \n[ -ideia3 ] Difícil')
        
    
    elif content == '-ideia1' and channel.name == '꒰💡꒱-ideias-desenhos':
        ideias1 = ['Desenha uma árvore', 'Desenha um espantalho', 'Desenha o Finn', 'Desenha o Jake', 'Desenha a Marceline',
        'Desenha o BMO', 'Desenha o Rei Gelado']
        r1 = random.choice(ideias1)
        await channel.send(r1)


    elif content == '-ideia2' and channel.name == '꒰💡꒱-ideias-desenhos':
        ideias2 = ['Desenha a Princesa de Fogo', 'Desenha o Finn e o Jake juntos', 'Desenha eu e a Marceline',
        'Desenha o Lich']
        r2 = random.choice(ideias2)
        await channel.send(r2)


    elif content == '-ideia3' and channel.name == '꒰💡꒱-ideias-desenhos':
        ideias3 = ['Faça uma caricatura de si mesmo(a)', 'Desenhe espelhos de diferentes ângulos',
        'Rascunhe você de super-heroína/super-herói', 'Tente desenhar a si mesmo(a) com o dobro da idade',
        'Rabisque um autorretrato no reflexo de uma colher', 'Ilustre a vista de uma janela',
        'Esboce as nuvens', 'Aproveite a perspectiva e trace a visão de cima de uma ponte ou de baixo de um penhasco',
        'Desenhe um objeto e, em seguida, coloque um rosto nele', 'Crie uma capa alternativa para seu livro ou álbum preferido',
        'Retrate uma cena para sua música favorita', 'Dê um rosto para o personagem de um livro que você ama',
        'Ilustre seu conto de fadas dos sonhos', 'Combine formas de animais e faça uma criatura mítica',
        'Transforme a cena de um sonho em um desenho', 'Crie sua própria logomarca', 'Desenhe todas as refeições que fizer ao logo da semana',
        'Escolha um objeto e o desenhe de formas diferentes por sete dias', 'Desenhe sapatos velhos',
        'Desenhe um copo de água', 'Desenhe uma cena em um restaurante', 'Desenhe garrafas de vinho',
        'Desenhe o seu animal de estimação favorito', 'Desenhe o rosto de uma pessoa idosa', 'Desenhe um carro velho',
        'Desenhe qualquer coisa feita de metal']
        r3 = random.choice(ideias3)

        await channel.send(r3)
        




@client.event
async def on_member_join(member):
    channel = client.get_channel(831000889178849313)
    await channel.send(f'Bem-vindo, {member.mention}!')




client.run('ODMxMDA1NzM4MTA0NjUxNzc2.YHO8Zw.PLhXKIXrclGu3AqPGnYfu7ffqb0')
