# Synthèse d'activité : incubateur-ademe (du 01/04 au 30/10)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des outils d'aide à la décision et une amélioration significative de la précision des modèles de calcul d'impact environnemental. L'intégration de l'intelligence artificielle dans [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions) et la refonte complète de l'expérience utilisateur sur des projets comme [benefriches](/repos/incubateur-ademe/benefriches) ou [france-chaleur-urbaine-pac](/repos/incubateur-ademe/france-chaleur-urbaine-pac) témoignent d'une volonté de rendre les données climatiques plus accessibles et actionnables pour les utilisateurs finaux.

Parallèlement, l'infrastructure a bénéficié de migrations technologiques majeures vers des solutions plus modernes (Strapi 5, NestJS 12), renforçant la robustesse et la scalabilité des services ([plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site), [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms)). L'automatisation de la gestion des accès et des processus de déploiement a également été un axe fort pour sécuriser et fluidifier l'exploitation des outils ([account-manager](/repos/incubateur-ademe/account-manager), [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher)).

## Sécurité
- **Gestion des accès et authentification** : Renforcement de la sécurité via l'authentification 2FA (passkeys, OTP) dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) et migration vers une authentification centralisée (FGP) pour [grafana](/repos/incubateur-ademe/grafana).
- **Gouvernance et Offboarding** : Automatisation du retrait des accès (GitHub, Notion) pour sécuriser la gestion des comptes dans [account-manager](/repos/incubateur-ademe/account-manager).
- **Maintenance corrective** : Résolution d'alertes de sécurité (CodeQL, Dependabot) dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher) et amélioration de la gestion du 2FA dans [vaultwarden](/repos/incubateur-ademe/vaultwarden).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Strapi 5 pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms), et adoption de NestJS 12 pour [benefriches](/repos/incubateur-ademe/benefriches).
- **Évolutions architecturales** : Migration vers tRPC pour [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions) et refonte modulaire en TypeScript pour [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy).
- **Outils de développement et Design System** : Création d'un "Builder UI" pour la personnalisation visuelle du Design System dans [dsfr-override](/repos/incubateur-ademe/dsfr-override) et optimisation des déploiements monorepos avec [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack).

## Dépôts les plus actifs
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) (et ses composants) : Amélioration majeure du modèle de calcul d'empreinte carbone et de l'expérience de simulation.
- [account-manager](/repos/incubateur-ademe/account-manager) : Automatisation poussée de la gestion des accès, des ressources et du suivi de conformité.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte de l'onboarding, du système d'emails automatisés et précision des scores d'impact.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ouverture du service aux entreprises privées et modernisation de l'infrastructure.
- [publicodes-commun](/repos/incubateur-ademe/publicodes-commun) : Mise à jour des données du mix électrique 2025 et stabilisation des processus de publication.
