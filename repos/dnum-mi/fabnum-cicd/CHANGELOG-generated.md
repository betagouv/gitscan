## Changelog : fabnum-cicd (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par une montée en puissance de la sécurité et de l'automatisation. L'intégration massive de l'authentification via GitHub App permet désormais de sécuriser et de simplifier les processus de publication. Les capacités de gestion des charts Helm et des images Docker ont été considérablement enrichies, offrant plus de flexibilité (notamment pour les monorepos) et une meilleure traçabilité grâce à l'attestation des composants.

### Évolutions fonctionnelles
- **Publication NPM** : Support de la publication de paquets vers des registres compatibles avec NPM.
- **Gestion Helm améliorée** : 
    - Introduction du mode "auto" pour la mise à jour des versions basée sur `appVersion`.
    - Support du mode local pour la publication de charts, facilitant la gestion des monorepos.
- **Sécurité** : Ajout d'un nouveau workflow de scan de secrets via Gitleaks.
- **Tests Docker** : Possibilité d'exécuter des commandes directement à l'intérieur d'une image construite pour valider son fonctionnement.
- **Déploiement d'applications** : Support des dépôts utilisant des versions immuables pour les releases.

### Évolutions techniques
- **Sécurité & Authentification** : 
    - Généralisation du support des GitHub Apps pour les workflows de publication (Helm, Docker, App) et de scan (Trivy).
    - Renforcement de la sécurité des workflows : protection contre les injections de commandes (shell injection) et sécurisation du passage des identifiants via les variables d'environnement.
- **Docker & Conteneurs** : 
    - Refonte de l'attestation des images en utilisant Cosign pour la génération de SBOMs.
    - Ajout de nouveaux paramètres de build (gestion du cache, signature, tags optionnels).
- **Helm & Kubernetes** : 
    - Refactorisation des workflows de mise à jour et de publication (séparation du mode local dans des workflows dédiés).
    - Ajout de la signature et de l'attestation des charts lors de la distribution.
- **CI/CD & Qualité** : 
    - Amélioration de la synchronisation des branches de pré-release.
    - Optimisation du nettoyage des images et des caches.
    - Renforcement des tests de conformité pour les workflows réutilisables (actionlint et tests de droits d'accès).

### Autres changements
- **Documentation** : Mise à jour majeure incluant un guide d'authentification GitHub App, un guide de release pour les monorepos et une réorganisation de l'index des workflows.
- **Maintenance** : Nettoyage du code (suppression des avertissements de linting YAML/Shell) et synchronisation des exemples de documentation avec les flux de travail actuels.
