## Changelog : device-management (30 derniers jours, au 28 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité, l'observabilité et l'amélioration de la gestion des déploiements. Des correctifs de sécurité importants ont été implémentés suite à un audit, et l'observabilité a été renforcée avec l'intégration de Tempo et Grafana. Des améliorations ont également été apportées à la gestion des secrets et à la configuration des déploiements Kubernetes.

### Évolutions fonctionnelles
- Amélioration de l'exposition de l'ID des plugins dans l'API `/catalog/api/plugins` pour remplacer l'utilisation des slugs. [#4cf65d4](https://github.com/IA-Generative/device-management/commit/4cf65d4)
- Ajout de la génération de fichiers XML pour les mises à jour (gupdate) et JSON pour Mozilla, permettant une gestion multi-cible des versions. [#cb68812](https://github.com/IA-Generative/device-management/commit/cb68812)
- Possibilité de configurer l'utilisation d'un token de service pour l'authentification. [#ad6797d](https://github.com/IA-Generative/device-management/commit/ad6797d)
- Intégration de Grafana avec SSO Keycloak pour une meilleure visualisation des données. [#41a2e8c](https://github.com/IA-Generative/device-management/commit/41a2e8c)
- Mise en place d'un système d'observabilité auto-hébergé avec Tempo et Grafana. [#c4ccf28](https://github.com/IA-Generative/device-management/commit/c4ccf28)

### Évolutions techniques
- Renforcement de la sécurité avec des correctifs suite à un audit de sécurité (Klaerenn). [#af8e3f7](https://github.com/IA-Generative/device-management/commit/af8e3f7), [#c66be0d](https://github.com/IA-Generative/device-management/commit/c66be0d), [#adb4658](https://github.com/IA-Generative/device-management/commit/adb4658), [#e6a9cb2](https://github.com/IA-Generative/device-management/commit/e6a9cb2)
- Durcissement de la validation des chemins de fichiers pour prévenir les vulnérabilités. [#0d07f9f](https://github.com/IA-Generative/device-management/commit/0d07f9f)
- Mise à jour de l'image Nginx pour corriger une vulnérabilité OpenSSL. [#d787f04](https://github.com/IA-Generative/device-management/commit/d787f04)
- Mise à jour des dépendances FastAPI et Starlette pour corriger des CVE. [#2e383d7](https://github.com/IA-Generative/device-management/commit/2e383d7)
- Correction d'un problème de signature de `TemplateResponse` pour la compatibilité avec Starlette >= 1.2. [#ccee26c](https://github.com/IA-Generative/device-management/commit/ccee26c)
- Amélioration de la gestion des secrets dans Kubernetes, avec une normalisation et une meilleure séparation des environnements. [#74941bf](https://github.com/IA-Generative/device-management/commit/74941bf), [#ed793b7](https://github.com/IA-Generative/device-management/commit/ed793b7), [#454de6d](https://github.com/IA-Generative/device-management/commit/454de6d)
- Suppression de composants obsolètes ou non sécurisés (Adminer, ingress Filebrowser). [#8cb802d](https://github.com/IA-Generative/device-management/commit/8cb802d), [#7b8eea2](https://github.com/IA-Generative/device-management/commit/7b8eea2)

### Autres changements
- Amélioration de la documentation, notamment la restructuration pour différentes audiences et l'ajout d'un plan de mise à jour. [#000b4fa](https://github.com/IA-Generative/device-management/commit/000b4fa), [#311c293](https://github.com/IA-Generative/device-management/commit/311c293), [#945aeeb](https://github.com/IA-Generative/device-management/commit/945aeeb)
- Ajout d'un script pour valider les clés API Scaleway. [#fe9beb6](https://github.com/IA-Generative/device-management/commit/fe9beb6)
- Suppression de fichiers de sécurité sensibles du dépôt. [#3c34791](https://github.com/IA-Generative/device-management/commit/3c34791)
- Mise à jour du `.gitignore` pour améliorer la sécurité et la propreté du dépôt. [#963d40e](https://github.com/IA-Generative/device-management/commit/963d40e)
- Correction de problèmes de timeout pour la récupération des JWKS. [#454de6d](https://github.com/IA-Generative/device-management/commit/454de6d)
