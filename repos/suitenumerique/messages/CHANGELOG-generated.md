## Changelog : messages (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'expérience mobile, la fiabilité de l'importation de données et la gestion du stockage. Les utilisateurs bénéficieront d'une application mobile plus fluide, d'un import de messages (PST/IMAP) plus précis et de nouveaux outils visuels pour suivre l'utilisation de leur espace de stockage. L'interface s'enrichit également de nouveaux indicateurs pour faciliter la communication et la gestion des services.

### Évolutions fonctionnelles
- **Expérience Mobile** : Amélioration significative de l'ergonomie (gestion du clavier sur iOS/Android, déchiffrement des notifications, navigation simplifiée par toucher unique) et passage à la version 0.2.1.
- **Importation de données** : Optimisation de l'importation des contacts et messages depuis Outlook (PST) et Orange (IMAP) pour une meilleure gestion des noms, des dates et de la structure des dossiers.
- **Gestion du stockage et quotas** : Introduction d'une jauge de stockage, de mécanismes de purge pour la corbeille/spams et d'une meilleure visibilité des quotas par domaine.
- **Interface utilisateur** : 
    - Ajout de bannières d'information (messages de service, indicateur de réponse automatique active).
    - Amélioration de l'affichage des aperçus de notifications push.
    - Optimisation de l'intégration avec Google Drive (détection de doublons, gestion de la taille des pièces jointes).
- **Authentification** : Mise à jour du thème Keycloak `lst-dsfr` incluant l'apparence ProConnect et de nouvelles options de déploiement.

### Évolutions techniques
- **Backend & Sécurité** : 
    - Refonte du moteur SMTP (`pymta`) pour renforcer la robustesse et la sécurité [#857].
    - Chiffrement des aperçus de notifications push pour les appareils mobiles.
    - Sécurisation des paramètres contenant des données sensibles via `SecretFileValue`.
- **Infrastructure & CI/CD** : 
    - Optimisation des builds Docker (ajout de tentatives de réessai) et sécurisation des déploiements d'images.
    - Mise à jour de Caddy [#859] et rafraîchissement des images de base et des certificats CA [#829].
- **Tests** : Amélioration de la stabilité des tests de bout en bout (E2E) sur la chaîne de CI.
- **Performance & Maintenance** : Pagination de la vue des métriques d'utilisation [#832] et optimisation du système de healthcheck [#822].

### Autres changements
- **Documentation** : Mise à jour du README [#839] et ajout de la documentation relative aux paramètres d'intégration Google Drive.
