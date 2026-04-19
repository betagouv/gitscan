## Changelog : maestro (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des prélèvements et des analyses, notamment en corrigeant des bugs et en ajoutant des fonctionnalités pour faciliter la saisie et la consultation des données. Des améliorations ont également été apportées à l'automatisation, à la documentation et à l'infrastructure du projet. Une migration vers un nouveau linter (BiomeJS) a été initiée pour améliorer la qualité du code.

### Évolutions fonctionnelles
- Possibilité d'éditer les descripteurs de prélèvements [#652](https://github.com/betagouv/maestro/issues/652).
- Amélioration de la consultation du tableau de bord des plans fermés [#696](https://github.com/betagouv/maestro/issues/696).
- Correction de l'affichage des décalages horaires pour les prélèvements [#710](https://github.com/betagouv/maestro/issues/710).
- Possibilité de filtrer les préleveurs par plan [#667](https://github.com/betagouv/maestro/issues/667).
- Correction de la validation de la programmation lorsque la région a approuvé celle-ci [#738](https://github.com/betagouv/maestro/issues/738).
- Possibilité de saisir le résultat des résidus complexes dans les analyses [#739](https://github.com/betagouv/maestro/issues/739).
- Déblocage des DAI (Demandes d'Analyse Individualisées) pour les LNR (Laboratoires Régionaux) [#714](https://github.com/betagouv/maestro/issues/714).
- Correction du filtre par entreprise dans les prélèvements [#7551fd](https://github.com/betagouv/maestro/commit/f7551fd).
- Correction du champ Saisie pour DAOA [#ba46613](https://github.com/betagouv/maestro/commit/ba46613).
- Gestion des erreurs pour les RAI (Requêtes d'Analyse Individualisées) [#749](https://github.com/betagouv/maestro/issues/749).
- Amélioration de la gestion des compétences analytiques (en cours de développement) [#491](https://github.com/betagouv/maestro/issues/491).

### Évolutions techniques
- Remplacement de ESLint et Prettier par BiomeJS pour le linting et le formattage du code [#672](https://github.com/betagouv/maestro/issues/672).
- Refactorisation du frontend pour typer les requêtes via les définitions des routes dans `shared` [#693](https://github.com/betagouv/maestro/issues/693).
- Préparation à la migration vers PostgreSQL 17 [#708](https://github.com/betagouv/maestro/issues/708).
- Ajout de schémas pour les échanges hors EDI Sacha [#711](https://github.com/betagouv/maestro/issues/711).
- Correction de l'injection des échantillons dans le seed [#662](https://github.com/betagouv/maestro/issues/662).
- Accélération des tests d'intégration [#724](https://github.com/betagouv/maestro/issues/724).
- Correction de l'historique de la programmation [#668](https://github.com/betagouv/maestro/issues/668).

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité.
- Documentation mise à jour, notamment l'architecture du projet [#680](https://github.com/betagouv/maestro/issues/680).
- Correction de sigles pour la compatibilité avec Sigal [#664](https://github.com/betagouv/maestro/issues/664).
- Correction de l'affichage du message "programmation pas encore disponible" [#669](https://github.com/betagouv/maestro/issues/669).
- Correction des droits de saisie des infos d'expéditions en DAOA [#723](https://github.com/betagouv/maestro/issues/723).
- Correction du dossier Carbone pour éviter les créations concurrentes [#746](https://github.com/betagouv/maestro/issues/746).
- Correction du préleveur dans les DAI [#744](https://github.com/betagouv/maestro/issues/744).
- Suppression de l'entête des matrices réalisées dans le dashboard [#700](https://github.com/betagouv/maestro/issues/700).
- Correction du filtre pour les admins dans les plans [#697](https://github.com/betagouv/maestro/issues/697).
- Correction de la récupération de l'utilisateur dans le local storage [#7a9b32d](https://github.com/betagouv/maestro/commit/7a9b32d) et [#819b19b](https://github.com/betagouv/maestro/commit/819b19b).
- Ajout d'une année et de plans aux ressources [#671](https://github.com/betagouv/maestro/issues/671).
- Si aucune détection, alors Conforme et on ne notifie plus [#654](https://github.com/betagouv/maestro/issues/654).
- Correction du status permission 2 [#722](https://github.com/betagouv/maestro/issues/722).
- Correction du nom du fichier et de l'extension dans les DAI [#715](https://github.com/betagouv/maestro/issues/715).
- Tri des plans par année puis ordre alpha [#703](https://github.com/betagouv/maestro/issues/703).
- Notifie les coordinateurs régionaux des plans concernés de l'ajout d'un nouveau document [#709](https://github.com/betagouv/maestro/issues/709).
