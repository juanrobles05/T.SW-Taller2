# Pokenea - Pokedex Paisa 🌟

Una aplicación Flask que presenta criaturas mágicas llamadas "Pokeneas" nacidas en Antioquia, Colombia.

## Características

- **API REST**: Endpoint que devuelve información aleatoria de Pokeneas en formato JSON
- **Interfaz Web**: Página que muestra imagen y frase filosófica de Pokeneas aleatorios
- **Containerización**: Preparado para Docker y Docker Swarm
- **Cultura Paisa**: Inspirado en la gastronomía y cultura antioqueña

## Pokeneas Disponibles

1. **Paisanchu** - Emprendimiento Paisa
2. **Arrozmon** - Cocinar Bandeja Paisa
3. **Arepita** - Perfecta Redondez
4. **Guarilazo** - Aguante Infinito
5. **Frijolero** - Nutrición Balanceada
6. **Maicero** - Crecimiento Dorado
7. **Chorizón** - Sabor Intenso
8. **Chicharrita** - Crujiente Defensa
9. **Platanuco** - Versatilidad Total
10. **Aguapanela** - Energía Dulce

## Rutas

- `/` - Muestra interfaz web con Pokenea aleatorio
- `/api/pokenea` - Devuelve JSON con datos de Pokenea aleatorio
- `/health` - Endpoint de verificación de salud

## Instalación Local

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd pokenea
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## Docker

### Construir imagen
```bash
docker build -t pokenea .
```

### Ejecutar contenedor
```bash
docker run -p 5000:5000 pokenea
```

### Docker Compose (Opcional)
```bash
docker-compose up
```

## Despliegue con Docker Swarm

### Inicializar Swarm
```bash
docker swarm init
```

### Crear servicio
```bash
docker service create \
  --name pokenea-service \
  --replicas 10 \
  --publish 5000:5000 \
  <tu-usuario-dockerhub>/pokenea:latest
```

### Verificar servicio
```bash
docker service ls
docker service ps pokenea-service
```

## Estructura del Proyecto

```
pokenea/
├── app.py                  # Aplicación principal Flask
├── models/
│   ├── __init__.py
│   └── pokenea.py         # Datos de los Pokeneas
├── templates/
│   └── pokenea.html       # Template HTML
├── requirements.txt        # Dependencias Python
├── Dockerfile             # Configuración Docker
├── .github/
│   └── workflows/
│       └── docker-build.yml # GitHub Actions
└── README.md              # Este archivo
```

## Configuración de GitHub Actions

Para usar GitHub Actions con DockerHub:

1. Crear secrets en GitHub:
   - `DOCKERHUB_USERNAME`: Tu usuario de DockerHub
   - `DOCKERHUB_TOKEN`: Token de acceso de DockerHub

2. El workflow se ejecutará automáticamente en push a main/master

## API

### GET /api/pokenea
Devuelve un Pokenea aleatorio:

```json
{
  "id": 1,
  "nombre": "Paisanchu",
  "altura": "0.8m",
  "habilidad": "Emprendimiento Paisa",
  "container_id": "abc123def456"
}
```

## Probar con curl y ejecutar múltiples contenedores

- Probar la API desde la terminal con curl:

```bash
# Obtener un Pokenea aleatorio en JSON
curl http://localhost:5000/api/pokenea

# Verificar el endpoint de salud
curl http://localhost:5000/health
```

- Ejecutar la imagen en Docker (nombre del contenedor y etiqueta recomendados):

```bash
# Construir la imagen (si no lo has hecho)
docker build -t <tu-usuario>/pokenea:latest .

# Ejecutar el contenedor principal en el puerto 5000
docker run -d -p 5000:5000 --name pokenea-main <tu-usuario>/pokenea:latest
```

- Ejecutar contenedores adicionales (puertos diferentes) para simular varias instancias:

```bash
# Segunda instancia en el puerto 5001
docker run -d -p 5001:5000 --name pokenea-2 <tu-usuario>/pokenea:latest

# Tercera instancia en el puerto 5002
docker run -d -p 5002:5000 --name pokenea-3 <tu-usuario>/pokenea:latest
```

- Probar cada instancia con curl (verás que el container_id cambia):

```bash
curl http://localhost:5000/api/pokenea
curl http://localhost:5001/api/pokenea
curl http://localhost:5002/api/pokenea
```

- Verificar contenedores en ejecución y sus IDs:

```bash
docker ps
# Muestra los contenedores en ejecución. La columna CONTAINER ID contiene el ID completo.

# Ver el ID y últimos logs de un contenedor
docker inspect --format='{{.Id}} {{.Name}}' pokenea-main
docker logs pokenea-main --tail 50
```

- El campo `container_id` que aparece en la API viene del hostname del contenedor y suele coincidir con los primeros 12 caracteres del ID que muestra `docker ps`.