## Changelog : matrix-admin-bot (30 derniers jours, au 07/09/2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la fiabilité et de la sécurité du processus de déploiement automatique (CI/CD) ainsi que sur la mise à jour de l'environnement système utilisé par le bot. Aucune nouvelle fonctionnalité n'a été ajoutée pour les utilisateurs finaux.

### Évolutions techniques
- **Optimisation de la CI/CD** : fixation des versions des GitHub Actions, correction des signatures et ajout de la construction automatique de l'image Docker lors des Pull Requests pour améliorer la stabilité des déploiements.
- **Correction de configuration** : résolution d'un problème lié à la propriété `push` manquante dans les workflows.
- **Mise à jour de l'infrastructure** : passage de l'image de base Docker vers Debian 13.
