## Changelog : quefairedemesobjets (30 derniers jours, au 16 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec une refonte de la page d'accueil de l'assistant et des corrections de bugs sur la fiche acteur. Des optimisations de performance ont également été apportées, ainsi que des améliorations techniques concernant l'indexation, le cache et la gestion des dépendances.

### Évolutions fonctionnelles
- Refonte de la page d'accueil de l'assistant pour une meilleure expérience utilisateur. [#2572](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2572)
- Affichage des liens des SIRET, SIREN et URL sur les fiches acteurs. [#2655](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2655)
- Ajout de la sous-catégorie "Smartphone" au PAM (Plan d'Action pour la Maîtrise des Déchets) pour les filières écologique et écosystème. [#2634](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2634)
- Correction d'un bug empêchant la fermeture correcte des fiches acteurs. [#2622](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2622)
- Correction d'un bug sur les traductions et le plan de site. [#2625](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2625)
- Amélioration de la recherche dans les tests e2e. [#2680](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2680)
- Correction de l'affichage de la distance en mode liste et sur la fiche acteur. [#2632](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2632)
- Ajout d'un avertissement si une page à rediriger existe déjà dans le CMS. [#2701](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2701)

### Évolutions techniques
- Optimisations de performances générales. [#2633](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2633)
- Utilisation de la dernière version de `django-modelsearch` pour une meilleure gestion des accents. [#2643](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2643)
- Amélioration de l'indexation lors de la publication d'une page Wagtail. [#2653](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2653)
- Rationalisation des environnements de développement. [#2659](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2659)
- Correction d'un problème de tests e2e lié au renommage des tables de cache. [#2717](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2717)
- Proxy PostHog via le domaine du projet. [#2720](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2720)
- Suppression de directives Nginx en double sur Scalingo. [#2718](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2718)
- Correction sur le map formulaire id du formulaire sur la fiche acteur. [#2695](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2695)
- Permettre de faire des clusters sur les latitudes et longitudes identiques. [#2703](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2703)
- Exclusion de la page de configuration de l'infotri de l'index Google. [#2702](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2702)

### Autres changements
- Documentation et Makefile pour la partie DBT. [#2631](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2631)
- Correction du script de backup de la base de données en local. [#2627](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2627)
- Suppression du script de migration de la page d'accueil. [#2637](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2637)
- Correction de la couleur des actions sur la fiche acteur. [#2654](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2654)
- Le cache npm n'est plus effectif car package-lock.json est dans webapp. [#2700](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2700)
