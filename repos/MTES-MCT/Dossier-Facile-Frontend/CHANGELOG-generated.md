## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de Dossier-Facile se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des informations des garants et des documents fiscaux. Des corrections de bugs ont également été apportées pour assurer la stabilité de l'application et améliorer la fiabilité des tests automatisés.

### Évolutions fonctionnelles
- L'adresse email du bénéficiaire est désormais obligatoire lors de la création d'un dossier. [#2005](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2005)
- Ajout de la possibilité de renseigner l'adresse email du garant naturel (caution). [#1999](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1999)
- Amélioration des messages d'erreur et d'information concernant l'analyse de la taxe foncière. [#1987](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1987) et [#1996](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1996)
- Modification du message concernant la déclaration d'honneur pour revenir à une version précédente. [#1988](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1988)
- Amélioration du message affiché lors d'une mauvaise classification d'un document lors de la revue de dossier. [#1995](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1995)
- Création d'un composant personnalisé pour la taxe foncière. [#1993](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1993)

### Évolutions techniques
- Correction d'un bug empêchant la navigation après validation d'un fichier et rechargement de la page. [#1997](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1997)
- Mise à jour des dépendances du projet. [#1998](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1998)
- Correction des tests E2E pour utiliser l'inscription native au lieu de FranceConnect. [#1986](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1986)
- Ajout d'un délai d'attente plus long pour l'analyse de la taxe foncière afin d'améliorer la fiabilité des tests. [#1989](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1989)
- Correction d'un problème de déconnexion FranceConnect après la suppression d'un locataire. [#1991](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1991)
- Ajout d'un scénario de test E2E pour les partenaires. [#1990](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/1990)
- Correction des tests E2E. [#2006](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2006)

### Autres changements
- Publication de la version V3.5.12.
