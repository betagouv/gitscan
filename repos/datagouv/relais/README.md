# relais

**R**estitution d'**E**xtractions de **L**istes d'**A**dministrés **I**dentifiés **S**écurisée.

Service de Proactivité — Récupération de l'écosystème API Entreprise. Sœur de
[`apistration`](../apistration) et [`data_pass`](../data_pass).

## Rôle

`relais` orchestre la récupération asynchrone d'extractions nominatives auprès
de fournisseurs externes (CNOUS en V1) à partir d'habilitations validées dans
DataPass, puis transmet les fichiers au flux Livraison.

Hors périmètre : la transmission aux collectivités (assurée par le flux
Livraison, hors de ce dépôt).

## Architecture (V1)

- Rails minimal (API-only) + PostgreSQL
- Background jobs via [GoodJob](https://github.com/bensheldon/good_job)
  (Postgres-backed, aligné sur `apistration/site`)
- Webhook DataPass → `ProactiviteRequest` `pending`
- Scheduler GoodJob → exécute le 2-step async (POST generate, GET download)
  vers le fournisseur → `completed` ou `failed`
- Stockage fichier V1 : `bytea` chiffré (cf. API-6718)
- Audit log applicatif (cf. API-6723)

> Hébergement : arbitrage en cours (Scalingo vs bare-metal/Ansible) — cf.
> umbrella infra **API-6750** et ADR **API-6726**. Les choix applicatifs ci-dessus
> sont indépendants de cette décision.

## Pré-requis

- Ruby `4.0.1` (cf. `.ruby-version`)
- PostgreSQL ≥ 14
- Bundler

## Installation locale

```bash
./bin/install.sh
```

Le script :
- installe les gems (`bundle install`)
- crée le rôle `relais` et les bases `relais_development` / `relais_test`
- prépare les schémas

Pour lancer l'app + le worker en parallèle :

```bash
foreman start -f Procfile.dev   # ou overmind start -f Procfile.dev
```

Variables d'env locales : copier `.env.example` vers `.env.local` et
renseigner les valeurs (le fichier `.env.local` est gitignoré).

## Tests / lint

```bash
bundle exec rspec               # suite RSpec
COVERAGE=true bundle exec rspec # avec coverage SimpleCov
bundle exec rubocop             # lint
bundle exec rubocop -A          # auto-fix
```

## Variables d'environnement

| Var | Défaut | Usage |
| --- | --- | --- |
| `POSTGRES_HOST` | `localhost` | Hôte Postgres |
| `POSTGRES_USER` | `relais` | Rôle Postgres |
| `POSTGRES_PASSWORD` | `wow*verysecret` | Mot de passe Postgres (dev) |
| `DATABASE_NAME_DEVELOPMENT` | `relais_development` | Base dev |
| `DATABASE_NAME_TEST` | `relais_test` | Base test |
| `DATABASE_NAME_PRODUCTION` | `relais_production` | Base prod |
| `RAILS_MAX_THREADS` | `15` | Pool Postgres + Puma |
| `GOOD_JOB_MAX_THREADS` | `5` | Workers GoodJob |
| `GOOD_JOB_POLL_INTERVAL` | `10` | Intervalle de poll (s) |

Les secrets fournisseurs (CNOUS, DataPass webhook, master key Rails) ne
sont jamais committés ni loggés (cf. `CLAUDE.md` — contraintes sécurité
R-005). Le canal de distribution dépend de l'arbitrage hébergeur en cours
(API-6750).

## Healthcheck

`GET /healthz` → `200 { "status": "ok" }`

## Déploiement

L'hébergement de `relais` est en cours d'arbitrage (Scalingo vs
bare-metal/Ansible) — cf. **API-6750** (umbrella infra) et **API-6726**
(ADR). La stratégie de déploiement, le provisioning et la CI auto-deploy
seront documentés une fois le choix tranché.

## Conventions

Voir [`CLAUDE.md`](./CLAUDE.md) — contraintes sécurité, style de code, périmètre
inter-dépôts.
