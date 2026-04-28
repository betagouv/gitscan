## Changelog : quefairedemesobjets (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la stabilité et des performances de la plateforme, notamment en corrigeant des erreurs et en optimisant les tests. Des améliorations significatives ont été apportées au tracking analytique, à la recherche et à l'indexation du contenu. Des travaux préliminaires sur un modèle de machine learning pour la déduplication des données ont également été réalisés.

### Évolutions fonctionnelles
- **Recherche :** Correction de l'affichage dupliqué du nom dans les résultats de recherche (Vélovélo) [#2754](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2754).
- **Redirections :** Mise en place de redirections depuis l'ancien domaine vers le nouveau [#2756](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2756) et ajout de redirections massives depuis l'ancien site vers le nouveau [#2639](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2639).
- **Fiche Acteur :** Correction de l'affichage des couleurs dans la fiche acteur [#2654](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2654) et ajout de la distance dans le mode liste et la fiche acteur [#2632](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2632).
- **Tracking :** Mise en place d'un nouveau système de tracking des pages vues et des événements [#2721](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2721) et tracking des clics sur les résultats de recherche [#2722](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2722).
- **Indexation :** Amélioration de l'indexation lors de la publication d'une page Wagtail [#2653](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2653).
- **Suggestion Groupe :** Passage des enrichissements d'URL sur la nouvelle architecture de SuggestionGroupe [#2621](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2621).

### Évolutions techniques
- **Tests :** Fiabilisation des tests analytics avec la résolution du Frame iframe [#2760](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2760) et correction des tests e2e en échec suite à des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2736).
- **Déploiement :** Suppression de directives Nginx en double sur Scalingo [#2718](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2718).
- **Architecture :** Refactoring de la gestion du tableau des suggestion groupe [#2619](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2619).
- **Machine Learning :** Premières itérations d'un modèle de machine learning pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2727) et exécution du clustering via un Notebook [#2662](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2662).
- **Performance :** Optimisations de performances générales [#2633](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2633).
- **Airflow :** Retour à une version antérieure d'Airflow pour résoudre des problèmes de compatibilité [#2646](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2646).

### Autres changements
- **Documentation :** Ajout du template manquant pour les tests analytics [#2757](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2757).
- **Configuration :** Suppression du script de migration de la page d'accueil [#2637](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2637).
- **Dépendances :** Mise à jour de nombreuses dépendances (Posthog, Django, etc.). Ces mises à jour sont gérées automatiquement et ne sont pas listées en détail ici.
- **Divers :** Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2749).
