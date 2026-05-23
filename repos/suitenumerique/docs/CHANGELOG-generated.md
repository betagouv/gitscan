## Changelog : docs (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité, la performance et l'expérience utilisateur. Des corrections de bugs ont été apportées pour améliorer la fiabilité de l'application, notamment en lien avec la collaboration, la gestion des documents et les intégrations SSO/OIDC. Des optimisations ont été réalisées pour améliorer la gestion des fichiers et l'intégration avec des services tiers comme Mistral. L'infrastructure a également été mise à jour pour supporter de nouvelles architectures et améliorer la sécurité.

### Évolutions fonctionnelles
- Ajout de la configuration de l'endpoint utilisateur OIDC via les paramètres [#24d58a1](https://github.com/suitenumerique/docs/commit/24d58a1)
- Prise en charge de la création de sous-documents à partir de fichiers [#cd75a17](https://github.com/suitenumerique/docs/commit/cd75a17)
- Support du déploiement sur PaaS, testé avec Scalingo [#c9cf3b6](https://github.com/suitenumerique/docs/commit/c9cf3b6)
- Intégration de la nouvelle fonctionnalité d'IA via le SDK Mistral, avec gestion de Langfuse [#b6efac3](https://github.com/suitenumerique/docs/commit/b6efac3) et [#33a9e99](https://github.com/suitenumerique/docs/commit/33a9e99)
- Amélioration de la gestion des documents lors des déplacements (suppression des accès et invitations lors des changements de portée) [#562ed0d](https://github.com/suitenumerique/docs/commit/562ed0d) et [#0a7aa58](https://github.com/suitenumerique/docs/commit/0a7aa58)
- Ajout d'un squelette de chargement pour le contenu, améliorant l'expérience utilisateur pendant le chargement des données [#a47c351](https://github.com/suitenumerique/docs/commit/a47c351)
- Mise à jour de la version de Docspec vers v3.0.0 avec adaptation de l'API de conversion [#2d2e326](https://github.com/suitenumerique/docs/commit/2d2e326)

### Évolutions techniques
- Migration de l'outil de construction de paquets de `pip` vers `uv` pour le backend et les actions CI/CD [#8fc13d7](https://github.com/suitenumerique/docs/commit/8fc13d7), [#1268bbe](https://github.com/suitenumerique/docs/commit/1268bbe), [#aea6fbe](https://github.com/suitenumerique/docs/commit/aea6fbe)
- Mise à jour de Next.js vers la version 16.2.6 (incluant des correctifs de sécurité) [#0501551](https://github.com/suitenumerique/docs/commit/0501551)
- Mise à jour de Axios vers la version 1.15.2 (incluant des correctifs de sécurité) [#85128c7](https://github.com/suitenumerique/docs/commit/85128c7)
- Mise à jour de lxml vers la version 6.1.0 (incluant des correctifs de sécurité) [#e747e03](https://github.com/suitenumerique/docs/commit/e747e03)
- Mise à jour de uuid vers la version 14 (incluant des correctifs de sécurité) [#c464715](https://github.com/suitenumerique/docs/commit/c464715)
- Utilisation de runners ARM64 pour la construction d'images pour l'architecture ARM64 [#c72336a](https://github.com/suitenumerique/docs/commit/c72336a)
- Ajout d'une étape Trivy pour l'analyse de vulnérabilités [#1a82b37](https://github.com/suitenumerique/docs/commit/1a82b37)
- Mise à jour de l'image Nginx vers la dernière version [#4fe508b](https://github.com/suitenumerique/docs/commit/4fe508b)
- Amélioration de la gestion des verrous lors de la création de documents [#a47c351](https://github.com/suitenumerique/docs/commit/a47c351)
- Refactorisation du module `core/utils.py` [#8f67b37](https://github.com/suitenumerique/docs/commit/8f67b37)
- Implémentation des headers `etag` et `last_modified` pour la récupération de contenu [#68f1600](https://github.com/suitenumerique/docs/commit/68f1600)

### Autres changements
- Correction de problèmes de flakiness dans les tests E2E [#c525694](https://github.com/suitenumerique/docs/commit/c525694)
- Suppression de commentaires inutiles dans le frontend [#0bfc697](https://github.com/suitenumerique/docs/commit/0bfc697)
- Suppression de code lié à une ancienne version de Cunningham [#48ba77b](https://github.com/suitenumerique/docs/commit/48ba77b)
- Mise à jour de Blocknote vers la version 0.51.1 [#41f76eb](https://github.com/suitenumerique/docs/commit/41f76eb)
- Dégradation de la version majeure de `@hocuspocus` [#9cde092](https://github.com/suitenumerique/docs/commit/9cde092)
- Correction d'une erreur dans les migrations Django [#abd03d1](https://github.com/suitenumerique/docs/commit/abd03d1)
- Mise à jour des chaînes de traduction [#4d68f39](https://github.com/suitenumerique/docs/commit/4d68f39)
- Suppression de la logique de suppression manuelle des accès depuis le hook de déplacement de document [#0a7aa58](https://github.com/suitenumerique/docs/commit/0a7aa58)
- Mise à jour des dépendances JavaScript [#18e9c3a](https://github.com/suitenumerique/docs/commit/18e9c3a) et [#9231730](https://github.com/suitenumerique/docs/commit/9231730)
- Fixe la configuration du réseau Lasuite en tant qu'externe [#fc68b71](https://github.com/suitenumerique/docs/commit/fc68b71)
- Correction de l'inclusion de modules avec uv_build [#0f14981](https://github.com/suitenumerique/docs/commit/0f14981)
- Maintien de la version de Node à 22 [#59499a8](https://github.com/suitenumerique/docs/commit/59499a8)
- Utilisation de uv dans les jobs de crowding [#5880493](https://github.com/suitenumerique/docs/commit/5880493)
- Épinglage des dépendances [#06eb49d](https://github.com/suitenumerique/docs/commit/06eb49d)
