# ☸️ Kubernetes Log Analytics

Sistema distribuido para analisis de logs de servidores Linux con Apache Spark.

---

## ✅ Descripcion

Simula logs, los procesa con Spark y expone resultados a traves de una API.

### ¿Que hace este proyecto?

- **Log Generator**: Simula logs de servidores Linux
- **Spark Processor**: Analiza logs con PySpark
- **Results API**: Expone resultados (errores, IPs sospechosas, endpoints top)

---

## ✨ Caracteristicas Principales

| Caracteristica | Descripcion |
|----------------|-------------|
| **Simulacion de logs** | Genera trafico realista |
| **Procesamiento distribuido** | Spark local o en cluster |
| **Deteccion de errores** | Frecuencia de codigos 4xx/5xx |
| **Seguridad** | IPs sospechosas |
| **API de resultados** | Endpoint `/results` |

---

## 🛠️ Stack Tecnologico

- **Python**: Generador y API
- **Apache Spark**: Analisis de logs
- **Docker / Kubernetes**: Orquestacion

---

## 📦 Instalacion y Uso

### Probar con Docker Compose

```bash
docker compose up --build
```

### Probar con Kubernetes

1) Construir imagenes:

```bash
docker build -t log-generator:latest -f docker/log-generator.Dockerfile .
docker build -t spark-log-processor:latest -f docker/spark-processor.Dockerfile .
docker build -t log-results-api:latest -f docker/api.Dockerfile .
```

2) Aplicar manifests:

```bash
kubectl apply -f k8s/storage.yaml
kubectl apply -f k8s/log-generator.yaml
kubectl apply -f k8s/spark-processor.yaml
kubectl apply -f k8s/results-api.yaml
```

3) Consultar resultados:

```bash
curl http://localhost:30081/results
```

---

## 🗂️ Estructura del Proyecto

```
kubernetes-log-analytics
├── logs
├── spark
├── api
├── k8s
├── docker
├── docker-compose.yml
└── README.md
```

---

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

