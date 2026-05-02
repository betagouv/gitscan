## Changelog : quefairedemesobjets (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la performance de la plateforme, avec des corrections de bugs, des mises à jour de dépendances et des optimisations de l'infrastructure. Des améliorations ont également été apportées à l'expérience utilisateur, notamment au niveau de la recherche et de l'affichage des informations sur les acteurs. Des travaux préliminaires sur l'amélioration de la déduplication des données ont également été réalisés.

### Évolutions fonctionnelles
- Correction de l'affichage dupliqué du nom dans les résultats de recherche pour Vélovélo [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- Suppression du bouton "Infos" obsolète sur la carte [#2759](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2759).
- Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2756).
- Correction de la recherche dans les tests e2e [#2680](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2680).
- Correction sur le formulaire : carte masquée et titre tronqué [#2682](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2682).
- Correction sur les couleurs dans la fiche acteur [#2654](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2654).
- Ajout d'un avertissement si la page à rediriger existe déjà dans le CMS [#2701](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2701).
- Affichage des liens (siret, url) sur les fiches acteurs [#2655](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2655).

### Évolutions techniques
- Amélioration de la robustesse des health checks en permettant plus de tentatives avant de signaler une erreur [#2763](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2763).
- Optimisations de performances générales [#2633](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2633).
- Mise à jour de nombreuses dépendances (Django, requests, psycopg, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Rationalisation des environnements de développement [#2659](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2659).
- Correction d'un problème lié à l'indexation à la publication d'une page Wagtail [#2653](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2653).
- Utilisation de la dernière version de `django-modelsearch` avec gestion des accents [#2643](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2643).
- Correction des tests e2e suite à des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2736) et [#2780](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2780).
- Revert de Pandas à la version 2.1.4 suite à des problèmes [#2761](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2761).

### Autres changements
- Premières itérations d'un modèle de Machine Learning pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2727).
- Ajout de tracking PostHog via notre propre domaine [#2720](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2720).
- Amélioration du tracking : pageView et events [#2721](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2721).
- Suppression du script de migration de la page d'accueil [#2637](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2637).
- Fiabilisation de la résolution du Frame iframe dans les tests analytics [#2760](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2760).
- Ajout du template manquant t_18_iframe_page_properties [#2757](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2757).
- Fusion des cartes Posthog et de l'assistant [#2752](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2752).
- Suppression de directives nginx en double sur scalingo [#2718](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2718).
- Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2749).
- Migration manquante [#2750](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2750).
