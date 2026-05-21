## Changelog : meet (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration de l'expérience utilisateur, notamment en ajoutant des réactions, en améliorant l'accessibilité et en permettant la gestion des permissions de muting des participants. Des améliorations significatives ont également été apportées à la synchronisation de la configuration des salles et à l'intégration d'un support préliminaire pour un add-in Microsoft Outlook.

### Évolutions fonctionnelles
- Ajout de réactions pendant les réunions, y compris sur mobile. [#issue](https://github.com/suitenumerique/meet/issues/)
- Possibilité pour les administrateurs de configurer si tous les participants peuvent mettre en sourdine les autres. [#issue](https://github.com/suitenumerique/meet/issues/)
- Amélioration de l'accessibilité de la barre d'outils de réactions. [#issue](https://github.com/suitenumerique/meet/issues/)
- Ajout d'un support préliminaire (alpha) pour un add-in Microsoft Outlook. [#issue](https://github.com/suitenumerique/meet/issues/)
- Amélioration du texte du lien pour télécharger les transcriptions audio en français. [#issue](https://github.com/suitenumerique/meet/issues/)
- Amélioration de l'attribution des locuteurs dans les transcriptions. [#issue](https://github.com/suitenumerique/meet/issues/)

### Évolutions techniques
- Refactorisation du code frontend pour améliorer la clarté et la maintenabilité des composants liés aux réactions.
- Refactorisation du code backend pour simplifier la sérialisation des sources.
- Ajout d'un mécanisme de synchronisation pour les mises à jour de la configuration des salles.
- Amélioration de la gestion des erreurs et de la robustesse du processus d'enregistrement.
- Utilisation de `uv` pour la gestion des dépendances dans les agents.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité (Django, postcss, webpack-dev-server, pytest, urllib3).
- Amélioration de la configuration Nginx pour le frontend DINUM.
- Validation de la configuration des salles avec un schéma Pydantic.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Correction de problèmes mineurs dans l'add-in Outlook (alpha).
- Amélioration des logs pour l'attribution des locuteurs.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests unitaires pour le service d'authentification JWT.
- Ajout d'un support pour le format WebM dans les transcriptions.
- Correction d'un bug dans l'assignation des utilisateurs aux résultats du diarization.
- Amélioration de la gestion des polices pour l'accessibilité.
