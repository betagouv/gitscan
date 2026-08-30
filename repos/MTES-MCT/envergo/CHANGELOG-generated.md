## Changelog : envergo (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par un renforcement majeur de la sécurité du système et une refonte importante de l'infrastructure de stockage. Parallèlement, l'expérience utilisateur a été affinée grâce à des améliorations sur les formulaires de saisie, une meilleure gestion de l'affichage mobile et une optimisation des performances de navigation.

### Évolutions fonctionnelles
- **Formulaires et saisie de données** :
    - Scission du formulaire "moulinette" en deux entités distinctes (RU / HRU).
    - Amélioration de la saisie des haies, avec une gestion optimisée des modales sur mobile pour éviter les affichages encombrants sur grand écran [#1229](https://github.com/MTES-MCT/envergo/pull/1229).
    - Ajout de nouvelles propriétés pour les contrôles "éviter / réduire" [#1235](https://github.com/MTES-MCT/envergo/pull/1235).
    - Mise à jour des choix de procédures lors des changements d'état [#1228](https://github.com/MTES-MCT/envergo/pull/1228).
- **Interface utilisateur (UI) et Ergonomie** :
    - Intégration d'un nouveau composant de pagination conforme au DSFR [#1230](https://github.com/MTES-MCT/envergo/pull/1230).
    - Optimisation de l'affichage du résumé (déplacement de la section "lecture seule" en bas de page).
    - Améliorations visuelles (CSS) et de l'affichage des échéances [#1226](https://github.com/MTES-MCT/envergo/pull/1226).
- **Contenu et métier** :
    - Mise à jour de la terminologie (wording) et des informations de contact de la CBN [#1242](https://github.com/MTES-MCT/envergo/pull/1242).
    - Ajustement de la logique de bascule entre les états "décision" et "attente de compléments".

### Évolutions techniques
- **Sécurité** :
    - Correction de vulnérabilités XSS par l'échappement systématique des données soumises par les utilisateurs et renforcement de la validation des données en backend [#1251](https://github.com/MTES-MCT/envergo/pull/1251).
- **Infrastructure et Stockage** :
    - Refonte complète de la gestion du stockage des fichiers via S3 et mise en place de nouveaux mécanismes pour la diffusion des fichiers hébergés [#1253](https://github.com/MTES-MCT/envergo/pull/1253).
    - Mise à jour de la pile de déploiement (Stack Scalingo) et passage à une version LTS de Node.js [#1252](https://github.com/MTES-MCT/envergo/pull/1252).
    - Optimisation de la configuration Nginx et de la gestion des assets de build.
- **Performance et Base de données** :
    - Optimisation des requêtes de permissions et réduction des requêtes redondantes lors de l'affichage des listes de dossiers [#1241](https://github.com/MTES-MCT/envergo/pull/1241).
    - Refactorisation de la logique de réimplantation [#1219](https://github.com/MTES-MCT/envergo/pull/1219).

### Autres changements
- **Tests** : Ajout de nouvelles suites de tests pour valider la protection contre les failles XSS et mesurer la performance des requêtes SQL.
- **Maintenance** : Nettoyage du projet (suppression de Gulp), mise à jour de la documentation interne (docstrings) et correction des erreurs de pré-commit.
