## Changelog : territoires-en-transitions (30 derniers jours, au 04 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'expérience utilisateur, notamment autour de la gestion des indicateurs et des audits. L'ajout de fonctionnalités comme le réordonnancement des colonnes, l'édition en ligne et l'import de données via copier-coller simplifient la saisie et la manipulation des données. Des efforts considérables ont également été consacrés à l'amélioration de la performance et de la robustesse de l'application, ainsi qu'à la préparation de la bascule vers de nouveaux référentiels.

### Évolutions fonctionnelles
- Ajout de la possibilité de réordonner les colonnes et les lignes dans la grille d'indicateurs par glisser-déposer. [#84a78bb](https://github.com/incubateur-ademe/territoires-en-transitions/issues/84a78bb)
- Implémentation de l'édition en ligne des valeurs dans la grille d'indicateurs avec auto-sauvegarde. [#845aba3](https://github.com/incubateur-ademe/territoires-en-transitions/issues/845aba3)
- Possibilité de coller des données tabulaires (depuis un tableur) directement dans la grille d'indicateurs. [#30a759e](https://github.com/incubateur-ademe/territoires-en-transitions/issues/30a759e)
- Ajout d'une fonctionnalité d'import de plans d'action à partir de fichiers (en cours de développement). [#2bb4132](https://github.com/incubateur-ademe/territoires-en-transitions/issues/2bb4132)
- Amélioration de l'export des indicateurs au format Excel, avec un format consolidé sur une seule feuille. [#eaa987c](https://github.com/incubateur-ademe/territoires-en-transitions/issues/eaa987c)
- Ajout d'une pastille d'information et d'un sélecteur pour indiquer la couverture des données Open Data. [#99fd78b](https://github.com/incubateur-ademe/territoires-en-transitions/issues/99fd78b)
- Possibilité de dupliquer un plan d'action existant. [#cd9269c](https://github.com/incubateur-ademe/territoires-en-transitions/issues/cd9269c)
- Amélioration de la gestion des documents et des preuves dans les audits, avec la possibilité de les télécharger en archive. [#e59576d](https://github.com/incubateur-ademe/territoires-en-transitions/issues/e59576d)
- Refonte de l'interface de l'audit, avec une nouvelle disposition et des fonctionnalités améliorées.

### Évolutions techniques
- Refactorings importants du code lié aux indicateurs pour améliorer la maintenabilité et la performance.
- Amélioration de la gestion des erreurs et des validations dans le formulaire d'import de plans d'action.
- Optimisation des tests E2E pour une exécution plus rapide et plus fiable.
- Mise à jour des dépendances, notamment Next.js et eslint-config-next.
- Migration de certaines parties de l'application vers une architecture plus modulaire.
- Amélioration de la sécurité, notamment en corrigeant des vulnérabilités potentielles et en renforçant les contrôles d'accès.
- Préparation de la bascule vers de nouveaux référentiels de données (TE).
- Amélioration de la gestion des permissions et des rôles utilisateurs.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Nettoyage du code et suppression de code obsolète.
- Amélioration de la gestion des logs et du monitoring.
- Ajout de la synchronisation des données CRM depuis les outils internes.
