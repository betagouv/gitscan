## Changelog : sites-conformes (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment l'ajout d'un système de notifications et l'amélioration de la gestion des traductions. Des efforts importants ont également été consacrés à l'amélioration de la qualité du code et à la mise en place de tests automatisés, en particulier des tests E2E avec Playwright.

### Évolutions fonctionnelles
- Ajout d'un panneau de notifications pour informer les utilisateurs des événements importants. Ce panneau inclut une date de début, un lien vers plus d'informations et est internationalisé. [#555](https://github.com/numerique-gouv/sites-conformes/issues/555)
- Amélioration de la gestion des traductions, notamment la correction d'erreurs et l'ajout de fichiers de traduction manquants.
- Ajout de la possibilité de choisir la balise de titre (heading) sur les composants stepper.
- Ajout d'une liste non ordonnée pour les tags.
- Amélioration de l'affichage des dates dans les entrées récentes d'événements.
- Ajout de la possibilité de choisir un titre pour les tags sélectionnés.

### Évolutions techniques
- Mise à jour des dépendances du projet. [#554](https://github.com/numerique-gouv/sites-conformes/issues/554)
- Refonte de l'implémentation des notifications, incluant une meilleure organisation du code, l'ajout de logs et une configuration pour les différentes branches.
- Utilisation de la version du package pour déterminer la version du site.
- Mise en place de tests E2E avec Playwright, incluant des tests de régression visuelle et une configuration pour l'environnement CI.
- Amélioration de la configuration et de l'exécution des tests Playwright pour éviter les blocages en CI.
- Utilisation de `manage.py` pour les commandes de traduction.
- Restructuration des scripts de gestion des médias locaux.
- Simplification de la gestion des migrations.

### Autres changements
- Ajout de traductions manquantes. [#553](https://github.com/numerique-gouv/sites-conformes/issues/553)
- Mise à jour de la documentation pour le projet Proconnect. [#547](https://github.com/numerique-gouv/sites-conformes/issues/547)
- Nettoyage du code et suppression de commentaires inutiles.
- Correction de problèmes de style CSS.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Correction de bugs mineurs et améliorations de la performance.
