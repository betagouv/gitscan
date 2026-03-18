## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'enrichissement de l'API avec l'ajout de nouvelles fonctionnalités liées aux plans de transition écologique et aux compétences, ainsi que sur l'amélioration de l'import de données et de la documentation. Des refactorings importants ont également été réalisés pour optimiser l'architecture et la performance de l'application. L'interface utilisateur a été améliorée avec la refonte de la page vocabulaire métier.

### Évolutions fonctionnelles
- **API Référentiel Collectivités :** Ajout d'une nouvelle API permettant d'accéder aux informations sur les collectivités. [#1234](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/1234)
- **Plans de transition et fiches action :** Intégration des données des plans de transition et des fiches action de la TC opendata, avec un job CRON dédié pour l'import via BullMQ.
- **Vocabulaire métier :** Refonte complète de la page "Vocabulaire métier" selon les maquettes Figma.
- **Compétences :** Les compétences sont désormais accessibles via un nouvel endpoint `/v1/groupements/competences` et sont incluses systématiquement.
- **Recherche :** Ajout d'un endpoint de recherche sur la page du référentiel et documentation associée.
- **Health Check :** Ajout d'une page d'accueil et d'un endpoint health check pour faciliter le monitoring de l'application.
- **Inclusion des compétences :** Possibilité d'inclure les compétences dans les réponses de l'API `/v1/communes/:code` via le paramètre `includeCompetences=true`.

### Évolutions techniques
- **Refactoring de l'architecture API :** Restructuration des APIs avec des préfixes dédiés pour une meilleure organisation.
- **Séparation des schémas PostgreSQL :** Séparation des tables en 3 schémas PostgreSQL pour une meilleure gestion des données.
- **Optimisation de l'import XLSX Banatic :**  Traitement des fichiers XLSX Banatic en streaming pour éviter les problèmes de mémoire liés aux fichiers volumineux.
- **Correction des noms de Foreign Keys :** Correction des noms de Foreign Keys dans le snapshot et le format TRUNCATE schema-qualifié.
- **Documentation Swagger :** Séparation et harmonisation des documents Swagger pour une meilleure clarté.
- **Monitoring Sentry :** Ajout du monitoring Sentry pour les CRONs d'import TC opendata.

### Autres changements
- **Documentation API :** Ajout de badges "Alpha" et d'exemples d'utilisation sur la documentation de l'API Référentiel.
- **Seed :** Correction du décodage des entités HTML et XML dans les données Banatic.
- **Nettoyage :** Suppression de badges "nouveau" et renommage de la carte API Projets.
- **Correction d'URL :** Correction de l'URL de génération de types OpenAPI et de l'URL de la source ZLV (SIREN→SIRET).
- **Migration :** Renommage d'une migration pour une meilleure description.
- **CI/CD :** Corrections de la CI et des problèmes remontés en revue.
