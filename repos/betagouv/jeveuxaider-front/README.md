# JeVeuxAider.gouv.fr — Frontend

Interface web de [JeVeuxAider.gouv.fr](https://jeveuxaider.gouv.fr), la plateforme publique du bénévolat proposée par la Réserve Civique.

## Objectif

JeVeuxAider.gouv.fr met en relation celles et ceux qui veulent agir pour l'intérêt général avec les associations, acteurs publics et collectivités territoriales qui ont besoin de bénévoles.

Les missions de bénévolat sont ouvertes à tout citoyen âgé de plus de 16 ans et résidant en France, sans condition de nationalité. Pour les personnes âgées de 16 à 18 ans, une autorisation du représentant légal est nécessaire.

Ce dépôt contient l'application frontend (Nuxt) qui couvre notamment :

- la recherche et la consultation de missions de bénévolat ;
- l'inscription et l'espace bénévole ;
- l'espace responsable et l'administration des structures ;
- la messagerie, les statistiques et les contenus éditoriaux.

## Pile technique

| Couche | Technologies |
|--------|-------------|
| Framework | [Nuxt 3](https://nuxt.com) (Vue 3, Composition API, TypeScript) |
| Rendu | SSR par défaut ; certaines zones en SPA (`/admin`, `/profile`, `/messages`…) |
| Styles | [Tailwind CSS](https://tailwindcss.com), [DSFR](https://www.systeme-de-design.gouv.fr/) (Design System de l'État) |
| État | [Pinia](https://pinia.vuejs.org) |
| Formulaires | [Yup](https://github.com/jquense/yup) (via le composable `useForm`) |
| Recherche | [Algolia](https://www.algolia.com) |
| CMS | [Strapi](https://strapi.io) (contenus éditoriaux) |
| API métier | Backend Laravel (`jeveuxaider-back`) via OAuth 2 |
| Analytics | Plausible, Google Tag Manager |
| Outils | ESLint, Prettier, `@nuxt/image`, `@nuxtjs/sitemap` |

**Prérequis :** Node.js 24, npm 11 (ou Yarn).

## Architecture

```
jeveuxaider-front/
├── pages/          # Routage file-based (Nuxt)
├── components/     # Composants Vue réutilisables
├── features/       # Logique métier par domaine (missions, organisations, search…)
├── composables/    # Hooks Vue partagés
├── store/          # Stores Pinia (auth, messaging, algolia…)
├── plugins/        # Initialisation (API, auth, labels, consentement…)
├── middleware/     # Garde-fous de navigation
├── server/         # Routes et middleware Nitro (sitemaps, redirections)
├── api/            # Clients pour services externes (Plausible, API Engagement…)
├── types/          # Types TypeScript
└── assets/         # CSS et ressources statiques
```

L'application s'appuie sur une API REST Laravel (`API_URL/api`) pour les données métier (missions, utilisateurs, participations…). Le plugin `plugins/api.ts` centralise les appels HTTP, l'authentification OAuth et la gestion des erreurs.

Services externes configurés via variables d'environnement :

- **Algolia** — recherche de missions, organisations et contenus ;
- **Strapi** — pages et contenus éditoriaux ;
- **Google Places** — autocomplétion d'adresses ;
- **Plausible / GTM / Axeptio** — mesure d'audience et consentement cookies.

## Démarrage en local

### 1. Prérequis

- Node.js **24** et npm **11** (ou Yarn)
- Le backend Laravel (`jeveuxaider-back`) lancé sur le port **8000** — voir le README du dépôt backend

### 2. Configuration

Copier le fichier d'exemple et renseigner les variables :

```bash
cp .env-example .env
```

Variables minimales pour un environnement local :

| Variable | Description | Valeur par défaut |
|----------|-------------|-------------------|
| `APP_URL` | URL du frontend | `http://localhost:3000` |
| `API_URL` | URL du backend Laravel | `http://localhost:8000` |
| `OAUTH_CLIENT_ID` | Identifiant OAuth Passport | — |
| `OAUTH_CLIENT_SECRET` | Secret OAuth Passport | — |

Les clés Algolia, Strapi, Google Places et autres services sont optionnelles pour un premier démarrage, mais nécessaires pour tester la recherche et certains contenus.

### 3. Installation et lancement

```bash
yarn install
yarn dev
```

L'application est accessible sur [http://localhost:3000](http://localhost:3000).

### 4. Build et preview production

```bash
yarn build    # génère le bundle dans .output/
yarn start    # serveur Node de production
yarn preview  # preview du build localement
```

## Scripts utiles

| Commande | Description |
|----------|-------------|
| `yarn dev` | Serveur de développement |
| `yarn build` | Build de production |
| `yarn start` | Lance le serveur Node (.output) |
| `yarn preview` | Preview du build |
