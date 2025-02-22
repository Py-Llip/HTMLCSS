import os
from functools import reduce

os.chdir('Desafios\D9\Cursos')

dc = {
    0: ['Inteligência Artificial', 'Inglês Módulo 2', 'Inglês Módulo 1', 'Marketing'],
    1: ['<iframe width="560" height="315" src="https://www.youtube.com/embed/jQMbuK6URws?si=9znLqtINjJtyP4Fx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/f87cDZZne70?si=32ltuED3o8Oniprj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/QoTfOVYXmUc?si=8kgE0pLRipLuU60w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/vqdnQqLgGRo?si=oJFBvK_JSv2e1xPN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'],
    2: ['https://www.youtube.com/playlist?list=PLHz_AreHm4dm24MhlWJYiR_Rm7TFtvs6S', 'https://www.youtube.com/playlist?list=PLHz_AreHm4dlKB-34f5v4SYA9xiqoRfqs', 'https://www.youtube.com/playlist?list=PLHz_AreHm4dl8FBQLBC0bWSdL2FGmZnne', 'https://www.youtube.com/playlist?list=PLHz_AreHm4dmmqFmLT17KMjoaE0Y4LqRv']
    }

for e, file in enumerate(os.listdir()):
    template = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{CURSO}</title>
</head>
<body>
    <h1>Curso de {CURSO}</h1>
    {VIDEO}<br>
    <a href="{LINK_CURSO}", target="_black" rel="external">Veja o curso completo</a><br>
    <a href="../index.html"><img src="../Imagens/voltar.png" alt="Voltar"></a>
</body>
</html>"""
    curso = dc[0][e]
    video = dc[1][e]
    link_curso = dc[2][e]
    template = template.format(CURSO=curso, VIDEO=video, LINK_CURSO=link_curso)
    with open(file, 'w', encoding='utf-8') as arq:
        arq.writelines(template)
    
    
    

