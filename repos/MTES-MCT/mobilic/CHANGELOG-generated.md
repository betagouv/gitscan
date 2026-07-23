## Changelog : mobilic (30 derniers jours, au 2026-07-23)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans les vues administrateur et employé, avec l'ajout de nouvelles fonctionnalités comme la contestation de recettes et la demande de détachement. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations d'accessibilité et de conformité avec le DSFR.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les employés de contester une recette. [#884](https://github.com/MTES-MCT/mobilic/pulls/884)
- Implémentation de la demande de détachement pour les employés avec une interface dédiée et un système de relance. [#898](https://github.com/MTES-MCT/mobilic/pulls/898)
- Ajout de la possibilité d'abandonner une mission en cours. [#889](https://github.com/MTES-MCT/mobilic/pulls/889)
- Amélioration de la vue des activités pour les administrateurs, avec des informations supplémentaires et une meilleure organisation. [#885](https://github.com/MTES-MCT/mobilic/pulls/885)
- Modification du libellé pour le transport de marchandises lourdes dans les congés. [#878](https://github.com/MTES-MCT/mobilic/pulls/878)
- Ajout de la possibilité pour les administrateurs de voir l'auteur du support lors de la validation d'une activité.
- Ajout de la possibilité de voir le temps de validation par mission pour les employés sur plusieurs jours.
- Ajout de la possibilité de filtrer les utilisateurs et équipes sur la page de validation des missions.

### Évolutions techniques
- Refactorisation du code pour améliorer la performance et la lisibilité, notamment dans les composants liés aux activités et à l'interface utilisateur.
- Mise à jour de l'infrastructure pour améliorer la gestion des erreurs et la surveillance des performances (Sentry).
- Amélioration de l'intégration avec le Design System de la République Française (DSFR) pour l'en-tête et le pied de page, améliorant l'accessibilité et la cohérence visuelle.
- Optimisation des requêtes GraphQL pour réduire les temps de chargement et améliorer la réactivité de l'application.
- Correction de problèmes de performance liés aux requêtes dupliquées.
- Amélioration de la gestion des états et des données dans l'application.

### Autres changements
- Correction de plusieurs problèmes d'accessibilité, notamment dans l'en-tête et le menu mobile.
- Mise à jour de la documentation et des commentaires dans le code.
- Corrections de style et de mise en page pour améliorer l'apparence de l'application.
- Suppression de l'option FranceConnect pour l'inscription des employés.
- Ajout de logos de partenaires sur la page dédiée.
- Correction de bugs mineurs et améliorations de la stabilité générale de l'application.
- Amélioration de la gestion des erreurs et des messages d'erreur.
- Corrections de linting et de code smells détectés par SonarCloud.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture de test.
