# Frontend RPC - Cliente de Visa App

## Descripción
Cliente RPC que se comunica con el backend mediante XML-RPC para gestionar pagos con tarjetas.

## Arquitectura
- **Protocolo:** XML-RPC sobre HTTP
- **Puerto:** 38000
- **Comunicación:** Frontend (VM3) ←→ Backend (VM2, puerto 28000)

## Configuración Rápida

### 1. Configurar URL del Backend
Editar archivo `env`:
```bash
RPCAPIBASEURL=http://localhost:28000/visaAppRPCBackend/rpc/
# O con IP de VM2: http://<IP_VM2>:28000/visaAppRPCBackend/rpc/
```

### 2. Instalar Dependencias
```powershell
pip install -r requirements.txt
```

### 3. Ejecutar Servidor
```powershell
python manage.py runserver 8001
# Para VM con acceso externo:
python manage.py runserver 0.0.0.0:38000
```

### 4. Acceder
```
http://localhost:8001/visaAppRPCFrontend/
http://localhost:8001/visaAppRPCFrontend/testbd/
```

## Ejecutar Tests
```powershell
python manage.py test visaAppRPCFrontend.tests_views
```

## Funcionalidades

### Endpoints Disponibles
- `/visaAppRPCFrontend/` - Inicio (verificar tarjeta)
- `/visaAppRPCFrontend/pago/` - Registrar pago
- `/visaAppRPCFrontend/testbd/` - Panel de pruebas completo

### Operaciones RPC
1. **verificar_tarjeta:** Valida si una tarjeta está registrada
2. **registrar_pago:** Crea un nuevo pago
3. **eliminar_pago:** Elimina un pago por ID
4. **get_pagos_from_db:** Lista pagos por idComercio

## Estructura del Proyecto
```
P1-rpc-frontend/
├── visaAppRPCFrontend/
│   ├── templates/          # Plantillas HTML
│   ├── forms.py           # Formularios Django
│   ├── views.py           # Vistas de la aplicación
│   ├── pagoDB.py          # Cliente RPC (llamadas remotas)
│   ├── urls.py            # Rutas de la aplicación
│   └── tests_views.py     # Tests automatizados
├── visaSite/
│   ├── settings.py        # Configuración (incluye RPCAPIBASEURL)
│   └── urls.py            # Rutas principales
├── env                     # Variables de entorno
├── manage.py              # Administrador Django
└── requirements.txt       # Dependencias
```

## Notas Importantes

### Prerrequisitos
⚠️ El **Backend RPC debe estar corriendo** en el puerto 28000 antes de iniciar el frontend.

### Archivos Eliminados (vs P1-base)
- `models.py` - No necesitamos modelos en el cliente
- `migrations/` - Sin migraciones en el frontend
- `management/` - Sin comandos de gestión de BD
- `tests_models.py` - Sin tests de modelos

### Binding Dinámico
El frontend usa **Dynamic Binding**: la URL del servidor se configura en tiempo de ejecución desde el archivo `env`, permitiendo flexibilidad sin recompilar código.

## Datos de Prueba
Tarjeta válida en la base de datos:
```
Número: 23
Nombre: 23
Fecha Caducidad: 23
Código Autorización: 23
```

## Troubleshooting

### "Connection refused"
- Verificar que el backend está corriendo
- Verificar RPCAPIBASEURL en archivo env

### "No module named 'visaAppRPCFrontend.models'"
- Asegurarse de que views.py no importa modelos
- Los modelos fueron eliminados intencionalmente

### Tests fallan
- Verificar que el backend RPC está accesible
- Verificar que hay datos de tarjetas en la base de datos
- Ejecutar `python manage.py populate` en el backend

## Autor
Práctica 2 - Sistemas Informáticos II
Grupo: [Tu grupo]
Fecha: Marzo 2026
