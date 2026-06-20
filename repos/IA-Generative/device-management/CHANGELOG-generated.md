## Changelog : device-management (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité, la stabilisation du déploiement et l'amélioration de la gestion des extensions et des mises à jour. Des corrections de vulnérabilités critiques ont été implémentées, ainsi que des améliorations de la documentation et de la gestion des secrets. Des optimisations ont également été apportées à l'infrastructure de déploiement et à la gestion des configurations.

### Évolutions fonctionnelles
- **Gestion du catalogue:** L'ID du plugin est maintenant exposé dans l'API publique `/catalog/api/plugins` au lieu du slug, améliorant l'identification des extensions. [#4cf65d4](https://github.com/IA-Generative/device-management/commit/4cf65d4)
- **Mises à jour:** Génération de fichiers `gupdate XML` et `Mozilla JSON` multi-cible pour faciliter la distribution des mises à jour. [#cb68812](https://github.com/IA-Generative/device-management/commit/cb68812)
- **Configuration:** Support des variables d'environnement `API_BASE`, `RELAY_ASSISTANT_BASE_URL`, `COMPTE_RENDU_URL`, `COMU_URL` et `TELEMETRY_ENDPOINT` pour une configuration plus flexible. [#f49adde](https://github.com/IA-Generative/device-management/commit/f49adde)
- **Authentification:** Amélioration de la gestion du `redirect_uri` Keycloak via les variables d'environnement `KEYCLOAK_REDIRECT_URI` et `ALLOWED`. [#f4012b9](https://github.com/IA-Generative/device-management/commit/f4012b9)

### Évolutions techniques
- **Sécurité:** Correction de plusieurs vulnérabilités de sécurité critiques, incluant des failles dans `starlette`, `pytest` et des problèmes d'authentification et de révocation de jetons.  Des audits de sécurité ont été réalisés et des mesures correctives ont été implémentées. [#2e383d7](https://github.com/IA-Generative/device-management/commit/2e383d7), [#635a223](https://github.com/IA-Generative/device-management/commit/635a223), [#c66be0d](https://github.com/IA-Generative/device-management/commit/c66be0d), [#adb4658](https://github.com/IA-Generative/device-management/commit/adb4658), [#e6a9cb2](https://github.com/IA-Generative/device-management/commit/e6a9cb2)
- **Déploiement:** Mise à jour de l'image Docker vers la version 0.6.0 avec configuration des variables d'environnement. [#1f324de](https://github.com/IA-Generative/device-management/commit/1f324de)
- **Infrastructure:** Suppression de services obsolètes ou non sécurisés comme Adminer et Filebrowser. [#8cb802d](https://github.com/IA-Generative/device-management/commit/8cb802d), [#7b8eea2](https://github.com/IA-Generative/device-management/commit/7b8eea2)
- **Gestion des secrets:** Normalisation de la gestion des secrets Kubernetes, en retirant les secrets du code source et en utilisant des overlays spécifiques à chaque environnement. [#950430a](https://github.com/IA-Generative/device-management/commit/950430a), [#ed793b7](https://github.com/IA-Generative/device-management/commit/ed793b7), [#2b071c0](https://github.com/IA-Generative/device-management/commit/2b071c0)
- **Base de données:** Ajout de l'extension `extension_id` et `gecko_id` à la base de données pour améliorer la gestion des extensions. [#3c8edb9](https://github.com/IA-Generative/device-management/commit/3c8edb9)

### Autres changements
- **Documentation:** Ajout d'une section "Comment fonctionnent les mises à jour" au fichier README.md. [#311c293](https://github.com/IA-Generative/device-management/commit/311c293)
- **Documentation:** Restructuration de la documentation par audience et suppression des artefacts internes du dépôt. [#000b4fa](https://github.com/IA-Generative/device-management/commit/000b4fa)
- **Documentation:** Consolidation du runbook de déploiement pour Scaleway et DGX. [#945aeeb](https://github.com/IA-Generative/device-management/commit/945aeeb)
- **Nettoyage du code:** Suppression de code mort et normalisation du code. [#b9408f3](https://github.com/IA-Generative/device-management/commit/b9408f3), [#cf95cf6](https://github.com/IA-Generative/device-management/commit/cf95cf6)
- **Build:** Ajout d'un fichier `.dockerignore` pour exclure les fichiers sensibles et inutiles du contexte de build Docker. [#c34fa31](https://github.com/IA-Generative/device-management/commit/c34fa31)
- **Divers:** Mise à jour des dépendances Python vers les dernières versions. [#c9f9719](https://github.com/IA-Generative/device-management/commit/c9f9719)
