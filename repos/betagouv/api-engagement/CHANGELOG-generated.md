## Changelog : api-engagement (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la robustesse de l'API, notamment en optimisant les recherches et en ajoutant des mécanismes de limitation de débit. Des corrections et améliorations ont également été apportées à l'interface utilisateur du back-office pour une meilleure expérience utilisateur, en particulier concernant l'accessibilité et la gestion des missions.

### Évolutions fonctionnelles
- Ajout de la gestion des missions de service civique dans le job Grimpio [#977](https://github.com/betagouv/api-engagement/issues/977).
- Amélioration de l'affichage de l'URL de l'API Sandbox dans l'exemple curl du back-office [#1012](https://github.com/betagouv/api-engagement/issues/1012).
- Correction de l'affichage des filtres de modération et du débordement des onglets dans le back-office [#975](https://github.com/betagouv/api-engagement/issues/975).
- Correction de l'alignement horizontal du sélecteur de date dans le back-office [#976](https://github.com/betagouv/api-engagement/issues/976).
- Amélioration de la conception réactive de la liste des utilisateurs et des formulaires utilisateurs dans le back-office, pour une meilleure accessibilité (RGAA 10.11) [#930](https://github.com/betagouv/api-engagement/issues/930).
- Correction du problème de déconnexion lors d'erreurs réseau dans le back-office [#928](https://github.com/betagouv/api-engagement/issues/928).
- Correction du problème de la page organisation désactivée dans le back-office [#922](https://github.com/betagouv/api-engagement/issues/922).
- Correction du blocage de la sélection du jour courant dans le sélecteur de date du back-office [#924](https://github.com/betagouv/api-engagement/issues/924).

### Évolutions techniques
- Refactorisation du middleware de contrôle d'accès avec ajout de tests [#1013](https://github.com/betagouv/api-engagement/issues/1013).
- Correction d'un problème de construction du job [#1018](https://github.com/betagouv/api-engagement/issues/1018).
- Ajout d'une configuration Mockoon pour les tests [#978](https://github.com/betagouv/api-engagement/issues/978).
- Optimisation de la recherche d'organisations en utilisant `tsvector` [#950](https://github.com/betagouv/api-engagement/issues/950).
- Suppression de la colonne `mission_id` dans la table `stat_events` pour améliorer la performance et simplifier la structure [#933](https://github.com/betagouv/api-engagement/issues/933).
- Suppression des champs dénormalisés de mission de la table `stat_event` [#921](https://github.com/betagouv/api-engagement/issues/921).
- Refactorisation de l'exécution séquentielle de l'agrégation du widget [#966](https://github.com/betagouv/api-engagement/issues/966).
- Refactorisation du traitement des missions avec exclusion de l'organisation publiant [#965](https://github.com/betagouv/api-engagement/issues/965).
- Suppression du magasin partagé de limitation de débit [#959](https://github.com/betagouv/api-engagement/issues/959).
- Ajout de limiteurs de débit (publisher et IP) [#932](https://github.com/betagouv/api-engagement/issues/932).
- Correction du scaling de l'API (max_scale) [#949](https://github.com/betagouv/api-engagement/issues/949).
- Ajout de jobs de sauvegarde de la base de données (RDB backup) [#955](https://github.com/betagouv/api-engagement/issues/955).
- Activation des jobs de sauvegarde RDB [#957](https://github.com/betagouv/api-engagement/issues/957).
- Amélioration des règles CLAUDE [#959](https://github.com/betagouv/api-engagement/issues/959).

### Autres changements
- Amélioration du script de vérification des champs orphelins de mission dans `stat_event` [#428515e](https://github.com/betagouv/api-engagement/commit/428515e).
- Publication des versions v1.4.0 et v1.4.1 [#956](https://github.com/betagouv/api-engagement/issues/956) et [#942](https://github.com/betagouv/api-engagement/issues/942).
