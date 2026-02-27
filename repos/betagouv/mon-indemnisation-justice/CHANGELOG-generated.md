## Changelog : mon-indemnisation-justice (30 derniers jours)

### Résumé
Ce mois-ci, l'application mon-indemnisation-justice a bénéficié d'améliorations significatives concernant la gestion des pièces jointes, la création de déclarations à partir de brouillons et la documentation de l'architecture du projet. Des corrections ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de l'application. Enfin, l'environnement de développement a été mis à jour avec une version plus récente de PHP.

### Évolutions fonctionnelles
- Possibilité de supprimer une pièce jointe (#cdc3d99).
- Correction de l'affichage du numéro de dossier sur la vue dossier (#ca63e31).
- Correction de la création de déclarations à partir d'un brouillon (#7b2c33b).
- Affichage des pièces jointes téléversées par l'agent FDO sur la page dossier (#9aa32cd, #2430100, #2264331, #0e4f2ab).
- Transmission des pièces jointes du brouillon à la déclaration (#2264331).
- Affichage des pièces jointes immédiatement après leur téléversement (#2430100).
- Amélioration de l'affichage des champs de pièces jointes en fonction du rapport au logement (#cd29c42).

### Évolutions techniques
- Mise à jour de PHP vers la version 8.4 (#e284c30).
- Documentation de l'architecture du projet (#7d2c21f, #6863d9d).
- Restructuration des gabarits pour faciliter les tests (#4561929).
- Regroupement des migrations en une seule opération (#b19aff2).
- Réorganisation des routes de connexion pour éviter les conflits (#62da5dd).
- Amélioration de la publication des rapports de test (#5d752c9).

### Autres changements
- Mise à jour de la version de Firefox (#02c74a3).
- Mise à jour des documents avec l'avis (#598c4c1).
- Tests unitaires ajoutés (#a574d35).
- Activation de la modale (#8e273c0).
- Correction de la logique de dossier éditable (#476124b).
