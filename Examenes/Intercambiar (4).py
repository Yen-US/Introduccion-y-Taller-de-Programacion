def intercambiar (Lista):
    if isinstance (Lista,list):
        return intercambiar_aux (Lista)
    else: return "Error"
def intercambiar_aux (Lista):
    if Lista==[]:
        return []
    else:
        return [Lista[1],Lista[0]]+ intercambiar_aux (Lista[2:])
