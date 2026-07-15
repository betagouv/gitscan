## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 8 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des dossiers locataires, notamment concernant l'analyse des documents de taxe foncière et la gestion des garants. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Taxe foncière :**
    - Ajout de nouveaux messages d'analyse pour les documents de taxe foncière [#1987](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1987).
    - Amélioration de la gestion des erreurs liées à la feuille de taxe foncière [#1996](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1996).
    - Création d'un composant personnalisé pour la taxe foncière [#1993](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1993).
    - Augmentation du délai d'attente pour l'analyse de la taxe foncière afin d'améliorer la fiabilité [#1989](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1989).
- **Garantie :** Ajout de l'adresse email du garant naturel [#1999](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1999).
- **Déconnexion FranceConnect :** Correction d'un bug qui empêchait la déconnexion FranceConnect après la suppression d'un locataire [#1991](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1991).
- **Message d'honneur :** Rétrogradation du message concernant la déclaration sur l'honneur [#1988](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1988).
- **Classification IA :** Modification du message d'IA lors d'une mauvaise classification de document dans la revue de dossier [#1995](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1995).

### Évolutions techniques
- Mise à jour des dépendances du projet [#1998](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1998).
- Utilisation de l'inscription native au lieu de FranceConnect dans les tests E2E [#1986](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1986).
- Correction d'une erreur de navigation lors du rechargement de la page après la validation d'un fichier [#1997](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1997).
- Ajout d'un scénario de test E2E pour les partenaires [#1990](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1990).
- Contournement de l'analyse pour l'enregistrement automatique dans le cas du locataire v3 [#1992](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1992).
