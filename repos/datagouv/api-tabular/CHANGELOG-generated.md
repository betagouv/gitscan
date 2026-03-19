## Changelog : api-tabular (30 derniers jours, au 6 mars 2026)

### Résumé
Ce mois-ci, l'API a bénéficié d'améliorations significatives en termes de flexibilité des requêtes, de sécurité (CORS), de robustesse et de qualité du code. L'ajout de la configuration d'agrégation générale et l'amélioration du point de terminaison de santé renforcent également les capacités de l'API.

### Évolutions fonctionnelles
- **Requêtes complexes :** Possibilité d'utiliser des conditions plus complexes dans les requêtes, offrant une plus grande flexibilité pour filtrer les données. [#103](https://github.com/datagouv/api-tabular/issues/103)
- **Configuration d'agrégation :** Ajout d'une configuration générale pour activer ou désactiver l'agrégation des données. [#102](https://github.com/datagouv/api-tabular/issues/102)
- **Point de terminaison de santé :** Remplacement de `uptime_seconds` par `uptime_since` dans le point de terminaison de santé pour une information plus claire sur la durée de fonctionnement de l'API. [#104](https://github.com/datagouv/api-tabular/issues/104)

### Évolutions techniques
- **Correction CORS :** Correction des en-têtes CORS statiques pour autoriser tous les domaines, améliorant la compatibilité avec les applications clientes. [#100](https://github.com/datagouv/api-tabular/issues/100)
- **Typage statique :** Ajout de `ty` pour la vérification de type et correction des erreurs de type dans le code. [#96](https://github.com/datagouv/api-tabular/issues/96)
- **Simplification CI :** Simplification de la configuration CircleCI pour optimiser le processus d'intégration continue. [#97](https://github.com/datagouv/api-tabular/issues/97)
- **Publication CI :** Modification du workflow CI pour éviter la double publication et exécuter les tests, le linting et la construction sur tous les pushs. [#99](https://github.com/datagouv/api-tabular/issues/99)

### Autres changements
- **Documentation :** Nettoyage mineur du fichier README. [#96](https://github.com/datagouv/api-tabular/issues/96)
