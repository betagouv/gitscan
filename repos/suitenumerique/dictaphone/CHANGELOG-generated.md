## Changelog : dictaphone (30 derniers jours, au 05 novembre 2026)

### Résumé
Ce mois-ci, dictaphone a franchi une étape majeure avec l'introduction d'un nouveau service dédié à l'extraction audio, permettant un traitement plus robuste et isolé des fichiers. L'accent a été mis sur la sécurité (renforcement de l'authentification et limitation des abus) et sur l'amélioration de l'expérience mobile, notamment pour la gestion des téléchargements et des alertes de quota.

### Évolutions fonctionnelles
- **Expérience Mobile** : 
    - Amélioration significative de la gestion des téléchargements (reprise automatique en cas de coupure, gestion des limites de débit et alertes de quota).
    - Corrections de l'affichage des transcriptions (numérotation des participants) et ajout d'états vides pour une interface plus claire.
    - Possibilité de supprimer des enregistrements bloqués en attente d'envoi.
- **Gestion des accès et sécurité** : 
    - Mise en place d'une page d'accès restreint avec des messages d'orientation personnalisés.
    - Intégration des politiques de sécurité OIDC pour restreindre certaines actions (création de compte, téléchargements, imports) selon le rôle de l'utilisateur.
- **Utilisation du service** : 
    - Amélioration de la lecture audio via l'utilisation de formats transcodés.
    - Meilleure visibilité sur les limites de quota et les durées de traitement des tâches d'intelligence artificielle.
    - Alignement du formatage des transcriptions entre le backend et le frontend.

### Évolutions techniques
- **Nouvelle architecture** : 
    - Création et déploiement d'un service autonome d'extraction audio (*audio-extractor*) pour isoler le traitement lourd du reste de l'application.
    - Introduction d'une passerelle S3 (*S3 gateway*) pour optimiser les transferts de fichiers entre les différents services.
- **Sécurité et Robustesse** : 
    - Renforcement de la protection des données (hachage des mots de passe via Argon2id, protection des données sensibles dans la télémétrie).
    - Mise en place de mécanismes de protection contre les abus (limitation du débit par utilisateur sur les opérations coûteuses, verrouillage des comptes et des IP en cas d'échec de connexion).
    - Sécurisation des échanges d'authentification (validation d'état PKCE).
- **Infrastructure et CI/CD** : 
    - Optimisation des pipelines CI/CD avec des workflows par composant et des filtres de chemin pour accélérer les tests.
    - Amélioration des images Docker (build natif pour le frontend, durcissement des images de conteneurs).
    - Mise à jour des charts Helm pour supporter la nouvelle architecture et améliorer la sécurité des workloads Kubernetes.
- **Observabilité** : 
    - Intégration de Sentry pour le suivi des erreurs et des métadonnées de release.
    - Amélioration de la journalisation (logs) pour le suivi des tâches d'extraction audio.

### Autres changements
- Mise à jour de la documentation technique et des schémas d'architecture (S3 gateway, workflow audio).
- Amélioration de l'expérience développeur (guides pour les messages de commit, configuration des outils locaux).
