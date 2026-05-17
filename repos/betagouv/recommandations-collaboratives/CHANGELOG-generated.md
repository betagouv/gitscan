## Changelog : recommandations-collaboratives (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur du CRM (gestion de la relation client), notamment la refonte de la présentation des utilisateurs, des projets et des notes. Des corrections ont également été apportées pour améliorer la gestion des notifications et des liens vers les démarches numériques. Des optimisations de performance et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- **CRM - Utilisateurs :** Nouvelle carte utilisateur pour le CRM, améliorant la présentation des informations. [#2056](https://github.com/betagouv/recommandations-collaboratives/pull/2056)
- **CRM - Projets :** Refonte de l'affichage des projets dans le CRM, incluant l'ajout d'informations sur les participants, les notes et l'historique. [#2018](https://github.com/betagouv/recommandations-collaboratives/pull/2018)
- **Notifications :** Correction du comportement des notifications de conversation, notamment le délai de consommation et l'ouverture du panneau associé. [#1989](https://github.com/betagouv/recommandations-collaboratives/pull/2024)
- **Recommandations :** Ajout d'un lien vers la ressource suggérée dans les conversations. [#2025](https://github.com/betagouv/recommandations-collaboratives/pull/2025)
- **Interface utilisateur :** Ajout d'informations contextuelles (infobulles) sur les éléments de l'interface, comme les boutons d'action et les en-têtes de colonnes.
- **Demarches Numériques :** Intégration d'informations sur les démarches numériques dans les cartes de recommandation et les tâches.
- **Gestion des fichiers :** Amélioration de la gestion des fichiers et ajout d'une fonctionnalité de téléchargement. [#1967](https://github.com/betagouv/recommandations-collaboratives/pull/2012)
- **Comptage des documents :** Correction du comptage des documents dans le CRM pour inclure tous les documents, et non seulement ceux de la conversation actuelle.
- **Suivi des activités :** Ajout d'informations sur les rappels et les prochaines actions.

### Évolutions techniques
- **Refactoring CRM :** Refactorisation du code du CRM pour améliorer la maintenabilité et la performance.
- **Tests Frontend :** Mise à jour et correction des tests frontend, notamment pour la gestion des notifications et des actions.
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Django, Wagtail, et les dépendances frontend (axios, postcss, dompurify, follow-redirects).
- **CI/CD :** Améliorations continues du pipeline CI/CD.
- **Sécurité :** Amélioration de la sanitisation des données pour prévenir les failles de sécurité.
- **Suppression de code obsolète :** Suppression de code obsolète lié à l'ancienne gestion des dossiers de démarches numériques (dsFolder).

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Nettoyage de code :** Nettoyage général du code pour améliorer la lisibilité et la maintenabilité.
- **Corrections de bugs mineurs :** Correction de plusieurs bugs mineurs liés à l'interface utilisateur et au comportement de l'application.
- **Amélioration des messages de log :** Ajout de messages de log plus informatifs pour faciliter le débogage.
- **Amélioration des tests :** Ajout de tests unitaires et d'intégration pour améliorer la couverture de code.
