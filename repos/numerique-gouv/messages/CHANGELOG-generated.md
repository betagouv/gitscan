## Changelog : messages (30 derniers jours, au 04 novembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur une meilleure maîtrise du stockage (suivi de l'espace utilisé et automatisation de la purge), l'amélioration de l'expérience mobile (notamment la sécurité des notifications) et le renforcement de la sécurité globale de l'infrastructure et des données.

### Évolutions fonctionnelles
- **Gestion du stockage et des messages** : 
    - Ajout de jauges de stockage pour visualiser l'espace utilisé par les boîtes mail.
    - Mise en place d'une logique de purge automatique pour les corbeilles et les spams.
    - Amélioration de la gestion des suppressions pour protéger les fils de discussion partagés.
- **Expérience Mobile** : 
    - Amélioration de la fluidité de l'interface (navigation par simple pression, corrections de styles).
    - Sécurisation des notifications : les aperçus de messages sont désormais chiffrés sur iOS et Android.
- **Interface Utilisateur (Web)** : 
    - Affichage de bannières d'information pour les messages de service ou l'activation de réponses automatiques.
    - Amélioration de la fenêtre de rédaction et de la gestion des notifications web.
    - Pagination de la vue des métriques d'utilisation [#832](https://github.com/numerique-gouv/messages/issues/832).
- **Authentification et Thèmes** : 
    - Mise à jour du thème Keycloak `lst-dsfr` pour adopter le rendu visuel "ProConnect".

### Évolutions techniques
- **Sécurité et Confidentialité** : 
    - Chiffrement des aperçus de notifications push envoyés aux appareils.
    - Sécurisation du stockage des paramètres sensibles via l'utilisation de types de données protégés.
    - Mise à jour des certificats de confiance (CA bundles) dans les images Docker pour renforcer la sécurité [#829](https://github.com/numerique-gouv/messages/issues/829).
- **Infrastructure et CI/CD** : 
    - Mise à jour de l'environnement backend vers Python 3.14.8 [#821](https://github.com/numerique-gouv/messages/issues/821).
    - Optimisation de la publication des images Docker pour assurer la compatibilité avec Podman [#820](https://github.com/numerique-gouv/messages/issues/820).
    - Intégration d'un scanner de vulnérabilités (OSS Scanner) dans le processus de déploiement.
- **Backend et Recherche** : 
    - Correction du moteur de recherche de fils de discussion en cas d'absence de configuration OpenSearch.
    - Ajout d'une commande d'exportation du corpus de spam vers le stockage objet.

### Autres changements
- **Documentation** : 
    - Mise à jour du fichier README [#839](https://github.com/numerique-gouv/messages/issues/839).
    - Ajout de la documentation concernant les paramètres requis pour l'intégration Google Drive.
