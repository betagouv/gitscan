# Synthèse d'activité : incubateur-ademe (du 01/08 au 31/08)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des outils d'aide à la décision et de simulation climatique. Des évolutions majeures ont été déployées pour faciliter l'analyse d'impact et la transition écologique, notamment via la refonte de l'aide à la décision dans [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site), l'enrichissement des analyses économiques dans [benefriches](/repos/incubateur-ademe/benefriches) et l'amélioration des outils de calcul carbone dans l'écosystème [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat).

Parallèlement, l'organisation renforce ses capacités de gestion et d'administration. Le déploiement opérationnel de [account-manager](/repos/incubateur-ademe/account-manager) et l'amélioration des interfaces de gestion des utilisateurs dans [tacct](/repos/incubateur-ademe/tacct) et [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) témoignent d'une volonté de professionnaliser le pilotage des plateformes et de l'engagement des utilisateurs.

## Sécurité
- **Gestion des accès et authentification** : Renforcement de la sécurité via l'implémentation de l'authentification à deux facteurs (2FA) dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) et l'amélioration de la gestion du 2FA dans [vaultwarden](/repos/incubateur-ademe/vaultwarden).
- **Centralisation des accès** : Migration vers une authentification consolidée via FGP pour [grafana](/repos/incubateur-ademe/grafana).
- **Sécurisation des flux** : Intégration de la compatibilité Tailscale pour [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy) et renforcement de la validation des processus d'inscription dans [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app).

## Autres changements notables
- **Migrations d'infrastructure et de CMS** : 
    - Migration de l'infrastructure de Heroku vers Scalingo pour [metabase](/repos/incubateur-ademe/metabase).
    - Migration du système de gestion de contenu vers Wagtail pour [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail).
- **Refontes architecturales et techniques** :
    - Passage à une architecture tRPC pour [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions).
    - Adoption de la "Clean Architecture" pour [benefriches](/repos/incubateur-ademe/benefriches).
    - Migration complète vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override).
    - Refonte du moteur de formulaires dans [benefriches](/repos/incubateur-ademe/benefriches) pour mutualiser la logique de création et de modification.
- **Optimisation du déploiement et DevOps** :
    - Amélioration du support des monorepos pnpm avec [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack).
    - Premier déploiement opérationnel et automatisation de l'offboarding pour [account-manager](/repos/incubateur-ademe/account-manager).

## Dépôts les plus actifs
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) : Évolutions continues du modèle de calcul carbone et de l'engagement utilisateur (IA, nouveaux catalogues).
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Refonte majeure de l'arbre de décision et de l'expérience utilisateur.
- [benefriches](/repos/incubateur-ademe/benefriches) : Amélioration significative de l'analyse économique et de la gestion des projets photovoltaïques.
- [dsfr-override](/repos/incubateur-ademe/dsfr-override) : Développement d'un outil de personnalisation visuelle du Design System Français.
- [tacct](/repos/incubateur-ademe/tacct) : Travaux importants sur l'accessibilité, la gestion des données et la stabilisation de l'infrastructure.
