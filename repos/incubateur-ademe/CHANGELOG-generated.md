# Synthèse d'activité : incubateur-ademe (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente est marquée par une montée en maturité des outils de diagnostic et de calcul d'impact environnemental, avec des améliorations de précision pour [publicodes-empreinte-carbone-chauffage](/repos/incubateur-ademe/publicodes-empreinte-carbone-chauffage) et [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat). L'organisation élargit également ses horizons en ouvrant ses plateformes à de nouveaux publics, comme les entreprises privées pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) ou les citoyens pour [ecopass](/repos/incubateur-ademe/ecopass).

Parallèlement, une forte dynamique de modernisation des interfaces utilisateur est observée, notamment pour faciliter la navigation et le partage de résultats dans [france-chaleur-urbaine-pac](/repos/incubateur-ademe/france-chaleur-urbaine-pac) et [benefriches](/repos/incubateur-ademe/benefriches), améliorant ainsi l'accessibilité et l'engagement des utilisateurs finaux.

## Sécurité
- **Authentification et accès** : Intégration du SSO/OIDC pour [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions) et [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles), et mise en place d'une authentification consolidée via FGP pour [grafana](/repos/incubateur-ademe/grafana).
- **Protection des sessions et des données** : Renforcement de la sécurité des sessions pour [account-manager](/repos/incubateur-ademe/account-manager) et [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app), et amélioration des contrôles d'accès pour [ecopass](/repos/incubateur-ademe/ecopass).
- **Sécurisation des infrastructures** : Renforcement de la protection de l'origine des requêtes dans [mutafriches](/repos/incubateur-ademe/mutafriches) et rotation des mots de passe pour [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets).

## Autres changements notables
- **Migrations majeures de CMS et de Backend** : Passage à Strapi 5 pour [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et [plusfraichemaville-cms](/repos/incubateur-ademe/plusfraichemaville-cms), et migration vers Wagtail pour [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail).
- **Refontes architecturales** : Adoption de la "Clean Architecture" dans [benefriches](/repos/incubateur-ademe/benefriches), passage au pattern Repository dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions) et modularisation en TypeScript pour [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy).
- **Modernisation du développement** : Migration massive vers TypeScript pour [dsfr-override](/repos/incubateur-ademe/dsfr-override) et optimisation des processus de déploiement (Terraform, pnpm) pour [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) et [ngc-scalingo-buildpack](/repos/incubateur-ademe/ngc-scalingo-buildpack).
- **Évolutions de données** : Migration vers MariaDB pour [tacct](/repos/incubateur-ademe/tacct) et mise à jour des modèles de calcul pour [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat).

## Dépôts les plus actifs
- [nosgestesclimat](/repos/incubateur-ademe/nosgestesclimat) (et ses composants app, server, site) : Évolutions majeures du modèle de calcul, de l'interface et de la gestion des résultats.
- [tacct](/repos/incubateur-ademe/tacct) (et tacct-legacy-nextjs) : Amélioration de la gestion des comptes utilisateurs et migration de la base de données.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ouverture aux entreprises et refonte de l'outil d'aide à la décision.
- [ecopass](/repos/incubateur-ademe/ecopass) : Structuration de la gestion des organisations et enrichissement des données produits.
- [benefriches](/repos/incubateur-ademe/benefriches) : Amélioration de l'analyse économique et refonte du moteur de formulaires.
