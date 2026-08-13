## Changelog : dictaphone (30 derniers jours, au 12 août 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la fiabilité du traitement audio et de l'expérience utilisateur. Les utilisateurs bénéficient désormais de notifications automatiques lors de la fin d'une transcription et d'une interface plus fluide. En coulisses, l'infrastructure a été renforcée pour optimiser la gestion du stockage et la performance des tâches de transcription.

### Évolutions fonctionnelles
- **Notifications** : Envoi d'un e-mail automatique dès qu'une transcription est prête.
- **Interface utilisateur** : 
    - Ajout d'un indicateur de chargement lors de la vérification des fichiers.
    - L'en-tête des métadonnées de la transcription reste désormais fixe lors du défilement (sticky header).
- **Compatibilité** : Amélioration du support du format vidéo MKV sur le navigateur Chrome.
- **Administration** : 
    - Meilleure visibilité sur l'état d'avancement des extractions audio.
    - Possibilité de relancer une extraction de fichier directement depuis l'interface d'administration.

### Évolutions techniques
- **Traitement audio et transcription** :
    - Optimisation du processus de conversion audio pour la transcription.
    - Déploiement de workers dédiés à l'extraction audio pour une meilleure isolation des tâches.
    - Limitation de la concurrence des workers audio pour stabiliser le système.
- **Gestion du stockage (S3)** :
    - Refonte de la configuration du stockage pour un routage plus précis vers les buckets configurés.
    - Amélioration de la gestion des endpoints et des noms de buckets via les variables d'environnement.
    - Mise en cache des clients S3 pour optimiser les performances.
- **Fiabilité et Backend** :
    - Prévention des créations de documents multiples en parallèle.
    - Utilisation de files d'attente (queues) explicites pour l'ensemble des tâches asynchrones.
    - Amélioration de la gestion des erreurs lors des tentatives d'extraction audio.
- **Qualité et CI/CD** :
    - Renforcement de la couverture de tests (nettoyage audio, gestion du stockage, limites de rétention).
    - Amélioration du pipeline CI (linting et intégration de ffmpeg).

### Autres changements
- **Développement** : Augmentation de la taille maximale des fichiers autorisés en environnement de développement local.
- **Documentation** : Harmonisation de la terminologie utilisée pour les profils de configuration.
