## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 22 mai 2026)

### Résumé
Ce changelog fait état d'une période axée sur la sécurité du site, avec des mises à jour de plusieurs dépendances pour corriger des vulnérabilités potentielles. Des améliorations ont également été apportées au processus de déploiement, notamment avec l'intégration de GRIST pour la sauvegarde et la comparaison des états du site. Enfin, quelques ajustements de contenu ont été effectués.

### Évolutions fonctionnelles
- Correction de l'injection du nonce, améliorant la sécurité du site. [#7b7c350](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/7b7c350)
- Modification du terme "Omnicité" par "Crème de la crème" dans le contenu du site. [#8e31dcd](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/8e31dcd)
- Ajout d'informations concernant Claude. [#73ec211](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/73ec211)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité :
    - `postcss` vers la version 8.5.10 [#c0d44f3](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/c0d44f3)
    - `axios` vers la version 1.15.2 [#aaf27d8](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/aaf27d8)
    - `fast-xml-builder` vers la version 1.1.6 [#84b6990](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/84b6990)
    - `fast-xml-parser` vers la version 5.7.0 [#7a2458b](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/7a2458b)
    - `follow-redirects` vers la version 1.16.0 [#56c9d5d](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/56c9d5d)
- Intégration de GRIST pour la sauvegarde de l'empreinte du site. [#ed3b772](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/ed3b772)
- Recopie de la démo GRIST en production. [#bfa3732](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/bfa3732)
- Utilisation d'un snapshot GRIST. [#9e58f1e](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/9e58f1e)
- Comparaison des GRIST dans la CI. [#961298d](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/961298d)
- Déploiement rendu dépendant de la comparaison GRIST. [#8cdb6f5](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/8cdb6f5)
- Téléchargement de l'empreinte GRIST. [#52081c2](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/52081c2)
- Rendre le déploiement manuel. [#37f3a2c](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/37f3a2c)

### Autres changements
- Suppression d'un fichier inutile. [#881c8bc](https://github.com/betagouv/anssi-demain-specialiste-cyber/issues/881c8bc)
