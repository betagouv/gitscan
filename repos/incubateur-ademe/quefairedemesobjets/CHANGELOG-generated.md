## Changelog : quefairedemesobjets (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la géolocalisation des acteurs, la correction de bugs et l'optimisation des performances. Des améliorations significatives ont été apportées au tracking et à l'analytics, ainsi qu'à la gestion des données et des tests. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Permet de clusteriser les acteurs par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- Permet plus de retries pour les health checks, améliorant la résilience du service [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- Suppression du bouton "Infos" obsolète de la carte, simplifiant l'interface utilisateur [#2759](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2759).
- Correction de l'affichage dupliqué du nom dans les résultats de recherche pour Vélovélo [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- Redirection du domaine legacy vers le domaine principal [#2756](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2756).
- Affichage des liens (SIRET, SIREN, URL) des acteurs [#2655](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2655).
- Corrige le map formulaire id du formulaire sur la fiche acteur [#2695](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2695).
- Exclusion de la page de configuration de l'infotri de l'indexation Google [#2702](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2702).

### Évolutions techniques
- Première itération d'un modèle de Machine Learning pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2727).
- Optimisations de performances générales [#2633](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2633).
- Refonte du tracking avec l'implémentation de `pageView` et d'événements personnalisés [#2721](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2721).
- Proxy PostHog via le domaine principal pour une meilleure confidentialité [#2720](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2720).
- Amélioration de la gestion des tests e2e suite à des mises à jour de dépendances [#2736](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2736) et [#2760](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2760).
- Correction d'un problème lié aux tests après une mise à jour de Pandas [#2735](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2735).
- Suppression du cache npm car le `package-lock.json` est maintenant dans le répertoire `webapp` [#2700](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2700).
- Ajout d'un avertissement si une page à rediriger existe déjà dans le CMS [#2701](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2701).

### Autres changements
- Ajout du template manquant `t_18_iframe_page_properties` [#2757](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2757).
- Migration pour corriger une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2749).
- Correction d'une erreur sur les termes de recherche orphelins [#2749](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2749).
- Suppression de directives Nginx en double sur Scalingo [#2718](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2718).
- Revert du bump de eslint ^10 car eslint-config-love n'est pas prêt [#2699](https://github.com/incubateur-ademe/quefiredemesobjets/issues/2699).
