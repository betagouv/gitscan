## Changelog : amidomar-cms (30 derniers jours, au 25 juin 2026)

### Résumé
Cette mise à jour améliore principalement l'expérience utilisateur et la gestion des contenus, notamment en ajoutant des fonctionnalités d'internationalisation (i18n) et en améliorant l'interface de gestion des tags et des titres. Des améliorations ont également été apportées aux scripts de gestion des médias.

### Évolutions fonctionnelles
- Ajout de la gestion de l'internationalisation (i18n) pour supporter plusieurs langues.
- Amélioration de l'interface de gestion des tags :
  - Ajout d'une liste non ordonnée pour les tags.
  - Ajout d'un titre pour les tags sélectionnés.
- Possibilité de choisir la balise de titre (heading tag) dans le stepper.
- Correction d'un problème d'alignement des divs dans l'éditeur de texte riche (richtext).
- Ajout de commentaires pour faciliter la compréhension du code.

### Évolutions techniques
- Amélioration des scripts de sauvegarde et restauration des médias :
  - Nommage spécifique du dossier média pour les scripts de descente et de restauration.
  - Amélioration de la gestion des sorties et des erreurs.
  - Optimisation de la commande `tar` dans le script `restore_local_medias.sh`.
- Correction et amélioration du script de migration.
- Vérification de l'exécution préalable des migrations pour éviter les erreurs.

### Autres changements
- Mise à jour de la documentation pour le connecteur Proconnect après la packagification. [#547](https://github.com/MTES-MCT/amidomar-cms/issues/547)
- Suppression temporaire de commentaires dans un script de migration pour faciliter le déploiement sur Scalingo.
