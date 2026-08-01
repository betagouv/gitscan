## Changelog : sites-conformes (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant la gestion des notifications, notamment l'ajout d'un panneau d'information et la gestion des dates. Des efforts considérables ont également été déployés pour améliorer la qualité et la fiabilité des tests, avec l'introduction de tests end-to-end (e2e) avec Playwright et des corrections pour stabiliser l'environnement de test. Enfin, des corrections de bugs et des améliorations de l'expérience utilisateur ont été apportées, notamment pour la gestion des traductions et l'affichage des pages d'erreur.

### Évolutions fonctionnelles
- Ajout d'un panneau d'information pour afficher des notifications aux utilisateurs. Ce panneau inclut une date de début, un lien vers plus d'informations et est internationalisé. [#555](https://github.com/numerique-gouv/sites-conformes/issues/555)
- Amélioration de l'affichage de la barre de recherche avec l'affichage de la requête actuelle.
- Correction des pages d'erreur 404 et 500 pour assurer un affichage correct du design système.
- Ajout d'une version conditionnelle des pages lors du chargement en iframe pour une meilleure compatibilité. [#551](https://github.com/numerique-gouv/sites-conformes/issues/551)
- Correction d'un bug empêchant la traduction d'une page avec un bloc ImageBlock imbriqué.
- Mise à jour des traductions et correction des erreurs liées à la gestion des fichiers de traduction.

### Évolutions techniques
- Introduction de tests end-to-end (e2e) avec Playwright pour une meilleure couverture des tests et une détection précoce des régressions.
- Mise en place d'un pipeline CI/CD pour l'exécution des tests e2e, incluant la comparaison visuelle avec la branche principale.
- Optimisation de l'installation de Playwright dans le pipeline CI/CD pour éviter les blocages.
- Refactorisation du code lié aux notifications pour une meilleure organisation et maintenabilité.
- Utilisation de `pyproject.toml` comme source principale pour la version du projet.
- Amélioration de la gestion des versions à travers les différents modes de déploiement.
- Mise à jour des dépendances du projet. [#554](https://github.com/numerique-gouv/sites-conformes/issues/554)
- Ajout de tests unitaires pour la gestion des notifications.
- Simplification de la configuration des tests e2e.
- Correction de problèmes liés à l'affichage du design système (DSFR) sur les pages d'erreur.

### Autres changements
- Ajout de documentation pour proconnect après packagification. [#547](https://github.com/numerique-gouv/sites-conformes/issues/547)
- Ajout de traductions manquantes. [#553](https://github.com/numerique-gouv/sites-conformes/issues/553)
- Mise à jour de la version de `tarteaucitronjs` à 1.33.0. [#552](https://github.com/numerique-gouv/sites-conformes/issues/552)
- Nettoyage du code et suppression de commentaires inutiles.
- Amélioration de la structure des fichiers et des répertoires.
- Correction de problèmes mineurs d'affichage et de style.
