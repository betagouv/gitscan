## Changelog : mobilic-api (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la gestion des entreprises et des employés, notamment en ajoutant des fonctionnalités de réactivation, de suivi de l'activité et de gestion des contrôles. Des améliorations ont également été apportées à l'intégration avec Brevo pour la gestion des emails et des notifications. Enfin, des corrections de bugs et des optimisations ont été réalisées pour améliorer la stabilité et la performance de l'API.

### Évolutions fonctionnelles
- Ajout de la possibilité de rattacher un employé après un licenciement (#653).
- Amélioration de la gestion des employés inactifs avec l'ajout d'un champ `last_active_at` et d'un trigger PostgreSQL pour le mettre à jour automatiquement (#639).
- Possibilité de filtrer les employés par leur statut de validation (#653).
- Restriction de la connexion des contrôleurs aux fournisseurs d'identité ProConnect autorisés (#662).
- Ajout d'une sanction en cas d'absence d'activité lors d'un contrôle (#657).
- Ajout de la localisation des contrôles via l'API (#651).
- Correction du calcul des alertes de travail de nuit (#650).
- Amélioration de l'interface d'administration pour la gestion des employés (#658, #656).
- Ajout d'un bouton pour détacher un employé dans l'interface d'administration (#656).
- Ajout d'une nouvelle page pour la gestion des BDC (Bordereau de Déclaration de Cotisations) (#660).

### Évolutions techniques
- Refactorisation du code lié aux métadonnées natinf pour la nouvelle BDC (#660).
- Amélioration de la gestion des transactions atomiques pour éviter les commits intempestifs lors de l'envoi d'emails (#656).
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs (#654, #657, #658, #659, #660).
- Mise en place d'un pipeline d'activation basé sur le statut des emails pour Brevo (#654).
- Modification du délai d'envoi du premier email d'activité de J+10 à J+7 (#654).
- Ajout de la colonne `dismissed_at` pour une gestion plus précise des licenciements (#653).
- Utilisation de `dismissed_at` au lieu de `is_dismissed` pour la réactivation des employés (#656).
- Suppression de la dépendance `pypdf3` (#660).

### Autres changements
- Correction du code natinf 32083 (#660).
- Gestion des cas où la date de naissance ou l'utilisateur contrôleur est absent (#660).
- Correction d'un bug dans le message d'erreur lié à l'IDP (#659).
- Exclusion des administrateurs du calcul des employés inactifs (#659).
- Ajout de propriétés de statut calculées pour les employés (#658).
- Ajout d'un filtre pour les employés par dernier utilisateur (#658).
- Ajout d'une mutation pour terminer plusieurs emplois en lot (#639).
- Amélioration de la documentation et des tests.
