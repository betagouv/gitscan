## Changelog : infra-apps (30 derniers jours, au 03/08/2026)

### Résumé
Ce mois a été marqué par une montée en puissance significative de la plateforme **Iterion**, notamment via l'automatisation de sa montée en charge et l'intégration de nouveaux outils de recherche et de scraping. Nous avons également procédé à une simplification de l'infrastructure en décommissionnant des services obsolètes au profit de solutions plus modernes et intégrées, tout en renforçant la stabilité et la sécurité de nos outils de BI (Metabase) et de gestion de jetons (Token-Bureau).

### Évolutions fonctionnelles
- **Iterion** : Support de l'authentification OAuth pour les abonnements via des SDK tiers en production.
- **Iterion** : Intégration de nouvelles capacités de recherche web et de scraping (Firecrawl et SearXNG) pour enrichir les capacités de la plateforme.

### Évolutions techniques
- **Plateforme Iterion & Runners** :
    - Mise en place de l'autoscaling via **KEDA** pour ajuster dynamiquement le nombre de runners en fonction de la profondeur de la file d'attente.
    - Amélioration de l'isolation avec l'activation de pods "sandbox" dédiés par exécution en production (ADR-082).
    - Optimisation de la stabilité : les runners terminent désormais leurs tâches avant de s'arrêter et bénéficient de limites de mémoire augmentées (jusqu'à 8Gi) pour éviter les erreurs de type OOM (Out Of Memory).
    - Migration des services d'IA (Claude/OpenAI) vers l'utilisation de l'OAuth pour remplacer les clés API limitées.
    - Optimisation du cache de build (gestion du cycle de vie des buckets S3 et désactivation des caches NFS problématiques).
- **Buildkit Operator** :
    - Série de mises à jour majeures (v0.13.0 à v0.21.0) incluant l'implémentation de mécanismes de "keep-warm" adaptatifs et de configurations par défaut déclaratives.
    - Déclaration explicite des spécificités de stockage et de Load Balancer pour l'environnement OVH.
- **Metabase** :
    - Mise à jour globale vers la version **v0.63.2**.
    - Renforcement de la sécurité via la rotation des clés de signature pour l'intégration (embedding) et correction de la gestion des certificats.
    - Optimisation des ressources (CPU et stockage CNPG) suite à un incident de saturation des journaux de transaction (WAL).
- **Token-Bureau** :
    - Amélioration de la gestion des permissions avec l'application de règles spécifiques par dépôt et extension des droits pour la CI egapro ([#49](https://github.com/SocialGouv/infra-apps/pull/49)).
- **Consolidation de l'infrastructure** :
    - Décommissionnement du service `buildkit-service` (désormais géré par l'operator) et de `huginn` (migré vers Iterion).

### Autres changements
- **Documentation** : Ajout de précisions sur la nécessité de rafraîchir ArgoCD lors de modifications de charts partagés et sur la suppression des tokens de type "bearer" pour le buildkit-operator.
- **Maintenance** : Nettoyage des sous-charts Helm et suppression de configurations obsolètes (Metabase AI, MB_ENABLE_EMBEDDING).
