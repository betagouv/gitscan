## Changelog : seves (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les modules de gestion des cas humains (SSA) et des enquêtes sanitaires (SV). L'intégration avec Mastro progresse, et des corrections ont été apportées pour améliorer la fiabilité et la performance de l'application. Des améliorations de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- **SSA (Cas Humains):**
    - Nouveau sélecteur d'arbre (treeselect) pour l'investigation des cas humains [#2038](https://github.com/betagouv/seves/issues/2038).
    - Amélioration de l'affichage des dates dans l'historique des événements.
- **SV (Enquêtes Sanitaires):**
    - Affichage amélioré des commentaires des fiches de zone délimitée et de détection au format HTML.
    - Ajout d'un bloc "éléments infestés" au formulaire SV, incluant l'affichage des lieux et prélèvements associés.
    - Possibilité de choisir une date lors de l'envoi d'un message de note.
    - Correction d'une régression sur le formulaire `EvenementProduitForm` avec le nouveau treeselect.
    - Amélioration de l'affichage des lieux et prélèvements sur la page de détails.
    - Possibilité de télécharger des données au format ZIP.
- **Général:**
    - Intégration avec Mastro finalisée [#1010cb5](https://github.com/betagouv/seves/pull/1010cb5).
    - Correction d'une vulnérabilité XSS potentielle liée au numéro de rappel conso.
    - Amélioration de la gestion des documents et des notifications.
    - Possibilité de voir les sous-objets ajoutés dans la même révision.

### Évolutions techniques
- **Dépendances:**
    - Mise à jour de Django (6.0.5 -> 6.0.6).
    - Mise à jour de Django-DSFR (3.4.2 -> 3.5.1).
    - Mise à jour de Redis (7.4.0 -> 8.0.0).
    - Mise à jour de Ruff (0.15.14 -> 0.15.16).
    - Mise à jour de Sentry-SDK (2.60.0 -> 2.61.1).
    - Mise à jour de Beautifulsoup4 (4.14.3 -> 4.15.0).
    - Mise à jour de Playwright (1.59.0 -> 1.60.0).
    - Mise à jour de pytest-rerunfailures (16.1 -> 16.3).
    - Mise à jour de pytest-playwright (0.7.2 -> 0.8.0).
    - Mise à jour de idna (3.7 -> 3.15).
    - Mise à jour de django-reversion (6.1.0 -> 6.2.0).
    - Mise à jour de gunicorn (25.3.0 -> 26.0.0).
    - Mise à jour de urllib3 (2.6.3 -> 2.7.0).
- **Refactoring & Performance:**
    - Refactorisation du formulaire `lieux`.
    - Optimisation des performances du bloc commun.
    - Amélioration de la fiabilité des tests.
    - Suppression de la limite de caractères sur le numéro RASFF dans SV.
- **Autres:**
    - Ajout d'un avertissement dans le README concernant l'utilisation de merge-commits pour la MEP.
    - Suppression du feature flag pour l'éditeur de texte enrichi.

### Autres changements
- Ajout de webhooks pour notifier Maestro.
- Changement d'URL de l'API BAN.
- Amélioration de la gestion des droits d'administration.
- Correction de problèmes d'affichage des sauts de ligne dans les commentaires.
- Suppression d'un avertissement dans les tests de django-widget-tweaks.
- Ajout de différentes couleurs pour les niveaux d'accordéon dans le treeselect.
- Amélioration de la gestion des dates de réception.
- Ajout de choixjs pour le filtre de structure sur la page d'administration.
- Correction d'un problème de type MIME EML.
- Exclusion des documents de la structure MUS lors de l'envoi de notifications.
- Nettoyage du code pour `choice_js_fill`.
- Amélioration de la fiabilité des tests pour SV.
- Modification de l'approche de mise à jour dans SV.
