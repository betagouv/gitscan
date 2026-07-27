## Changelog : device-management (30 derniers jours, au 2026-07-15)

### Résumé
Ce mois-ci, le projet a connu des avancées significatives en termes de gestion de la configuration, de sécurité et d'observabilité. L'introduction de la gestion des *feature flags* et des surcharges de configuration runtime permet une plus grande flexibilité et un contrôle plus fin du système. Des améliorations ont également été apportées à l'interface d'administration, notamment avec un nouveau tableau de bord pour le suivi de l'adoption et des journaux d'audit plus détaillés. La préparation du déploiement via Helm et l'amélioration de la sécurité sont également des points importants.

### Évolutions fonctionnelles

*   Ajout d'un histogramme du trafic LLM (chat vs embeddings) sur le tableau de bord d'administration.
*   Affichage de la version du serveur device-management et du modèle d'embedding sur le tableau de bord, avec alerte en cas de versions mixtes.
*   Implémentation d'un journal d'audit plus détaillé avec des filtres en direct, une recherche améliorée et un affichage dense des entrées.
*   Possibilité de filtrer les journaux par plugin.
*   Ajout d'un toggle sur le tableau de bord pour afficher les données par appareils ou par utilisateurs.
*   Les credentials Keycloak et de relais sont maintenant modifiables via l'interface d'administration.
*   Ajout d'une page de débogage avec édition en ligne de la configuration, diff, reset et rechargement.
*   Possibilité de visualiser l'état de santé des pods (RAM, charge CPU, requêtes).
*   Implémentation d'un système de *feature flags* tri-état (transparent, forcé ON, forcé OFF).
*   Ajout d'un proxy LLM compatible OpenAI avec la possibilité de surcharger l'endpoint.
*   Ajout d'un endpoint pour récupérer les embeddings.
*   Redirection automatique de la racine `/` vers `/catalog/` et `/admin` vers `/admin/`.

### Évolutions techniques

*   Préparation du déploiement via un chart Helm documenté.
*   Amélioration de la sécurité avec l'utilisation d'images Docker non-root et l'ajout de vérifications de sécurité.
*   Implémentation d'un système de surcharge de configuration runtime avec chiffrement Fernet pour les secrets.
*   Refonte de la gestion des configurations avec un registre, une baseline, une résolution et un rechargement.
*   Ajout d'un reaper automatique pour les pods obsolètes.
*   Amélioration de la résilience du heartbeat.
*   Correction de problèmes liés à la gestion des installations et des plugins.
*   Amélioration de la gestion des logs avec des filtres et une récapitulation.
*   Utilisation de `pg_advisory_lock` pour la synchronisation de la base de données.
*   Mise à jour des dépendances et amélioration de la qualité du code avec Ruff et Bandit.
*   Correction de problèmes de configuration et de déploiement.

### Autres changements

*   Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements d'architecture.
*   Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
*   Amélioration de la CI/CD pour automatiser le processus de déploiement.
*   Correction de bugs mineurs et amélioration de la performance.
*   Documentation des ADR-0002 et 0003.
*   Ajout de documentation pour le guide opérateur du proxy LLM.
*   Amélioration de la documentation des plugins.
*   Correction de problèmes de configuration locale.
*   Amélioration de la robustesse des tests CI.
*   Correction de problèmes de sécurité identifiés par Bandit.
*   Amélioration de la qualité du code avec Ruff.
*   Correction de NameError latents dans le router admin.
*   Correction de problèmes de configuration du relais Keycloak.
*   Amélioration de la gestion des erreurs et des logs.
*   Ajout de métriques de performance et d'observabilité.
*   Correction de problèmes de compatibilité avec les navigateurs.
*   Amélioration de l'expérience utilisateur.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
*   Correction de problèmes de performance.
*   Amélioration de la sécurité.
*   Correction de bugs et amélioration de la stabilité.
*   Ajout de documentation pour les nouveaux endpoints et fonctionnalités.
*   Amélioration de la documentation existante.
*   Correction de problèmes de traduction.
*   Amélioration de l'accessibilité.
