## Changelog : mon-indemnisation-justice (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à l'application mon-indemnisation-justice au cours des 30 derniers jours. Les principales évolutions concernent la gestion des pièces jointes, la correction de bugs liés aux brouillons de déclaration et l'amélioration de la documentation de l'architecture du projet. Une mise à jour de la version de PHP a également été effectuée.

### Évolutions fonctionnelles
- Possibilité de supprimer une pièce jointe (#cdc3d99).
- Correction de l'affichage du numéro de dossier sur la vue dossier (#ca63e31).
- Correction de la création de déclaration à partir d'un brouillon (#7b2c33b).
- Affichage des pièces jointes téléversées par l'agent FDO sur la page dossier (#9aa32cd).
- Les pièces jointes sont maintenant transmises du brouillon à la déclaration (#2264331).
- Liaison du modèle de déclaration FDO et de son brouillon aux pièces jointes (#0e4f2ab).
- Exclusion du brouillon de la liste après sa soumission (#967b44d).
- Amélioration de l'affichage des champs de pièces jointes selon le rapport au logement (#cd29c42).
- Correction d'un bug Sentry concernant l'absence de fichier sélectionné (#3a51c0a).
- Suppression d'un brouillon rafraîchit instantanément la liste (#ff07eff).

### Évolutions techniques
- Mise à jour de PHP vers la version 8.4 (#e284c30).
- Documentation de l'architecture du projet (#7d2c21f).
- Restructuration des gabarits pour faciliter les tests (#4561929).
- Fusion des migrations en une seule opération (#b19aff2).
- Ajout de tests unitaires (#a574d35).

### Autres changements
- Mise à jour des documents avec l'avis (#598c4c1).
- Tests du rendu du corps et du document (#dec05ef).
- Amélioration de la publication des rapports de test (#5d752c9).
- Conservation du rôle ROLE_AGENT lors de la mise à jour d'un agent (#ddc5f7b).
- Activation de la modale (#8e273c0).
- Premier jet pour un brouillon générique avec déclaration de la méthode patch (#ab200fe).
- Affichage des pièces jointes après leur téléversement (#2430100).
