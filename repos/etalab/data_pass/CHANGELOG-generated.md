## Changelog : data_pass (30 derniers jours, au 29 juin 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de l'expérience utilisateur, notamment via la gestion des autorisations, l'ajout de fonctionnalités pour les API et la correction de bugs. Des mises à jour de sécurité et de conformité ont également été apportées, ainsi que des améliorations de la documentation et de la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout de la possibilité de lister les cas d'usages [#1645](https://github.com/etalab/data_pass/pull/1645).
- Implémentation de la modification d'une définition d'autorisation [#1640](https://github.com/etalab/data_pass/pull/1640).
- Affichage des définitions d'autorisation avec une fonction de recherche [#1637](https://github.com/etalab/data_pass/pull/1637).
- Amélioration des libellés pour les cas d'usage API particulier [#1647](https://github.com/etalab/data_pass/pull/1647).
- Ajout d'un lien "Ne plus recevoir ces emails" dans les emails d'instruction [#1592](https://github.com/etalab/data_pass/pull/1592).
- Mise à jour des CGU Prosanté Connect et TDAE [#1585](https://github.com/etalab/data_pass/pull/1585), [#1590](https://github.com/etalab/data_pass/pull/1590).
- Possibilité de trier les résultats des endpoints de l'API DataPass [#1636](https://github.com/etalab/data_pass/pull/1636).
- Activation des brouillons pour les instructeurs FranceConnect [#1597](https://github.com/etalab/data_pass/pull/1597).
- Amélioration de la gestion des préférences et ajout d'un token de désinscription pour les emails [#1606](https://github.com/etalab/data_pass/pull/1606).
- Permettre aux développeurs de créer et supprimer leurs clés API [#1618](https://github.com/etalab/data_pass/pull/1618).
- Amélioration de la recherche d'utilisateurs et de la gestion des droits [#1625](https://github.com/etalab/data_pass/pull/1625).

### Évolutions techniques
- Réduction de la durée de vie de la session DataPass à 12 heures, alignée sur ProConnect [#1625](https://github.com/etalab/data_pass/pull/1625).
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP [#1622](https://github.com/etalab/data_pass/pull/1622).
- Refactoring de la gestion des communes CNOUS pour une meilleure validation et affichage [#1633](https://github.com/etalab/data_pass/pull/1633).
- Amélioration des performances du dashboard en réduisant les requêtes répétées et en optimisant l'utilisation de Rails Pulse [#1564](https://github.com/etalab/data_pass/pull/1564).
- Correction d'un bug empêchant la suppression correcte des droits utilisateurs [#1634](https://github.com/etalab/data_pass/pull/1634).
- Mise à jour de Ruby à la dernière version stable [#1285](https://github.com/etalab/data_pass/pull/1285).
- Correction de tests Cucumber instables liés à l'API particulier [#1590](https://github.com/etalab/data_pass/pull/1590).
- Suppression de lignes de code inutilisées et amélioration de la lisibilité du code.
- Mise à jour des dépendances (Rubocop, Yard, Faraday, etc.).

### Autres changements
- Ajout de documentation pour l'authentification ProConnect [#1622](https://github.com/etalab/data_pass/pull/1622).
- Amélioration de la gestion des erreurs et des validations pour les données CNOUS.
- Correction de liens brisés dans la documentation Swagger.
- Ajout d'un seed pour la fonctionnalité geo/cnous.
- Amélioration des messages d'erreur et de l'UX pour les formulaires dynamiques.
- Ajout d'un service de migration de scope pour standardiser les renommages.
- Correction de bugs mineurs et amélioration de la qualité du code.
