## Changelog : grist-budget-agriculture (30 derniers jours, au 03 mai 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de la gestion des droits d'accès, la correction de bugs liés à l'analyse des données budgétaires et l'optimisation du fonctionnement hors connexion. Des améliorations ont également été apportées à la communication par email et à la documentation du projet.

### Évolutions fonctionnelles
- Correction d'un bug dans la logique de mise à jour des droits d'accès, permettant de mieux gérer les utilisateurs listés dans `/access` mais sans droits actuellement.
- L'analyse des données des Documents de Programme (DP) est désormais incluse dans le récapitulatif envoyé par email.
- Limitation de l'analyse de cohérence des montants des Éléments Justificatifs (EJ) aux Budgets Commis (BC) de l'année de l'INFBUD, améliorant la performance et la pertinence de l'analyse.

### Évolutions techniques
- Simplification du fonctionnement hors connexion grâce au stockage des données Grist en local.
- Fixe la version de Python à 3.11.14 pour assurer la compatibilité et la stabilité de l'environnement.
- Facilité de débogage de l'analyse des INFBUD en local.
- Mutualisation du template de lien pour une meilleure cohérence et maintenabilité du code.

### Autres changements
- Mise à jour du fichier README pour refléter les dernières évolutions du projet.
- Ajout de `.grist-cache` au fichier `.gitignore` pour éviter de versionner des fichiers temporaires.
