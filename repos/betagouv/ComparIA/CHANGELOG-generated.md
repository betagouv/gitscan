## Changelog : ComparIA (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion de la base de données, notamment l'archivage des données, la correction de données corrompues et l'optimisation des requêtes.  Des améliorations ont également été apportées à l'infrastructure, avec l'ajout d'une installation Docker simplifiée et la mise en place d'un système de limitation de débit pour certaines fonctionnalités. Enfin, la détection de spam a été améliorée.

### Évolutions fonctionnelles
*   Ajout d'un système de limitation de débit pour la sélection personnalisée de modèles afin de prévenir les abus. [#384](https://github.com/betagouv/ComparIA/issues/384)
*   Amélioration de la détection de spam grâce à l'utilisation du modèle Gemini et à la persistance des résultats dans la base de données. [#398](https://github.com/betagouv/ComparIA/issues/398)
*   Ajout de la possibilité d'exporter les données du dataset pour un pays spécifique. [#418](https://github.com/betagouv/ComparIA/issues/418)
*   Ajout de nouveaux modèles de langage : Gemma 4 26B A4B, Gemma 4 31B, Kimi K2.6, Qwen 3.6 Plus, MiniMax M2.7, LFM2 24B A2B. [#425](https://github.com/betagouv/ComparIA/issues/425), [#449](https://github.com/betagouv/ComparIA/issues/449)
*   Ajout d'un captcha Altcha pour les endpoints de l'arène afin de réduire les abus.
*   Amélioration de l'affichage dans le classement des modèles si les données ne sont pas encore disponibles.

### Évolutions techniques
*   Refonte de l'infrastructure de calcul des classements des modèles, avec stockage des résultats en cache Redis pour une meilleure performance.
*   Simplification de l'installation avec l'ajout d'une image Docker autonome avec Caddy comme reverse proxy. [#429](https://github.com/betagouv/ComparIA/issues/429)
*   Suppression des logs PostgreSQL. [#454](https://github.com/betagouv/ComparIA/issues/454)
*   Refactorisation importante du code lié à la base de données : suppression de colonnes obsolètes, amélioration des requêtes, ajout d'outils pour l'archivage et la correction des données.
*   Utilisation de `cyclopts` pour la gestion des arguments en ligne de commande dans le module `dataset`.
*   Amélioration de la gestion des erreurs et des timeouts pour l'analyse avec le modèle Gemini.
*   Mise à jour des dépendances (eslint, jsdom, npm).
*   Refactorisation des scripts Jenkins pour une meilleure maintenance.

### Autres changements
*   Ajout de documentation pour l'installation via Docker.
*   Mise à jour des traductions en Estonien et en Danois.
*   Correction de bugs mineurs et améliorations de la qualité du code.
*   Ajout de commentaires et de documentation pour faciliter la compréhension du code.
*   Suppression de modèles de langage obsolètes (OLMO 3 32B Think, LFM2 8B A1B, Gemini 3 Pro).
*   Configuration de Dependabot pour des mises à jour moins fréquentes.
*   Ajout d'un outil en ligne de commande pour la gestion de la base de données (archivage, correction, etc.).
