## Changelog : OpenGateLLM (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'architecture interne d'OpenGateLLM, notamment au niveau de la gestion des rôles et des modèles. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier dans l'interface Playground et pour la transcription audio.

### Évolutions fonctionnelles
- Correction d'un problème dans l'interface Playground où une erreur WebSocket se produisait après une mise à jour de Reflex [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828).
- Correction d'un problème empêchant la création d'un administrateur bootstrap dans certains cas [#827](https://github.com/etalab-ia/OpenGateLLM/issues/827).
- Correction d'une erreur dans l'interface Playground concernant la longueur maximale du mot de passe (72 caractères) [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809).
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en" [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807).
- Correction d'un problème où la langue par défaut était envoyée au modèle Whisper, même si non pertinente [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819).
- Amélioration de l'affichage des valeurs non affichées dans les formulaires de Provider, Router et User dans l'interface Playground [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802).

### Évolutions techniques
- Refactorisation de la gestion des rôles (endpoints `/v1/admin/roles`) pour une architecture plus propre et plus maintenable [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808), [#801](https://github.com/etalab-ia/OpenGateLLM/issues/801).
- Refactorisation du modèle de configuration pour un code plus propre [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823).
- Refactorisation de la classe `BaseModelProvider` pour une architecture plus propre [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796).
- Suppression des URLs spécifiques dans les métriques Prometheus pour la gestion des chunks de documents, en utilisant des patterns de routes plus génériques [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824).
- Suppression d'imports inutiles dans le domaine des modèles [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822).
- Suppression de préfixes inutiles dans les messages d'erreur [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826).
- Initialisation du bootstrap admin [#799](https://github.com/etalab-ia/OpenGateLLM/issues/799).

### Autres changements
- Aucun changement significatif à signaler.
