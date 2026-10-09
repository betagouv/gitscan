## Changelog : hyyypertool (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, l'effort principal a porté sur la stabilisation et la performance de l'outil. Une refonte majeure de la suite de tests automatisés a été réalisée pour garantir la fiabilité des fonctionnalités, accompagnée d'une optimisation des processus de déploiement continu. Quelques corrections mineures ont également été apportées pour améliorer l'expérience de support et la navigation.

### Évolutions fonctionnelles
- Correction du lien vers la liste des dirigeants sur l'annuaire-entreprises [#1847](https://github.com/proconnect-gouv/hyyypertool/issues/1847).
- Ajout de l'adresse e-mail de support Crisp lors des actions de support [#1846](https://github.com/proconnect-gouv/hyyypertool/issues/1846).
- Amélioration de la gestion des conversations Crisp pour assurer un repli automatique vers une nouvelle conversation en cas de ticket obsolète [#1800](https://github.com/proconnect-gouv/hyyypertool/issues/1800).

### Évolutions techniques
- **Tests E2E :** Migration massive de la suite de tests de fonctionnalités vers un nouveau moteur (`buncept`) afin d'améliorer la robustesse et la maintenance des tests [#1827](https://github.com/proconnect-gouv/hyyypertool/issues/1827), [#1866](https://github.com/proconnect-gouv/hyyypertool/issues/1866).
- **CI/CD :** Optimisation de la vitesse d'exécution des tests grâce au partitionnement (sharding) sur plusieurs runners simultanés [#1881](https://github.com/proconnect-gouv/hyyypertool/issues/1881), [#1894](https://github.com/proconnect-gouv/hyyypertool/issues/1894).
- **CI/CD :** Automatisation et amélioration du workflow de publication des versions (releases) via `release-action` [#1857](https://github.com/proconnect-gouv/hyyypertool/issues/1857), [#1864](https://github.com/proconnect-gouv/hyyypertool/issues/1864).
- **Architecture :** Modularisation du thème Tailwind du Design System (DSFR) en l'extrayant dans un package dédié au sein du workspace [#1791](https://github.com/proconnect-gouv/hyyypertool/issues/1791).
- **Infrastructure :** Mise à jour de l'environnement d'exécution vers Bun 1.4.2 [#1790](https://github.com/proconnect-gouv/hyyypertool/issues/1790).

### Autres changements
- Nettoyage du code et suppression de signatures redondantes déjà gérées par Crisp [#1891](https://github.com/proconnect-gouv/hyyypertool/issues/1891).
- Suppression des commentaires de release automatiques sur GitHub pour épurer les notifications [#1861](https://github.com/proconnect-gouv/hyyypertool/issues/1861).
