## Changelog : recommandations-collaboratives (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des documents, notamment l'ajout de documents privés, la gestion des fichiers et des corrections liées à l'interface utilisateur. Des optimisations de performance et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- **Gestion des documents :** Ajout de la gestion des documents privés, permettant de restreindre l'accès à certains documents aux conseillers uniquement.
- **Téléchargement de fichiers :** Amélioration du processus de téléchargement de fichiers, notamment dans le cadre des conversations et des notes.
- **Affichage des ressources :** Suppression des informations sur l'auteur d'une ressource dans l'interface.
- **Notes :** Possibilité d'ajouter des documents (publics et privés) aux notes.
- **Tâches :** Nouvelle route spécifique pour la publication de recommandations depuis une tâche, avec un message de confirmation plus clair.
- **Conversations :** Amélioration de l'ouverture du panneau de brouillon après la création d'une recommandation.
- **Géolocalisation :** Mise à jour de la gestion des communes et intégration d'une commande de gestion pour l'attribution de nouvelles communes aux projets.
- **Notifications :** Ajout de notifications lors du téléchargement de documents.
- **Catégories :** Amélioration de l'interface du sélecteur de catégories pour les ressources.

### Évolutions techniques
- **Refactoring :** Suppression de code mort et simplification de certaines logiques, notamment dans la gestion des notes et des documents.
- **Dépendances :** Mise à jour de plusieurs dépendances, incluant Django, PostgreSQL, Redis, Alpine.js, Bootstrap, DSFR, ainsi que des librairies JavaScript (axios, lodash, picomatch, flatted, follow-redirects, dompurify, vite, cryptography, pygments, requests).
- **CI/CD :** Utilisation de `uv` pour la gestion des dépendances Python et la génération du fichier `requirements.txt`.
- **Performance :** Préchargement des tags pour les tâches afin d'améliorer les performances.
- **Architecture :** Utilisation de `Alpine.store` pour une meilleure gestion de l'état de l'application.
- **Tests :** Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'interface.
- **Configuration :** Mise à jour de l'URL de base des démarches.
- **Nettoyage de code :** Suppression de commentaires inutiles et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de plusieurs bugs mineurs liés à l'interface utilisateur, à la gestion des URLs et à l'affichage des informations.
- **Amélioration de l'accessibilité :** Ajout d'attributs ARIA pour améliorer l'accessibilité des composants de l'interface utilisateur.
