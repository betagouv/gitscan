# Synthèse d'activité : incubateur-ademe (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte orientation vers l'amélioration de l'expérience utilisateur et la précision des outils d'aide à la décision. Des avancées majeures ont été réalisées sur [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) et [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets), notamment avec le lancement de l'Assistant V2 et l'amélioration de la découverte des actions climatiques. Parallèlement, l'ouverture de nouveaux services, comme l'accès aux entreprises privées pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) ou la synchronisation Notion pour [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles), renforce l'utilité métier des outils.

Les modèles de calcul environnementaux gagnent également en finesse, avec des mises à jour de précision pour les projets [publicodes-empreinte-carbone-chauffage](/repos/incubateur-ademe/publicodes-empreinte-carbone-chauffage) et [publicodes-commun](/repos/incubateur-ademe/publicodes-commun).

## Sécurité
- Résolution de vulnérabilités sur des dépendances critiques dans [aldo](/repos/incubateur-ademe/aldo).
- Correction d'alertes de sécurité (CodeQL/Dependabot) dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher).
- Renforcement de la sécurité via l'authentification FGP dans [grafana](/repos/incubateur-ademe/grafana) et l'amélioration du mécanisme de protection de l'origine dans [mutafriches](/repos/incubateur-ademe/mutafriches).
- Amélioration de la configuration de sécurité du serveur dans [nosgestesclimat-server](/repos/incubateur-ademe/nosgestesclimat-server).

## Autres changements notables
- **Migrations d'infrastructure et de frameworks** : Passage à Strapi 5 pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms), migration de Heroku vers Scalingo pour [metabase](/repos/incubateur-ademe/metabase), et modernisation vers Node 24/TypeScript pour [aldo](/repos/incubateur-ademe/aldo).
- **Évolutions architecturales** : Mise en place d'un serveur MCP pour l'IA dans [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions), refonte de l'architecture client vers un modèle modulaire dans [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy), et migration complète vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override).
- **Automatisation et Observabilité** : Automatisation du cycle de vie des modèles dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher) et intégration poussée de l'observabilité (PostHog, OpenTelemetry) dans [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) et [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions).
- **Gestion des accès** : Refonte de l'architecture d'authentification via SSO OAuth pour [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles).

## Dépôts les plus actifs
- [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) : Optimisations massives de l'infrastructure, de l'observabilité et de la découverte des actions.
- [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) : Lancement de l'Assistant V2 et ouverture d'une API v1.
- [dsfr-override](/repos/incubateur-ademe/dsfr-override) : Création d'une interface de personnalisation visuelle (Builder UI) et migration TypeScript.
- [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) : Ajout de fonctionnalités clés comme la synchronisation Notion et le mode iframe.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Migration vers Strapi 5 et ouverture aux entreprises privées.
