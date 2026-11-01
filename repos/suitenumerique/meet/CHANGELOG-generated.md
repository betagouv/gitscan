## Changelog : meet (30 derniers jours, au 31 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure en renforçant la traçabilité grâce à l'implémentation d'un système complet de journaux d'audit. L'expérience utilisateur a été enrichie par de nouvelles options de gestion des enregistrements et des améliorations significatives en matière d'accessibilité. La sécurité a également été une priorité avec la correction de plusieurs vulnérabilités et un renforcement des mécanismes d'authentification.

### Évolutions fonctionnelles
- **Gestion des réunions et enregistrements** :
    - Possibilité pour les visiteurs non connectés de démarrer une réunion.
    - Les utilisateurs authentifiés peuvent désormais lancer des enregistrements.
    - Choix de l'encodage disponible lors du lancement d'un enregistrement.
    - Mise en place de la suppression "douce" (soft-delete) des salles avec purge automatique après un délai de rétention.
- **Accessibilité et Expérience Utilisateur** :
    - Amélioration de l'accessibilité : annonce de la coupure du micro via les raccourcis [#1816], navigation au clavier améliorée pour la pagination des participants et visibilité accrue des contours de focus [#1797].
    - Avertissement visuel pour les utilisateurs en cas de bascule de connexion sur le protocole TURN.
    - Remplacement du chat Crisp par le formulaire de support officiel de La Suite.
- **Confidentialité** : Protection des salles contre l'indexation par les moteurs de recherche et les IA.

### Évolutions techniques
- **Sécurité et Audit** :
    - Déploiement d'un système de journaux d'audit structurés (suivi des actions administrateur, des appels API, des enregistrements, des transcriptions et de la création d'utilisateurs).
    - Renforcement de l'authentification via l'échange de jetons (token exchange) pour les intégrations en iframe.
    - Maintenance de sécurité : correction de plusieurs vulnérabilités (CVE) sur Nginx, Brotli, Pillow, Node.js et libx11.
- **Performance et Stabilité** :
    - Optimisation de la base de données avec l'ajout d'un pool de connexions PostgreSQL et d'un index pour les recherches d'utilisateurs par email.
    - Amélioration de la résilience face aux erreurs de l'API LiveKit via la gestion systématique des timeouts.
    - Déplacement de l'envoi des notifications d'enregistrement vers des tâches asynchrones (Celery).
- **Infrastructure et DevOps** :
    - Support natif de l'architecture arm64 pour les images Docker.
    - Intégration de Vitest pour les tests unitaires du frontend.
    - Mise à jour des charts Helm et optimisation des scripts de release sur NixOS.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant les journaux d'audit et corrections du fichier README.
