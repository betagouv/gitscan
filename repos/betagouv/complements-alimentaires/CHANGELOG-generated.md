## Changelog : complements-alimentaires (30 derniers jours, au 20/08/2026)

### Résumé
Ce mois a été marqué par une modernisation majeure de l'infrastructure frontend avec la migration vers Vite, ainsi que par une série de corrections visant à stabiliser l'expérience utilisateur. Les améliorations portent principalement sur la fiabilité des filtres de recherche, l'affichage des données d'ingrédients et la correction des processus d'exportation (Excel et PDF).

### Évolutions fonctionnelles
- **Corrections de bugs** :
    - Résolution des problèmes liés aux filtres de statut ([#3072](https://github.com/betagouv/complements-alimentaires/pull/3072)).
    - Correction d'une erreur 404 survenant lors de l'accès à une déclaration sans déclarant ([#3071](https://github.com/betagouv/complements-alimentaires/pull/3071)).
    - Correction des URLs de téléchargement pour les fichiers Excel ([#3064](https://github.com/betagouv/complements-alimentaires/pull/3064)) et pour les certificats PDF ([#3034](https://github.com/betagouv/complements-alimentaires/pull/3034)).
    - Correction du composant de création d'entreprise.
- **Améliorations de l'interface** :
    - Optimisation de l'affichage des listes : possibilité de supprimer les filtres dans les tableaux d'entreprises et de compléments alimentaires ([#3066](https://github.com/betagouv/complements-alimentaires/pull/3066)).
    - Amélioration de la lisibilité des ingrédients et substances (masquage des tableaux vides pour les substances non actives et mise à jour des labels).

### Évolutions techniques
- **Modernisation du Frontend** :
    - Migration vers l'architecture Vite ([#3050](https://github.com/betagouv/complements-alimentaires/pull/3050)) et suppression des anciens processus de build npm ([#3052](https://github.com/betagouv/complements-alimentaires/pull/3052)).
    - Mise en place d'un nouveau workflow GitHub Actions pour la construction (build) du frontend.
    - Centralisation des appels API via l'utilisation de `createFetch`.
- **Infrastructure et Déploiement** :
    - Optimisation de la configuration Docker et intégration de Vite-Docker ([#3065](https://github.com/betagouv/complements-alimentaires/pull/3065)).
    - Meilleure gestion de la configuration via l'utilisation de variables d'environnement pour les URLs de l'API et du backend.
    - Exposition du frontend et ajustements des politiques de sécurité (CSP).

### Autres changements
- **Documentation et Nettoyage** :
    - Mise à jour du fichier README.
    - Suppression de fichiers et de tags obsolètes (notamment `python.json` et certains tags redondants).
    - Déplacement du fichier `robots.txt`.
