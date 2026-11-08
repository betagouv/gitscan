## Changelog : infra-apps (30 derniers jours, au 6 novembre 2026)

### Résumé
Ce mois a été marqué par une phase de transition majeure de l'infrastructure (projet "Matryoshka") et par une série de mises à jour importantes de la plateforme Iterion (versions v3.2xx). Ces évolutions visent à renforcer la stabilité du système, à améliorer l'expérience utilisateur dans le Studio et à intégrer de nouveaux modèles d'intelligence artificielle performants.

### Évolutions fonctionnelles
- **Améliorations du Studio** : Ajout du rendu Markdown pour les livrables, mise en place d'adresses de partage via des liens spécifiques et amélioration de l'accessibilité (contrastes et focus visuels) [[#2622](https://github.com/SocialGouv/infra-apps/issues/2622), [#2638](https://github.com/SocialGouv/infra-apps/issues/2638)].
- **Évolutions de "Claw"** : Support des sorties structurées compatibles avec OpenAI [[#2664](https://github.com/SocialGouv/infra-apps/issues/2664)], amélioration de l'interface de révision [[#2705](https://github.com/SocialGouv/infra-apps/issues/2705)] et mise en place de mécanismes de récupération automatique en cas d'erreur [[#2710](https://github.com/SocialGouv/infra-apps/issues/2710)].
- **Automatisation GitLab** : Déploiement d'un système de bootstrap via OAuth permettant la création automatique de "project bots" pour chaque dépôt.
- **Gestion des flux** : Possibilité de choisir la posture de "merge-gate" directement depuis le Studio [[#2479](https://github.com/SocialGouv/infra-apps/issues/2479)].

### Évolutions techniques
- **Migration d'infrastructure (Matryoshka)** : Exécution de la transition vers la nouvelle architecture, incluant le gel de l'environnement de production OVH, la gestion des alias d'hôtes publics et la suppression des anciens jeux de déploiement (ApplicationSets).
- **Intelligence Artificielle** : 
    - Pilotage du modèle `deepseek-v4.1-flash` sur le pool "honorabilite".
    - Mise à jour des catalogues de modèles (GLM-5.3) et optimisation de la résolution des passerelles (gateways).
- **Résilience et Haute Disponibilité** :
    - Renforcement de la haute disponibilité pour les bases de données et services critiques (MongoDB, NATS et Valkey) avec des règles d'anti-affinité et des budgets de perturbation.
    - Optimisation du stockage SeaweedFS avec un paramétrage précis des slots de serveurs de volumes.
    - Mise en place de quotas de ressources (ResourceQuota/LimitRange) pour mieux encadrer la consommation de calcul.
- **Sécurité et Réseau** :
    - Sécurisation de l'environnement de production par la fermeture des endpoints de santé (`/healthz`, `/readyz`) à l'accès internet.
    - Amélioration des contrôles d'accès pour l'opérateur ECK.
- **Déploiement et CI/CD** :
    - Mise à jour de l'opérateur Buildkit pour le bootstrap sur le cluster de management.
    - Optimisation de l'ARC (Agent Runner Controller) pour une meilleure gestion du cycle de vie des runners.

### Autres changements
- **Nettoyage** : Suppression des entrées de modèles obsolètes (EOL), retrait de secrets CI inutilisés et nettoyage des anciens manifestes de déploiement.
