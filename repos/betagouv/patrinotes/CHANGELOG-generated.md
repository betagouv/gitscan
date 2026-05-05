## Changelog : patrinotes (30 derniers jours, au 4 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment en corrigeant des problèmes de crash de l'application et en améliorant la gestion des rapports. Des fonctionnalités ont été ajoutées pour faciliter l'intégration avec d'autres systèmes (CRVIF) et pour mieux identifier les utilisateurs. Des corrections ont également été apportées à l'affichage et à la gestion des données.

### Évolutions fonctionnelles
- Correction d'un crash de l'application lié au routeur frontend.
- Redirection des utilisateurs depuis le système CRVIF.
- Ajout d'un composant d'information pour les utilisateurs lors de l'inscription.
- Amélioration de l'affichage de la section "Clauses" dans le formulaire "ServiceInstructeurForm".
- Affichage du rapport uniquement après la sélection du MH (Monument Historique).
- Correction de l'affichage des rapports dupliqués sans sections.
- Ajout du nombre de "personnes_presentes" au PDF des rapports, et correction des requêtes de comptage du service de statistiques. [#70](https://github.com/betagouv/patrinotes/issues/70)
- Intégration des 2 derniers sprints dans l'application. [#69](https://github.com/betagouv/patrinotes/issues/69)
- Correction du label lors du dessin sur une image.
- Correction de la réinitialisation des données locales.

### Évolutions techniques
- Modification de l'identification des utilisateurs, utilisant l'adresse email au lieu de l'ID.
- Correction des migrations de la base de données.

### Autres changements
- Exclusion des pièces jointes des rapports PDF.
