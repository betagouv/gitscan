## Changelog : infra (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois a été marqué par une étape majeure avec le déploiement du socle de la nouvelle infrastructure. Les efforts se sont concentrés sur le renforcement de la sécurité (isolation réseau, gestion des secrets) et l'optimisation des processus de déploiement automatisés (CI/CD) pour garantir une meilleure stabilité des services.

### Évolutions fonctionnelles
- Mise à disposition d'une nouvelle image Docker pour le déploiement de Matomo [#244](https://github.com/mission-apprentissage/infra/pull/244).

### Évolutions techniques
- **Architecture & Core** :
    - Mise en place du socle de la nouvelle infrastructure [#248](https://github.com/mission-apprentissage/infra/pull/248).
    - Intégration de la pile système pour `lba-preview` [#242](https://github.com/mission-apprentissage/infra/pull/242).
    - Configuration spécifique pour `containerd`.
- **Sécurité & Réseau** :
    - Migration de `bal.production` sur un réseau privé pour une meilleure isolation.
    - Renforcement de la gestion des secrets via la rotation des clés SOPS.
    - Amélioration de la gestion des clés OpenPGP dans les workflows et les conteneurs runners [#246](https://github.com/mission-apprentissage/infra/pull/246).
    - Corrections des règles de pare-feu (Nftables) pour MongoDB et les services BAL.
- **CI/CD & Observabilité** :
    - Optimisation des runners (passage sur Ubuntu 26.04 et gestion du trousseau GnuPG).
    - Amélioration de la stabilité de la CI (validation des environnements et synchronisation des sous-modules) [#243](https://github.com/mission-apprentissage/infra/pull/243).
    - Optimisation de la pile de logs avec Fluentd (gestion des chemins S3, parsing syslog et épinglage des dépendances Ruby) [#240](https://github.com/mission-apprentissage/infra/pull/240).

### Autres changements
- **Maintenance & Nettoyage** :
    - Homogénéisation des scripts mutualisés.
    - Retrait du produit `bal` des chaînes de déploiement.
    - Diverses corrections de typos dans les inventaires (Sentry, LBA) et les fichiers de configuration.
    - Mise à jour de plusieurs images Docker (Fluentd, Runner) et des sous-modules.
