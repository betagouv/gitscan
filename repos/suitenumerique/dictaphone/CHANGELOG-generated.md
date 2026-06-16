## Changelog : dictaphone (30 derniers jours, au 15 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application mobile, notamment en matière de gestion des enregistrements hors ligne, de sélection de la langue de transcription et de robustesse générale. L'interface utilisateur web a également été améliorée avec de nouvelles fonctionnalités d'exportation de transcriptions et une meilleure accessibilité. Des corrections de bugs et des optimisations de sécurité ont été apportées à l'ensemble du projet.

### Évolutions fonctionnelles
- **Mobile :** Ajout de la possibilité de télécharger un fichier non uploadé. [#1234](https://github.com/suitenumerique/dictaphone/issues/1234)
- **Mobile :** Amélioration de la gestion des enregistrements hors ligne : enregistrement local des fichiers audio, suppression automatique des fichiers locaux après l'upload, et gestion des erreurs de synchronisation.
- **Mobile :** Ajout de la sélection de la langue de transcription avant l'enregistrement.
- **Mobile :** Ajout de sons de démarrage et d'arrêt d'enregistrement.
- **Web :** Ajout de la possibilité d'exporter les transcriptions au format SRT.
- **Web :** Ajout de boutons pour copier le texte de la transcription et ouvrir le document dans Indocs.
- **Web :** Amélioration de l'interface utilisateur de la liste des enregistrements.
- **Web :** Ajout d'un indicateur visuel de l'état de la transcription.
- **Web :** Ajout d'un tooltip sur le bouton d'upload pour indiquer la taille maximale autorisée.
- **Web :** Amélioration de l'accessibilité de l'application (étiquettes ARIA, titres, etc.).
- **Backend :** Ajout de la possibilité de spécifier la langue de transcription lors de la création d'un fichier.
- **Backend :** Amélioration de la gestion des erreurs et ajout de codes d'erreur plus précis.
- **Backend :** Prise en charge de davantage de formats audio/vidéo.

### Évolutions techniques
- **Backend :** Mise à jour de Python vers la version 3.14.5 et de Django vers la version 5.12.4.
- **Frontend :** Mise à jour des dépendances pour corriger des vulnérabilités de sécurité (React, i18next, etc.).
- **Frontend :** Utilisation de Node 24.
- **Backend :** Amélioration de la suppression des données S3 après la transcription.
- **Backend :** Implémentation de la gestion automatique de la politique de confidentialité des données.
- **Helm :** Ajout de tâches cron pour la suppression des fichiers originaux et la suppression définitive des fichiers.
- **Frontend :** Refactoring du code pour améliorer la performance et la maintenabilité.
- **Frontend :** Amélioration de la gestion de l'état du composant d'enregistrement.
- **Frontend :** Rework du composant d'enregistrement avec indicateur de niveau audio.
- **Mobile :** Mise à jour de l'API React Native Audio.

### Autres changements
- Ajout d'un lien vers la salle Matrix du projet dans le README.
- Mise à jour de la documentation légale.
- Correction de bugs mineurs et améliorations de la robustesse de l'application.
- Ajout de logs pour faciliter le débogage des problèmes de connexion mobile.
- Amélioration de la configuration des logs.
- Correction de vulnérabilités de sécurité identifiées par Snyk.
