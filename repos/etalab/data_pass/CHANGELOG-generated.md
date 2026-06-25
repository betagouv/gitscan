## Changelog : data_pass (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment via la simplification des processus de désinscription, la mise à jour des informations FranceConnect et la gestion des clés API. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. Enfin, des mises à jour de dépendances ont été réalisées pour assurer la sécurité et la compatibilité du système.

### Évolutions fonctionnelles
- Simplification de la désinscription : ajout d'un lien de désinscription en un clic dans les emails d'instruction. [#1606](https://github.com/etalab/data_pass/pull/1606)
- Mise à jour des informations FranceConnect : amélioration des emails et activation des brouillons pour FranceConnect. [#1576](https://github.com/etalab/data_pass/pull/1576), [#1590](https://github.com/etalab/data_pass/pull/1590)
- Gestion des clés API : les développeurs peuvent désormais créer et supprimer leurs propres clés API. [#1618](https://github.com/etalab/data_pass/pull/1618), [#1624](https://github.com/etalab/data_pass/pull/1624)
- Amélioration de la recherche d'utilisateurs et de la gestion des droits. [#1610](https://github.com/etalab/data_pass/pull/1610)
- Ajout du formulaire pré-rempli MGDIS Aides facultatives départementales. [#1501](https://github.com/etalab/data_pass/pull/1501)
- Mise à jour des CGU pour TDAE et Prosante Connect. [#1585](https://github.com/etalab/data_pass/pull/1585), [#1596](https://github.com/etalab/data_pass/pull/1596)
- Ajout d'un lien pour gérer les préférences de notification dans les emails d'instruction. [#1577](https://github.com/etalab/data_pass/pull/1577)
- Les demandes validées sont maintenant incluses dans les résultats de recherche par ID. [#1619](https://github.com/etalab/data_pass/pull/1619)

### Évolutions techniques
- Migration du scope TVA de VIES vers la DGFIP pour l'API Entreprise. [#1638](https://github.com/etalab/data_pass/pull/1638)
- Standardisation des migrations de renommage de scope avec `ScopeMigrationService`. [#1638](https://github.com/etalab/data_pass/pull/1638)
- Réduction de la durée de session DataPass à 12 heures, alignée sur ProConnect. [#1625](https://github.com/etalab/data_pass/pull/1625)
- Remplacement de "Approbation" par "Validation" dans l'interface. [#1639](https://github.com/etalab/data_pass/pull/1639)
- Optimisation des requêtes pour le dashboard afin de réduire les problèmes de N+1 et le bruit dans Sentry. [#1604](https://github.com/etalab/data_pass/pull/1604)
- Amélioration de la robustesse des tests Cucumber. [#1608](https://github.com/etalab/data_pass/pull/1608)
- Mise à jour des dépendances Ruby et des actions Docker. [#1620](https://github.com/etalab/data_pass/pull/1620), [#1579](https://github.com/etalab/data_pass/pull/1579)
- Correction d'un bug empêchant la suppression correcte des droits utilisateurs. [#1634](https://github.com/etalab/data_pass/pull/1634)

### Autres changements
- Documentation de l'authentification ProConnect mise à jour. [#1622](https://github.com/etalab/data_pass/pull/1622)
- Amélioration de la gestion des erreurs et des logs.
- Corrections de style et de conformité RGAA.
- Mise à jour des liens CGU pour les services CISIRH. [#1621](https://github.com/etalab/data_pass/pull/1621)
- Ajout de tests unitaires et d'intégration.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances pour assurer la sécurité et la compatibilité.
