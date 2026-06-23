## Changelog : st-home (30 derniers jours, au 22 juin 2026)

### Résumé
Les dernières mises à jour de st-home se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec une refonte du blog (pagination, catégories, partage) et des corrections sur la carte de déploiement (deploymap). Des améliorations techniques ont également été apportées, avec la migration du système de tâches asynchrones de Celery vers Dramatiq pour une meilleure performance et fiabilité.

### Évolutions fonctionnelles
- **Blog :** Amélioration significative du blog avec l'ajout de la pagination, des catégories et des liens de partage pour faciliter la navigation et la diffusion des articles. [#69](https://github.com/suitenumerique/st-home/issues/69)
- **Carte de déploiement (Deploymap) :**
    - Correction de l'affichage du seuil ANCT sur la carte.
    - Prise en compte correcte du seuil dans le calcul affiché sur la carte.
    - Amélioration de l'affichage des régions et départements sur la carte. [#65](https://github.com/suitenumerique/st-home/issues/65)
- **RPNT :** Autorisation de certains redirects vers des sites gouv dans le cadre de la version 1.6 du RPNT. [#69](https://github.com/suitenumerique/st-home/issues/69)
- **Services :** Correction de l'affichage des services ProConnect en liste, éliminant les doublons.
- **Services :** Ajout des Messages et Fichiers au seuil ANCT.

### Évolutions techniques
- **Architecture :** Migration du système de tâches asynchrones de Celery vers Dramatiq pour une meilleure performance et une gestion plus robuste des tâches en arrière-plan. [#70](https://github.com/suitenumerique/st-home/issues/70)
- **Worker :** Adaptation des mécanismes de retries et mise à jour du dashboard du worker.
- **Banatic :** Mise à jour de l'URL de la source de données Banatic.

### Autres changements
- **Documentation :** Mise à jour du lien vers le centre d'aide (helpcenter). [#67](https://github.com/suitenumerique/st-home/issues/67)
- **Recherche de communes :** Correction pour forcer l'inclusion des organisations ayant un nom exact.
