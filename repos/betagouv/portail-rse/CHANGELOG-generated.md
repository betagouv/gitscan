## Changelog : portail-rse (30 derniers jours, au 14 avril 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se sont concentrées sur l'amélioration de la gestion des entreprises, notamment avec l'ajout du code postal, la simplification des processus d'habilitation et d'invitation, et l'amélioration de l'accès aux fonctionnalités pour les entreprises non qualifiées. Des optimisations techniques ont également été apportées, notamment le remplacement de pipenv par uv et des refactorings pour une meilleure maintenabilité du code.

### Évolutions fonctionnelles
- **Gestion des entreprises :** Ajout du code postal des entreprises, avec affichage dans le tableau de bord et possibilité de préremplissage de rapports VSME à partir de rapports précédents. [#90738f3](https://github.com/betagouv/portail-rse/commit/90738f3)
- **Accès aux fonctionnalités :** Les entreprises non qualifiées ont désormais accès aux analyses IA et à l'espace indicateurs VSME. [#fe4a823](https://github.com/betagouv/portail-rse/commit/fe4a823)
- **Habilitations et invitations :** Simplification des processus d'habilitation et d'invitation, avec suppression du concept de confirmation d'habilitation et fusion des acceptations d'invitation. [#c237bed](https://github.com/betagouv/portail-rse/commit/c237bed), [#00cc764](https://github.com/betagouv/portail-rse/commit/00cc764)
- **Proconnect :** Les utilisateurs Proconnect deviennent éditeurs sur une entreprise existante sur le portail. [#a98c0de](https://github.com/betagouv/portail-rse/commit/a98c0de)
- **Rapports VSME :** Amélioration du template Excel d'export des indicateurs VSME. [#41be294](https://github.com/betagouv/portail-rse/commit/41be294)
- **Création d'entreprise :** Possibilité d'ajouter une entreprise sans être connecté. [#05d614e](https://github.com/betagouv/portail-rse/commit/05d614e)

### Évolutions techniques
- **Outils de gestion des dépendances :** Remplacement de pipenv par uv pour une meilleure gestion des dépendances. [#b5226ab](https://github.com/betagouv/portail-rse/commit/b5226ab)
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la lisibilité et la maintenabilité du code, notamment au niveau de la gestion des propriétaires, des invitations et des rapports VSME. [#daefdea](https://github.com/betagouv/portail-rse/commit/daefdea), [#31887ed](https://github.com/betagouv/portail-rse/commit/31887ed), [#a7911ff](https://github.com/betagouv/portail-rse/commit/a7911ff)
- **Documentation :** Mise à jour du README pour une meilleure documentation du projet. [#f5a838b](https://github.com/betagouv/portail-rse/commit/f5a838b)

### Autres changements
- **Configuration :** Ajout du fichier `.python-version` pour faciliter le déploiement. [#32a1ad9](https://github.com/betagouv/portail-rse/commit/32a1ad9)
- **Nettoyage du code :** Suppression de code inutile et de fichiers non versionnés. [#7f3ae19](https://github.com/betagouv/portail-rse/commit/7f3ae19), [#8fec709](https://github.com/betagouv/portail-rse/commit/8fec709), [#35fd976](https://github.com/betagouv/portail-rse/commit/35fd976)
- **Correction de typos :** Correction de quelques coquilles dans le code et la documentation. [#5dd698e](https://github.com/betagouv/portail-rse/commit/5dd698e)
- **Firewall :** Documentation concernant la configuration du firewall sur la machine IA. [#674bd38](https://github.com/betagouv/portail-rse/commit/674bd38)
