## Changelog : dictaphone (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante en renforçant considérablement sa sécurité et la fiabilité de ses services. Les utilisateurs bénéficieront d'une meilleure gestion des téléchargements sur mobile (reprise automatique, alertes de quota) et d'une interface plus claire concernant les accès restreints. Côté technique, une nouvelle architecture pour l'extraction audio a été déployée pour optimiser les transferts de fichiers, accompagnée d'un durcissement global des politiques de sécurité et de limitation de débit.

### Évolutions fonctionnelles
- **Expérience Mobile** : 
    - Amélioration de la fiabilité des téléchargements avec gestion automatique des reprises, des alertes de limite de quota et des erreurs réseau.
    - Meilleure gestion des états (affichage d'un état vide lorsqu'il n'y a pas d'enregistrements).
    - Correction de la numérotation des participants dans les transcriptions.
- **Interface Utilisateur (Web & Mobile)** :
    - Ajout d'une page d'accès restreint avec des instructions configurables pour guider les utilisateurs.
    - Amélioration de la visibilité des limites de quota et des alertes de dépassement.
    - Correction des liens vers les documents légaux et de l'affichage des transcriptions.
- **Administration** :
    - Nouvelles capacités de suivi des tâches d'extraction audio et visualisation de la durée des jobs dans l'interface d'administration.

### Évolutions techniques
- **Sécurité et Contrôle d'accès** :
    - Renforcement de l'authentification via l'application des politiques d'accès OIDC pour la création de comptes et les téléchargements.
    - Mise en place de limitations de débit (rate limiting) par utilisateur pour les opérations coûteuses (création de fichiers, tâches IA).
    - Durcissement de la protection des données : utilisation d'Argon2id pour le hachage des mots de passe, protection des comptes administrateurs (verrouillage IP/compte) et sécurisation des payloads externes.
    - Sécurisation des flux de déconnexion mobile (révocation des tokens de rafraîchissement).
- **Architecture et Infrastructure** :
    - Introduction d'un nouveau service d'extraction audio et d'une passerelle S3 pour optimiser les transferts de stockage entre les workers.
    - Mise à jour de l'extracteur audio vers FFmpeg 9.
    - Optimisation de la CI/CD : séparation des workflows par composant, intégration des tests mobiles et frontend, et builds Docker multi-plateformes natifs.
    - Intégration de Sentry pour le suivi des erreurs et la télémétrie.
- **Optimisations Backend** :
    - Amélioration de la gestion des quotas de transcription (gestion des échecs de jobs et des suppressions de fichiers).
    - Normalisation du traitement des emails pour assurer la cohérence des correspondances de données.

### Autres changements
- **Documentation** : Mise à jour des diagrammes d'architecture (incluant la passerelle S3) et des guides de contribution (utilisation des gitmojis).
- **Développement** : Consolidation de la configuration des services via des fichiers d'environnement et optimisation des tests avec `pytest-xdist`.
