## Changelog : envergo (30 derniers jours, au 25/08/2026)

### Résumé
Ce mois-ci, le projet a bénéficié d'une mise à jour majeure de son infrastructure pour garantir une meilleure stabilité, d'un renforcement important de la sécurité contre les failles XSS, et d'améliorations significatives de l'interface utilisateur. Ces évolutions visent notamment une meilleure utilisation sur mobile et une gestion plus intuitive des dossiers urgents et des formulaires de validation.

### Évolutions fonctionnelles
- **Interface et expérience utilisateur** :
    - Ajout de badges d'urgence dans la liste des dossiers et les résumés pour une meilleure visibilité.
    - Amélioration de l'ergonomie mobile, notamment via l'utilisation de fenêtres modales pour la saisie des données relatives aux haies.
    - Optimisation de la navigation avec l'intégration d'un système de pagination (DSFR) et une meilleure gestion de l'accessibilité.
    - Amélioration de la clarté des formulaires : nouveaux messages d'alerte, validation plus stricte des dates et des champs, et affichage des dates de demande de compléments.
- **Nouvelles fonctionnalités et contenus** :
    - Mise en place de nouveaux formulaires pour les vérifications "éviter/réduire" et les accusés de réception.
    - Mise à jour des coefficients de compensation par type.
    - Actualisation des informations de contact pour le CBN.

### Évolutions techniques
- **Sécurité** :
    - Correction de vulnérabilités XSS par l'échappement systématique des données soumises par les utilisateurs et renforcement de la validation côté backend [#1251](https://github.com/MTES-MCT/envergo/issues/1251).
    - Mise en place d'une politique de sécurité du contenu (CSP).
- **Infrastructure et Déploiement** :
    - Mise à jour majeure de la stack de déploiement (Scalingo, Node.js LTS et buildpack GDAL) [#1252](https://github.com/MTES-MCT/envergo/issues/1252).
    - Refonte complète du système de stockage des fichiers hébergés et optimisation des scripts de sauvegarde S3 [#1253](https://github.com/MTES-MCT/envergo/issues/1253).
    - Configuration de Nginx en amont de Gunicorn pour une meilleure gestion du serveur web.
- **Performance** :
    - Optimisation des requêtes SQL pour la liste des dossiers afin d'éviter les doublons et réduire la charge de la base de données [#1241](https://github.com/MTES-MCT/envergo/issues/1241).

### Autres changements
- **Tests** : Ajout de suites de tests dédiées pour la détection des vulnérabilités XSS et pour les tests de performance.
- **Maintenance** : Nettoyage du projet avec la suppression de Gulp et du code non utilisé.
