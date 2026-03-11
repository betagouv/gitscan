## Changelog : messages (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à la plateforme, notamment des optimisations de performance, de nouvelles fonctionnalités pour l'administration et l'import/export de boîtes aux lettres, ainsi que des corrections de bugs pour une meilleure expérience utilisateur. L'ajout du support ARM64 permet également une plus grande flexibilité de déploiement.

### Évolutions fonctionnelles
- Ajout d'un bouton d'aide personnalisable dans l'en-tête (#537).
- Possibilité d'exporter une boîte aux lettres au format mbox, avec les libellés (#553).
- Support de l'import de fichiers PST et amélioration du streaming de données pour l'import mbox (#544).
- Ajout d'une liste noire pour les préfixes de boîtes aux lettres personnelles (#540).
- Possibilité d'ajouter des images directement dans le corps des messages via l'éditeur BlockNote.
- Amélioration de l'éditeur de signature avec une disposition en colonnes (#551).
- Affichage du nombre de threads sélectionnés dans le panneau de droite (#576).
- Ajout d'un lien de navigation rapide pour les utilisateurs de clavier (#573).
- Correction : le défilement est maintenant conservé lors des rendus (#578).
- Correction : les sauts de ligne sont correctement convertis en `<br>` dans le texte formaté (#577).
- Correction : les libellés et le rôle de l'utilisateur sont correctement restreints à la boîte aux lettres demandée.
- Correction : le panneau latéral se ferme correctement après l'envoi d'un message si nécessaire.

### Évolutions techniques
- Ajout de métriques d'utilisation plus précises et granulaires (#575).
- Amélioration de la résilience de la vérification DNS (#574).
- Exposition des flags `oidc_autojoin` et `identity_sync` pour la configuration (#542).
- Migration vers la nouvelle API Drive (nécessite Drive >= 0.13.0).
- Refonte de l'architecture pour l'utilisation de uv, rustfs et caddy (#556).
- Passage à Python 3.14 (#556).
- Ajout de support pour l'architecture ARM64 dans les images Docker (#554).
- Ajout d'événements Celery pour la surveillance des workers (#549).
- Ajout d'un backend DeployCenter pour la synchronisation des administrateurs de domaines de messagerie (#572).
- Ajout d'une commande de gestion pour afficher tous les utilisateurs de l'instance (#506).
- Mise à jour de django-lasuite vers la version 0.0.24 (#546).
- Optimisation de la sérialisation et de la gestion du corps des MessageTemplate (#545).
- Remplacement de Nginx par Caddy pour le reverse proxy et le déploiement Scalingo (#556).
- Remplacement de MinIO par RustFS pour le stockage d'objets en développement (#556).
- Ajout de throttling pour les destinataires des messages sortants (#506).

### Autres changements
- Mise à jour de la documentation traduite.
- Mise à jour de la version de Keycloak (26.5.3 et 26.5.4).
- Mise à jour des étapes des workflows GitHub Actions.
- Correction de bugs liés à la construction des images Docker pour ARM64.
- Amélioration de l'expérience développeur avec une nouvelle commande `make`.
- Suppression des catalogues de traduction Django i18n et backend.
- Correction de la régénération des fichiers `uv.lock` lors de l'incrémentation de la version.
- Suppression de l'ID de la boîte aux lettres dans les métriques.
