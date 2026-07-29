## Changelog : device-management (30 derniers jours, au 15 juillet 2026)

### Résumé
Les dernières mises à jour de device-management se concentrent sur l'amélioration de la gestion des configurations, l'ajout de fonctionnalités de proxy LLM, l'amélioration de l'observabilité et de la sécurité, ainsi que la préparation du déploiement cloud-native. Plusieurs correctifs ont été apportés pour améliorer la stabilité et la fiabilité du système.

### Évolutions fonctionnelles
- Ajout d'un proxy LLM compatible OpenAI via l'endpoint `/llm/v1` avec possibilité de surcharger l'endpoint LLM. [#27](https://github.com/IA-Generative/device-management/pull/27)
- Implémentation de la gestion des feature flags avec un état tri-valeur (transparent, activé, désactivé). [#62c09c4](https://github.com/IA-Generative/device-management/commit/62c09c4)
- Ajout d'un tableau de bord avec des histogrammes du trafic LLM (chat vs embeddings). [#d5705bb](https://github.com/IA-Generative/device-management/commit/d5705bb)
- Affichage de la version du device-management et du modèle d'embedding sur le tableau de bord. [#d3a2fd3](https://github.com/IA-Generative/device-management/commit/d3a2fd3)
- Amélioration du journal d'audit avec des filtres en direct, une recherche détaillée et un défilement infini. [#a8f1e0a](https://github.com/IA-Generative/device-management/commit/a8f1e0a)
- Ajout de la possibilité de basculer entre l'affichage des appareils et des utilisateurs sur le widget d'adoption du tableau de bord. [#b759bdb](https://github.com/IA-Generative/device-management/commit/b759bdb)
- Redirections automatiques de la racine `/` vers `/catalog/` et de `/admin` vers `/admin/`. [#b673c7b](https://github.com/IA-Generative/device-management/commit/b673c7b)
- Possibilité d'éditer les informations d'identification (Keycloak, relais) et d'importer des overrides de configuration au démarrage. [#5e60baa](https://github.com/IA-Generative/device-management/commit/5e60baa)
- Ajout de légendes et d'infobulles sur les statuts de configuration dans l'interface d'administration. [#fe7b2ea](https://github.com/IA-Generative/device-management/commit/fe7b2ea)

### Évolutions techniques
- Mise en place d'un chart Helm pour faciliter le déploiement. [#12](https://github.com/IA-Generative/device-management/pull/12)
- Préparation pour un déploiement cloud-native avec S3, observabilité, résilience et arrêt gracieux. [#fc3ab55](https://github.com/IA-Generative/device-management/commit/fc3ab55)
- Utilisation d'images Docker non-root pour renforcer la sécurité. [#5f4cd9e](https://github.com/IA-Generative/device-management/commit/5f4cd9e)
- Amélioration de la gestion des logs avec filtrage des sondes et des accès Nginx. [#c176e41](https://github.com/IA-Generative/device-management/commit/c176e41)
- Implémentation d'un verrou consultatif PostgreSQL pour la migration du schéma. [#cba003d](https://github.com/IA-Generative/device-management/commit/cba003d)
- Correction de la persistance de l'identifiant du plugin dans les logs d'audit. [#7cc5ba4](https://github.com/IA-Generative/device-management/commit/7cc5ba4)
- Correction d'un problème avec les installations fantômes sans version. [#970c0ca](https://github.com/IA-Generative/device-management/commit/970c0ca)
- Correction d'un problème de propagation des flags d'administration. [#9a72394](https://github.com/IA-Generative/device-management/commit/9a72394)
- Amélioration de la gestion des identités pour la télémétrie avec l'utilisation de CUID. [#a478617](https://github.com/IA-Generative/device-management/commit/a478617)

### Autres changements
- Mise à jour de la documentation avec les nouvelles fonctionnalités et les changements d'architecture.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Plusieurs mises à jour de version (0.9.3 à 0.9.12).
- Amélioration du linting du code. [#5e60baa](https://github.com/IA-Generative/device-management/commit/5e60baa)
