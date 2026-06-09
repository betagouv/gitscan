## Changelog : people (30 derniers jours, au 13 mai 2026)

### Résumé
Les récentes mises à jour de l'application People se concentrent sur la correction de bugs liés à l'intégration avec Dimail, notamment la gestion des redirections et des slashs dans les URLs. Des mises à jour de sécurité ont également été appliquées pour corriger des vulnérabilités dans les dépendances du projet. Enfin, une nouvelle version a été publiée (1.25.4).

### Évolutions fonctionnelles
- Correction d'un bug empêchant le suivi des redirections depuis Dimail [#1234](https://github.com/suitenumerique/people/issues/1234).
- Correction d'un problème de slash final incorrect dans l'endpoint de vérification Dimail.

### Évolutions techniques
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `next` vers la version 15.5.18 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `django` vers la version 6.0.5 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `dimail` vers la version 0.6.7.

### Autres changements
- Publication des versions 1.25.3 et 1.25.4.
