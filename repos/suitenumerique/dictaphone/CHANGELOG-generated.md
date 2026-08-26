## Changelog : dictaphone (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, Dictaphone a franchi une étape importante dans la fiabilité de son traitement audio et l'expérience mobile. Les utilisateurs bénéficient désormais d'un meilleur suivi de l'avancement des transcriptions et de fonctionnalités mobiles enrichies, comme les téléchargements en arrière-plan. En coulisses, l'infrastructure a été renforcée pour améliorer la gestion des données et la stabilité des processus de transcription.

### Évolutions fonctionnelles
- **Expérience Mobile (v1.6.x) :**
    - Support des téléchargements en arrière-plan pour iOS et Android.
    - Ajout d'un sélecteur de documents pour faciliter l'importation de fichiers.
    - Amélioration du suivi de l'état de l'extraction audio et des notifications de téléchargement.
    - Optimisation des performances de téléchargement sur Android.
- **Interface Web & Administration :**
    - Affichage détaillé de l'état de l'extraction audio (succès ou échec) directement sur la page des enregistrements.
    - Amélioration de la gestion des fichiers dans l'interface d'administration (suppression multiple, gestion des tentatives de réessai).
    - Mise à jour des documents légaux concernant les politiques de conservation des données.
- **Notifications :**
    - Envoi automatique d'un e-mail de notification dès qu'une transcription est prête.

### Évolutions techniques
- **Traitement Audio & IA :**
    - Mise en place de workers dédiés à l'extraction audio pour isoler et stabiliser les processus lourds.
    - Optimisation de la conversion audio pour la transcription et amélioration de la robustesse via FFmpeg.
    - Mise en place d'un suivi précis des temps de file d'attente et des résultats d'extraction.
- **Gestion des données & Stockage :**
    - Support des politiques de données spécifiques par domaine (multitenancy).
    - Optimisation du routage vers les buckets S3 et gestion des configurations via les variables d'environnement.
    - Amélioration de la gestion de la rétention des fichiers et des processus de purge.
- **Architecture Backend :**
    - Utilisation de files d'attente (queues) explicites pour l'ensemble des tâches asynchrones.
    - Sécurisation de l'exécution des commandes média et limitation de la concurrence pour les workers audio.
    - Amélioration de la gestion de la concurrence lors de la création de documents.

### Autres changements
- **Documentation :** Ajout massif de diagrammes techniques détaillant l'architecture globale, le routage des fichiers, les processus de transcription, les webhooks et l'authentification mobile.
- **Tests & CI/CD :** Renforcement de la couverture de tests (nettoyage audio, délais de rétention, stockage) et intégration de FFmpeg dans la chaîne de CI.
