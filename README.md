# FastAPI Railway Deployment

A simple FastAPI application configured for deployment on Railway.

## Features

- ✅ Simple REST API with multiple endpoints
- ✅ Health check endpoint
- ✅ Interactive API documentation (Swagger UI)
- ✅ Railway-ready configuration
- ✅ Multiple deployment options

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /api/hello/{name}` - Personalized greeting
- `GET /api/info` - Application information
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation (ReDoc)

## Local Development

### Prerequisites

- Python 3.11 or higher
- pip

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
# Using Uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or using Hypercorn (Railway uses this)
hypercorn main:app --bind 0.0.0.0:8000
```

3. Open your browser and visit:
- http://localhost:8000 - API root
- http://localhost:8000/docs - Interactive documentation

## Deployment on Railway

### Method 1: Deploy from GitHub (Recommended)

1. Push this repository to GitHub
2. Go to [Railway](https://railway.app)
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will automatically detect the configuration and deploy
7. Go to Settings > Networking > Generate Domain to get a public URL

### Method 2: Deploy using Railway CLI

1. Install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login to Railway:
```bash
railway login
```

3. Initialize and deploy:
```bash
railway init
railway up
```

4. Generate a domain:
```bash
railway domain
```

### Method 3: Deploy with Dockerfile

Railway automatically detects the `Dockerfile` in your project root and uses it for deployment.

1. Make sure `Dockerfile` is present in the root directory
2. Deploy via GitHub or CLI
3. Railway will use Docker to build and deploy

### Method 4: One-Click Deploy

Use Railway's template deployment:
1. Visit [Railway FastAPI Templates](https://railway.com/templates?q=fastapi)
2. Click "Deploy" on any template
3. Eject from template to create your own copy

## Configuration Files

### railway.json

Defines the deployment configuration:
- **builder**: NIXPACKS (Railway's build system)
- **startCommand**: Uses Hypercorn ASGI server
- **restartPolicy**: Automatically restarts on failure

### Dockerfile

Alternative deployment method using Docker:
- Based on Python 3.11 slim image
- Installs dependencies from requirements.txt
- Uses Hypercorn as ASGI server
- Binds to Railway's PORT environment variable

### requirements.txt

Python dependencies:
- **fastapi**: Web framework
- **uvicorn**: ASGI server for local development
- **hypercorn**: ASGI server used by Railway

## Environment Variables

Railway automatically provides:
- `PORT` - The port your application should listen on

You can add custom environment variables in Railway's dashboard under the "Variables" tab.

## Monitoring and Logs

After deployment:
1. View logs in Railway dashboard
2. Monitor performance metrics
3. Set up health checks using the `/health` endpoint

## Next Steps

- Add a database (PostgreSQL, MySQL, MongoDB, Redis)
- Set up environment-specific configurations
- Add authentication and authorization
- Implement background tasks with cron jobs
- Set up monitoring and alerting

## Resources

- [Railway Documentation](https://docs.railway.app)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Railway FastAPI Guide](https://docs.railway.app/guides/fastapi)
