## Changelog : infra (30 derniers jours, au 30 octobre 2026)

### Résumé
Ce mois-ci, l'accent a été mis sur le renforcement de la sécurité et de la fiabilité de l'infrastructure. Les principales évolutions concernent l'isolation de certains services sur des réseaux privés, l'amélioration de la gestion des clés de sécurité lors des déploiements automatisés, et une optimisation importante du système de collecte de logs pour une meilleure visibilité sur l'état des serveurs.

### Évolutions fonctionnelles
- Mise à disposition d'une nouvelle image Docker pour l'outil d'analyse d'audience Matomo [#244].

### Évolutions techniques
- **Sécurité et Réseau** :
    - Migration de `bal.production` vers un réseau privé pour renforcer l'isolation des services.
    - Correction et mise à jour des règles de pare-feu (Nftables) pour les services `bal.production`, `bal.staging` et `mongodb-lba`.
- **CI/CD et Automatisation** :
    - Amélioration de la gestion des clés OpenPGP dans les conteneurs de déploiement (importation des clés, utilisation d'un trousseau GnuPG dédié [#246], passage en mode batch).
    - Stabilisation des pipelines de CI, notamment sur la validation des environnements [#243].
    - Exclusion de `bal.production` des cycles de redémarrage automatique des serveurs.
- **Observabilité et Logs** :
    - Mise à jour majeure de la pile de logging avec Fluentd (passage en version 1.7.0, correction du parsing syslog et de la gestion des chemins S3 [#240, #241]).
- **Infrastructure et Conteneurs** :
    - Support de la nouvelle pile système pour `lba-preview` [#242].
    - Optimisation de la configuration de `containerd` et mise à jour des images Docker des runners.
    - Correction de compatibilité avec Docker Compose (retrait de paramètres obsolètes).

### Autres changements
- Nettoyage de diverses erreurs de saisie (typos) dans les inventaires (Sentry, LBA).
- Mise à jour de sous-modules et homogénéisation des scripts mutualisés.
- Suppression de références obsolètes dans les fichiers de configuration externes.
