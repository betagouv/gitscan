## Changelog : meet (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment l'ajout de réactions, l'amélioration de l'accessibilité et la gestion des permissions de muting. Des travaux importants ont également été réalisés sur l'infrastructure backend pour supporter de nouvelles fonctionnalités comme les add-ons et la configuration dynamique des salles. L'intégration initiale d'un add-in pour Microsoft Outlook est également disponible en version alpha.

### Évolutions fonctionnelles
- Ajout de réactions pendant les réunions, y compris sur mobile. [#issue](https://github.com/suitenumerique/meet/issues/)
- Possibilité pour les administrateurs de configurer si tout le monde peut mettre en sourdine les autres participants. [#issue](https://github.com/suitenumerique/meet/issues/)
- Amélioration de l'accessibilité de la barre d'outils de réactions.
- Intégration initiale (alpha) d'un add-in pour Microsoft Outlook.
- Amélioration du texte du lien de téléchargement des transcriptions audio en français.
- Support du format WebM pour les transcriptions.
- Amélioration de l'assignation des intervenants.

### Évolutions techniques
- Refactor de composants frontend pour une meilleure clarté et maintenabilité.
- Simplification de la sérialisation des sources.
- Synchronisation des mises à jour de la configuration des salles entre le frontend et le backend.
- Amélioration de la gestion des erreurs et de la robustesse du processus d'enregistrement.
- Mise à jour de la gestion des dépendances avec l'utilisation de `uv`.
- Validation de la configuration des salles avec un schéma Pydantic.
- Amélioration de la sécurité avec la validation de la présence des participants avant les opérations de mise en sourdine.
- Refactor de la récupération de l'identité de l'appelant.
- Amélioration de la gestion des jetons d'authentification.
- Ajout de tests unitaires pour le service de jetons JWT.
- Configuration de l'encodage des enregistrements LiveKit Egress est maintenant configurable.
- Ajout de support pour plusieurs workers de transcription.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Corrections de bugs mineurs dans l'interface utilisateur et le backend.
- Amélioration des logs pour le suivi de l'assignation des intervenants.
- Mise à jour de plusieurs dépendances (django, postcss, webpack-dev-server, pytest).
- Correction d'un bug lié à la boucle de reconnexion.
- Correction d'un problème de régression de l'espacement dans la barre de contrôle mobile.
- Correction d'un problème lié à la génération des IDs de salles.
- Correction d'un bug dans l'assignation des utilisateurs aux résultats de la diarisation.
- Amélioration de la gestion des polices d'accessibilité.
