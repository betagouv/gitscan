## Changelog : seves (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et la correction de bugs, notamment dans les modules TIAC et SSA. Des améliorations significatives ont été apportées aux formulaires, aux filtres et à la gestion des données, avec une attention particulière portée à la précision et à la fiabilité des informations affichées. L'intégration avec Mastro a été finalisée.

### Évolutions fonctionnelles
- Amélioration de la navigation dans SV avec une harmonisation du libellé.
- Ajout de l'organisme nuisible dans SV.
- Possibilité de choisir une date lors de l'envoi d'un message (note).
- Affichage de la catégorie de danger pour ICH sur SSA.
- Amélioration de l'affichage des établissements dans les cartes TIAC et SSA.
- Pré-remplissage du formulaire de conclusion basé sur les valeurs existantes.
- Correction de l'affichage des valeurs lors de la fermeture des modales Lieu et Repas sans sauvegarde.
- Amélioration de l'importation des données Agricoll pour les utilisateurs.
- Ajout d'un avertissement pour les enregistrements simples lorsque le nombre de personnes malades est supérieur ou égal à 10.
- Correction de l'édition et de l'annulation des valeurs dans l'établissement TIAC.
- Mise en place d'un nouveau treeselect pour l'investigation des cas humains (SSA) [#2038](https://github.com/betagouv/seves/issues/2038).
- Implémentation d'un nouveau treeselect sur les filtres d'événements SSA.
- Possibilité de voir les sous-objets ajoutés dans la même révision.

### Évolutions techniques
- Refactorisation des tests pour les messages SV afin d'utiliser des helpers.
- Amélioration de la sécurité des vues sur TIAC.
- Refactorisation du formulaire `Lieux` dans SV.
- Isolation du filtre treeselect legacy pour les événements en préparation de la nouvelle implémentation.
- Mise à jour des dépendances : Django, Django-DSFR, Redis, BeautifulSoup4, Ruff, Sentry-SDK, Django-reversion.
- Optimisation de la taille des instances Scalingo.
- Amélioration de la précision des tests pour TIAC.
- Correction de bugs liés à l'affichage des cases à cocher après la mise à jour de django-dsfr.
- Amélioration de la gestion des CSRF tokens.
- Correction de problèmes de tests sur TIAC et conclusion.
- Finalisation de l'intégration avec Mastro.

### Autres changements
- Ajout d'un avertissement dans le README.md concernant l'utilisation d'un merge-commit pour la MEP [#2030](https://github.com/betagouv/seves/issues/2030).
- Correction de typos.
- Ajout de tooltips sur la description pour la vue SSA.
- Correction de l'ordre des messages pour les notes avec date sélectionnée.
- Correction du nom de l'en-tête pour l'export CSV TIAC.
- Exclusion des membres de l'équipe SEVES de la désactivation du compte.
- Amélioration des tests pour les messages SV.
- Ajout de tests unitaires pour le composant `treeselect`.
- Correction de petits bugs d'interface utilisateur.
- Amélioration de la précision du CSP (Content Security Policy).
- Correction de problèmes de tests sur la suppression de documents.
- Correction de problèmes de tests sur TIAC.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de l'affichage des dates de révision pour les sous-objets.
- Mise à jour de la documentation.
