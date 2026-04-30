## Changelog : quefairedemesobjets (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et des performances de la plateforme, ainsi que sur des corrections de bugs et des améliorations de l'expérience utilisateur. Des travaux ont également été menés sur la déduplication des données et l'amélioration de la recherche. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la compatibilité du projet.

### Évolutions fonctionnelles
- Correction de l'affichage dupliqué du nom dans les résultats de recherche pour Vélovélo [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- Suppression du bouton "Infos" obsolète de la carte [#2759](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2759).
- Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2756).
- Ajout du template manquant pour les propriétés de la page iframe [#2757](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2757).
- Fusion des cartes PostHog et de l'assistant [#2752](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2752).
- Amélioration de l'indexation à la publication d'une page Wagtail [#2653](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2653).
- Correction de la couleur des icônes dans la fiche acteur [#2654](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2654).
- Affichage des liens des SIRET, SIREN et URL [#2655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2655).
- Ajout du tracking des clics sur les résultats de recherche [#2722](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2722).

### Évolutions techniques
- Augmentation du nombre de tentatives de health check avant de déclarer une erreur [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- Optimisations de performances générales [#2633](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2633).
- Rationalisation des environnements de développement [#2659](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2659).
- Passage des enrichissements d'URL sur la nouvelle architecture de SuggestionGroupe [#2621](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2621).
- Correction des tests e2e suite à des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2736) et [#2760](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2760).
- Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2749).
- Première itération d'un modèle de Machine Learning pour la déduplication [#2727](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2727).
- Utilisation de la dernière version de django-modelsearch avec la gestion des accents [#2643](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2643).
- Suppression du script de migration de la page d'accueil [#2637](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2637).
- Revert de pandas à la version 2.1.4 [#2761](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2761).

### Autres changements
- Mise à jour de nombreuses dépendances (Ruff, eslint, pytest, django, etc.).
- Correction de problèmes liés aux tests e2e.
- Suppression de directives Nginx en double sur Scalingo [#2718](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2718).
- Ajout d'un avertissement si la page à rediriger existe déjà dans le CMS [#2701](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2701).
- Proxy PostHog via le domaine principal [#2720](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2720).
- Correction de l'icône bonus réparation [#2660](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2660).
