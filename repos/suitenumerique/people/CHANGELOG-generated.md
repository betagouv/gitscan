## Changelog : people (30 derniers jours, au 13 mai 2026)

### Résumé
Les dernières mises à jour de People se concentrent sur l'amélioration de l'intégration avec dimail, notamment en corrigeant des problèmes de redirection et de gestion des URL. Des mises à jour de sécurité ont également été appliquées pour corriger des vulnérabilités dans les dépendances.

### Évolutions fonctionnelles
- Correction d'un problème empêchant le suivi des redirections lors de l'utilisation de dimail. [#65cbaac](https://github.com/suitenumerique/people/commit/65cbaac)
- Correction d'un bug où le code de connexion était envoyé à une URL dimail incorrecte. [#2162b0a](https://github.com/suitenumerique/people/commit/2162b0a)
- Passage à la version v2 des mailboxes pour l'importation depuis dimail, améliorant ainsi la compatibilité et la fiabilité. [#8f4e1ad](https://github.com/suitenumerique/people/commit/8f4e1ad)
- Correction d'un problème de slash final dans l'endpoint de vérification dimail. [#65cbaac](https://github.com/suitenumerique/people/commit/65cbaac)

### Évolutions techniques
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0 pour corriger une vulnérabilité de sécurité. [#7d06025](https://github.com/suitenumerique/people/commit/7d06025)
- Mise à jour de la dépendance `next` vers la version 15.5.18 pour corriger une vulnérabilité de sécurité. [#54c48a8](https://github.com/suitenumerique/people/commit/54c48a8)
- Mise à jour de la dépendance `django` vers la version 6.0.5 pour corriger une vulnérabilité de sécurité. [#baafb39](https://github.com/suitenumerique/people/commit/baafb39)
- Mise à jour de la dépendance `dimail` vers la version 0.6.7. [#040d37e](https://github.com/suitenumerique/people/commit/040d37e)

### Autres changements
- Publication des versions 1.25.1, 1.25.2, 1.25.3 et 1.25.4.
- Mise à jour des chaînes de caractères traduites. [#e8dda05](https://github.com/suitenumerique/people/commit/e8dda05)
