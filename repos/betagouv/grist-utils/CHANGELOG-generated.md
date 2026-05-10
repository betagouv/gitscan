## Changelog : grist-utils (30 derniers jours, au 8 mai 2026)

### Résumé
Ce changelog fait état de mises à jour principalement axées sur la maintenance et la sécurité des outils de déploiement de Grist. Les changements incluent des mises à jour de dépendances pour assurer la compatibilité et corriger des vulnérabilités potentielles, ainsi que la désactivation temporaire des tests antivirus suite à une demande spécifique.

### Évolutions fonctionnelles
- Désactivation des tests antivirus, suite à une demande de JCOP [#0e58ec3](https://github.com/betagouv/grist-utils/commit/0e58ec3).

### Évolutions techniques
- Mise à jour de plusieurs dépendances dans `/grist-deployment-tests` :
    - `axios` de 1.13.6 à 1.15.0 [#e989f3b](https://github.com/betagouv/grist-utils/commit/e989f3b)
    - `fast-xml-builder` [#8f119c3](https://github.com/betagouv/grist-utils/commit/8f119c3)
    - `fast-xml-parser` [#bb9b3c4](https://github.com/betagouv/grist-utils/commit/bb9b3c4)
    - `basic-ftp` (plusieurs mises à jour) [#6e6afc5](https://github.com/betagouv/grist-utils/commit/6e6afc5), [#cf1404b](https://github.com/betagouv/grist-utils/commit/cf1404b)
    - `ip-address` et `socks` [#3b25bdb](https://github.com/betagouv/grist-utils/commit/3b25bdb)
    - `picomatch` [#4af9dff](https://github.com/betagouv/grist-utils/commit/4af9dff)
    - `brace-expansion` [#7cceb57](https://github.com/betagouv/grist-utils/commit/7cceb57)
    - `lodash` [#f05fa10](https://github.com/betagouv/grist-utils/commit/f05fa10)
    - `follow-redirects` [#63fd032](https://github.com/betagouv/grist-utils/commit/63fd032)
- Mise à jour des dépendances de développement [#9c03076](https://github.com/betagouv/grist-utils/commit/9c03076)
- Mise à jour des dépendances de production [#96fd9dd](https://github.com/betagouv/grist-utils/commit/96fd9dd)

### Autres changements
- Aucun changement significatif à signaler.
