## Changelog : mon-indemnisation-justice (30 derniers jours, au 03 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités pour la gestion des dossiers et des agents, ainsi que sur l'intégration de données externes et l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'un espace public pour le test d'éligibilité. Des corrections de sécurité (CSP) et de gestion des erreurs ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un espace public pour le test d'éligibilité avec un formulaire et des étapes guidées. [#33aa28c](https://github.com/betagouv/mon-indemnisation-justice/commit/33aa28c)
- Possibilité de modifier les critères de recherche des dossiers. [#b3785de](https://github.com/betagouv/mon-indemnisation-justice/commit/b3785de)
- Affichage des pièces jointes au format PDF directement dans l'application. [#216a13f](https://github.com/betagouv/mon-indemnisation-justice/commit/216a13f)
- Création d'un onglet dédié aux "Agents à valider" pour faciliter la gestion des accès. [#69e1d74](https://github.com/betagouv/mon-indemnisation-justice/commit/69e1d74)
- Amélioration du navigateur de pages pour une meilleure expérience utilisateur. [#6778b21](https://github.com/betagouv/mon-indemnisation-justice/commit/6778b21)
- Ajout d'un composant "Frise temporelle" pour visualiser l'historique des dossiers. [#e909378](https://github.com/betagouv/mon-indemnisation-justice/commit/e909378)
- Possibilité de masquer les outils Tanstack pour une interface plus épurée. [#e8aeaf1](https://github.com/betagouv/mon-indemnisation-justice/commit/e8aeaf1)
- Précision du test d'éligibilité pour les bris de porte. [#613b72b](https://github.com/betagouv/mon-indemnisation-justice/commit/613b72b)
- Mise à jour du lien vers le questionnaire de satisfaction. [#d5e0003](https://github.com/betagouv/mon-indemnisation-justice/commit/d5e0003)

### Évolutions techniques
- Refonte de l'architecture du worker avec l'utilisation de `pierrelemee/supervisor-docker` pour la gestion et la surveillance des tâches. [#dd74ef7](https://github.com/betagouv/mon-indemnisation-justice/commit/dd74ef7)
- Création d'images Docker pour le déploiement des applications web et worker. [#dad9add](https://github.com/betagouv/mon-indemnisation-justice/commit/dad9add)
- Intégration de Sentry pour la gestion des erreurs et le suivi des performances. [#9a526f7](https://github.com/betagouv/mon-indemnisation-justice/commit/9a526f7)
- Amélioration de la gestion des erreurs FIP6 et FDO avec affichage et remontée des erreurs. [#8272609](https://github.com/betagouv/mon-indemnisation-justice/commit/8272609) et [#4d0b818](https://github.com/betagouv/mon-indemnisation-justice/commit/4d0b818)
- Mise en place d'un cache buster via une variable d'environnement. [#fc393c6](https://github.com/betagouv/mon-indemnisation-justice/commit/fc393c6)
- Correction de problèmes de CSP (Content Security Policy) pour améliorer la sécurité de l'application. [#6c29178](https://github.com/betagouv/mon-indemnisation-justice/commit/6c29178) et autres commits liés.
- Utilisation de la version legacy de `react-pdf` pour résoudre des problèmes de compatibilité. [#f6e7923](https://github.com/betagouv/mon-indemnisation-justice/commit/f6e7923)

### Autres changements
- Importation des données des gendarmeries et création de l'entité `EtablissementFDO`. [#8a87013](https://github.com/betagouv/mon-indemnisation-justice/commit/8a87013) et [#a50541d](https://github.com/betagouv/mon-indemnisation-justice/commit/a50541d)
- Ajout d'un importeur CSV basique. [#ed7b87b](https://github.com/betagouv/mon-indemnisation-justice/commit/ed7b87b)
- Correction de divers bugs et améliorations de la qualité du code.
- Mise à jour de la documentation et des tests unitaires.
- Suppression de Storybook dans l'espace visiteur et refactoring du code de l'espace public. [#e69825b](https://github.com/betagouv/mon-indemnisation-justice/commit/e69825b) et autres commits liés.
