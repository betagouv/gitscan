## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 22 mai 2026)

### Résumé
Ce changelog fait état d'une période d'amélioration de la sécurité du site, avec des mises à jour de plusieurs dépendances pour corriger des vulnérabilités potentielles. Des améliorations ont également été apportées à l'intégration et au déploiement du site, notamment via l'outil GRIST. Enfin, quelques ajustements de contenu ont été effectués.

### Évolutions fonctionnelles
- Modification du texte "Omnicité" par "Crème de la crème" dans le contenu du site. [#8e31dcd](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/8e31dcd)
- Ajout d'informations concernant Claude. [#73ec211](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/73ec211)

### Évolutions techniques
- **Sécurité:** Mises à jour de plusieurs dépendances pour corriger des vulnérabilités :
    - `postcss` vers la version 8.5.10 [#c0d44f3](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/c0d44f3)
    - `axios` vers la version 1.15.2 [#aaf27d8](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/aaf27d8)
    - `fast-xml-builder` vers la version 1.1.6 [#84b6990](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/84b6990)
    - `fast-xml-parser` vers la version 5.7.0 [#7a2458b](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7a2458b)
    - `follow-redirects` vers la version 1.16.0 [#56c9d5d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/56c9d5d)
- **Déploiement & Intégration Continue:**
    - Amélioration du processus de déploiement avec GRIST : sauvegarde de l'empreinte, recopie de la démo en production, utilisation de snapshots, comparaison des grist dans la CI, et rendu du déploiement dépendant de cette comparaison. [#ed3b772](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ed3b772), [#bfa3732](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/bfa3732), [#9e58f1e](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/9e58f1e), [#961298d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/961298d), [#8cdb6f5](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/8cdb6f5), [#52081c2](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/52081c2), [#37f3a2c](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/37f3a2c)
- Correction de l'injection du nonce pour améliorer la sécurité. [#7b7c350](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7b7c350)

### Autres changements
- Suppression d'un fichier inutile. [#881c8bc](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/881c8bc)
