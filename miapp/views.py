from django.shortcuts import render
from datetime import datetime

def love_page(request):
    context = {
        'nombre_novia': 'el amor de mi vida',
        'fecha_inicio': '24 de mayo de 2024',
        'mensajes_amor': [
            {
                "texto": "Cada día me enamoro más de ti",
                "imagen": "miapp/images/mensaje1.jpeg",
            },
            {
                "texto": "Eres el amor de mi vida",
                "imagen": "miapp/images/mensaje2.jpeg",
            },
            {
                "texto": "Contigo todo es mejor",
                "imagen": "miapp/images/mensaje3.jpeg",
            },
            {
                "texto": "Me haces inmensamente feliz",
                "imagen": "miapp/images/mensaje4.jpeg",
            },
            {
                "texto": "Eres mi persona favorita",
                "imagen": "miapp/images/mensaje5.jpeg",
            },

            {
                "texto": "Eres el amor de mi única vida",
                "imagen": "miapp/images/mensaje6.jpeg",
            },
        ],
    }
    return render(request, 'miapp/index.html', context)

