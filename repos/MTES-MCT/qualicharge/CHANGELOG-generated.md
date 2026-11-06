## Changelog : qualicharge (30 derniers jours, au 04/11/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la fiabilité des indicateurs de performance et le renforcement de la gestion des comptes utilisateurs. La sécurité a été consolidée par la mise à jour de dépendances critiques et la stabilité des processus automatisés a été améliorée.

### Évolutions fonctionnelles
- **Indicateurs** : Correction du calcul des indicateurs e2, e3 et e6 pour assurer la précision des données même en présence de statuts manquants.
- **Gestion des utilisateurs** : Ajout de la possibilité de réinitialiser le mot de passe des utilisateurs.

### Évolutions techniques
- **Sécurité** : Mise à jour des dépendances transitives pour corriger des vulnérabilités.
- **Maintenance** : Ajout d'une commande de nettoyage pour supprimer automatiquement les anciens mots de passe expirés.
- **CI/CD** : Correction du processus d'amorçage (seeding) de la base de données pour les workflows Prefect sur GitHub.

### Autres changements
- Passage à la version 0.35.1.
