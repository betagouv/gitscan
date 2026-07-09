## Changelog : audiodescription (30 derniers jours, au 8 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'infrastructure et l'intégration de nouveaux services pour l'envoi d'emails et le stockage de fichiers. Des corrections de cache et des ajustements de configuration ont également été apportés pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Intégration de Proconnect pour la gestion des utilisateurs, avec ajout d'une option d'authentification via Proconnect sur le formulaire de connexion.
- Remplacement de Brevo par Sendethic pour l'envoi d'emails, notamment pour la gestion du patrimoine. [#11](https://github.com/betagouv/audiodescription/pull/11)
- Ajout d'un exemple de configuration pour les paramètres dans le répertoire de configuration Docker.
- Correction de l'icône "affiches parlantes".
- Suppression des messages Drupal inutiles sur la page d'inscription à la newsletter.

### Évolutions techniques
- Mise à jour de la configuration Matomo pour utiliser l'instance "culture" au lieu de "beta".
- Implémentation de RustFS pour le stockage S3.
- Ajout de Redis pour la mise en cache.
- Mise à jour du Dockerfile pour la production et du fichier `compose.staging.yml`.
- Amélioration de la gestion du cache sur la création et la mise à jour des nœuds.
- Correction d'une erreur lors de la génération du HTML.
- Mise à jour de la configuration S3 pour l'environnement de pré-production.
- Utilisation de la nouvelle URL pour Sendethic.

### Autres changements
- Suppression d'un hook inutilisé dans la configuration S3.
- Suppression d'un processus inutile de la documentation.
- Mise à jour de la configuration pour l'environnement S3.
- Mise à jour des versions dans la documentation.
- Correction du fichier `composer.lock`.
- Mise à jour des packages.
