## Changelog : monstagedeseconde (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, la maintenance et l'amélioration de l'expérience utilisateur, notamment au niveau du formulaire de création d'offres et de la gestion des partenaires. Des refactorings techniques ont également été réalisés pour améliorer la qualité du code et la maintenabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration du formulaire de création d'offres : corrections de bugs et amélioration de la visualisation des erreurs [#937](https://github.com/betagouv/monstagedeseconde/pull/937).
- Limitation de la longueur de la description des offres via l'API [#922](https://github.com/betagouv/monstagedeseconde/pull/922).
- Suppression du bloc "Devenez partenaire" sur la page d'accueil [#921](https://github.com/betagouv/monstagedeseconde/pull/921), [#920](https://github.com/betagouv/monstagedeseconde/pull/920).
- Modification de l'accès aux contacts [#917](https://github.com/betagouv/monstagedeseconde/pull/917).
- Optimisation de la gestion des offres publiques et privées [#912](https://github.com/betagouv/monstagedeseconde/pull/912).
- Mise à jour des pages partenaires [#942](https://github.com/betagouv/monstagedeseconde/pull/942).
- Adaptation pour la maintenance estivale 2026 [#943](https://github.com/betagouv/monstagedeseconde/pull/943).

### Évolutions techniques
- Refactoring du code pour une meilleure lisibilité et maintenabilité, notamment au niveau des libellés des états des candidatures dans les tableaux de bord [#936](https://github.com/betagouv/monstagedeseconde/pull/936).
- Mutualisation de code pour éviter les répétitions et améliorer la cohérence [#938](https://github.com/betagouv/monstagedeseconde/pull/938).
- Renforcement de la sécurité : correction d'une vulnérabilité potentielle de détournement de compte [#932](https://github.com/betagouv/monstagedeseconde/pull/932) et correction d'un risque XSS lié à l'injection de contenu HTML non échappé [#933](https://github.com/betagouv/monstagedeseconde/pull/933).
- Correction de plusieurs erreurs et améliorations de la robustesse du code (gestion des valeurs `nil`, tests, etc.) [#931](https://github.com/betagouv/monstagedeseconde/pull/931), [#930](https://github.com/betagouv/monstagedeseconde/pull/930), [#929](https://github.com/betagouv/monstagedeseconde/pull/929).
- Mise à jour de plusieurs dépendances (webpack-dev-server, babel/core, http-proxy-middleware, undici, concurrent-ruby, form-data, launch-editor)

### Autres changements
- Correction d'un problème lié au seed de la base de données [#902](https://github.com/betagouv/monstagedeseconde/pull/902).
- Suppression d'un bloc de code inutile et amélioration de la documentation.
- Amélioration des tests et correction de tests défaillants.
- Nettoyage du code et suppression de code mort.
