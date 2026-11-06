## Changelog : drive-migrator (30 derniers jours, au 03/11/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de la fiabilité des migrations grâce à un nouveau système de tentatives automatiques en cas d'erreur réseau. L'expérience utilisateur est également plus fluide : les erreurs de connexion sont mieux expliquées, et la gestion des fichiers refusés par la destination est simplifiée grâce à un archivage automatique et un accès facilité via les emails de notification.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur (UX) :**
    - Meilleure communication lors des déconnexions : les utilisateurs sont désormais informés de la raison pour laquelle ils doivent se reconnecter.
    - Guidage des utilisateurs : redirection automatique vers Drive pour les utilisateurs ne possédant pas encore de compte.
    - Information sur la disponibilité de certaines fonctionnalités (ex: transfert d'accès).
- **Gestion des échecs de migration :**
    - Les fichiers refusés par la destination sont désormais archivés et un lien est ajouté dans les emails de notification pour les récupérer facilement.
    - Ajout d'un point de terminaison (endpoint) permettant de télécharger directement les fichiers refusés.
    - Les fichiers bloqués par Drive sont désormais ignorés au lieu de faire échouer l'intégralité de la migration.
- **Interface et Administration :**
    - Ajout des informations relatives au workspace dans la liste des tâches de l'interface d'administration.
    - Amélioration de la visibilité des workspaces verrouisés pour les utilisateurs ayant le rôle d'Animateur sur Resana.
- **Données :**
    - Optimisation du fichier CSV des membres Drive par la suppression des colonnes de noms [#296].

### Évolutions techniques
- **Fiabilité et Résilience :**
    - Implémentation d'une session de tentatives partagée (`RetryingSession`) pour gérer automatiquement les erreurs API transitoires (timeouts, erreurs 5xx) sur les services Osmose, Resana et Drive.
- **Infrastructure et DevOps :**
    - Migration complète de la gestion du projet vers l'outil `uv`.
    - Optimisation des images Docker (utilisation de bases Alpine) et de la configuration Nginx.
    - Amélioration des performances du serveur avec l'utilisation de workers threadés pour Gunicorn.
- **Sécurité et Maintenance :**
    - Mises à jour de sécurité critiques sur Django, PyJWT, certifi et Pillow.
    - Mise à jour des environnements Node et Brotli.
- **Observabilité et Qualité :**
    - Renforcement de la couverture de tests unitaires, notamment pour les helpers de migration [#297].
    - Amélioration de la journalisation (logs INFO vers la console, suivi de la durée de vie des tokens et des logs d'upload Drive).
    - Intégration de l'envoi de métadonnées (taille de workspace, types de fichiers) vers PostHog pour l'analyse.

### Autres changements
- Nettoyage du backend par la suppression de dépendances de production inutilisées.
