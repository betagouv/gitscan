## Changelog : sites-conformes (30 derniers jours, au 18 août 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment via une meilleure gestion des erreurs et de la recherche, ainsi que sur le renforcement de la fiabilité du projet grâce à l'optimisation des tests automatisés et des processus de déploiement (CI/CD).

### Évolutions fonctionnelles
- **Amélioration de la recherche** : la requête saisie par l'utilisateur est désormais affichée dans la barre de recherche pour une meilleure visibilité.
- **Gestion des erreurs** : correction des pages d'erreur 404 et 500, avec une garantie que les pages 404 respectent le Design System de l'État (DSFR).
- **Affichage en iframe** : ajout d'une version conditionnelle des pages lors de leur chargement dans une iframe ([#551](https://github.com/numerique-gouv/sites-conformes/pull/551)).

### Évolutions techniques
- **Tests et Qualité** :
    - Intégration de nouveaux tests pour le module blog ([#544](https://github.com/numerique-gouv/sites-conformes/pull/544)).
    - Amélioration de la robustesse et de la lisibilité des tests liés aux taxonomies.
- **CI/CD et Infrastructure** :
    - Optimisation des tests fonctionnels e2e pour qu'ils s'exécutent uniquement sur les branches de Pull Request.
    - Optimisation de la gestion de l'internationalisation (i18n) dans le pipeline CI pour ignorer la documentation.
    - Passage en mode lecture seule de la tâche de validation des notifications.
- **Refactoring** :
    - Centralisation des noms de templates d'erreur sous forme de constantes dans la configuration des URLs pour faciliter la maintenance.

### Autres changements
- Ajout de la gestion de la version du projet.
