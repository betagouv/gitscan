## Changelog : data_pass (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les évolutions de data_pass se concentrent sur l'amélioration de la sécurité et de l'expérience utilisateur, notamment avec la réduction de la durée de vie des sessions, l'ajout de liens de gestion des notifications, et l'amélioration de la gestion des droits et des accès. Des corrections de bugs et des mises à jour de dépendances ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Sécurité :** Réduction de la durée de vie de la session à 12 heures avec un maximum de 24 heures, alignement avec ProConnect [#1625](https://github.com/etalab/data_pass/pull/1625).
- **Gestion des utilisateurs :** Les managers peuvent désormais attribuer le rôle développeur à leurs utilisateurs.
- **Authentification :** Ajout d'un lien de gestion des notifications dans les emails d'instruction [#1592](https://github.com/etalab/data_pass/pull/1592).
- **Désinscription :** Simplification de la désinscription via un lien unique dans les emails [#1606](https://github.com/etalab/data_pass/pull/1606).
- **API :** Possibilité de trier les résultats des endpoints de l'API [#1646](https://github.com/etalab/data_pass/pull/1646).
- **Formulaires :** Amélioration de la gestion des templates de cas d'usage pour les formulaires [#1564](https://github.com/etalab/data_pass/pull/1564).
- **FranceConnect :** Activation des brouillons pour les instructeurs FranceConnect [#1597](https://github.com/etalab/data_pass/pull/1597).
- **Interface utilisateur :** Affichage des demandes validées dans les résultats de recherche par ID [#1619](https://github.com/etalab/data_pass/pull/1619).
- **CGU :** Mise à jour des CGU pour TDAE et Prosante Connect [#1585](https://github.com/etalab/data_pass/pull/1585), [#1596](https://github.com/etalab/data_pass/pull/1596).

### Évolutions techniques
- **API :** Intégration des catégories légales des organisations via le mapping INSEE [#1582](https://github.com/etalab/data_pass/pull/1582).
- **Bridges :** Amélioration de la gestion des bridges HubEE, notamment pour les formulaires dynamiques [#1626](https://github.com/etalab/data_pass/pull/1626) et la proactivité [#1633](https://github.com/etalab/data_pass/pull/1633).
- **Tests :** Correction de tests Cucumber instables [#1608](https://github.com/etalab/data_pass/pull/1608), [#1590](https://github.com/etalab/data_pass/pull/1590).
- **Performance :** Optimisation des requêtes dans le dashboard pour éviter les N+1 et réduire le bruit Sentry [#1604](https://github.com/etalab/data_pass/pull/1604).
- **Sécurité :** Renforcement de la protection CSRF et configuration explicite de SameSite pour les cookies.
- **Authentification :** Mise à jour des valeurs MFA pour OmniAuth Proconnect [#1636](https://github.com/etalab/data_pass/pull/1636).

### Autres changements
- **Documentation :** Documentation du processus d’authentification ProConnect [#1622](https://github.com/etalab/data_pass/pull/1622).
- **Maintenance :** Mises à jour des dépendances (Ruby, Rubocop, Docker, etc.).
- **Refactoring :** Amélioration de la structure du code et suppression de code obsolète.
- **Correction de bugs :** Correction de la suppression de lignes de droits utilisateur [#1634](https://github.com/etalab/data_pass/pull/1634) et de problèmes liés à la saisie tactile des codes INSEE.
