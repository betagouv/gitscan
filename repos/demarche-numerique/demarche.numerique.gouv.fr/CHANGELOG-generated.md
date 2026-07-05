## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'accessibilité, de la performance et de la robustesse de la plateforme. Des corrections de bugs et des optimisations ont été apportées, notamment au niveau de la gestion des pièces justificatives, de l'expérience utilisateur et de la sécurité. Plusieurs refactorings ont été effectués pour moderniser le code et faciliter les évolutions futures.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité de la zone de dépôt des pièces justificatives (RGAA 3.3).
- Ajout d'un indicateur visuel pour signaler les dossiers partagés avec l'utilisateur.
- Ajout d'un système de bannières d'information administratives.
- Amélioration de l'expérience utilisateur pour la correction de dossier, avec affichage des champs modifiés.
- Ajout d'un indicateur de lecture des messages pour les instructeurs.
- Ajout de la possibilité de filtrer les dossiers par procédure.
- Amélioration de l'affichage des informations sur les procédures dans la liste des dossiers.
- Ajout de la gestion des NAF 2025 pour les personnes morales.
- Ajout de la possibilité de publier une démarche via GraphQL.
- Ajout de la possibilité de modifier une démarche via GraphQL.
- Ajout d'un système de gestion des bannières d'information.
- Amélioration de l'affichage des informations sur les procédures dans la liste des dossiers.
- Ajout d'une page dédiée en cas de procédure non trouvée.
- Ajout de la possibilité d'ajouter des sauts de page dans l'éditeur d'attestation.
- Amélioration de l'expérience utilisateur pour la demande de correction.

### Évolutions techniques
- Mise à jour de Rails en version 8.0.
- Refactorisation de nombreux composants HAML vers ERB.
- Optimisation des requêtes GraphQL pour éviter les problèmes de performance (N+1).
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des dépendances.
- Optimisation de l'export des données en XLSX avec streaming pour réduire la consommation de mémoire.
- Amélioration de la gestion des jobs asynchrones (Sidekiq).
- Refonte de la gestion des adresses avec intégration de l'API BAN.
- Amélioration de la gestion des pièces justificatives avec intégration de l'OCR.
- Mise en place d'un système de gestion des features flags (Flipper).
- Amélioration de la sécurité de l'application.
- Correction de plusieurs bugs et vulnérabilités.
- Ajout d'un système de purge des jobs cron orphelins.
- Amélioration de la gestion des erreurs dans l'upload des attestations.
- Amélioration de la gestion des données de l'API Entreprise.

### Autres changements
- Mise à jour de la documentation.
- Correction de fautes d'orthographe et d'erreurs de traduction.
- Amélioration de la configuration de l'application.
- Nettoyage du code.
- Suppression de code obsolète.
- Ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des dépendances.
- Amélioration de la gestion des logs.
- Ajout de métriques pour le suivi de la performance de l'application.
