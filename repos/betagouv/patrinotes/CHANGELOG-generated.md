## Changelog : patrinotes (30 derniers jours, au 17 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la génération de rapports PDF, notamment en corrigeant des problèmes d'affichage et en s'assurant que toutes les informations pertinentes sont incluses. Des corrections de bugs ont également été apportées à l'interface utilisateur et à la gestion des formulaires. Enfin, une nouvelle fonctionnalité permet de sélectionner un métier et d'afficher une liste de personnes dans le compte rendu.

### Évolutions fonctionnelles
- Amélioration de la génération des rapports PDF :
    - Correction de l'affichage des images dans les PDF [#75](https://github.com/betagouv/patrinotes/issues/75).
    - Correction de la vitesse de dégradation dans les PDF.
    - Correction de l'affichage du représentant dans les PDF.
    - Correction de l'affichage des détails de la visite dans les PDF.
    - Correction de l'affichage des textes et des listes à puces dans les PDF [#75](https://github.com/betagouv/patrinotes/issues/75).
    - Sauvegarde correcte des détails de la visite.
- Ajout de la possibilité de sélectionner un métier et d'afficher une liste de personnes dans le compte rendu [#71](https://github.com/betagouv/patrinotes/issues/71).
- Correction du lien vers la FAQ.
- Correction d'une typo dans les emails.

### Évolutions techniques
- Correction d'une clause `WHERE` manquante dans la route des statistiques d'administration.
- Correction d'un problème empêchant l'envoi du formulaire infoform par la touche Entrée.
- Correction d'un problème lié à l'affichage du nombre de pièces jointes.
- Correction d'un problème lié à l'affichage des labels des images lors du chargement multiple.
- Correction d'un hotfix concernant la réinitialisation du mot de passe.

### Autres changements
- Mise à jour des sprints 6 et 7 [#75](https://github.com/betagouv/patrinotes/issues/75).
