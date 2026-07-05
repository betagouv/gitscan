## Changelog : datagouv-client (30 derniers jours, au 2 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la bibliothèque, notamment la migration de l'interface en ligne de commande vers `datagouv-cli`, l'optimisation des appels à l'API Tabular et le remplacement de la librairie `httpx` par `niquests` pour une meilleure gestion des requêtes HTTP. Des corrections et des ajustements de configuration ont également été effectués.

### Évolutions fonctionnelles
- Migration de l'interface en ligne de commande vers `datagouv-cli` pour une meilleure expérience utilisateur et une maintenance simplifiée. [#67](https://github.com/datagouv/datagouv-client/pull/67)
- Correction d'un problème empêchant l'utilisation des en-têtes de session pour l'interface en ligne de commande. [#66](https://github.com/datagouv/datagouv-client/pull/66)
- Optimisation des appels à l'API Tabular en retardant leur exécution jusqu'à ce qu'ils soient réellement nécessaires, améliorant ainsi les performances. [#59](https://github.com/datagouv/datagouv-client/pull/59)

### Évolutions techniques
- Remplacement de la librairie `httpx` par `niquests` pour une gestion plus performante et fiable des requêtes HTTP. [#63](https://github.com/datagouv/datagouv-client/pull/63)
- Refactorisation du nom du dépôt. [#68](https://github.com/datagouv/datagouv-client/pull/68)
- Mise à jour de la configuration CI pour utiliser le token UV_PUBLISH_TOKEN recommandé. [#64](https://github.com/datagouv/datagouv-client/pull/64)
- Modification de la déclaration des dépendances de développement. [#61](https://github.com/datagouv/datagouv-client/pull/61)
- Mise à jour des instructions d'installation des dépendances de développement dans la documentation. [#65](https://github.com/datagouv/datagouv-client/pull/65)

### Autres changements
- Publication de la version 0.5.0.
- Publication de la version 0.4.0.
