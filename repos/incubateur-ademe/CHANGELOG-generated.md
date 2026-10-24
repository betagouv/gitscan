# Synthèse d'activité : incubateur-ademe (du 01/10 au 15/10/2026)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique de modernisation des outils d'aide à la décision et de simulation environnementale. Les utilisateurs bénéficieront d'expériences nettement améliorées grâce à des refontes d'interface majeures sur [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) et [benefriches](/repos/incubateur-ademe/benefriches), ainsi que par l'intégration de nouvelles fonctionnalités comme l'import de données par IA dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions).

Parallèlement, l'ouverture de services à de nouveaux publics, notamment pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site), et l'automatisation accrue de la gestion des accès via [account-manager](/repos/incubateur-ademe/account-manager) renforcent la maturité opérationnelle et la scalabilité de l'écosystème.

## Sécurité
- Résolution d'alertes de sécurité (CodeQL et Dependabot) pour [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher).
- Renforcement de la sécurité des accès via la migration vers l'authentification FGP pour [grafana](/repos/incubateur-ademe/grafana).
- Amélioration de la protection de l'origine des intégrateurs dans [mutafriches](/repos/incubateur-ademe/mutafriches).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage à Strapi 5 pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms), migration de Heroku vers Scalingo pour [metabase](/repos/incubateur-ademe/metabase), et transition de PostgREST vers tRPC pour [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions).
- **Évolutions architecturales** : Passage d'une structure monolithique à une architecture modulaire pour [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy) et centralisation des calculs via un module partagé dans [benefriches](/repos/incubateur-ademe/benefriches).
- **Modernisation du développement** : Migration massive vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override) et [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy).
- **Automatisation DevOps** : Mise en place de workflows CI/CD pour le déploiement de [metabase](/repos/incubateur-ademe/metabase) et optimisation du déploiement de monorepos pnpm avec [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack).

## Dépôts les plus actifs
- [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) : Optimisations massives de performance, d'observabilité (PostHog, OpenTelemetry) et de l'expérience utilisateur.
- [account-manager](/repos/incubateur-ademe/account-manager) : Automatisation poussée de l'offboarding (GitHub, Notion) et renforcement de la visibilité sur les ressources.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte complète de l'onboarding, du système d'emails automatisés et amélioration de la précision des scores d'impact.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ouverture aux entreprises privées et migration vers Strapi 5.
- [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher) : Lancement de la version publique et automatisation du cycle de vie des modèles.
