# Synthèse d'activité : incubateur-ademe (dernières semaines)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une forte dynamique d'évolution des produits utilisateurs et une modernisation profonde des infrastructures. Les outils de simulation et d'aide à la décision, tels que [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) et [benefriches](/repos/incubateur-ademe/benefriches), bénéficient de modèles de calcul plus précis et de parcours utilisateurs enrichis, incluant de nouveaux catalogues d'actions, un onboarding fluidifié et des systèmes de communication automatisés.

Parallèlement, une vague de migrations technologiques majeures est en cours, notamment le passage à Strapi 5 pour plusieurs services ([territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions), [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site)) et une adoption généralisée de TypeScript pour renforcer la robustesse des outils ([dsfr-override](/repos/incubateur-ademe/dsfr-override), [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy)).

## Sécurité
- Automatisation du retrait des accès GitHub et Notion pour améliorer l'offboarding dans [account-manager](/repos/incubateur-ademe/account-manager).
- Résolution de vulnérabilités CodeQL et Dependabot dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher).
- Renforcement de la sécurité des connexions PostgreSQL via la vérification TLS dans [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions).
- Sécurisation des commandes de base de données via l'utilisation de variables d'environnement dans [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets).
- Correction du mécanisme de protection de l'origine (*origin guard*) dans [mutafriches](/repos/incubateur-ademe/mutafriches).
- Migration vers une authentification centralisée via FGP pour [grafana](/repos/incubateur-ademe/grafana).

## Autres changements notables
- **Migrations de CMS** : Passage à Strapi 5 pour [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions), [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms).
- **Migrations de langages et frameworks** : Conversion complète vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override) et [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy), et refonte architecturale vers Django/React pour [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) ainsi que vers NestJS 12 pour [benefriches](/repos/incubateur-ademe/benefriches).
- **Infrastructure et Observabilité** : Mise en place d'outils de suivi avancés (PostHog, OpenTelemetry) dans [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app) et automatisation du cycle de vie des modèles dans [scalingo-watcher](/repos/incubateur-ademe/scalingo-watcher).
- **Authentification** : Refonte de l'architecture d'authentification via SSO OAuth dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles).

## Dépôts les plus actifs
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) : Évolutions majeures du moteur de règles, de l'interface et de la précision des simulations.
- [account-manager](/repos/incubateur-ademe/account-manager) : Automatisation poussée de la gestion des accès et du suivi des ressources.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte de l'onboarding, du système d'emails et des calculs d'impact.
- [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) : Déploiement de l'Assistant V2 et changement d'architecture technique.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ouverture du service aux entreprises privées et migration vers Strapi 5.
