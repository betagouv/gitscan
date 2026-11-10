## Changelog : qualicharge (30 derniers jours, au 08/11/2026)

### Résumé
Les récentes évolutions se sont concentrées sur la fiabilité des indicateurs de performance, le renforcement de la sécurité des comptes utilisateurs et la stabilisation de l'infrastructure de données et des migrations de base de données.

### Évolutions fonctionnelles
- **Indicateurs de performance** : Amélioration de la précision des calculs pour les indicateurs e2, e3 et e6 en prenant désormais en compte les statuts manquants.
- **Gestion des utilisateurs** : Ajout de fonctionnalités de maintenance incluant la possibilité de réinitialiser les mots de passe et une commande de nettoyage automatique des anciens mots de passe expirés.

### Évolutions techniques
- **Sécurité** : 
    - Correction d'une fuite de données empêchant l'exposition des mots de passe de réinitialisation dans les journaux (logs) du fournisseur.
    - Mise à jour des dépendances pour corriger des vulnérabilités identifiées.
- **Base de données** : Résolution de problèmes de migration liés aux extensions `geoalchemy2` et `postgresql-audit`.
- **Infrastructure & Workflow** : Correction du processus d'initialisation (seeding) de la base de données pour les workflows Prefect.

### Autres changements
- Passage à la version 0.35.1.
- Correction des erreurs de linter suite aux récentes mises à jour du projet.
