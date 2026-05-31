# n8n-image

Images Docker personnalisées pour n8n, incluant des noeuds supplémentaires (IMAP, Playwright), le task runner JavaScript, et une image Playwright standalone.

## Structure

```
├── versions.env          # Source unique des versions n8n / n8n-runners
├── nodes/
│   └── package.json      # Noeuds npm installés dans n8n
├── n8n/
│   └── Dockerfile        # Image n8n avec les noeuds personnalisés
├── n8n-runners/
│   └── Dockerfile        # Image n8n task runner JavaScript
└── playwright/
    └── Dockerfile        # Image Playwright standalone (serveur de browsers)
```

---

## Mettre à jour la version de n8n

La version de n8n est centralisée dans **`versions.env`** à la racine. Elle s'applique aux deux images `n8n` et `n8n-runners`.

**Fichier à modifier : `versions.env`**

```env
N8N_VERSION=2.17.5   # ← changer ici uniquement
```

Les images `n8n/Dockerfile` et `n8n-runners/Dockerfile` reçoivent cette valeur via un `ARG` Docker passé par le CI. Aucune modification dans les Dockerfiles n'est nécessaire.

> **Renovate** met à jour `versions.env` automatiquement chaque lundi avant 6h via un `regexManager` configuré dans `renovate.json`.  
> Une seule PR Renovate met à jour les deux images simultanément.

### Build local

```bash
source versions.env
docker build --build-arg N8N_VERSION=$N8N_VERSION -f n8n/Dockerfile .
docker build --build-arg N8N_VERSION=$N8N_VERSION -f n8n-runners/Dockerfile .
```

Sans `--build-arg`, il y aura une erreur.

---

## Mettre à jour les noeuds installés dans n8n

Les noeuds npm supplémentaires sont déclarés dans **`nodes/package.json`**.

**Fichier à modifier : `nodes/package.json`**

```json
{
  "dependencies": {
    "n8n-nodes-imap": "^2.14.0",
    "n8n-nodes-playwright-core": "^1.1.1"
  }
}
```

### Ajouter un nouveau noeud

```bash
cd nodes
npm install <nom-du-paquet>
# nodes/package.json et nodes/package-lock.json sont mis à jour
```

### Mettre à jour un noeud existant

Modifier la version dans `nodes/package.json` puis :

```bash
cd nodes
npm install
```

Le CI (`build-images.yml` / `.gitlab-ci-dso.yml`) exécute `npm install` dans `nodes/` avant de construire l'image `n8n`. Le répertoire `nodes/node_modules` est copié dans l'image.

> **Renovate** met à jour `n8n-nodes-imap` automatiquement chaque lundi avant 6h (`nodes/package.json`).  
> `n8n-nodes-playwright-core` est également suivi — sa version est intégrée dans le tag de l'image `n8n` (suffixe `-playwright-X.Y.Z`).

---

## Mettre à jour la version de Playwright

Playwright est utilisé à deux endroits :

| Fichier | Rôle |
|---|---|
| `playwright/Dockerfile` | Image serveur de browsers (Firefox, Chromium) |
| `nodes/package.json` | Noeud n8n `n8n-nodes-playwright-core` |

Ces deux versions doivent rester **compatibles** entre elles mais sont indépendantes.

### Mettre à jour l'image Playwright

La version Playwright est centralisée dans **`versions.env`** à la racine, au même titre que la version n8n.

**Fichier à modifier : `versions.env`**

```env
PLAYWRIGHT_VERSION=1.58.2          # version semver, utilisée par npx playwright@X.Y.Z
PLAYWRIGHT_IMAGE_TAG=v1.58.2-jammy # tag complet de l'image Microsoft (suffixe variable selon les versions)
```

Les deux variables sont distinctes car Microsoft ne suit pas un schéma de tag fixe (`-jammy`, `-focal`, `-noble`...). Le `playwright/Dockerfile` utilise :
- `PLAYWRIGHT_IMAGE_TAG` → `FROM mcr.microsoft.com/playwright:${PLAYWRIGHT_IMAGE_TAG}`
- `PLAYWRIGHT_VERSION` → `npx playwright@${PLAYWRIGHT_VERSION}` (build + runtime)

Sans `--build-arg`, le build échoue immédiatement — il n'y a pas de valeur par défaut dans le Dockerfile.

> **Renovate** surveille `PLAYWRIGHT_IMAGE_TAG` via un `regexManager` sur `mcr.microsoft.com/playwright` (Docker) et `PLAYWRIGHT_VERSION` via npm. Les deux doivent rester alignées lors d'une mise à jour.

### Build local

```bash
source versions.env
docker build \
  --build-arg PLAYWRIGHT_VERSION=$PLAYWRIGHT_VERSION \
  --build-arg PLAYWRIGHT_IMAGE_TAG=$PLAYWRIGHT_IMAGE_TAG \
  -f playwright/Dockerfile .
```

### Mettre à jour le noeud `n8n-nodes-playwright-core`

```bash
cd nodes
npm install n8n-nodes-playwright-core@<nouvelle-version>
```

---

## CI/CD

Les images sont buildées automatiquement par **GitHub Actions** (`.github/workflows/build-images.yml`) et **GitLab CI** (`.gitlab-ci-dso.yml`) lors de tout push sur `main`, `develop`, ou les branches `v*`.

Les tags d'images générés suivent le format :

| Image | Tag |
|---|---|
| `n8n` | `n8n:<version_n8n>-playwright-<version_noeud>` |
| `n8n-runners` | `n8n-runners:<version_n8n>` |
| `playwright` | `playwright:<version_playwright>` |
