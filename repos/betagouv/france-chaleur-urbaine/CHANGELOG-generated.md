## Changelog : france-chaleur-urbaine (30 derniers jours)

### Résumé
Les dernières mises à jour de france-chaleur-urbaine se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur le formulaire d'éligibilité et la gestion des commentaires. Des améliorations techniques ont également été apportées pour optimiser la gestion des données, la configuration des tuiles et l'intégration d'outils d'analyse. Enfin, une migration progressive du markdown vers du HTML est en cours pour améliorer la cohérence visuelle.

### Évolutions fonctionnelles
- Le formulaire d'éligibilité a été amélioré avec le remplacement des checkboxes par des listes déroulantes pour une meilleure expérience utilisateur (#1194).
- Correction d'un bug concernant la réaffection des gestionnaires (#1197).
- Amélioration du formulaire de test en masse pour corriger l'état initial (#1198).
- Suppression de la bannière du comparateur de coûts.
- Ajout d'un champ commentaire sur les tags pour la vue statistiques par tag.
- Le CTA vers le comparateur affiche maintenant un événement Matomo pour le suivi.
- Le message d'avertissement pour Paris a été factorisé et amélioré.
- Masquage de l'encart "non ouvert" pour les réseaux de froid.

### Évolutions techniques
- Intégration de PostHog pour le suivi analytics (#1203).
- Refactorisation du code lié aux données open data (#1205) : déplacement des fichiers dans un module et suppression de documentation obsolète.
- Passage de TypeScript en dépendances.
- Harmonisation de la configuration des tuiles API et de leur génération.
- Extraction des tables synchronisées Airtable dans une structure dédiée.
- Suppression de tables Airtable obsolètes.
- Amélioration de la gestion des données lors de la modification d'un commentaire sur un tag.
- Conversion progressive du markdown en HTML pour les textes d'éligibilité.
- Utilisation de `cx` pour une meilleure gestion des classes CSS.
- Remplacement de certains composants par des alternatives plus modernes (FCUArrowIcon, button-link, arrow-item).

### Autres changements
- Ajout du logo de la République Française en SVG pour une meilleure qualité visuelle.
- Suppression de fichiers inutilisés et de composants non utilisés.
- Ajout d'un événement à la configuration analytics.
- Suppression du fichier `CLAUDE.md`.
- Correction d'une adresse de test dans le formulaire d'éligibilité.
- Ajout d'un libellé pour l'événement `tag_comment_updated`.
- Suppression de puces inutiles et harmonisation des styles suite au passage markdown -> html.
