## Changelog : infra-apps (30 derniers jours, au 11/10/2026)

### Résumé
Ce mois a été marqué par une transition majeure de l'infrastructure de stockage, passant de MinIO à SeaweedFS, ainsi que par une montée en puissance de la plateforme Iterion avec l'intégration de nouveaux modèles d'IA (Opus 5.5, GPT-6). Les capacités de calcul (runners CI) ont également été stabilisées et optimisées pour mieux gérer les pics de charge.

### Évolutions fonctionnelles
- **Nouveaux modèles IA** : Déploiement des runtimes pour Opus 5.5 et GPT-6 sur Iterion.
- **Interface Studio** : Refonte de l'accès au Studio, désormais disponible sous le chemin `/studio`.
- **Gestion d'infrastructure** : Mise à disposition d'un outil CLI signé pour le redémarrage du plan de contrôle Kubernetes sur OVH.

### Évolutions techniques
- **Stockage objet** : Migration complète du stockage de MinIO vers SeaweedFS, incluant la synchronisation des données et le retrait définitif de MinIO de la production.
- **Plateforme Iterion** :
    - Déploiement de la première "sovereign pool" (v3.249.0).
    - Amélioration du routage des modèles (Claude, honorabilite pool) et sécurisation des accès via des références de clés pour les JWT et les URIs MongoDB.
    - Amélioration de la stabilité via le "digest pinning" des serveurs et des runners pour garantir l'immuabilité des déploiements [#2313].
- **CI/CD (ARC Runners)** :
    - Migration des runners vers un nodepool dédié pour une meilleure gestion des ressources et des pics de demande.
    - Amélioration de la robustesse des runners : gestion des limites `inotify` [#70, #55], attente de l'API `dind` au démarrage [#56], et alertes en cas d'interruption de service [#54].
    - Optimisation de la gestion du cache (Go, Node) et sécurisation des conteneurs privilégiés par digest [#71, #67].
- **Sécurité** :
    - Déploiement de ClamAV sur l'environnement de production OVH pour l'application Domifa.
    - Ajustement des politiques réseau (NetworkPolicies) pour ClamAV afin de permettre les flux intra-namespace.

### Autres changements
- **Documentation** : Mise à jour des notes techniques concernant l'utilisation de Corepack et le couplage entre les images de runners et les digests des serveurs.
- **Nettoyage** : Retrait des jobs de migration SeaweedFS une fois la synchronisation validée.
