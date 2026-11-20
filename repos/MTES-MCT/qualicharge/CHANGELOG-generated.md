## Changelog : qualicharge (30 derniers jours, au 17 novembre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur le renforcement de la sécurité des comptes utilisateurs et la fiabilisation des indicateurs de données. Des corrections importantes ont également été apportées à la gestion des bases de données et aux processus d'automatisation pour garantir une meilleure stabilité du système.

### Évolutions fonctionnelles
- **Indicateurs de performance** : Amélioration du calcul des indicateurs e2, e3 et e6 pour assurer une précision accrue même en présence de statuts manquants.
- **Gestion des accès** : Ajout de la possibilité de réinitialiser les mots de passe des utilisateurs.

### Évolutions techniques
- **Sécurité** : 
    - Correction d'une faille de sécurité empêchant la fuite de mots de passe de réinitialisation dans les journaux (logs) du fournisseur.
    - Mise à jour de plusieurs dépendances critiques (directes et transitives) pour corriger des vulnérabilités.
- **Base de données et Workflows** :
    - Résolution de problèmes liés aux migrations de base de données (GeoAlchemy2 et PostgreSQL-audit).
    - Correction de l'amorçage (seeding) des bases de données pour les workflows Prefect.
- **Maintenance et outils** :
    - Ajout d'une commande de nettoyage pour supprimer automatiquement les anciens mots de passe expirés.
    - Correction des erreurs de linter suite aux mises à jour de l'environnement de développement.

### Autres changements
- Publication de la version 0.35.1.
