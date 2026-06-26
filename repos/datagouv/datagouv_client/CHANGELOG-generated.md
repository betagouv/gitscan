## Changelog : datagouv_client (30 derniers jours, au 24 juin 2026)

### Résumé
Cette nouvelle version de `datagouv_client` apporte des améliorations techniques et de la maintenance, notamment le remplacement de la librairie `httpx` par `niquests` et des ajustements concernant le CI/CD et les dépendances de développement. Une optimisation a été apportée pour retarder les appels à l'API Tabular jusqu'à ce qu'ils soient réellement nécessaires, améliorant potentiellement la performance.

### Évolutions fonctionnelles
- Retard des appels à l'API Tabular : Les appels à l'API Tabular sont maintenant différés jusqu'à ce qu'ils soient requis, ce qui peut améliorer la performance dans certains cas [#59](https://github.com/datagouv/datagouv_client/pull/59).

### Évolutions techniques
- Remplacement de `httpx` par `niquests` : La librairie `httpx` a été remplacée par `niquests` [#63](https://github.com/datagouv/datagouv_client/pull/63).
- Mise à jour des dépendances de développement : La manière de déclarer les dépendances de développement a été modifiée [#61](https://github.com/datagouv/datagouv_client/pull/61).
- Utilisation du token UV_PUBLISH_TOKEN recommandé : Le CI utilise maintenant le token UV_PUBLISH_TOKEN recommandé pour les publications [#64](https://github.com/datagouv/datagouv_client/pull/64).
- Mise à jour des instructions d'installation des dépendances de développement : La documentation a été mise à jour pour refléter les nouvelles instructions d'installation [#65](https://github.com/datagouv/datagouv_client/pull/65).

### Autres changements
- Publication de la version 0.4.0.
