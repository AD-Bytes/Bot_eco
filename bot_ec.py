import random
import discord
def bot():
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready(ctx):
        print(f'We have logged in as {bot.user}')
        
    @bot.command()
    async def Help(ctx):

        await ctx.send("Hola, soy un bot pato-ecologo-filosofo-astronauta, Estoy aqui para resolver tus dudas sobre la ecologia \n Puedes pedirme un consejo con: $Dame_un_Consejo \n Tambien puedes recibir informacion de distintos tipos de contaminacion usando: $Que_tipos_de_contaminacion_exiten \n como lo puedes notar la magia empieza con el simbolo '$' Este se usa para detectar que ahi empieza un comanzo, si quieres poner un comando, comienza por ahi. ")


    @bot.command()   
    async def hello(ctx):
        await ctx.send(f'Hola, soy un bot {bot.user}! Me gusta la ecologia.')

    @bot.command()
    async def Dame_un_Consejo(ctx):
        mensaje = random.randint(1, 5)
        if mensaje == 1:
            mensaje = "Para mantener un buen clima en esta tierra debemos preservar la vida y el equilibrio que hay en ella, puedes tener plantas y hacer que cumplan con su funcion de hacer fotosintesis para ayudar a la madre tierra."
        elif mensaje == 2:
            mensaje = "Una buena forma de preservar el medio ambiente, es reciclar, es simple, puedes reusar las botellas de plastico, o cosas que te sirvan de algun modo u otro y encontrarles un uso, para asi no tener que tirarlos y generar mas contaminacion. O en el caso de que no seas tan creativo, esta bien, basta con ponerlo en un tacho de basura verde que tenga el simbolo de reciclaje."
        elif mensaje == 3:
            mensaje = "puedes comprar cosas ecoamigables, asi no te tendras que preocupar si la tiras, como su nombre indica, estos productos son amigables con el medio ambiente, y tienen una degradacion que no suelta quimicos malos para este mismo, pero no te olvides, tienes que echarlo en la basura, no solo por que sea ecoamigable significa que puedas dejarlo por donde sea."
        elif mensaje == 4:
            mensaje = "Para un buen desarrollo de una civilizacion se deben desarrollar tecnologias que no dejen huella de carbono o otro tipo de quimicos, puedes apoyar estas busquedas de tecnologias donando tu dinero a organizaciones de cientificos que se encargan de buscar tecnologia buena para el medio ambiente."
        else:
            mensaje = "Puedes enseñarle a las personas en tu circulo social como cuidar el medio ambiente, y de esta manera formar un cambio mas solido y estable, mejor hacerlo acompañado que solo."
        await ctx.send(mensaje)
    
    @bot.command()
    async def Que_tipos_de_contaminacion_existen(ctx):
        mensaje = "Contaminación del aire. Supone la existencia de partículas sólidas, líquidas o gases en el aire que perjudican a los seres vivos. Uno de los contaminantes que se encuentra con más frecuencia en el aire es el monóxido de carbono. \n Contaminación del agua. Se produce, sobre todo, en los ríos, los lagos y el mar. Puede deberse a plásticos o a vertidos de aguas residuales. \n Contaminación de la tierra. En ocasiones, se producen vertidos de productos químicos que se filtran por la tierra y la contaminan. Podemos destacar el petróleo o los metales pesados, así como los herbicidas y plaguicidas. \n Contaminación por basura. En las grandes ciudades se generan muchos residuos que suelen ir a parar a vertederos. Puede ocurrir que la basura acumulada sea arrastrada por el viento o por el agua y contamine la tierra o los ríos. \n Contaminación térmica. Se puede producir, por ejemplo, un aumento de la temperatura del agua de los océanos debido al efecto invernadero que tenga consecuencias sobre los seres vivos que habitan ese medio. \n Contaminación acústica. Cualquier persona que haya vivido en una gran ciudad ha escuchado el ruido de los coches, de las obras, de los motores, de los aviones: en eso consiste la contaminación acústica. \n Contaminación lumínica. También existe en las grandes ciudades una gran contaminación lumínica debida a las luces de los edificios, de los coches o de las farolas y que impide ver las estrellas."
        await ctx.send(mensaje)
        
    

    bot.run("TOKEN HERE")

bot()

