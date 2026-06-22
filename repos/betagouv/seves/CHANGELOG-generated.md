## Changelog : seves (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'interface utilisateur et les fonctionnalités de Sèves, notamment avec l'implémentation d'un nouveau composant "treeselect" pour faciliter la sélection d'éléments dans plusieurs vues. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et la réactivité de l'application. L'intégration avec Mastro a été finalisée.

### Évolutions fonctionnelles
- Implémentation d'un nouveau composant "treeselect" pour filtrer les événements dans la section SSA (Surveillance Sanitaire Animale) [#2038](https://github.com/betagouv/seves/issues/2038).
- Amélioration de l'importation des données Agricoll pour les utilisateurs.
- Ajout d'un champ de date obligatoire pour les investigations TIAC (Troubles Infectieux et Allergiques).
- Ajout d'un champ "organisme nuisible" dans la section SV (Surveillance Végétale).
- Possibilité de sélectionner une date lors de l'envoi d'un message de note.
- Affichage amélioré des informations dans les blocs ARS (Agences Régionales de Santé).
- Finalisation de l'intégration avec Mastro, permettant une meilleure communication des données.
- Possibilité de voir les sous-objets ajoutés dans la même révision.
- Ajout d'un avertissement dans le README.md concernant l'utilisation d'un merge-commit pour la MEP.
- Amélioration de l'affichage des sauts de ligne dans les commentaires des fiches de zone délimitée et de détection.
- Correction d'une régression dans le formulaire `EvenementProduitForm` avec le nouveau treeselect.

### Évolutions techniques
- Refactorisation du code du composant "treeselect" pour permettre l'utilisation de querysets.
- Réduction de la taille des instances Scalingo pour optimiser les coûts.
- Mise à jour de plusieurs dépendances :
    - Django-dsfr (3.4.2 -> 3.5.1) [#2041](https://github.com/betagouv/seves/issues/2041)
    - Redis (7.4.0 -> 8.0.0) [#2032](https://github.com/betagouv/seves/issues/2032)
    - Sentry-sdk (2.60.0 -> 2.61.1) [#2033](https://github.com/betagouv/seves/issues/2033)
    - Ruff (0.15.16 -> 0.15.17, 0.15.15 -> 0.15.16, 0.15.14 -> 0.15.15, 0.15.13 -> 0.15.14)
    - Beautifulsoup4 (4.14.3 -> 4.15.0)
    - Django (6.0.5 -> 6.0.6)
    - pytest-rerunfailures (16.2 -> 16.3)
    - pytest-playwright (0.7.2 -> 0.8.0)
- Refactorisation du formset `lieux` dans la section SV.
- Isolation du treeselect legacy pour les filtres d'événements en préparation de la nouvelle implémentation.

### Autres changements
- Suppression de code mort.
- Amélioration de la précision des tests pour l'investigation TIAC.
- Correction de fautes de frappe.
- Amélioration des performances du bloc commun.
- Corrections de tests pour améliorer leur fiabilité.
- Correction d'une vulnérabilité XSS potentielle dans le numéro de rappel conso.
- Exclusion des documents de la structure MUS lors de l'envoi de notifications.
- Ajout de tooltips pour la description de la liste SSA.
- Ajout d'un placeholder dans l'éditeur de texte enrichi.
- Amélioration de la gestion des types MIME EML.
- Correction de l'ordre des messages pour les notes avec date sélectionnée.
- Amélioration de l'affichage des cases à cocher après la mise à jour vers django-dsfr 3.5.1.
- Ajout de couleurs différentes pour les niveaux 2+ dans les accordéons du treeselect.
- Correction de l'affichage du label complet avec les catégories dans le bouton du treeselect.
- Amélioration de la fiabilité de l'application account.
- Ajout de choixjs pour le filtre structure sur la page d'administration.
- Suppression d'un avertissement dans les tests de django-widget-tweaks.
- Amélioration des performances des tests.
- Correction d'un bug lié au nombre de résultats dans les choix de SV.
- Adaptation des exports Europhyt dans la section SV.
