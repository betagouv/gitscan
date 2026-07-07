## Changelog : audiodescription (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives en termes d'infrastructure et de services externes. Le service d'envoi d'emails a été migré vers Sendethic, remplaçant Brevo. Des optimisations ont été apportées à la configuration pour le déploiement en pré-production et en production, incluant l'ajout de Redis et l'utilisation de RustFS pour le stockage S3.

### Évolutions fonctionnelles
- Remplacement de Brevo par Sendethic pour l'envoi d'emails, notamment pour la gestion du patrimoine [#11](https://github.com/betagouv/audiodescription/pull/11).
- Correction de l'icône "affiches parlantes" pour une meilleure expérience utilisateur.
- Suppression des messages Drupal inutiles sur la page d'inscription à la newsletter.

### Évolutions techniques
- Migration de Matomo vers l'instance culture pour le suivi analytique.
- Ajout de Redis pour améliorer les performances et la scalabilité.
- Intégration de RustFS pour l'utilisation de S3.
- Mise à jour de la configuration Dockerfile pour la production.
- Mise à jour des fichiers de configuration pour le déploiement en pré-production (compose.staging.yml).
- Utilisation de la nouvelle URL pour le service Sendethic.

### Autres changements
- Ajout d'un exemple de configuration dans le répertoire de configuration Docker.
- Mise à jour de la documentation avec les versions actuelles.
- Correction du fichier `composer.lock`.
- Mise à jour des packages PHP.
