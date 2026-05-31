Voici un exemple de `Dockerfile` et de `helm chart` pour déployer une application Python avec CUDA sur Kubernetes.  Ce sont des exemples de base, et tu devras les adapter à tes besoins spécifiques (dépendances, points d'entrée, etc.).

**Important:**

*   **CUDA Driver:** L'installation du driver CUDA dans le conteneur est **généralement déconseillée**.  Il est préférable de s'assurer que le(s) nœud(s) Kubernetes où ton pod est déployé dispose(nt) déjà du driver CUDA installé et configuré.  Le conteneur utilise alors le driver du nœud hôte.
*   **`nvidia-docker` obsolète:**  `nvidia-docker` est obsolète.  Utilise plutôt le `NVIDIA Device Plugin` pour Kubernetes.  (Je vais utiliser cette approche dans cet exemple.)
*   **Image de base:** Choisis une image de base adaptée à tes besoins.  `nvidia/cuda` est un bon point de départ, mais tu peux aussi utiliser des images plus légères (par exemple, une image Ubuntu ou Alpine avec CUDA installé).
*   **Versions:** Adapte les versions de CUDA, Python, et des dépendances à tes besoins.

**1. Dockerfile**

```dockerfile
# Utilise une image de base avec CUDA (vérifie la version CUDA souhaitée)
# https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/supported-tags.md
FROM nvidia/cuda:12.8.1-devel-ubuntu24.04

# Mettre à jour et installer les dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt (si tu en as un)
COPY requirements.txt .

# Installer les dépendances Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Définir la commande d'exécution
CMD ["python3", "main.py"] # Remplace "main.py" par ton script principal
```

**Explication du Dockerfile:**

*   `FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04`: Utilise une image de base NVIDIA CUDA.  Adapte la version à ta configuration.  Cette image inclut déjà CUDA et cuDNN.
*   `RUN apt-get update && apt-get install ...`: Installe les dépendances système nécessaires (Python, pip, git).
*   `WORKDIR /app`: Définit le répertoire de travail dans le conteneur.
*   `COPY requirements.txt .`: Copie le fichier `requirements.txt` (si tu en as un) dans le conteneur.
*   `RUN pip3 install ...`: Installe les dépendances Python spécifiées dans `requirements.txt`.
*   `COPY . .`: Copie tout le code source de ton application dans le conteneur.
*   `CMD ["python3", "main.py"]`: Définit la commande à exécuter lorsque le conteneur démarre.

**2. requirements.txt (exemple)**

```
numpy
torch
torchvision
# Ajoute tes autres dépendances ici
```

**3. Helm Chart (Structure)**

Crée un répertoire pour ton Helm Chart (par exemple, `my-cuda-app`).  À l'intérieur, crée la structure suivante :

```
my-cuda-app/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   └── service.yaml
```

**4. Chart.yaml**

```yaml
apiVersion: v2
name: my-cuda-app
description: A Helm chart for deploying my CUDA Python application.
type: application
version: 0.1.0
appVersion: 1.0.0
```

**5. values.yaml**

```yaml
image: your-dockerhub-username/my-cuda-app:latest  # Remplace par ton image Docker
replicaCount: 1
port: 5000

resources:
  requests:
    cpu: "1"
    memory: "4Gi"
    nvidia.com/gpu: 1  # Demande un GPU
  limits:
    cpu: "2"
    memory: "8Gi"
    nvidia.com/gpu: 1
```

**6. templates/deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-cuda-app-deployment
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: my-cuda-app
  template:
    metadata:
      labels:
        app: my-cuda-app
    spec:
      containers:
      - name: my-cuda-app-container
        image: {{ .Values.image }}
        ports:
        - containerPort: {{ .Values.port }}
        resources:
          requests:
            cpu: {{ .Values.resources.requests.cpu }}
            memory: {{ .Values.resources.requests.memory }}
            nvidia.com/gpu: {{ .Values.resources.requests.nvidia.com/gpu }}
          limits:
            cpu: {{ .Values.resources.limits.cpu }}
            memory: {{ .Values.resources.limits.memory }}
            nvidia.com/gpu: {{ .Values.resources.limits.nvidia.com/gpu }}
```

**7. templates/service.yaml**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-cuda-app-service
spec:
  selector:
    app: my-cuda-app
  ports:
    - protocol: TCP
      port: {{ .Values.port }}
      targetPort: {{ .Values.port }}
  type: LoadBalancer  # Ou ClusterIP si tu n'as pas besoin d'un accès externe
```

**Explication du Helm Chart:**

*   `Chart.yaml`: Définit les métadonnées du chart.
*   `values.yaml`: Définit les valeurs par défaut pour les variables du chart.  Tu peux les remplacer lors de l'installation.
*   `deployment.yaml`: Définit le déploiement de ton application.  Important :
    *   `nvidia.com/gpu: 1`:  Demande un GPU à Kubernetes.  Assure-toi que le `NVIDIA Device Plugin` est installé et configuré sur tes nœuds Kubernetes.
    *   Les ressources `requests` et `limits` sont importantes pour garantir que ton application a suffisamment de ressources.
*   `service.yaml`: Définit le service Kubernetes pour exposer ton application.  `type: LoadBalancer` créera un load balancer externe (si ton cluster le prend en charge).  `ClusterIP` exposera l'application uniquement à l'intérieur du cluster.

**Étapes pour déployer:**

1.  **Construis l'image Docker:**

    ```bash
    docker build -t your-dockerhub-username/my-cuda-app:latest .
    docker push your-dockerhub-username/my-cuda-app:latest
    ```

2.  **Ajoute le dépôt Helm (si nécessaire):**

    Si tu utilises un dépôt Helm personnalisé, ajoute-le :

    ```bash
    helm repo add my-repo <URL du dépôt>
    helm repo update
    ```

3.  **Installe le chart Helm:**

    ```bash
    helm install my-cuda-app ./my-cuda-app
    # Ou, si tu utilises un dépôt :
    # helm install my-cuda-app my-repo/my-cuda-app
    ```

4.  **Vérifie le déploiement:**

    ```bash
    kubectl get pods
    kubectl get services
    ```

**Points importants:**

*   **NVIDIA Device Plugin:**  Assure-toi que le `NVIDIA Device Plugin` est installé et configuré sur tes nœuds Kubernetes avant de déployer ton application.  Consulte la documentation NVIDIA pour plus d'informations.
*   **Driver CUDA:** Le driver CUDA doit être installé sur les nœuds Kubernetes.
*   **Ressources:** Ajuste les ressources (CPU, mémoire, GPU) en fonction des besoins de ton application.
*   **Sécurité:**  Prends en compte les aspects de sécurité (par exemple, l'utilisation de secrets pour les informations sensibles).
*   **Logging et Monitoring:**  Implémente le logging et le monitoring pour surveiller ton application.

N'oublie pas d'adapter ce code à tes besoins spécifiques.  La configuration peut varier en fonction de ton environnement Kubernetes et des exigences de ton application.
