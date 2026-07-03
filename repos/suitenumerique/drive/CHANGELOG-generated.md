## Changelog : drive (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration de la recherche et du filtrage des fichiers, ainsi que sur l'ajout d'une aide contextuelle pour faciliter l'utilisation de l'application. Des améliorations ont également été apportées à la conversion de fichiers et à la gestion des analyses de sécurité.

### Évolutions fonctionnelles
- Ajout d'un menu d'aide dans le panneau latéral gauche pour guider les utilisateurs.
- Amélioration du filtre de recherche avec la possibilité de filtrer par emplacement, type de fichier, contact et date de modification.
- Possibilité de définir une plage de dates personnalisée pour le filtre de modification.
- Ajout d'un filtre "plus d'un an" pour la date de modification.
- Ajout de la prise en charge du téléchargement de fichiers Grist.
- Amélioration de l'interface utilisateur pour les liens publics, avec des actions contextuelles pour les utilisateurs authentifiés et anonymes.
- Ajout d'un modal de conversion de fichiers.
- Affichage des fichiers en cours de conversion dans l'explorateur de fichiers.

### Évolutions techniques
- Mise à jour de la bibliothèque UI-kit vers la version 0.24.0.
- Amélioration de la gestion des requêtes de conversion OnlyOffice avec la signature JWT.
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter le buffering.
- Amélioration de la gestion des analyses de fichiers pour permettre la conversion pendant l'analyse.
- Correction de problèmes liés à la gestion des chemins d'accès dans les noms de fichiers créés par des templates.
- Correction d'un problème de healthcheck Collabora en l'absence de curl.
- Mise à jour des dépendances PyJWT et cryptography pour corriger des failles de sécurité.
- Refactorisation du code pour améliorer la gestion des filtres dans l'explorateur de fichiers.
- Extraction de requêtes de localisation d'éléments pour une meilleure organisation.
- Généralisation du poller pour les éléments transitoires.

### Autres changements
- Amélioration de la documentation README pour plus de clarté et de cohérence.
- Enrichissement des guidelines de contribution.
- Ajout de fixtures pour les types de fichiers dans les données de démonstration.
- Amélioration des tests E2E pour couvrir les nouveaux flux de conversion et de filtrage.
- Correction de tests pour s'adapter aux changements dans l'interface utilisateur.
