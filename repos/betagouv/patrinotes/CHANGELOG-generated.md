## Changelog : patrinotes (30 derniers jours, au 10 mai 2026)

### Résumé
Les dernières mises à jour de Patrinotes se concentrent sur l'amélioration de la synchronisation des données, notamment des rapports et de leurs pièces jointes, ainsi que sur l'expérience utilisateur lors de l'inscription et de la gestion des formulaires. Des corrections de bugs ont également été apportées pour stabiliser l'application et améliorer sa fiabilité.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des rapports d'état et de leurs pièces jointes.
- Redirection des utilisateurs depuis CRVIF.
- Ajout d'un composant d'information (Notice) au formulaire d'inscription pour fournir des informations aux utilisateurs.
- Affichage du rapport uniquement après la sélection du MH (Maître d'Hôtel).
- Correction de l'affichage des sections lors de la duplication d'un rapport.
- Ajout du nombre de personnes présentes au PDF généré pour les rapports [#70](https://github.com/betagouv/patrinotes/issues/70).
- Ajout des 2 derniers sprints à l'application [#69](https://github.com/betagouv/patrinotes/issues/69).
- Mise à jour de la mise en page du formulaire `ServiceInstructeurForm` pour la section Clauses.

### Évolutions techniques
- Mise à jour de l'identification des utilisateurs par l'adresse email au lieu de l'ID interne.
- Correction d'un crash du routeur frontend.
- Correction des migrations de la base de données.
- Correction de la réinitialisation des données locales.
- Correction du label lors du dessin sur une image.

### Autres changements
- Mise à jour des données POP.
- Exclusion des pièces jointes PDF des rapports lors de la synchronisation.
