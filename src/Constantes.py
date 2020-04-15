from Enderecos import *
TOKEN_ID= ''
VIDEO_ID = ''
URL = "https://streaming-graph.facebook.com/" + VIDEO_ID + "/live_comments"
PARAMETROS = {'access_token': TOKEN_ID, 'comment_rate':'ten_per_second'}

dicionarioComandos = dict([
    ('pena',MARIO_PENINHA),
    ('pequeno',MARIO_PEQUENO),
    ('cogumelo',MARIO_GRANDE),
    ('flor',MARIO_FLOR_DE_FOGO),
    ('peninha',MARIO_PENINHA),
    ('fogo',MARIO_FLOR_DE_FOGO)
])
listaComandos = [
    ('pena'),
    ('pequeno'),
    ('cogumelo'),
    ('flor'),
    ('peninha'),
    ('fogo')
]
