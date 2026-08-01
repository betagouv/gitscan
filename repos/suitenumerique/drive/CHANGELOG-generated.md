## Changelog : drive (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des quotas de stockage, avec l'introduction d'un indicateur de stockage et de nouvelles options de configuration. L'expérience de partage de fichiers est également améliorée, notamment avec la possibilité d'importer des contacts à partir d'un fichier. Des corrections de bugs et des optimisations de performance ont été apportées à l'ensemble du système.

### Évolutions fonctionnelles
- Ajout d'un indicateur de stockage (storage gauge) pour visualiser l'utilisation de l'espace disque. [#d3d9dff](https://github.com/suitenumerique/drive/commit/d3d9dff)
- Possibilité de partager des fichiers avec des contacts importés à partir d'un fichier. [#ab8e0eb](https://github.com/suitenumerique/drive/commit/ab8e0eb)
- Amélioration de l'expérience de partage avec la mise à jour de l'interface utilisateur (ui-kit 0.28). [#f239b58](https://github.com/suitenumerique/drive/commit/f239b58)
- Ajout d'un bouton pour accéder au widget de messages depuis le menu d'aide. [#9120c81](https://github.com/suitenumerique/drive/commit/9120c81)
- Affichage de messages spécifiques concernant les quotas de stockage en cas d'actions rejetées. [#0274332](https://github.com/suitenumerique/drive/commit/0274332)
- Ajout d'informations sur le quota utilisateur dans l'API des droits (entitlements). [#d9cfb4d](https://github.com/suitenumerique/drive/commit/d9cfb4d)

### Évolutions techniques
- Refactorisation du service de synchronisation des accès aux descendants. [#22c7eac](https://github.com/suitenumerique/drive/commit/22c7eac)
- Déplacement de l'API des favoris vers `/items/favorites/`. [#9b1bc4b](https://github.com/suitenumerique/drive/commit/9b1bc4b)
- Mise à jour de plusieurs dépendances : Django, pillow, next, vite, turbo, idna. [#ab2855a](https://github.com/suitenumerique/drive/commit/ab2855a), [#d2c1e47](https://github.com/suitenumerique/drive/commit/d2c1e47), [#756203e](https://github.com/suitenumerique/drive/commit/756203e), [#20e5d6f](https://github.com/suitenumerique/drive/commit/20e5d6f)
- Amélioration de la sécurité du Dockerfile. [#6ff79c6](https://github.com/suitenumerique/drive/commit/6ff79c6)
- Mise à jour de l'image Collabora et adaptation au nouveau contrat d'exécution. [#bd6f6b8](https://github.com/suitenumerique/drive/commit/bd6f6b8)
- Ajout d'un backend local pour la gestion des droits avec des limites de stockage. [#0f7ee3a](https://github.com/suitenumerique/drive/commit/0f7ee3a)
- Mise à jour de ui-kit vers les versions 0.27.0 et 0.28. [#5ed2639](https://github.com/suitenumerique/drive/commit/5ed2639), [#41e796b](https://github.com/suitenumerique/drive/commit/41e796b)
- Correction de bugs liés à la suppression d'éléments et au calcul du stockage. [#6c61275](https://github.com/suitenumerique/drive/commit/6c61275), [#e5f22ea](https://github.com/suitenumerique/drive/commit/e5f22ea)

### Autres changements
- Correction de la documentation de l'endpoint de la corbeille. [#d4a8c45](https://github.com/suitenumerique/drive/commit/d4a8c45)
- Correction de fautes d'orthographe concernant les codes de dépassement de quota. [#1d14ef0](https://github.com/suitenumerique/drive/commit/1d14ef0), [#1a7fcd4](https://github.com/suitenumerique/drive/commit/1a7fcd4)
- Mise à jour de la version de release à 0.20.0. [#1776a71](https://github.com/suitenumerique/drive/commit/1776a71)
- Contrainte de version de joserfc >=1.6.8 pour corriger une vulnérabilité CVE-2026-49852. [#25e693b](https://github.com/suitenumerique/drive/commit/25e693b)
