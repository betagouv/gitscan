## Changelog : mon-indemnisation-justice (30 derniers jours)

### Résumé
Ce mois-ci, l'application mon-indemnisation-justice a bénéficié d'améliorations significatives concernant la gestion des pièces jointes et des brouillons de déclaration. Les agents de l'administration pourront désormais mieux gérer les documents, supprimer des pièces jointes, et voir les pièces jointes téléversées par les agents FDO. L'architecture du projet a également été documentée et la version de PHP a été mise à jour.

### Évolutions fonctionnelles
- Permet la suppression d'une pièce jointe (#cdc3d99).
- Affiche les pièces jointes téléversées par l'agent FDO sur la page dossier (#9aa32cd).
- Corrige la création de déclaration à partir d'un brouillon (#7b2c33b).
- Affiche les pièces jointes après leur téléversement (#2430100).
- Transmet les pièces jointes du brouillon à la déclaration (#2264331).
- Lie le modèle de déclaration FDO et son brouillon aux pièces jointes (#0e4f2ab).
- Exclut le brouillon de la liste après sa soumission (#967b44d).
- Affine l'affichage des champs de pièces jointes selon le rapport au logement (#cd29c42).
- Rectifie la logique de dossier éditable (#476124b).
- Rectifie l'affichage du numéro sur la vue dossier (#ca63e31).
- Mise à jour des documents avec l'avis (#598c4c1).

### Évolutions techniques
- Mise à jour de PHP en version 8.4 (#e284c30).
- Documentation de l'architecture du projet (#7d2c21f).
- Fusion des migrations en une seule (#b19aff2).
- Ajout de tests unitaires (#a574d35).
- Amélioration de la publication des rapports de test (#5d752c9).
- Restructuration des gabarits pour faciliter les tests (#4561929).

### Autres changements
- Correction d'un bug Sentry : message d'erreur "aucun fichier sélectionné" (#3a51c0a).
- Activation de la modale (#8e273c0).
- Premier jet du brouillon générique : déclaration de la méthode patch (#ab200fe).
- Tests du rendu du corps et du document (#dec05ef).
