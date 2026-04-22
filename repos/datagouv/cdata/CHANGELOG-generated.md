## Changelog : cdata (30 derniers jours, au 20 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à cdata au cours des 30 derniers jours. Les principales évolutions concernent l'exploration tabulaire des données, l'amélioration de l'interface utilisateur pour la gestion des ressources et la modération, ainsi que des mises à jour techniques importantes incluant l'adoption de Nuxt 4 et des optimisations de performance.

### Évolutions fonctionnelles
- **Exploration tabulaire :** Ajout d'une nouvelle fonctionnalité permettant d'explorer les données tabulaires. [#971](https://github.com/datagouv/cdata/issues/971)
- **Gestion des ressources :** L'explorateur de ressources est maintenant responsive et s'adapte aux différentes tailles d'écran. [#1014](https://github.com/datagouv/cdata/issues/1014)
- **Modération :**
    - Amélioration du filtre des types de sujets dans le tableau de bord de modération, avec l'utilisation d'onglets. [#1033](https://github.com/datagouv/cdata/issues/1033)
    - Améliorations générales de l'interface de la page de modération. [#1021](https://github.com/datagouv/cdata/issues/1021)
- **Recherche :** Ajout du support des "Topics" (sujets) dans la recherche globale. [#1030](https://github.com/datagouv/cdata/issues/1030)
- **Aide IA :** Le lien vers l'aide IA n'est affiché que si une suggestion a été faite. [#1046](https://github.com/datagouv/cdata/issues/1046)
- **Affichage des schémas :** Amélioration de la formulation pour les jeux de données liés à des schémas. [#1019](https://github.com/datagouv/cdata/issues/1019)
- **Prévisualisation des ressources :** Amélioration de la gestion des en-têtes CORS pour l'affichage des prévisualisations. [#954](https://github.com/datagouv/cdata/issues/954)
- **Catégories restreintes :** Affichage de la définition des catégories restreintes. [#1017](https://github.com/datagouv/cdata/issues/1017)

### Évolutions techniques
- **Mise à jour de Nuxt :** Passage à Nuxt 4 (versions minimales, 4.0, 4.1 et 4.2). [#1023](https://github.com/datagouv/cdata/issues/1023), [#1035](https://github.com/datagouv/cdata/issues/1035), [#1047](https://github.com/datagouv/cdata/issues/1047)
- **API Keys :** Implémentation d'un nouveau système de clés API. [#962](https://github.com/datagouv/cdata/issues/962), [#1006](https://github.com/datagouv/cdata/issues/1006)
- **Node.js :** Mise à jour de Node.js vers la version 24. [#1011](https://github.com/datagouv/cdata/issues/1011)
- **Dépendances :** Mise à jour des dépendances du projet. [#1002](https://github.com/datagouv/cdata/issues/1002)
- **CI/CD :** Mise à jour des versions des actions utilisées dans le workflow CI/CD. [#1013](https://github.com/datagouv/cdata/issues/1013)
- **Refactoring :** Suppression de la duplication de code entre les prévisualisations. [#1018](https://github.com/datagouv/cdata/issues/1018)
- **Correction de bug Nitro :** Correction d'un bug lié à la configuration du serveur Nitro de Nuxt. [#1053](https://github.com/datagouv/cdata/issues/1053)
- **Correction de bug d'initialisation :** Correction d'un problème d'initialisation des fonctionnalités du harvester. [#1043](https://github.com/datagouv/cdata/issues/1043)
- **Correction de patch Nuxt :** Réapplication d'un patch Nuxt qui avait été supprimé. [#1039](https://github.com/datagouv/cdata/issues/1039)

### Autres changements
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API de démonstration. [#1045](https://github.com/datagouv/cdata/issues/1045)
- **Correction de liens OEmbed :** Correction des liens OEmbed. [#1026](https://github.com/datagouv/cdata/issues/1026)
- **Correction d'un bug d'affichage :** Correction d'un débordement de cellule dans le tableau de bord de modération. [#1050](https://github.com/datagouv/cdata/issues/1050)
- **Correction d'un bug de valeur manquante :** Correction d'une valeur manquante pour les sujets. [#1032](https://github.com/datagouv/cdata/issues/1032)
- **Revert :** Annulation d'une modification concernant la liste des reviewers dans les pull requests. [#1029](https://github.com/datagouv/cdata/issues/1029)
- **Amélioration des tests :** Tentative de correction de tests instables. [#1028](https://github.com/datagouv/cdata/issues/1028)
- **Correction d'import Crisp :** Correction d'un problème d'import de Crisp. [#1016](https://github.com/datagouv/cdata/issues/1016)
- **Informations de preview :** Ajout d'informations supplémentaires sur les previews manquantes. [#1025](https://github.com/datagouv/cdata/issues/1025)
