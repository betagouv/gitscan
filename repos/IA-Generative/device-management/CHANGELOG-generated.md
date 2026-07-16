## Changelog : device-management (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes de gestion de la configuration, de sécurité et d'observabilité. L'ajout de fonctionnalités de gestion des feature flags, d'un proxy LLM et d'une interface d'administration plus complète permettent une plus grande flexibilité et un contrôle accru sur le système. Des corrections de sécurité et des optimisations de performance ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'une interface utilisateur pour la gestion des feature flags avec des états (transparent, activé, désactivé) [#62c09c4](https://github.com/IA-Generative/device-management/pull/62c09c4).
- Implémentation d'un proxy LLM compatible OpenAI avec la possibilité de surcharger l'endpoint LLM [#27](https://github.com/IA-Generative/device-management/pull/27).
- Ajout d'un tableau de bord affichant l'adoption du système par les appareils et les utilisateurs [#21](https://github.com/IA-Generative/device-management/pull/21).
- Nouvelle page de débogage dans l'interface d'administration permettant l'édition en ligne de la configuration, le diff, le reset, le rechargement et la visualisation de l'état de santé du système [#32](https://github.com/IA-Generative/device-management/pull/32).
- Possibilité de modifier les credentials Keycloak et du relais depuis l'interface d'administration [#29](https://github.com/IA-Generative/device-management/pull/29).
- Ajout d'un histogramme du trafic LLM (chat vs embeddings) sur le dashboard [#13](https://github.com/IA-Generative/device-management/pull/13).
- Affichage de la version du DM et du modèle d'embedding sur le tableau de bord [#12](https://github.com/IA-Generative/device-management/pull/12).
- Redirections automatiques de la racine vers le catalogue et de `/admin` vers `/admin/` [#21](https://github.com/IA-Generative/device-management/pull/21).
- Amélioration du journal d'audit avec des filtres en direct, une recherche détaillée et un défilement infini [#30](https://github.com/IA-Generative/device-management/pull/30).

### Évolutions techniques
- Mise en place d'un chart Helm pour le déploiement du système [#12](https://github.com/IA-Generative/device-management/pull/12).
- Refonte de la gestion de la configuration avec un module runtime_config pour la synchronisation, la résolution et le rechargement de la configuration [#19](https://github.com/IA-Generative/device-management/pull/19).
- Implémentation du chiffrement réversible Fernet pour les secrets de surcharge runtime [#17](https://github.com/IA-Generative/device-management/pull/17).
- Amélioration de la sécurité avec une image Docker non-root et des vérifications de sécurité renforcées [#27](https://github.com/IA-Generative/device-management/pull/27).
- Correction de problèmes de sécurité liés à la validation des chemins de fichiers [#17](https://github.com/IA-Generative/device-management/pull/17).
- Utilisation de `pg_advisory_lock` pour verrouiller les opérations de schéma de base de données [#20](https://github.com/IA-Generative/device-management/pull/20).
- Amélioration de la robustesse et de la résilience du système avec un reaper automatique des pods obsolètes et un heartbeat résilient [#29](https://github.com/IA-Generative/device-management/pull/29).
- Passage à Bandit comme source unique de SAST et amélioration de la qualité du code avec Ruff [#17](https://github.com/IA-Generative/device-management/pull/17).

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements d'architecture [#28](https://github.com/IA-Generative/device-management/pull/28).
- Corrections de bugs mineurs et améliorations de la stabilité.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour des dépendances.
