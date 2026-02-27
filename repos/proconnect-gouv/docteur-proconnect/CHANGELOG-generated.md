## Changelog : docteur-proconnect (30 derniers jours)

### Résumé
Les dernières mises à jour de Docteur ProConnect incluent des corrections de tests end-to-end défaillants, une simplification de la configuration en supprimant une variable d'environnement inutile, et des mises à jour de certaines dépendances pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Suppression de la variable d'environnement `title` qui n'était plus utilisée (#35).
- Correction de tests E2E défaillants (#37).

### Évolutions techniques
- Mise à jour de `express-session` de la version 1.18.2 à la version 1.19.0 (#43).
- Mise à jour de `ejs` de la version 3.1.10 à la version 4.0.1 (#42).
- Mise à jour de `qs` de la version 6.14.1 à la version 6.14.2 (#39, #685252b).
- Regroupement des mises à jour de dépendances mineures et correctives pour une meilleure gestion (#40, #41).
