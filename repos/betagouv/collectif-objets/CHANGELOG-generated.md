## Changelog : collectif-objets (30 derniers jours, au 29 février 2024)

### Résumé
Les dernières évolutions se concentrent sur l'amélioration de la stabilité et de la performance de l'application, notamment en remplaçant des solutions temporaires par des outils plus robustes et en optimisant les requêtes statistiques. Des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur et la fiabilité du système.

### Évolutions fonctionnelles
- Correction d'un bug empêchant le comptage correct des objets prioritaires. [#1537](https://github.com/betagouv/collectif-objets/issues/1537)
- Correction d'un problème d'affichage des numéros de téléphone trop longs dans la liste des conservateurs.
- Mise à jour des chemins d'accès aux images POP. [#1533](https://github.com/betagouv/collectif-objets/issues/1533)
- Amélioration de la robustesse des tests, notamment en corrigeant des tests aléatoires. [#1535](https://github.com/betagouv/collectif-objets/issues/1535)

### Évolutions techniques
- Remplacement des solutions temporaires (Turbo workarounds) par la gem Capybara::Lockstep pour améliorer la stabilité des tests et l'interaction avec l'interface utilisateur.
- Refonte de la récupération des statistiques, remplaçant l'utilisation de Metabase par des requêtes SQL directes pour une meilleure performance et contrôle. [#1524](https://github.com/betagouv/collectif-objets/issues/1524)
- Mise à jour de Rubocop et application du linter pour améliorer la qualité du code. [#1534](https://github.com/betagouv/collectif-objets/issues/1534)
- Suppression d'un déploiement obsolète.
- Correction d'une condition de course causant des échecs intermittents des tests.

### Autres changements
- Mise à jour de la dépendance `bcrypt` de la version 3.1.20 à 3.1.22. [#1526](https://github.com/betagouv/collectif-objets/issues/1526)
- Mise à jour de la dépendance `activesupport` de la version 7.2.2.2 à 7.2.3.1. [#1529](https://github.com/betagouv/collectif-objets/issues/1529)
