# Synthèse d'activité : incubateur-ademe (du [Date Début] au [Date Fin])

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une volonté de renforcer la précision des outils de simulation et d'enrichir l'expérience utilisateur. Des projets majeurs comme [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) et [benefriches](/repos/incubateur-ademe/benefriches) ont bénéficié de refontes profondes, notamment sur les parcours d'onboarding et la découverte des actions climatiques, rendant les outils plus intuitifs et personnalisés.

L'intégration de technologies avancées, telles que le Machine Learning dans [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) pour la gestion des données ou l'usage de l'IA dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions), permet d'offrir des analyses toujours plus fines. Enfin, l'élargissement de l'audience, comme l'ouverture de [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) aux entreprises privées, démontre une dynamique de croissance et d'ouverture des outils de l'incubateur.

## Sécurité
- **Gestion des accès et authentification** : Renforcement de la sécurité via l'intégration de l'authentification FGP dans [grafana](/repos/incubateur-ademe/grafana), l'ajout de l'authentification à deux facteurs (2FA) dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) et [vaultwarden](/repos/incubateur-ademe/vaultwarden), et amélioration de la configuration des cookies JWT dans [nosgestesclimat-server](/repos/incubateur-ademe/nosgestesclimat-server).
- **Corrections de vulnérabilités** : Résolution d'alertes de sécurité (CodeQL et Dependabot) dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher) et correction du mécanisme de protection de l'origine dans [mutafriches](/repos/incubateur-ademe/mutafriches).

## Autres changements notables
- **Migrations technologiques majeures** : Passage à Strapi 5 pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site), [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms) et [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions), et migration vers NestJS 12 pour [benefriches](/repos/incubateur-ademe/benefriches).
- **Modernisation du code et de l'architecture** : Migration massive vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override) et [aldo](/repos/incubateur-ademe/aldo), et refonte vers une architecture modulaire dans [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy).
- **Optimisation de l'infrastructure** : Automatisation des déploiements sur Scalingo pour [metabase](/repos/incubateur-ademe/metabase) et amélioration des processus de déploiement des monorepos avec [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack).
- **Intelligence Artificielle** : Implémentation d'un serveur MCP pour permettre aux agents IA d'accéder aux outils métier dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions).

## Dépôts les plus actifs
- [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) : Optimisations massives de l'infrastructure, de l'observabilité et de la découverte des actions climatiques.
- [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) : Avancées majeures en Machine Learning et déploiement d'un nouveau système de gestion des suggestions.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte du parcours utilisateur, du système d'emails automatisés et amélioration des scores d'impact.
- [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) : Ajout de fonctionnalités clés comme la synchronisation Notion et la gestion de domaines personnalisés.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ouverture aux entreprises privées et migration vers Strapi 5.
