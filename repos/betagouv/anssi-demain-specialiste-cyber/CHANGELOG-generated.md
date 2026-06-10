## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 22 mai 2026)

### Résumé
Ce changelog fait état d'une période principalement axée sur la sécurité et l'amélioration des processus de déploiement. Des mises à jour de dépendances ont été effectuées pour corriger des vulnérabilités potentielles, et des améliorations ont été apportées à l'intégration continue pour garantir la cohérence des déploiements. Une modification de terminologie a également été effectuée pour aligner le site avec la nouvelle appellation "Crème de la crème".

### Évolutions fonctionnelles
- Modification du terme "Omnicité" par "Crème de la crème" sur le site web. [#8e31dcd](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/8e31dcd)

### Évolutions techniques
- **Sécurité :** Mises à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité :
    - `postcss` vers la version 8.5.10 [#c0d44f3](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/c0d44f3)
    - `axios` vers la version 1.15.2 [#aaf27d8](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/aaf27d8)
    - `fast-xml-builder` vers la version 1.1.6 [#84b6990](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/84b6990)
    - `fast-xml-parser` vers la version 5.7.0 [#7a2458b](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7a2458b)
    - `follow-redirects` vers la version 1.16.0 [#56c9d5d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/56c9d5d)
- **Déploiement :** Amélioration du processus de déploiement avec l'intégration de GRIST :
    - Sauvegarde de l'empreinte GRIST [#ed3b772](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ed3b772)
    - Recopie de la démo GRIST en production [#bfa3732](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/bfa3732)
    - Utilisation d'un snapshot GRIST [#9e58f1e](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/9e58f1e)
    - Comparaison des GRIST dans la CI [#961298d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/961298d)
    - Déploiement dépendant de la comparaison GRIST [#8cdb6f5](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/8cdb6f5)
    - Téléchargement de l'empreinte GRIST [#52081c2](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/52081c2)
    - Rendre le déploiement manuel [#37f3a2c](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/37f3a2c)
- **Sécurité :** Correction de l'injection du nonce pour améliorer la sécurité du site. [#7b7c350](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7b7c350)

### Autres changements
- Ajout d'informations pour Claude. [#73ec211](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/73ec211)
- Suppression d'un fichier inutile. [#881c8bc](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/881c8bc)
