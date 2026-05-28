## Changelog : patrinotes (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'application patrinotes a bénéficié d'améliorations significatives concernant la synchronisation des données, la gestion des rapports d'état et l'expérience utilisateur lors de la création de compte. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des rapports d'état et de leurs pièces jointes.
- Ajout d'une liste de personnes présentes et du comptage des services dans les rapports PDF.  [#70](https://github.com/betagouv/patrinotes/issues/70)
- Redirection des utilisateurs depuis CRVIF.
- Amélioration de la présentation du formulaire d'inscription avec l'ajout d'un composant d'information pour l'utilisateur. [#71](https://github.com/betagouv/patrinotes/issues/71)
- Affichage conditionnel du rapport après la sélection du MH (Monument Historique).
- Sélection du responsable de la mission et liste des personnes présentes dans le Compte Rendu.

### Évolutions techniques
- Mise à jour des données de population (pop data).
- Correction d'un crash du routeur frontend.
- Correction des migrations de la base de données.
- Utilisation de l'email pour identifier les utilisateurs au lieu de l'ID interne.
- Correction de problèmes liés à la réinitialisation des données locales.

### Autres changements
- Amélioration de l'étiquette lors du dessin sur une image.
- Correction de l'affichage des sections dans le formulaire `ServiceInstructeurForm`.
- Correction d'un bug empêchant la duplication de rapports sans sections.
- Exclusion des pièces jointes PDF des rapports lors de certaines opérations.
