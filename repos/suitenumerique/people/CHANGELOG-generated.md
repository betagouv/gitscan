## Changelog : people (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la fiabilité de l'importation et de la gestion des boîtes aux lettres via l'intégration avec dimail. Des corrections ont été apportées pour gérer correctement les redirections et les versions de l'API dimail, ainsi que des mises à jour de sécurité pour les dépendances du projet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le suivi des redirections lors de l'utilisation de l'intégration dimail. [#1234](https://github.com/suitenumerique/people/issues/1234)
- Correction d'un problème lié à une barre oblique finale incorrecte dans l'endpoint de vérification dimail.
- Passage à la version 2 de l'API mailboxes pour l'importation, améliorant la compatibilité et la stabilité.

### Évolutions techniques
- Mise à jour de la dépendance `urllib3` vers la version 2.7.0 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `next` vers la version 15.5.18 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `django` vers la version 6.0.5 pour corriger une vulnérabilité de sécurité.
- Mise à jour de la dépendance `dimail` vers la version 0.6.7.

### Autres changements
- Publication des versions 1.25.3 et 1.25.4 incluant les corrections mentionnées ci-dessus.
