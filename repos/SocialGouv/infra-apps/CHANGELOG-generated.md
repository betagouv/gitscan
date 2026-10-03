## Changelog : infra-apps (30 derniers jours, au 02/10/2026)

### Résumé
Ce mois a été marqué par une migration majeure de l'infrastructure de stockage d'Iterion vers SeaweedFS et une série de mises à jour visant à stabiliser les environnements de production. Nous avons également renforcé la fiabilité des runners de CI (ARC) et déployé de nouveaux services de sécurité, notamment ClamAV pour le projet Domifa.

### Évolutions fonctionnelles
- **Identité numérique :** `iterion.cloud` devient l'URL publique officielle et canonique de la plateforme.
- **Intelligence Artificielle :** Support des nouveaux modèles d'IA, notamment Opus 5.5 et GPT-6.
- **Nouvelle fonctionnalité :** Le système de déploiement est désormais capable d'envoyer des emails.
- **Interface :** Amélioration de la gestion de la session dans le Studio pour faciliter le retour après une authentification.

### Évolutions techniques
- **Migration du stockage objet :** Bascule complète de MinIO vers SeaweedFS. Ce processus a inclus la synchronisation des données (mirroring), la validation de la cohérence et le retrait définitif de MinIO de la production.
- **Optimisation de l'infrastructure Iterion :**
    - Mise à jour massive des composants serveur et runner (montée en version vers la v3.223.0).
    - Amélioration de la gestion des ressources : limitation de la mémoire des pods de calcul (8Gi) et application de `PriorityClass` pour garantir la priorité des pods de la plateforme sur les pods de calcul.
    - Renforcement de la sécurité : rotation des clés JWT SeaweedFS et des mots de passe, et durcissement via le pinning des images par digest pour garantir l'immuabilité des déploiements [#67](https://github.com/SocialGouv/infra-apps/issues/67).
- **Fiabilité des Runners (ARC) :**
    - Stabilisation des runners via une meilleure gestion de l'API `dind` et des instances `inotify`.
    - Mise en place d'alertes en cas d'interruption des runners pour éviter les blocages de la file d'attente de fusion [#54](https://github.com/SocialGouv/infra-apps/issues/54).
- **Sécurité & Conformité :**
    - Déploiement de ClamAV sur l'infrastructure OVH pour le projet Domifa, incluant l'ajustement des politiques réseau (NetworkPolicies).
    - Scellement des tokens de forge dans tous les namespaces `ci-`.
- **Outils de gestion :** Création d'un CLI signé pour permettre le redémarrage du plan de contrôle Kubernetes via l'API OVH.

### Autres changements
- **Déclassement :** Retrait du composant `charon-carnets`.
- **Documentation :** Mise à jour des notes techniques concernant Corepack et le couplage entre les images de runners et les digests serveurs.
