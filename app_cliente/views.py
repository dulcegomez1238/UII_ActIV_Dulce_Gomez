from django.shortcuts import render

# Create your views here.

def mostrar_datos(request):
    
    
    datos_cliente = [
        
        
        {  
            'nombre' : 'Dulce Gomez',
            'edad' : 22,
            'telefono' : '656 874 5478'
        },
        
        {
            'nombre' : 'Juan Ramirez ',
            'edad' : 18,
            'telefono' : '656 549 3254'
        },
        
        {
            
            'nombre' : 'Sofia Martinez',
            'edad' : 25,
            'telefono' : '656 415 8721' 
            
        }
]

    
        
    contexto={
        'titulo_pagina': 'Farmacia Clientes',
        'clientes': datos_cliente
    }
    
    return render (request, 'index.html', contexto)