## Changelog : lab-anssi-lib (30 derniers jours, au 26 octobre 2026)

### Résumé
Ce mois-ci, la bibliothèque a franchi une étape majeure avec le passage en version 3.0.0. Les évolutions se concentrent sur une simplification importante du modèle de données : la gestion des articles passe d'un système basé sur les catégories à un système basé sur le chemin (path), et certaines informations moins critiques (comme les dates de publication) ont été supprimées pour alléger l'API.

### Évolutions fonctionnelles
- **Nouvelle gestion des articles** : la récupération d'un article s'effectue désormais via son chemin complet (path) plutôt que par catégorie.
- **Amélioration du contenu** : enrichissement des résumés d'articles et retour systématique du chemin complet de l'article.
- **Simplification du modèle** : suppression de la notion de catégorie et des champs de dates (publication et mise à jour) pour simplifier l'usage.
- **Correction** : résolution d'un problème lors de la génération de clés.

### Évolutions techniques
- **Version majeure** : passage à la version 3.0.0 (et mise à jour immédiate en 3.0.1).
- **Refactoring TypeScript** : nettoyage du code avec la suppression de types superficiels et de surcharges de types inutiles pour améliorer la maintenabilité.
