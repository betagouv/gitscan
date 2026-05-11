## Changelog : srdt (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières mises à jour de l'assistant virtuel SRDT se concentrent sur l'amélioration de la stabilité et de la performance, notamment en revenant à ChatGPT pour la production et en ajustant le modèle de langage utilisé. Des améliorations de l'interface utilisateur ont également été apportées, comme l'affichage constant du badge de convention collective et des corrections pour l'IDCC.

### Évolutions fonctionnelles
- Ajout d'un badge de convention collective affiché en permanence dans l'interface utilisateur ([#365](https://github.com/SocialGouv/srdt/issues/365)).
- Amélioration de l'affichage et de l'ergonomie du champ IDCC ([#364](https://github.com/SocialGouv/srdt/issues/364)).
- Possibilité de changer de modèle de langage via la configuration Kubernetes ([#366](https://github.com/SocialGouv/srdt/issues/366)).
- Ajout d'un badge de convention collective sur les messages de l'assistant ([#344](https://github.com/SocialGouv/srdt/issues/344)).
- Possibilité d'appeler l'API en mode debug avec un token bearer ([#346](https://github.com/SocialGouv/srdt/issues/346)).
- Amélioration de la permissivité du prompt utilisé par l'assistant ([#363](https://github.com/SocialGouv/srdt/issues/363)).
- Correction des liens directs vers les conventions collectives ([#319](https://github.com/SocialGouv/srdt/issues/319)).
- Amélioration du placeholder de suivi dans l'interface de chat ([#347](https://github.com/SocialGouv/srdt/issues/347)).

### Évolutions techniques
- Retour à l'utilisation de ChatGPT pour la production afin d'améliorer la performance et la stabilité ([1c6eb9f](https://github.com/SocialGouv/srdt/commit/1c6eb9f3993341c7101d06249a4c6f11adfa2480)).
- Correction de bugs liés aux contributions et à la gestion des données ([#351](https://github.com/SocialGouv/srdt/issues/351), [#352](https://github.com/SocialGouv/srdt/issues/352), [#357](https://github.com/SocialGouv/srdt/issues/357), [#359](https://github.com/SocialGouv/srdt/issues/359)).
- Suppression de l'anonymisation des localisations ([#370](https://github.com/SocialGouv/srdt/issues/370)).
- Ajustements et retours sur l'utilisation du modèle Mistral, avec un retour temporaire à ChatGPT puis une restauration de Mistral avant un nouveau retour à ChatGPT.
- Mise à jour du prompt utilisé par l'assistant.

### Autres changements
- Publication des versions 1.40.3, 1.40.2, 1.40.1, 1.40.0, 1.39.7, 1.39.6, 1.39.5, 1.39.4, 1.39.3, 1.39.2, 1.39.1, 1.39.0 et 1.38.3.
