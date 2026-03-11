## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives, notamment l'ajout d'une nouvelle API Référentiel Collectivités et de nouvelles fonctionnalités pour l'API existante, comme la possibilité d'inclure les compétences associées aux communes. L'interface utilisateur a également été améliorée, avec une refonte de la page vocabulaire et des ajustements visuels. Des corrections ont été apportées pour améliorer la robustesse de l'import de données et du proxy.

### Évolutions fonctionnelles
- Ajout d'une nouvelle API Référentiel Collectivités [#993b043](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/993b043)
- Possibilité d'inclure les compétences associées aux communes via le paramètre `includeCompetences` dans l'API `/v1/communes/:code` [#3c9df57](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3c9df57) et [#3c47e23](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/3c47e23)
- Refonte de la page vocabulaire dans l'espace ressources [#eab719b](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/eab719b)
- Ajout d'un endpoint GET pour les catégories de compétences `/v1/competences/categories` [#c4530b6](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/c4530b6)
- Ajout de pages d'accueil et d'un endpoint health check pour l'API [#e27425f](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/e27425f)
- Améliorations visuelles : retrait des badges "nouveau" et renommage de la carte API Projets [#ae8cb93](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/ae8cb93) et [#78b6faa](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/78b6faa)

### Évolutions techniques
- Amélioration du parsing du fichier XLSX Banatic en streaming pour éviter les erreurs de mémoire [#fb7bd16](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/fb7bd16) et [#cb01e05](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/cb01e05)
- Correction du décodage des entités HTML dans les données Banatic [#14e6802](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/14e6802)
- Correction de l'URL de la source ZLV (SIREN→SIRET) [#91ac890](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/91ac890)
- Refactoring de la migration 0028 pour une meilleure clarté [#6af43d0](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/6af43d0)
- Séparation des documents Swagger et harmonisation des titres [#4e811b1](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/4e811b1)
- Ajout d'un proxy pour analyses-convergence [#34f27f7](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/34f27f7)
- Correction du proxy pour supporter les attributs HTML avec guillemets simples [#f9d4d1a](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/f9d4d1a)
- Correction de la réécriture des chemins dans le proxy [#fd90aa5](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/fd90aa5)

### Autres changements
- Documentation de l'API : ajout de la description de l'endpoint recherche et ajout d'un badge Alpha [#193672e](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/193672e), [#4622849](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/4622849) et [#587c0ed](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/587c0ed)
- Correction du nom de domaine dans les exemples curl de l'API [#8b6c8cf](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/commit/8b6c8cf)
- Publication de plusieurs versions (0.1.18, 0.1.19, 0.1.20, 0.1.21, 0.1.22, 0.1.23, 0.1.24) via GitHub Actions.
