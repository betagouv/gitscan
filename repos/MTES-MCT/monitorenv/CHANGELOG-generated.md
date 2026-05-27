## Changelog : monitorenv (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des tags, des zones de vigilance et des missions. Des corrections de données et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Tags :** Création d'un backoffice pour la gestion des tags et affichage des tags dans l'interface utilisateur. Possibilité de filtrer les couches de la carte par tags [#29fd525](https://github.com/MTES-MCT/monitorenv/pulls/29fd525).
- **Zones de vigilance :** Amélioration de l'affichage du planning des zones de vigilance en vue liste, avec ajout d'infobulles pour les périodes [#9f3c08d](https://github.com/MTES-MCT/monitorenv/pulls/9f3c08d). Correction du nom de la source de l'unité de contrôle sur le survol [#4c8b7b3](https://github.com/MTES-MCT/monitorenv/pulls/4c8b7b3).
- **Missions :** Refonte de la table des missions pour la rendre extensible, avec affichage des tags associés et des actions environnementales [#d225a21](https://github.com/MTES-MCT/monitorenv/pulls/d225a21). Ajout d'un bouton de réinitialisation dans les modales de mission, de reporting et de tableau de bord [#153e04a](https://github.com/MTES-MCT/monitorenv/pulls/153e04a).
- **Cartographie :** Correction de la requête de recherche dans l'input de la carte [#ad1ef22](https://github.com/MTES-MCT/monitorenv/pulls/ad1ef22).
- **Données CACEM :** Correction de la gestion des hachages CACEM [#dc4b4a5](https://github.com/MTES-MCT/monitorenv/pulls/dc4b4a5).

### Évolutions techniques
- **Node et NPM :** Mise à niveau vers Node 24 et NPM 11 [#84ee855](https://github.com/MTES-MCT/monitorenv/pulls/84ee855).
- **Dépendances :** Mise à jour de plusieurs dépendances frontend (Cypress, @sentry/browser, ol-mapbox-style, etc.) et pipeline (python-dotenv, pytest, cryptography, black) via Dependabot.
- **Tests :** Ajout de tests E2E pour les tags et les zones réglementaires [#9ca8ed3](https://github.com/MTES-MCT/monitorenv/pulls/9ca8ed3). Corrections de tests unitaires et E2E.
- **Architecture :** Refactorisation de MonthBox [#f4e7cc7](https://github.com/MTES-MCT/monitorenv/pulls/f4e7cc7). Suppression de code obsolète pour les zones réglementaires [#f92eefc](https://github.com/MTES-MCT/monitorenv/pulls/f92eefc).
- **CI/CD :** Configuration de Dependabot pour exclure `package.lock` et désactiver le rebase automatique [#22391f0](https://github.com/MTES-MCT/monitorenv/pulls/22391f0) et [#5ec9a44](https://github.com/MTES-MCT/monitorenv/pulls/5ec9a44).

### Autres changements
- **Documentation :** Correction d'une faute de frappe dans le README [#5bd4eb4](https://github.com/MTES-MCT/monitorenv/pulls/5bd4eb4).
- **Accessibilité :** Amélioration de l'accessibilité de la liste des périodes dans les zones de vigilance [#83c688b](https://github.com/MTES-MCT/monitorenv/pulls/83c688b).
- **Divers :** Ajout de colonnes liées à la plongée pour les contrôles conchylicoles [#29b6535](https://github.com/MTES-MCT/monitorenv/pulls/29b6535). Correction de l'icône UI [#a5d8c0b](https://github.com/MTES-MCT/monitorenv/pulls/a5d8c0b).
