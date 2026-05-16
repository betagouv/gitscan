## Changelog : plusfraisautravail (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, le projet plusfraisautravail a connu des améliorations significatives en termes d'infrastructure et de déploiement, avec une migration vers OpenTofu et Scaleway. De nouvelles fonctionnalités liées aux alertes (vigilances météo et Ecowatt) ont été ajoutées, ainsi que des améliorations de l'interface utilisateur pour la visualisation de ces alertes. Des optimisations et des corrections de code ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des vigilances météo et des alertes Ecowatt (électricité) via l'API. [#2b77f7e](https://github.com/incubateur-ademe/plusfraisautravail/pulls/2b77f7e)
- Amélioration de l'interface utilisateur du widget d'alerte :
    - Ajout d'un lien vers la source de l'alerte pour chaque ligne. [#b81bd86](https://github.com/incubateur-ademe/plusfraisautravail/pulls/b81bd86)
    - Ajout d'infobulles DSFR avec une répartition quotidienne pour chaque type d'alerte. [#f6d5919](https://github.com/incubateur-ademe/plusfraisautravail/pulls/f6d5919)
    - Vue "phenomenon-list" pour l'affichage des alertes. [#8c73f08](https://github.com/incubateur-ademe/plusfraisautravail/pulls/8c73f08)
    - Mode test/démo pour le widget d'alerte avec des scénarios nommés. [#fe2a41b](https://github.com/incubateur-ademe/plusfraisautravail/pulls/fe2a41b)
- Traduction de l'application. [#2175e29](https://github.com/incubateur-ademe/plusfraisautravail/pulls/2175e29)

### Évolutions techniques
- Migration de l'infrastructure de déploiement vers OpenTofu et Scaleway. [#879a871](https://github.com/incubateur-ademe/plusfraisautravail/pulls/879a871)
- Mise en place de workflows de déploiement basés sur les environnements GitHub. [#1fbec38](https://github.com/incubateur-ademe/plusfraisautravail/pulls/1fbec38)
- Utilisation de `website_endpoint` (bucket-prefixed) pour la configuration CORS et les URLs. [#d2a3742](https://github.com/incubateur-ademe/plusfraisautravail/pulls/d2a3742)
- Correction de l'encodage des booléens en JSON dans `bootstrap-environments`. [#3b3bd0d](https://github.com/incubateur-ademe/plusfraisautravail/pulls/3b3bd0d)
- Suppression du préfixe de région du `container_id` Scaleway dans le workflow de déploiement de l'API. [#fb8949d](https://github.com/incubateur-ademe/plusfraisautravail/pulls/fb8949d)
- Ajout de la variable d'environnement `CORS_ORIGINS` pour la configuration CORS de l'API. [#67d1965](https://github.com/incubateur-ademe/plusfraisautravail/pulls/67d1965)
- Refactoring du code et application du formatage avec Ruff. [#329b07b](https://github.com/incubateur-ademe/plusfraisautravail/pulls/329b07b)
- Mise en place de pre-commit hooks pour garantir la qualité du code. [#ede6487](https://github.com/incubateur-ademe/plusfraisautravail/pulls/ede6487)
- Correction d'un problème de déploiement. [#18d778d](https://github.com/incubateur-ademe/plusfraisautravail/pulls/18d778d)
- Mise à jour de l'espace de noms pour éviter les conflits. [#fc661da](https://github.com/incubateur-ademe/plusfraisautravail/pulls/fc661da)

### Autres changements
- Ajout d'un workflow Tofu pour l'application sur l'environnement `tofu-apply`. [#ee49441](https://github.com/incubateur-ademe/plusfraisautravail/pulls/ee49441)
- Suppression du cache des dépendances Vite du `.gitignore`. [#74fe25e](https://github.com/incubateur-ademe/plusfraisautravail/pulls/74fe25e)
- Travaux préparatoires pour l'ajout d'un autodiag, la migration vers un monorepo et l'utilisation de Terraform. [#25dd957](https://github.com/incubateur-ademe/plusfraisautravail/pulls/25dd957)
- Amélioration de la structure du code et de la documentation. [#ea159b9](https://github.com/incubateur-ademe/plusfraisautravail/pulls/ea159b9)
