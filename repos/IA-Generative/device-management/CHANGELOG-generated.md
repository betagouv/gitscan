## Changelog : device-management (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, le projet device-management a bénéficié d'une attention particulière à la sécurité, avec de nombreuses corrections de vulnérabilités et un audit de sécurité. Des améliorations ont également été apportées à la gestion des secrets, au déploiement et à la documentation, ainsi qu'à la gestion du catalogue d'extensions et des mises à jour.

### Évolutions fonctionnelles
- Amélioration de l'exposition de l'ID des plugins dans l'API `/catalog/api/plugins` pour une meilleure identification. [#4cf65d4](https://github.com/IA-Generative/device-management/commit/4cf65d4)
- Génération de fichiers XML pour les mises à jour GUpdate et JSON pour Mozilla, permettant une gestion multi-cible des mises à jour. [#cb68812](https://github.com/IA-Generative/device-management/commit/cb68812)
- Support de variables d'environnement supplémentaires pour la configuration de l'application : `API_BASE`, `RELAY_ASSISTANT_BASE_URL`, `COMPTE_RENDU_URL`, `COMU_URL`, `TELEMETRY_ENDPOINT`. [#f49adde](https://github.com/IA-Generative/device-management/commit/f49adde)
- Ajout d'une section "Comment fonctionnent les mises à jour" à la documentation. [#311c293](https://github.com/IA-Generative/device-management/commit/311c293)
- Possibilité d'utiliser un token de service pour la configuration des versions et l'upload des artefacts. [#ad6797d](https://github.com/IA-Generative/device-management/commit/ad6797d)

### Évolutions techniques
- Correction de plusieurs vulnérabilités de sécurité, notamment dans les dépendances (FastAPI, Starlette, pytest) et dans la configuration du serveur (désactivation de Filebrowser, suppression d'Adminer). [#2e383d7](https://github.com/IA-Generative/device-management/commit/2e383d7), [#635a223](https://github.com/IA-Generative/device-management/commit/635a223), [#d787f04](https://github.com/IA-Generative/device-management/commit/d787f04), [#8cb802d](https://github.com/IA-Generative/device-management/commit/8cb802d)
- Renforcement de la couche d'authentification suite à un audit de sécurité. [#e6a9cb2](https://github.com/IA-Generative/device-management/commit/e6a9cb2)
- Mise à jour de Nginx en version 1.29-alpine pour corriger une vulnérabilité OpenSSL. [#d787f04](https://github.com/IA-Generative/device-management/commit/d787f04)
- Amélioration de la gestion des secrets : normalisation de la gestion des secrets Kubernetes, suppression des clés secrètes du dépôt git, utilisation de fichiers `.env` et `secret-patch.yaml`. [#74941bf](https://github.com/IA-Generative/device-management/commit/74941bf), [#ed793b7](https://github.com/IA-Generative/device-management/commit/ed793b7), [#2b071c0](https://github.com/IA-Generative/device-management/commit/2b071c0)
- Refactorisation du code pour supprimer le relais `/llm` devenu inutile. [#30c105d](https://github.com/IA-Generative/device-management/commit/30c105d)
- Amélioration du healthcheck avec un timeout JWKS plus approprié. [#a335a1f](https://github.com/IA-Generative/device-management/commit/a335a1f)

### Autres changements
- Restructuration de la documentation par audience et sortie des artefacts internes du dépôt. [#000b4fa](https://github.com/IA-Generative/device-management/commit/000b4fa)
- Mise à jour des dépendances Python vers les dernières versions. [#c9f9719](https://github.com/IA-Generative/device-management/commit/c9f9719)
- Nettoyage du code. [#b9408f3](https://github.com/IA-Generative/device-management/commit/b9408f3)
- Ajout d'un fichier `.dockerignore` pour exclure les fichiers sensibles et inutiles du contexte de build Docker. [#c34fa31](https://github.com/IA-Generative/device-management/commit/c34fa31)
- Consolidation du runbook de déploiement pour Scaleway et DGX. [#945aeeb](https://github.com/IA-Generative/device-management/commit/945aeeb)
- Suppression de code mort. [#cf95cf6](https://github.com/IA-Generative/device-management/commit/cf95cf6)
