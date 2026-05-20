## Changelog : helpcenter (30 derniers jours, au 18 mai 2026)

### Résumé
Cette mise à jour marque le lancement initial du projet Helpcenter !  Les premières améliorations se concentrent sur la correction de bugs liés à l'affichage du contenu (schéma des URLs, blocs d'appel à l'action, navigation) et à l'indexation de la documentation. Une optimisation de la performance est également apportée en partageant le cache Redis pour l'API Docs.

### Évolutions fonctionnelles
- Correction de l'affichage des URLs, des blocs d'appel à l'action et de la navigation "précédent/suivant" en bas de page. [#70d43fa](https://github.com/suitenumerique/helpcenter/commit/70d43fa)
- Amélioration de l'indexation de la documentation suite à la nouvelle configuration de l'endpoint Docs. [#b8bc5b7](https://github.com/suitenumerique/helpcenter/commit/b8bc5b7)

### Évolutions techniques
- Mise en place d'un cache Redis partagé pour l'API Docs afin d'améliorer les performances. [#bca7ce3](https://github.com/suitenumerique/helpcenter/commit/bca7ce3)
- Initialisation du projet Helpcenter. [#281dae8](https://github.com/suitenumerique/helpcenter/commit/281dae8)
