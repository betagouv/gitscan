## Changelog : docteur-proconnect (30 derniers jours)

### Résumé
Les récentes mises à jour de Docteur ProConnect se concentrent sur la correction de bugs, l'amélioration de la stabilité des tests et la préparation d'une nouvelle version. Des ajustements ont été apportés pour corriger des erreurs dans le code et supprimer des tests automatisés défaillants.

### Évolutions fonctionnelles
- Correction d'un bug où `currentUrl` était utilisé avant d'être défini (#29).
- Préparation de mises à jour pour une future publication (#36).

### Évolutions techniques
- Suppression de tests E2E défaillants pour améliorer la fiabilité de la suite de tests (#37).
- Correction de vulnérabilités identifiées par `npm audit` (#29).
- Suppression d'une variable d'environnement inutile (`title`) (#35).

### Autres changements
- Mise à jour de la dépendance `qs` de la version 6.14.1 à la version 6.14.2 (#39).
