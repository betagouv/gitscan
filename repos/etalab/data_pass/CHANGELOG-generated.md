## Changelog : data_pass (30 derniers jours, au 01 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface utilisateur et de l'API, notamment l'ajout de nouveaux formulaires pré-remplis pour des aides spécifiques (MGDIS, Andyvie/Recreo), une gestion améliorée des droits d'accès et une refonte de la recherche d'utilisateurs. Des corrections de bugs et des mises à jour techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout du formulaire pré-rempli MGDIS pour les aides facultatives départementales. [#1501](https://github.com/etalab/data_pass/pull/1501)
- Ajout du formulaire pré-rempli Andyvie (Recreo). [#1577](https://github.com/etalab/data_pass/pull/1577)
- Amélioration de la recherche d'utilisateurs dans la gestion des droits, avec possibilité de rechercher par formatted_id (D/H). [#1575](https://github.com/etalab/data_pass/pull/1575)
- Implémentation de la gestion des rôles et des droits d'accès pour les administrateurs, incluant la possibilité de s'auto-éditer. [#1573](https://github.com/etalab/data_pass/pull/1573)
- Ajout d'une interface pour la gestion des droits utilisateur, avec l'ajout du domaine et des règles métier correspondantes. [#1544](https://github.com/etalab/data_pass/pull/1544)
- Limitation du nombre de fichiers uploadés à 6 par champ document. [#1554](https://github.com/etalab/data_pass/pull/1554)
- Ajout d'un encart de connexion rapide hors production. [#1550](https://github.com/etalab/data_pass/pull/1550)
- Implémentation du bloc CNOUS data extraction criteria (vue ERB côté usager). [#1550](https://github.com/etalab/data_pass/pull/1550)

### Évolutions techniques
- Ajout du mapping des codes INSEE pour la catégorie juridique des organisations via l'API. [#1582](https://github.com/etalab/data_pass/pull/1582)
- Suppression du champ `recurrence` du bloc `cnous_data_extraction_criteria` dans l'API. [#1581](https://github.com/etalab/data_pass/pull/1581)
- Refactorisation des contrôleurs pour adopter `params.expect` pour Rails/StrongParametersExpect. [#1576](https://github.com/etalab/data_pass/pull/1576)
- Mise à jour de la gestion des scopes DHTOUR (hébergement touristique) en les dépréciant. [#1574](https://github.com/etalab/data_pass/pull/1574)
- Mise à jour de la version de View Component (3.24.0 -> 4.9.0). [#1559](https://github.com/etalab/data_pass/pull/1559)
- Mise à jour de Rails Pulse à la version 0.3.1. [#1553](https://github.com/etalab/data_pass/pull/1553)
- Amélioration de la gestion des tests Cucumber pour éviter les tests aléatoires. [#1562](https://github.com/etalab/data_pass/pull/1562)
- Correction de bugs et amélioration de la robustesse des tests. [#1590](https://github.com/etalab/data_pass/pull/1590)

### Autres changements
- Mise à jour de la documentation concernant l'habilitation de type dynamique et la réorganisation du dossier de documentation. [#1549](https://github.com/etalab/data_pass/pull/1549), [#1548](https://github.com/etalab/data_pass/pull/1548)
- Mise à jour des CGU TDAE. [#1585](https://github.com/etalab/data_pass/pull/1585)
- Amélioration de la lisibilité du tutoriel de lecture de l'API. [#1569](https://github.com/etalab/data_pass/pull/1569)
- Corrections de style et amélioration de la qualité du code (Rubocop). [#1570](https://github.com/etalab/data_pass/pull/1570)
