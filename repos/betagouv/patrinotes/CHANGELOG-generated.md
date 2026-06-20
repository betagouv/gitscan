## Changelog : patrinotes (30 derniers jours, au 18 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la génération de rapports PDF, notamment concernant la mise en page des images et des informations de visite. Des corrections ont également été apportées pour améliorer la stabilité de la réinitialisation du mot de passe et la sauvegarde des détails de visite. Enfin, des ajustements ont été faits à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Amélioration de la génération des rapports PDF :
    - Correction de l'affichage des images dans les rapports PDF [#71](https://github.com/betagouv/patrinotes/issues/71).
    - Correction de la représentation des informations de visite dans les rapports PDF.
    - Amélioration de la vitesse de génération des rapports PDF.
    - Correction de typos dans les emails.
- Ajout de la sélection de métier et de la liste des personnes dans les comptes rendus [#71](https://github.com/betagouv/patrinotes/issues/71).
- Correction du lien vers la FAQ [#71](https://github.com/betagouv/patrinotes/issues/71).
- Correction de la sauvegarde des détails de visite.
- Correction pour empêcher la soumission du formulaire par la touche Entrée.

### Évolutions techniques
- Correction d'une clause `WHERE` manquante dans la route des statistiques d'administration [#71](https://github.com/betagouv/patrinotes/issues/71).
- Correction d'un problème de réinitialisation du mot de passe [#71](https://github.com/betagouv/patrinotes/issues/71).
- Suppression des balises `<unbreakable />` inutiles.

### Autres changements
- Préparation des sprints 6 et 7 [#75](https://github.com/betagouv/patrinotes/issues/75).
- Amélioration de l'affichage du nombre de pièces jointes.
- Correction de l'affichage des labels des images lors du téléchargement.
- Correction du texte des en-têtes et des listes à puces dans les rapports PDF.
