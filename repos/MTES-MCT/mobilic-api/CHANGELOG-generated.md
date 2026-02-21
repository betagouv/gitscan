## Changelog : mobilic-api (30 derniers jours)

### Résumé
Les dernières mises à jour de l'API Mobilic se concentrent sur l'amélioration de la gestion des employés, notamment la réactivation, la gestion des employés inactifs et le suivi de leur activité. Des améliorations ont également été apportées à l'intégration avec Brevo (Sendinblue) pour la gestion des emails et des notifications, ainsi qu'à l'API de localisation des contrôles.

### Évolutions fonctionnelles
- Possibilité de rattacher un employé précédemment terminé (#653).
- Ajout d'une fonctionnalité pour afficher les employés inactifs (#653).
- Amélioration du calcul des alertes concernant le travail de nuit (#650).
- Ajout d'une nouvelle API pour la localisation des contrôles (#651).
- Ajout d'une étape d'activation basée sur le statut des emails via Brevo (#654).
- Modification de la date d'envoi du premier email d'activité de J+10 à J+7 (#654).
- Ajout d'un email de rappel J+14 pour les entreprises sans activité (#654).
- Possibilité de terminer plusieurs employés en batch.
- Ajout du champ `dismissed_at` pour une meilleure gestion des employés terminés.
- Ajout du champ `validation_status` pour les employés.
- Le champ `last_active_at` est maintenant accessible et mis à jour automatiquement lors de la fin d'une mission (#639).

### Évolutions techniques
- Refactorisation de la gestion des emails pour éviter les commits dans les transactions atomiques (#656).
- Amélioration de la gestion des statuts des employés pour exclure les administrateurs du calcul des employés inactifs (#659).
- Ajout de tests unitaires et d'intégration pour la fonctionnalité de rattachement d'employés (#653).
- Ajout de tests IDOR pour la fonctionnalité de rattachement d'employés.
- Ajout d'une colonne `last_active_at` à la table `employment` avec un trigger PostgreSQL pour la mise à jour automatique.

### Autres changements
- Amélioration de la table d'administration (#658).
- Modification du bouton de détachement pour les administrateurs (#656).
- Correction d'une utilisation de variable non utilisée et utilisation de `const` dans les tests (#650).
