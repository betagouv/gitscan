## Changelog : infra-apps (30 derniers jours, au 31/10/2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la plateforme Iterion, avec des améliorations notables de l'interface Studio et un renforcement majeur de la résilience de l'infrastructure. Les efforts se sont concentrés sur la stabilisation des services critiques (bases de données, stockage) et l'optimisation des pools de calcul pour les tâches d'intelligence artificielle.

### Évolutions fonctionnelles
- **Améliorations du Studio** : 
    - Ajout du rendu Markdown pour les livrables.
    - Mise en place de liens de partage via l'adresse `?file=`.
    - Ajout d'une ligne dédiée aux livrables dans l'interface.
    - Optimisation de l'ergonomie (amélioration du contraste et des indicateurs de focus).
- **Gestion des flux** : Possibilité de choisir la posture de "merge-gate" directement depuis l'interface du Studio [#2479](https://github.com/SocialGouv/infra-apps/issues/2479).
- **Intelligence Artificielle** : Support des sorties structurées pour "Claw" via des passerelles compatibles OpenAI [#2664](https://github.com/SocialGouv/infra-apps/issues/2664).

### Évolutions techniques
- **Haute disponibilité et résilience** :
    - Renforcement de la répartition des nœuds pour MongoDB et NATS afin de garantir la présence d'un membre par nœud et d'éviter les éjections simultanées.
    - Correction de l'anti-affinité pour Valkey afin d'utiliser les valeurs de labels réelles des pods.
    - Optimisation de l'allocation des slots pour les serveurs de volume SeaweedFS.
- **Sécurité** : Restriction de l'accès public aux endpoints de santé (`/healthz` et `/readyz`) sur l'environnement `ovh-prod`.
- **Gestion des Runners et CI/CD** :
    - Déploiement de nouveaux pools de runners (`vao`, `egapro`, `honorabilite`) avec routage spécifique vers les modèles de passerelles (Scaleway/GLM).
    - Mise à jour du contrôleur ARC pour permettre la reconstruction automatique des runners défaillants.
    - Amélioration du réseau des sandboxes via l'utilisation d'un proxy de run [#2313](https://github.com/SocialGouv/infra-apps/issues/2313).
- **Automatisation et Déploiement** :
    - Automatisation de la création de "project bots" via l'authentification OAuth GitLab.
    - Généralisation du "pinning" des images (server, runner, sandbox) par digest pour garantir la stabilité et faciliter la récupération après incident [#2710](https://github.com/SocialGouv/infra-apps/issues/2710), [#2705](https://github.com/SocialGouv/infra-apps/issues/2705).
    - Mise en place de l'application de bootstrap sur le cluster de management pour le `buildkit-operator`.
