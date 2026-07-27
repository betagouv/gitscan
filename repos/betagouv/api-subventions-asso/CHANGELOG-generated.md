## Changelog : api-subventions-asso (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et la gestion des données des associations, notamment via l'intégration de sources externes comme Sirene et Chorus. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la fiabilité de l'API.

### Évolutions fonctionnelles
- Intégration de l'importation automatisée des établissements Sirene via une tâche cron (#4006).
- Import des fichiers parquet RNA Waldec (#4000).
- Intégration des établissements Sirene (#3995).
- Amélioration des notifications lors de l'importation de données des fournisseurs (#3954).
- Correction d'un bug d'affichage d'alertes de doublons SIREN sur le front-end (#3965).

### Évolutions techniques
- Refactorisation pour remplacer l'utilisation de l'ID utilisateur par l'entité `UserEntity` (#3978).
- Remplacement de l'identifiant unique Chorus par un index composite (#3968).
- Suppression des codes d'erreur HTTP personnalisés au profit des codes standards (#3979).
- Mise à jour de l'URL de l'unité légale Sirene Stock pour utiliser un lien stable (#3983).
- Ajout de tests d'intégration pour l'importation des établissements Sirene (#4012).
- Correction d'une erreur 404 lors de l'appel à l'API asso et ajout d'un `await` manquant (#3981).

### Autres changements
- Mise à jour du script de publication pour mettre à jour tous les paquets, y compris le paquet racine.
- Suppression d'une exclusion d'âge de publication pnpm obsolète.
- Regénération du changelog.
- Suppression d'un ancien nom de connexion Pro Connect.
- Correction de tests suite à la mise à jour de l'URL Sirene Stock.
