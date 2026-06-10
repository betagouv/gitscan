# JeVeuxAider.gouv.fr — Backend

API métier de [JeVeuxAider.gouv.fr](https://jeveuxaider.gouv.fr), la plateforme publique du bénévolat proposée par la Réserve Civique.

## Objectif

JeVeuxAider.gouv.fr met en relation celles et ceux qui veulent agir pour l'intérêt général avec les associations, acteurs publics et collectivités territoriales qui ont besoin de bénévoles.

Les missions de bénévolat sont ouvertes à tout citoyen âgé de plus de 16 ans et résidant en France, sans condition de nationalité. Pour les personnes âgées de 16 à 18 ans, une autorisation du représentant légal est nécessaire.

Ce dépôt contient l'API Laravel consommée par le frontend Nuxt (`jeveuxaider-front`). Elle gère notamment :

- les missions, structures et participations ;
- l'authentification et les profils utilisateurs (bénévoles, responsables, référents) ;
- la messagerie, les notifications et les emails transactionnels ;
- la modération, les statistiques et les exports ;
- l'indexation Algolia et les intégrations tierces (France Connect, API Engagement, SNU…).

## Pile technique

| Couche            | Technologies                                                                             |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Framework         | [Laravel 12](https://laravel.com) (PHP 8.2+)                                             |
| Base de données   | [PostgreSQL](https://www.postgresql.org)                                                 |
| Authentification  | [Laravel Passport](https://laravel.com/docs/passport) (OAuth 2)                          |
| Recherche         | [Laravel Scout](https://laravel.com/docs/scout) + [Algolia](https://www.algolia.com)     |
| Files d'attente   | [Redis](https://redis.io) + [Laravel Horizon](https://laravel.com/docs/horizon)          |
| Stockage fichiers | S3 (via Flysystem) + [Spatie Media Library](https://spatie.be/docs/laravel-medialibrary) |
| Emails            | Brevo, SendGrid                                                                          |
| Observabilité     | [Sentry](https://sentry.io)                                                              |
| Tests             | [Pest](https://pestphp.com)                                                              |
| Qualité           | Laravel Pint, PHP-CS-Fixer                                                               |

**Extensions PHP requises :** `redis`, `sodium`.

## Architecture

```
jeveuxaider-back/
├── app/
│   ├── Http/Controllers/Api/   # Contrôleurs REST
│   ├── Models/                 # Modèles Eloquent
│   ├── Services/               # Intégrations externes (Algolia, France Connect, OpenAI…)
│   ├── Jobs/                   # Tâches asynchrones (Horizon)
│   ├── Actions/                # Actions métier
│   ├── Mail/                   # Emails transactionnels
│   ├── Notifications/          # Notifications applicatives
│   └── Console/Commands/       # Commandes Artisan planifiées
├── routes/
│   └── api.php                 # Routes API (/api/*)
├── database/
│   ├── migrations/             # Schéma PostgreSQL
│   └── seeders/                # Données initiales (rôles…)
└── resources/views/emails/     # Templates Blade des emails
```

L'API expose des endpoints REST sous `/api`, protégés par OAuth 2 (Passport) pour les routes authentifiées. Le frontend Nuxt s'y connecte via `API_URL`.

Services externes configurés via variables d'environnement :

- **Algolia** — indexation et recherche de missions, organisations ;
- **S3** — stockage des médias et exports ;
- **Brevo** — envoi d'emails ;
- **France Connect** — connexion via l'identité numérique ;
- **API Engagement, SNU, France Travail** — référentiels et synchronisations ;
- **Anthropic** — modération et analyse de contenu.

En production, les tâches planifiées et les files d'attente sont gérées par Horizon (`Procfile`).

## Démarrage en local

### 1. Prérequis

- PHP **8.2+** avec les extensions `redis`
- [Composer](https://getcomposer.org)
- PostgreSQL
- Redis (recommandé ; la file peut rester en `sync` pour un premier démarrage)
- Le frontend Nuxt (`jeveuxaider-front`) sur le port **3000** pour tester l'application complète

### 2. Configuration

Copier le fichier d'exemple et renseigner les variables :

```bash
cp .env.example .env
```

Variables minimales pour un environnement local :

| Variable                      | Description               | Valeur par défaut       |
| ----------------------------- | ------------------------- | ----------------------- |
| `APP_URL`                     | URL du backend            | `http://localhost:8000` |
| `FRONT_URL`                   | URL du frontend           | `http://localhost:3000` |
| `DB_DATABASE`                 | Nom de la base PostgreSQL | `jva`                   |
| `DB_USERNAME` / `DB_PASSWORD` | Identifiants PostgreSQL   | —                       |
| `QUEUE_CONNECTION`            | Driver de file d'attente  | `sync`                  |

Les clés Algolia, S3, email et autres services sont optionnelles pour un premier démarrage, mais nécessaires pour tester la recherche, les uploads et les envois d'emails.

### 3. Installation et lancement

```bash
composer install
php artisan key:generate
php artisan migrate
php artisan db:seed
php artisan passport:install
php artisan serve
```

L'API est accessible sur [http://localhost:8000](http://localhost:8000).

Lors de `passport:install`, récupérer l'identifiant et le secret du client **Password Grant** (second jeu de credentials) et les renseigner dans le `.env` du frontend :

```
OAUTH_CLIENT_ID=
OAUTH_CLIENT_SECRET=
```

### 4. Files d'attente et tâches planifiées

Pour exécuter les jobs asynchrones en local :

```bash
php artisan horizon
```

Pour les tâches planifiées (emails de bilan, synchronisations…) :

```bash
php artisan schedule:work
```

## Scripts utiles

| Commande                    | Description                   |
| --------------------------- | ----------------------------- |
| `php artisan serve`         | Serveur de développement      |
| `php artisan migrate`       | Applique les migrations       |
| `php artisan db:seed`       | Seed les rôles                |
| `php artisan horizon`       | Supervise les files d'attente |
| `php artisan schedule:work` | Exécute le scheduler          |
| `./vendor/bin/pest`         | Lance la suite de tests       |
| `./vendor/bin/pint`         | Formate le code PHP           |
