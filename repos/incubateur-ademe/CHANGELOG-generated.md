# Synthèse d'activité : incubateur-ademe (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des outils d'aide à la décision environnementale et une amélioration significative de l'expérience utilisateur. Des projets majeurs comme [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions) et [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) ont franchi des étapes clés avec la mise en place de nouveaux parcours de diagnostic et d'outils d'aide à la décision opérationnels.

Parallèlement, la précision des modèles de calcul est renforcée, notamment pour les empreintes carbone dans [publicodes-empreinte-carbone-chauffage](/repos/incubateur-ademe/publicodes-empreinte-carbone-chauffage) et [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat). Ces évolutions, complétées par la simplification des processus de déclaration dans [ecopass](/repos/incubateur-ademe/ecopass), permettent aux utilisateurs de bénéficier de données plus fiables et d'interfaces plus intuitives, mieux adaptées aux usages mobiles.

## Sécurité
- **Renforcement de l'authentification et des accès** : mise en place du SSO OAuth et de l'authentification à deux facteurs (2FA) via passkeys/OTP dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles), migration vers l'authentification FGP pour [grafana](/repos/incubateur-ademe/grafana), et amélioration de la gestion du 2FA dans [vaultwarden](/repos/incubateur-ademe/vaultwarden).
- **Protection des données et de l'infrastructure** : implémentation du chiffrement des données sensibles dans [tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs), correction du mécanisme de protection de l'origine dans [mutafriches](/repos/incubateur-ademe/mutafriches) et sécurisation des cookies JWT dans [nosgestesclimat-server](/repos/incubateur-ademe/nosgestesclimat-server).

## Autres changements notables
- **Modernisation des infrastructures et des outils de développement** : migration vers Wagtail pour la gestion de contenu dans [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail), adoption de TypeScript et création d'une interface de personnalisation visuelle (Builder UI) pour [dsfr-override](/repos/incubateur-ademe/dsfr-override), et refonte de l'environnement de développement local (Docker/Supabase) pour [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions).
- **Refactorisations architecturales majeures** : passage à une architecture modulaire pour [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy) et refonte profonde du système de création de projets via un moteur de formulaires dans [benefriches](/repos/incubateur-ademe/benefriches).
- **Optimisation du déploiement** : amélioration des processus de déploiement sur Scalingo via le buildpack [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack) et automatisation du déploiement de [metabase](/repos/incubateur-ademe/metabase).

## Dépôts les plus actifs
- [territories-en-transitions](/repos/incubateur-ademe/territories-en-transitions) : Développement majeur du processus PCAET et modernisation complète de la stack de développement.
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) : Évolutions des règles de calcul (transport/mobilité) et optimisation des processus de déploiement.
- [benefriches](/repos/incubateur-ademe/benefriches) : Refonte complète de l'expérience de création et de modification de projets photovoltaïques.
- [dsfr-override](/repos/incubateur-ademe/dsfr-override) : Transformation majeure vers TypeScript et lancement d'un outil de personnalisation visuelle du Design System.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Refonte de l'outil d'aide à la décision et intégration de nouvelles données.
