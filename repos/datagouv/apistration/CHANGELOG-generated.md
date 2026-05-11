## Changelog : apistration (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la robustesse et de la maintenabilité de la plateforme, avec un accent particulier sur la gestion des erreurs, la surveillance et la documentation. De nouvelles fonctionnalités ont été ajoutées, notamment un tableau de bord amélioré pour les fournisseurs, une newsletter de changelog et la possibilité d'exporter des données en CSV. Des améliorations ont également été apportées aux SDK Ruby pour faciliter l'intégration avec l'API.

### Évolutions fonctionnelles
- Ajout d'une newsletter hebdomadaire récapitulant les changements récents pour les abonnés. [#95](https://github.com/datagouv/apistration/pull/95)
- Amélioration du tableau de bord des fournisseurs avec des filtres de plage de dates et la possibilité d'exporter les données au format CSV. [#105](https://github.com/datagouv/apistration/pull/105), [#109](https://github.com/datagouv/apistration/pull/109)
- Ajout d'une page "Nouveautés" accessible depuis les deux sous-domaines de l'API. [#92](https://github.com/datagouv/apistration/pull/92)
- Possibilité de déléguer l'accès à l'API via des tokens d'éditeur. [#31](https://github.com/datagouv/apistration/pull/31)
- Amélioration de la gestion des erreurs et ajout d'un registre centralisé des erreurs. [#48](https://github.com/datagouv/apistration/pull/48)
- Ajout d'une sonde de monitoring pour DataSubvention. [#43](https://github.com/datagouv/apistration/pull/43)
- Correction d'un bug empêchant l'affichage correct des informations de civilité pour certains cas. [#34](https://github.com/datagouv/apistration/pull/34)
- Ajout de la possibilité de spécifier l'année de campagne pour l'API CNOUS des bourses étudiantes. [#69](https://github.com/datagouv/apistration/pull/69)

### Évolutions techniques
- Refactorisation de la gestion des erreurs avec un nouveau registre et une meilleure propagation des exceptions. [#48](https://github.com/datagouv/apistration/pull/48)
- Migration de la gestion des fichiers MJML vers MRML (Rust) pour améliorer les performances. [#102](https://github.com/datagouv/apistration/pull/102)
- Amélioration de la gestion des descripteurs de fichiers pour éviter les erreurs EBADF sous Puma. [#27](https://github.com/datagouv/apistration/pull/27)
- Refactorisation du code pour utiliser des configurations centralisées et memoïsées. [#27](https://github.com/datagouv/apistration/pull/27)
- Ajout de tests d'acceptation pour le système d'expansion de fichiers. [#88](https://github.com/datagouv/apistration/pull/88)
- Mise en place d'un workflow CI/CD pour les SDK Ruby. [#30](https://github.com/datagouv/apistration/pull/30)
- Ajout de SDK Ruby officiels pour l'API Entreprise et l'API Particulier. [#30](https://github.com/datagouv/apistration/pull/30)
- Amélioration de la gestion des dépendances et ajout de cooldowns pour les mises à jour automatiques. [#29](https://github.com/datagouv/apistration/pull/29)

### Autres changements
- Documentation améliorée pour l'utilisation des SDK Ruby et la gestion des erreurs.
- Ajout d'un fichier CONTRIBUTING.md pour encourager les contributions externes. [#35](https://github.com/datagouv/apistration/pull/35)
- Mise à jour des dépendances et des outils de développement.
- Amélioration de la configuration et de l'environnement de développement local avec l'utilisation de worktrees et de dotenv. [#61](https://github.com/datagouv/apistration/pull/61)
- Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
- Correction de bugs mineurs et améliorations de la performance.
