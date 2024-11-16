import random

def M_L():
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
    return mensaje