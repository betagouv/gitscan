## Changelog : meet (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'introduction de fonctionnalités de "picture-in-picture" (PiP) pour les documents, l'amélioration des réactions, et l'ajout de la possibilité de couper le son des autres participants en fonction de la configuration de la salle. Des corrections et des optimisations ont également été apportées, notamment concernant la sécurité et la gestion des configurations. Enfin, un support initial pour un add-in Microsoft Outlook est disponible en version alpha.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité "picture-in-picture" (PiP) pour les documents, incluant une barre de contrôle, un menu d'options et un indicateur de connexion.
- Amélioration de la réactivité et de l'accessibilité de la barre d'outils de réactions, avec prise en charge sur mobile.
- Possibilité pour les participants de couper le son des autres en fonction de la configuration de la salle.
- Amélioration de l'assignation des intervenants lors de la transcription.
- Ajout d'un lien direct vers l'ouverture des enregistrements dans les emails.
- Support initial (alpha) d'un add-in Microsoft Outlook.
- Clarification du texte du lien de téléchargement des transcriptions audio en français.

### Évolutions techniques
- Refactorisation du code frontend pour améliorer la clarté et la maintenabilité, notamment des composants liés aux réactions et aux strips.
- Utilisation de `uv` pour la gestion des dépendances dans certains composants.
- Amélioration de la synchronisation de la configuration de la salle entre le backend et le frontend.
- Validation de la configuration de la salle avec un schéma Pydantic.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer les performances (Django, PostCSS, Pytest, Webpack-dev-server, urllib3).
- Amélioration de la robustesse du processus de démarrage de l'enregistrement.
- Refactorisation du code lié à l'identité de l'appelant.
- Amélioration de la gestion des jetons CSRF.
- Ajout de tests unitaires pour le service de jetons JWT.

### Autres changements
- Mise à jour de la documentation et du changelog.
- Correction de bugs mineurs liés à l'interface utilisateur (espacement, positionnement des tooltips, titres de page PiP).
- Amélioration des logs pour le débogage de l'assignation des intervenants.
- Correction d'un problème de boucle de reconnexion.
- Suppression des exigences de `buildpack requirements.txt` au profit de `uv.lock`.
- Mise à jour de la configuration Nginx pour le frontend DINUM.
- Correction d'un bug dans le label du lien de transcription audio.
- Mise à jour des terminologies liées aux rôles pour la localisation.
