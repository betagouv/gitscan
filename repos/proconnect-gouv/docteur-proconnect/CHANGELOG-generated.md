## Changelog : docteur-proconnect (30 derniers jours)

### Résumé
Cette mise à jour apporte des corrections de bugs, des améliorations de la qualité du code et la suppression de tests E2E défaillants. L'application a également été renommée pour une meilleure cohérence linguistique.

### Évolutions fonctionnelles
- Correction d'un bug où `currentUrl` était utilisé avant d'être défini (#29).
- Renommage de "Doctor" en "Docteur" dans l'interface utilisateur (#29).

### Évolutions techniques
- Suppression des tests E2E défaillants (#37, #29).
- Correction de vulnérabilités identifiées par `npm audit` (#29).
- Suppression de la variable d'environnement `title` non utilisée (#35).

### Autres changements
- Préparation de la publication d'une nouvelle version (#36).
