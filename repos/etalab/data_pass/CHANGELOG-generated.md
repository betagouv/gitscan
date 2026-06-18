## Changelog : data_pass (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la gestion des inscriptions et des droits d'accès. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'intégration avec des services tiers comme HubEE et ProConnect a été renforcée.

### Évolutions fonctionnelles
- Possibilité de se désinscrire facilement des notifications par email via un lien unique et chiffré présent dans les emails. [#1606](https://github.com/etalab/data_pass/pull/1606)
- Amélioration de la présentation des préférences utilisateur et correction de l'accessibilité (RGAA). [#1606](https://github.com/etalab/data_pass/pull/1606)
- Envoi individuel des emails d'instruction pour une meilleure délivrabilité et un suivi plus précis. [#1606](https://github.com/etalab/data_pass/pull/1606)
- Correction d'un bug empêchant la suppression correcte d'une ligne de droit utilisateur. [#1634](https://github.com/etalab/data_pass/pull/1634)
- Amélioration de la recherche d'utilisateurs et de la gestion des droits, avec une meilleure expérience utilisateur. [#1610](https://github.com/etalab/data_pass/pull/1610)
- Possibilité de définir plusieurs modèles de cas d'usage pour un même formulaire, offrant une plus grande flexibilité. [#1564](https://github.com/etalab/data_pass/pull/1564)
- Ajout d'un lien pour gérer les préférences de notification dans les emails d'instruction. [#1575](https://github.com/etalab/data_pass/pull/1575)
- Les demandes validées sont maintenant incluses dans les résultats de recherche par ID. [#1619](https://github.com/etalab/data_pass/pull/1619)
- Mise à jour des CGU pour les services Prosante Connect et TDAE. [#1596](https://github.com/etalab/data_pass/pull/1596), [#1585](https://github.com/etalab/data_pass/pull/1585)
- Amélioration de la recherche et de l'affichage des données géographiques (CNous). [#1582](https://github.com/etalab/data_pass/pull/1582)
- Intégration du formulaire pré-rempli Andyvie (Recreo) dans l'API. [#1577](https://github.com/etalab/data_pass/pull/1577)
- Ajout du formulaire pré-rempli MGDIS Aides facultatives départementales. [#1501](https://github.com/etalab/data_pass/pull/1501)
- Possibilité pour les administrateurs de s'auto-éditer leurs droits. [#1573](https://github.com/etalab/data_pass/pull/1573)

### Évolutions techniques
- Intégration du bridge HubEE par bloc, améliorant la gestion de la proactivité. [#1633](https://github.com/etalab/data_pass/pull/1633)
- Amélioration de la gestion des erreurs et des performances du tableau de bord, notamment en corrigeant les requêtes N+1 et en réduisant le bruit dans Sentry. [#1604](https://github.com/etalab/data_pass/pull/1604)
- Documentation du processus d'authentification ProConnect. [#1622](https://github.com/etalab/data_pass/pull/1622)
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (Faraday, JWT, Rubocop, Puma, etc.).
- Amélioration de la robustesse des tests Cucumber. [#1608](https://github.com/etalab/data_pass/pull/1608)

### Autres changements
- Mise à jour des liens vers la documentation Swagger. [#1623](https://github.com/etalab/data_pass/pull/1623)
- Correction de liens obsolètes dans la documentation. [#1617](https://github.com/etalab/data_pass/pull/1617)
- Suppression de code HTML générique inutile dans les emails. [#1600](https://github.com/etalab/data_pass/pull/1600)
- Amélioration de la prévisualisation des emails FranceConnect. [#1599](https://github.com/etalab/data_pass/pull/1599)
- Suppression de TODO et remplacement par des données métier. [#1594](https://github.com/etalab/data_pass/pull/1594)
- Mise à jour de la version de Ruby. [#1285](https://github.com/etalab/data_pass/pull/1285)
