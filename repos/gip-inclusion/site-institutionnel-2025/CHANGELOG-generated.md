## Changelog : site-institutionnel-2025 (30 derniers jours, au 2026-07-06)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'internationalisation (i18n) du site, notamment l'ajout de la gestion des traductions et des migrations associées. Des corrections et améliorations ont également été apportées à l'interface utilisateur, en particulier concernant la gestion des tags et du rich text, ainsi qu'à la gestion des médias.

### Évolutions fonctionnelles
- Ajout de la gestion de l'internationalisation (i18n) pour supporter plusieurs langues.
- Amélioration de l'affichage des tags : ajout d'un titre pour les tags sélectionnés et suppression de l'ordre imposé dans la liste des tags.
- Correction d'un problème d'alignement dans l'éditeur de texte riche (rich text).
- Ajout de la possibilité de choisir le niveau de titre (heading tag) dans le stepper.

### Évolutions techniques
- Amélioration des scripts de sauvegarde et restauration des médias, avec un nom de dossier spécifique et une gestion des erreurs plus robuste.
- Optimisation de la commande `tar` utilisée dans le script de restauration des médias.
- Ajout de vérifications pour éviter de relancer des migrations déjà exécutées.
- Correction d'une erreur dans le script de migration.

### Autres changements
- Ajout de commentaires dans le code pour une meilleure compréhension.
- Regénération des migrations et des traductions.
