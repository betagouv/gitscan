## Changelog : data_pass (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la gestion des autorisations et des droits d'accès, ainsi que sur l'ajout de nouvelles fonctionnalités liées à la pré-remplissage de formulaires et à l'intégration avec des services tiers comme FranceConnect et Andyvie. Des corrections de bugs et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la gestion des droits utilisateurs : ajout d'une interface pour gérer les rôles et les autorisations des utilisateurs, avec possibilité pour les administrateurs de s'auto-éditer leurs droits. [#1570](https://github.com/etalab/data_pass/pull/1570) [#1544](https://github.com/etalab/data_pass/pull/1544) [#1521](https://github.com/etalab/data_pass/pull/1521)
- Ajout d'un lien "Ne plus recevoir ces emails" dans les emails d'instruction. [#1592](https://github.com/etalab/data_pass/pull/1592)
- Activation des brouillons d'instructeur pour FranceConnect, permettant une meilleure gestion des demandes. [#1597](https://github.com/etalab/data_pass/pull/1597)
- Mise à jour des CGU pour Prosante Connect. [#1596](https://github.com/etalab/data_pass/pull/1596)
- Ajout du formulaire pré-rempli MGDIS Aides facultatives départementales. [#1578](https://github.com/etalab/data_pass/pull/1578)
- Intégration du formulaire pré-rempli Andyvie (Recreo). [#1577](https://github.com/etalab/data_pass/pull/1577)
- Possibilité de pré-remplir une demande via des paramètres d'URL. [#1566](https://github.com/etalab/data_pass/pull/1566)
- Amélioration de la recherche d'utilisateurs dans la gestion des droits. [#1544](https://github.com/etalab/data_pass/pull/1544)
- Limitation de la taille des fichiers uploadés. [#1554](https://github.com/etalab/data_pass/pull/1554)
- Ajout de la possibilité de trier les résultats des endpoints de l'API par date de création. [#1593](https://github.com/etalab/data_pass/pull/1593)
- Amélioration de la prévisualisation des emails FranceConnect. [#1599](https://github.com/etalab/data_pass/pull/1599)
- Ajout du mappage des codes INSEE pour la catégorie juridique des organisations via l'API. [#1582](https://github.com/etalab/data_pass/pull/1582)

### Évolutions techniques
- Mise à jour de Ruby à la dernière version. [#1285](https://github.com/etalab/data_pass/pull/1285)
- Amélioration de la gestion des tests Cucumber pour éviter les faux positifs. [#1562](https://github.com/etalab/data_pass/pull/1562)
- Refactorisation du code pour adopter les recommandations RuboCop. [#1570](https://github.com/etalab/data_pass/pull/1570)
- Utilisation de `params.expect` pour Rails/StrongParametersExpect. [#1572](https://github.com/etalab/data_pass/pull/1572)
- Mise à jour des dépendances (ViewComponent, Bootsnap, CSS Parser, Faraday, JWT).
- Amélioration de la configuration des tests en local avec un wrapper parallèle. [#1562](https://github.com/etalab/data_pass/pull/1562)

### Autres changements
- Mise à jour de la documentation (conception.md). [#1594](https://github.com/etalab/data_pass/pull/1594)
- Suppression des `TODO` remplacés par des données métier. [#1594](https://github.com/etalab/data_pass/pull/1594)
- Correction d'un bug empêchant l'affichage correct des modèles d'emails personnalisés au format texte. [#1600](https://github.com/etalab/data_pass/pull/1600)
- Correction d'un test Cucumber pour l'API particulier. [#1590](https://github.com/etalab/data_pass/pull/1590)
- Mise à jour des CGU TDAE. [#1585](https://github.com/etalab/data_pass/pull/1585)
- Suppression du champ `recurrence` du bloc `cnous_data_extraction_criteria`. [#1581](https://github.com/etalab/data_pass/pull/1581)
- Correction de l'affichage du fil d'Ariane dans l'interface d'administration. [#1573](https://github.com/etalab/data_pass/pull/1573)
