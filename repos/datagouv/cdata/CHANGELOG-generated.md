## Changelog : cdata (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur la modernisation de la plateforme avec une mise à niveau majeure vers Nuxt 4, ainsi que sur l'amélioration de l'expérience utilisateur, notamment au niveau de la modération et de la recherche de données. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- **Recherche :** Ajout du support des "Topics" dans la recherche globale [#1030](https://github.com/datagouv/cdata/issues/1030).
- **Modération :**
    - Amélioration de la page de modération avec des onglets pour filtrer les types de sujets [#1033](https://github.com/datagouv/cdata/issues/1033).
    - Ajout d'informations supplémentaires sur les aperçus manquants [#1025](https://github.com/datagouv/cdata/issues/1025).
    - Correction d'un problème de dépassement de cellule dans le tableau de bord de modération [#1050](https://github.com/datagouv/cdata/issues/1050).
- **Aperçu des données :** Amélioration de l'affichage des aperçus en tenant compte des en-têtes CORS et en affichant un lien vers le feedback IA après une suggestion [#1046](https://github.com/datagouv/cdata/issues/1046).
- **Documentation :** Ajout de documentation sur l'obtention d'une clé API de la démo [#1045](https://github.com/datagouv/cdata/issues/1045).
- **Catégories restreintes :** Affichage de la définition des catégories restreintes [#1017](https://github.com/datagouv/cdata/issues/1017).
- **Schémas de données :** Amélioration de la formulation pour les jeux de données liés à un schéma [#1019](https://github.com/datagouv/cdata/issues/1019).

### Évolutions techniques
- **Nuxt :** Mise à niveau vers Nuxt 4.2 [#1047](https://github.com/datagouv/cdata/issues/1047), puis vers les versions 4.1 [#1035](https://github.com/datagouv/cdata/issues/1035) et 4.0 [#1023](https://github.com/datagouv/cdata/issues/1023).
- **Refactoring :** Suppression de la duplication entre les aperçus [#1018](https://github.com/datagouv/cdata/issues/1018) et simplification de la structure des pages en ne conservant que les blocs d'édition [#1015](https://github.com/datagouv/cdata/issues/1015).
- **Dépendances :** Mise à jour de Node vers la version 24 [#1011](https://github.com/datagouv/cdata/issues/1011) et des dépendances générales [#1002](https://github.com/datagouv/cdata/issues/1002).
- **CI/CD :** Mise à jour des versions des actions GitHub utilisées dans le workflow CI/CD [#1013](https://github.com/datagouv/cdata/issues/1013).
- **API Keys :** Ajout de la gestion de nouvelles clés API [#962](https://github.com/datagouv/cdata/issues/962) et de la configuration associée [#1006](https://github.com/datagouv/cdata/issues/1006).
- **Rate Limiting:** Ajout de l'URL de limitation de débit aux services de données [#1005](https://github.com/datagouv/cdata/issues/1005).

### Autres changements
- Correction d'un bug empêchant l'initialisation des fonctionnalités du récolteur au premier chargement de la page [#1043](https://github.com/datagouv/cdata/issues/1043).
- Correction d'un patch Nuxt qui n'était plus appliqué [#1039](https://github.com/datagouv/cdata/issues/1039).
- Correction d'un problème de liens OEmbed [#1026](https://github.com/datagouv/cdata/issues/1026).
- Correction d'un crash lors du changement de layout en mode développement [#1004](https://github.com/datagouv/cdata/issues/1004).
- Suppression de code mort lié à ProducerSelect [#1003](https://github.com/datagouv/cdata/issues/1003).
- Correction d'un problème d'importation de Crisp [#1016](https://github.com/datagouv/cdata/issues/1016).
- Annulation d'une tentative d'amélioration de la liste des reviewers dans les pull requests [#1029](https://github.com/datagouv/cdata/issues/1029).
- Correction d'un problème de valeur manquante pour les sujets [#1032](https://github.com/datagouv/cdata/issues/1032).
- Tentative de correction des tests instables [#1028](https://github.com/datagouv/cdata/issues/1028).
