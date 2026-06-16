## Changelog : patrinotes (30 derniers jours, au 15 juin 2026)

### Résumé
Cette version apporte des corrections de bugs et des améliorations concernant la génération de rapports de condition (CR), la gestion des mots de passe, et l'interface utilisateur. Une nouvelle fonctionnalité permet de sélectionner un métier et d'afficher une liste de personnes dans les rapports de condition.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la sauvegarde des détails de visite.
- Amélioration de la génération de PDF pour les rapports de condition :
  - Correction du texte des en-têtes et des listes à puces. [#71](https://github.com/betagouv/patrinotes/issues/71)
  - Ajout de la possibilité de sélectionner un métier et d'afficher une liste de personnes dans le rapport. [#71](https://github.com/betagouv/patrinotes/issues/71)
- Correction du problème empêchant la soumission du formulaire d'information avec la touche Entrée.
- Correction de l'affichage du nombre de pièces jointes lorsque celles-ci ont un libellé.
- Correction du maintien du libellé des images lors du chargement de plusieurs images.
- Correction d'un bug dans la route des statistiques d'administration, ajout d'une clause `WHERE` manquante.

### Évolutions techniques
- Correction d'un hotfix concernant la réinitialisation du mot de passe.

### Autres changements
- Préparation pour les sprints 6 et 7. [#75](https://github.com/betagouv/patrinotes/issues/75)
