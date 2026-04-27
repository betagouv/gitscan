## Changelog : cdata (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'application cdata a bénéficié d'une refonte significative avec la migration vers Nuxt 4, apportant des améliorations de performance et de nouvelles fonctionnalités. Des améliorations ont également été apportées à l'exploration des données tabulaires, à la recherche, et à l'interface de modération, ainsi qu'à la gestion des previews et des informations sur les ressources.

### Évolutions fonctionnelles
- **Exploration des données tabulaires :** Nouvelle page d'exploration des données tabulaires est disponible [#971].
- **Recherche :** Ajout du support des "Topics" dans la recherche globale [#1030]. Possibilité de rechercher des filtres personnalisés [#1048].
- **Interface de modération :**
    - Amélioration de la page de modération avec des onglets pour filtrer les types de sujets [#1033].
    - Correction d'un problème de dépassement de cellule dans le tableau de bord de modération [#1050].
    - Ajout d'informations supplémentaires sur les previews manquantes [#1025].
- **Previews :** Amélioration de l'affichage des previews de ressources, notamment en vérifiant les en-têtes CORS avant de tenter de les afficher [#954].
- **Feedback IA :** Le lien vers le feedback IA n'est affiché que après une suggestion [#1046].
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API de démonstration [#1045].
- **Éditeur de blocs :** Suppression des pages pour ne conserver que les blocs d'édition [#1015].

### Évolutions techniques
- **Migration Nuxt :** Mise à jour vers Nuxt 4.0, puis 4.1 et 4.2 [#1023, #1035, #1047].
- **Optimisation SVG :** Utilisation d'images SVG simples et optimisation avec svgo [#1057].
- **Correction Nitro :** Correction d'un problème avec le serveur Nitro de Nuxt [#1053].
- **Refactoring :** Suppression de la duplication entre les previews [#1018].
- **CI/CD :** Mise à jour des versions des actions CI/CD [#1013].
- **Correction Harvester :** Initialisation des fonctionnalités du harvester lors du premier chargement de la page [#1043].

### Autres changements
- Correction d'un problème de valeur manquante pour les topics [#1032].
- Correction d'un patch Nuxt qui n'était plus appliqué [#1039].
- Correction de liens OEmbed [#1026].
- Amélioration de la formulation pour les datasets liés à un schéma [#1019].
- Correction d'un problème de flakiness dans les tests [#1028].
- Suppression d'une tentative d'amélioration de la liste des reviewers dans les pull requests (révertée) [#1029].
- Ajout d'informations sur les catégories restreintes [#1017].
- Correction d'un bug concernant l'affichage des blocs [#1027].
- Correction d'un bug lié à l'initialisation des features du harvester [#1043].
- Correction d'un bug lié à l'affichage des previews [#1056].
