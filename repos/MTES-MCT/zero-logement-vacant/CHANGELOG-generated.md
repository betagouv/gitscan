## Changelog : zero-logement-vacant (30 derniers jours)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à la gestion des documents, notamment un nouveau système d'upload, la possibilité de lier des documents existants et un suivi plus précis des actions sur les documents. Des corrections et optimisations ont également été apportées à la gestion des données de logement et à l'infrastructure du projet. Enfin, des améliorations de l'interface utilisateur et des corrections de bugs ont été implémentées pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'un nouveau système d'upload de documents avec une étape de liaison aux logements.
- Possibilité de renommer et de supprimer des documents.
- Affichage de l'ID de parcelle à la place de la référence cadastrale.
- Amélioration de la gestion des données d'énergie (DPE, GES, RNB) des logements.
- Ajout d'un filtre par localisation relative dans la liste des logements.
- Mise à jour des libellés et des options pour le filtre de localisation relative.
- Amélioration de l'interface utilisateur pour la gestion des documents.
- Mise à jour de la procédure d'habitat indigne.
- Mise à jour de la page 404.

### Évolutions techniques
- Refactorisation importante de la gestion des documents côté serveur et frontend.
- Ajout de tables `document_events` et `housing_document_events` pour le suivi des actions sur les documents.
- Mise en place d'un système d'événements pour le suivi des actions sur les documents.
- Migration vers Web Streams pour l'import des données.
- Amélioration des performances et de l'efficacité du cache avec NX.
- Mise à jour des dépendances (webpack, axios, express, etc.).
- Correction de problèmes liés à l'upload de documents.
- Amélioration des tests unitaires et d'intégration.
- Utilisation de esbuild pour la compilation du serveur.
- Ajout de scripts pour l'export de données utilisateurs pour Portail DF.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et améliorations.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Suppression de code obsolète.
- Synchronisation des fichiers de configuration Talisman.
- Mise à jour des configurations des sources externes (Insee, etc.).
- Correction de problèmes de tests et de CI/CD.
