## Changelog : dictaphone (30 derniers jours, au 14 août 2026)

### Résumé
Cette période a été marquée par une amélioration majeure de l'expérience mobile, notamment avec le support des téléchargements en arrière-plan et la sélection de documents. Le système de traitement audio a été considérablement renforcé par l'introduction de workers dédiés et une meilleure gestion des erreurs, offrant ainsi une plus grande fiabilité. Les utilisateurs bénéficient également d'une meilleure visibilité sur l'avancement des transcriptions, tant sur le web que sur mobile.

### Évolutions fonctionnelles
- **Application Mobile** :
    - Ajout de la sélection et du téléchargement de documents depuis l'appareil.
    - Support des téléchargements en arrière-plan sur iOS et Android.
    - Meilleure visibilité sur l'état de l'extraction audio et mise à jour des messages de notification de téléchargement.
- **Interface Web** :
    - Affichage précis du statut de l'extraction audio (succès ou échec) sur la page des enregistrements.
    - Amélioration de l'ergonomie avec un en-tête de métadonnées de transcription fixe et des indicateurs de chargement.
    - Mise à jour des documents légaux pour la conformité aux nouvelles politiques de données.
- **Notifications** :
    - Envoi automatique d'un e-mail de notification dès que la transcription est prête.

### Évolutions techniques
- **Traitement Audio et Médias** :
    - Déploiement de workers dédiés à l'extraction audio pour optimiser les performances.
    - Fiabilisation du traitement via FFmpeg et optimisation de la conversion audio pour la transcription.
    - Meilleure gestion des erreurs d'extraction et suivi précis des résultats et des temps d'attente en file d'attente.
- **Infrastructure et Stockage** :
    - Renforcement de la gestion du stockage S3 (routage par bucket, configuration via variables d'environnement et mise en cache des clients).
    - Prise en charge des politiques de données multi-entités (multitenant).
    - Optimisation de la gestion des tâches via l'utilisation de files d'attente (queues) explicites et limitation de la concurrence des workers audio.
- **Backend** :
    - Introduction de la création synchrone de documents.
    - Amélioration de la robustesse de l'API et du schéma de configuration des domaines via Pydantic.

### Autres changements
- **Administration** :
    - Amélioration des outils de gestion : suppression multiple de fichiers, relance des tentatives d'extraction et visibilité accrue des statuts d'extraction.
- **Qualité et CI/CD** :
    - Augmentation de la couverture de tests (nettoyage audio, politiques de rétention, gestion des fuseaux horaires).
    - Amélioration de la configuration de la CI (intégration de FFmpeg, correction des problèmes de linting).
