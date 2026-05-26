## Changelog : patrinotes (30 derniers jours, au 10 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la synchronisation des données, notamment des rapports et de leurs pièces jointes, ainsi que sur l'expérience utilisateur lors de l'inscription et de la manipulation des rapports. Des corrections de bugs ont également été apportées pour améliorer la stabilité de l'application.

### Évolutions fonctionnelles
- Amélioration du formulaire d'inscription avec l'ajout d'un composant d'information pour l'utilisateur [#69](https://github.com/betagouv/patrinotes/issues/69).
- Synchronisation des rapports d'état et de leurs pièces jointes.
- Redirection des utilisateurs depuis CRVIF.
- Affichage du rapport après la sélection du MH (Maître d'Hôtel).
- Amélioration de l'affichage des statistiques du service et ajout du nombre de "personnes_presentes" au PDF [#70](https://github.com/betagouv/patrinotes/issues/70).
- Ajout des 2 derniers sprints au rapport.

### Évolutions techniques
- Mise à jour de la gestion des identifiants utilisateurs, utilisant l'adresse email au lieu de l'ID interne.
- Correction d'un crash du routeur frontend.
- Correction de problèmes liés aux migrations de la base de données.
- Correction de problèmes de réinitialisation des données locales.

### Autres changements
- Correction de l'étiquette lors du dessin sur une image.
- Correction de l'exclusion des pièces jointes PDF lors de la synchronisation.
- Ajustement de la mise en page de la section "Clauses" dans le formulaire "ServiceInstructeurForm".
- Correction d'un bug de duplication sans sections.
- Mise à jour des données POP.
