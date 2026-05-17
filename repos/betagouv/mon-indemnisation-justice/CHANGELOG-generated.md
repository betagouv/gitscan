## Changelog : mon-indemnisation-justice (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'application, notamment l'implémentation d'un nouveau système de gestion des brouillons, l'amélioration de l'expérience utilisateur lors du dépôt de dossier, et la correction de plusieurs bugs critiques affectant la stabilité et la fiabilité de la plateforme. Des améliorations ont également été apportées à la gestion des erreurs et à la surveillance de l'application avec l'intégration de Sentry.

### Évolutions fonctionnelles
- **Dépôt de dossier :** Refonte complète du processus de dépôt de dossier avec création d'étapes distinctes et amélioration de la navigation.
- **Pièces jointes :** Ajout de la possibilité de prévisualiser les pièces jointes avant de les soumettre.
- **Gestion des brouillons :** Implémentation d'un système de brouillons pour permettre aux utilisateurs de sauvegarder leur progression et de reprendre le dépôt plus tard.
- **Types d'attestations :** Ajout du type d'attestation "Avis d'intervention".
- **Informations requérant :** Amélioration de la gestion des informations relatives au requérant, notamment la distinction entre personne physique et morale.
- **Autocomplete adresse :** Ajout d'une fonctionnalité d'autocomplétion pour le champ adresse.
- **Page récapitulative :** Création d'une page récapitulative pour vérifier les informations avant la soumission.
- **Notifications :** La référence à rappeler est maintenant incluse dans l'email de confirmation de dépôt.
- **France Connect :** Amélioration de la gestion des erreurs et ajout de la remontée des erreurs France Connect dans Sentry.
- **Affichage dossier (espace rédacteur) :** Corrections d'affichage pour l'espace rédacteur.

### Évolutions techniques
- **Mise à jour des dépendances :** Mise à jour de Symfony et Doctrine vers la version 8.0.
- **Refactoring API :** Réorganisation de la route API listant les communes par code postal.
- **Suppression API Platform :** Suppression de l'utilisation d'API Platform.
- **Normalisation des données :** Amélioration de la normalisation des données.
- **Docker :** Mise à jour de l'image Docker pour retirer `APP_RUNTIME`.
- **Tests :** Correction des tests unitaires backend et adaptation des tests end-to-end.
- **Sentry :** Intégration de Sentry pour la surveillance des erreurs et la collecte de logs.
- **Architecture :** Utilisation de Tanstack Router pour l'espace requérant.
- **Base de données :** Création d'une table dédiée pour les bris de porte.
- **DTOs :** Création de Data Transfer Objects (DTOs) pour l'échange de données avec l'espace FIP6.

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant les nouveaux points d'intégration.
- **Configuration :** Correction d'une configuration obsolète pour Doctrine en production.
- **Nettoyage de code :** Suppression de classes de mapper inutilisées.
- **Fixtures :** Correction des données de fixtures et des tests associés.
- **Pages :** Création d'une page d'erreur 404.
- **Crisp :** Installation de Crisp pour le support client.
- **Schéma de base de données :** Documentation du schéma de base de données.
