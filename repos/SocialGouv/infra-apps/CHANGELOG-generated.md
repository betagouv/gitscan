## Changelog : infra-apps (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois a été marqué par une transition majeure de l'infrastructure de stockage vers SeaweedFS et l'enrichissement de la plateforme Iterion. De nouvelles capacités d'IA (Claw) et des améliorations significatives de l'interface Studio ont été déployées, parallèlement à une optimisation des pools de runners pour améliorer la performance et la gestion des ressources.

### Évolutions fonctionnelles
- **Améliorations du Studio Iterion** : Ajout du rendu Markdown, de nouvelles adresses de fichiers partageables et d'une ligne dédiée aux livrables ([#2622](https://github.com/SocialGouv/infra-apps/issues/2622), [#2638](https://github.com/SocialGouv/infra-apps/issues/2638)).
- **Contrôle de déploiement** : Possibilité de configurer la posture du "merge-gate" directement depuis le Studio ([#2479](https://github.com/SocialGouv/infra-apps/issues/2479)).
- **Intelligence Artificielle** : Amélioration de l'expérience de revue de code avec l'intégration de Claw (support des sorties structurées via des passerelles compatibles OpenAI [#2664](https://github.com/SocialGouv/infra-apps/issues/2664) et nouvelle interface de revue [#2705](https://github.com/SocialGouv/infra-apps/issues/2705)).
- **Automatisation GitLab** : Mise en place d'un mécanisme de bootstrap via OAuth permettant la création automatique de bots de projet par dépôt.

### Évolutions techniques
- **Migration du stockage** : Transition complète de l'objet store de MinIO vers SeaweedFS, incluant la phase de mirroring et la coupure définitive.
- **Gestion des Runners et Compute** :
    - Déploiement de nouveaux pools de runners : `vao` (PLIAGE) et `egapro`.
    - Optimisation des runners ARC : migration vers un nodepool CI dédié et amélioration de la gestion de la taille des requêtes.
    - Enrichissement de l'environnement de build avec l'intégration de Go et Node.js dans le cache des outils.
- **Infrastructure Iterion** :
    - Déploiement de la série de versions v3.2xx de l'engine et du serveur.
    - Optimisation du routage des modèles pour le pool `honorabilite` via le catalogue Scaleway.
    - Renforcement de la sécurité réseau en restreignant l'accès aux endpoints de santé (`/healthz`, `/readyz`) sur l'environnement OVH.
    - Stabilisation de la base de données par le couplage (binding) de MongoDB et NATS.
    - Amélioration de la communication entre le gateway sandbox et le proxy de run ([#2313](https://github.com/SocialGouv/infra-apps/issues/2313)).
- **Sécurité et Services** :
    - Déploiement de ClamAV sur l'environnement OVH pour le service Domifa.
    - Corrections des politiques réseau (netpol) pour ClamAV.
- **Charon** : Corrections sur la configuration des callbacks et support des appels locaux ProConnect.

### Autres changements
- **Sécurité** : Rotation des clés JWT de SeaweedFS et du mot de passe valkeyfiler.
- **Outils** : Mise à disposition d'une CLI signée pour le redémarrage du plan de contrôle Kubernetes.
- **Documentation** : Mise à jour des notes concernant Corepack et le conteneur Firecrawl.
