## Changelog : france-chaleur-urbaine (30 derniers jours)

### Résumé
Les dernières mises à jour de france-chaleur-urbaine se concentrent sur l'amélioration de l'expérience utilisateur, notamment sur le formulaire d'éligibilité et les fiches réseaux, ainsi que sur l'ajout de nouvelles fonctionnalités de suivi et d'analyse. Des corrections de bugs et des refactorings techniques ont également été réalisés pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Correction d'un bug sur le flag "ouvert" au raccordements sur la fiche réseau (#1192).
- Amélioration du formulaire d'éligibilité :
    - Remplacement des checkbox par une liste déroulante pour une meilleure expérience utilisateur (#1194).
    - Correction d'un bug de réinitialisation du tag (#1192).
    - Ajout d'un champ commentaire sur le tag pour la vue statistique par tag.
- Ajout d'un CTA vers le comparateur de coûts avec suivi analytics (#1199).
- Suppression de la bannière du comparateur de coûts.
- Correction du test d'adresse, suppression du cas particulier Bordeaux.
- Masquage de l'encart "non ouvert" pour les réseaux de froid.
- Ajout d'un grand textarea dans une dialog pour les commentaires longs.
- Ajout d'un commentaire sur l'état initial du formulaire de test en masse.

### Évolutions techniques
- Intégration du suivi analytics via PostHog (#1203).
- Refactorisation du code lié aux données open data (#1205) : déplacement des fichiers dans un module et suppression de documentation obsolète.
- Refactorisation de la configuration des tuiles API et génération.
- Passage de TypeScript en dépendances.
- Suppression de composants inutilisés et de fichiers obsolètes.
- Utilisation de `cx` pour une meilleure lisibilité du code.
- Amélioration de la gestion des données et des requêtes.
- Correction de la gestion de l'affectation des gestionnaires.

### Autres changements
- Remplacement du logo de la République Française par une version SVG.
- Harmonisation des styles suite à la conversion du markdown en HTML.
- Ajout d'événements Matomo pour le suivi des actions utilisateurs.
- Suppression d'un fichier de configuration inutile.
- Suppression du fichier `CLAUDE.md`.
- Correction de l'évenement tag_comment_updated.
- Ajout de l'évenement à la config analytics.
