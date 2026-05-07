## Changelog : quefairedemesobjets (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la cartographie et du clustering des acteurs du réemploi, la correction de bugs et l'optimisation des performances. Des améliorations significatives ont également été apportées au tracking et à l'intégration avec PostHog, ainsi qu'à la gestion des dépendances et de l'infrastructure.

### Évolutions fonctionnelles
- Permet de clusteriser les acteurs par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- Amélioration de la résolution du Frame iframe dans les tests analytics [#2760](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2760).
- Ajout du template manquant pour les propriétés de la page iframe [#2757](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2757).
- Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2756).
- Correction de l'affichage dupliqué du nom dans les résultats de recherche (Vélovélo) [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- Affichage des liens (SIRET, URL) pour les acteurs [#2655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2655).
- Correction du map formulaire id sur la fiche acteur [#2695](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2695).
- Exclusion de la page de configuration de l'infotri de l'index Google [#2702](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2702).
- Ajout d'un avertissement si une page à rediriger existe déjà dans le CMS [#2701](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2701).

### Évolutions techniques
- Mise en place d'un modèle ML pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2727).
- Optimisations de performances générales [#2633](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2633).
- Amélioration de la gestion des health checks avec plus de tentatives avant de signaler une erreur [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- Suppression du cache npm car le `package-lock.json` est maintenant géré dans le répertoire `webapp` [#2700](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2700).
- Refonte du tracking avec PostHog : implémentation de `pageView` et d'événements [#2721](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2721).
- Proxy PostHog via le domaine principal pour une meilleure confidentialité [#2720](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2720).

### Autres changements
- Suppression du bouton "Infos" obsolète de la carte [#2759](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2759).
- Correction de tests e2e après des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2736) et [#2761](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2761).
- Diverses mises à jour de dépendances (Django, React, PostgreSQL, etc.). Ces mises à jour sont effectuées pour maintenir la sécurité et la stabilité du projet.
- Correction d'erreurs sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2749).
- Migration manquante [#2750](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2750).
