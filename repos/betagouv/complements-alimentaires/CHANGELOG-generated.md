## Changelog : complements-alimentaires (30 derniers jours, au 20/08/2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'architecture frontend avec la migration vers Vite, visant à améliorer les performances de développement. Parallèlement, plusieurs correctifs ont été apportés pour stabiliser l'expérience utilisateur, notamment sur la gestion des filtres de recherche, la fiabilité des téléchargements de documents (PDF, Excel) et la navigation sur le site.

### Évolutions fonctionnelles
- **Amélioration de la gestion des filtres** : possibilité de réinitialiser les filtres sur les listes d'entreprises et de compléments alimentaires ([#3066](https://github.com/betagouv/complements-alimentaires/pull/3066)).
- **Corrections des téléchargements** : résolution de bugs impactant l'URL de téléchargement des exports Excel ([#3064](https://github.com/betagouv/complements-alimentaires/pull/3064)) et la génération des certificats PDF ([#3034](https://github.com/betagouv/complements-alimentaires/pull/3034)).
- **Fiabilisation de la navigation et de l'affichage** : 
    - Correction d'erreurs 404 sur les déclarations sans déclarant ([#3071](https://github.com/betagouv/complements-alimentaires/pull/3071)).
    - Résolution de problèmes liés aux filtres de statut ([#3072](https://github.com/betagouv/complements-alimentaires/pull/3072)).
    - Correction du composant de création d'entreprise ([#3063](https://github.com/betagouv/complements-alimentaires/pull/3063)).
- **Optimisation de l'affichage des données** : amélioration de la présentation des ingrédients et substances (affichage ciblé des substances actives et masquage des tableaux vides).

### Évolutions techniques
- **Migration de l'architecture frontend** : passage à Vite pour moderniser le build et le développement ([#3050](https://github.com/betagouv/complements-alimentaires/pull/3050), [#3065](https://github.com/betagouv/complements-alimentaires/pull/3065)).
- **Modernisation de la CI/CD** : ajout de nouveaux workflows GitHub Actions pour la construction (build) du frontend.
- **Refactoring et infrastructure** :
    - Centralisation des appels API et des credentials via l'utilisation de `createFetch`.
    - Optimisation de l'image Docker et exposition du frontend.
    - Passage au format `type:module` pour le JavaScript.
    - Mise à jour de la gestion des variables d'environnement pour l'URL de l'API.

### Autres changements
- **Nettoyage du code** : suppression de dépendances obsolètes, de fichiers de configuration inutilisés (`python.json`) et de tags de template redondants.
- **Documentation et configuration** : mise à jour du README, ajout d'un fichier d'exemple pour les variables d'environnement (`env.example`) et ajustement du fichier `robots.txt`.
