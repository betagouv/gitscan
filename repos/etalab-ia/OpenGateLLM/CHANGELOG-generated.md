## Changelog : OpenGateLLM (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de sécurité, de gestion des documents audio, de monitoring et de refactoring du code pour une meilleure architecture et maintenabilité. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment dans l'interface du playground et la gestion des fichiers PDF.

### Évolutions fonctionnelles
- Ajout du support de la transcription diarizée pour l'audio [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832).
- Intégration du support Langfuse pour le suivi de l'utilisation des modèles [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812).
- Correction d'un bug qui empêchait la fermeture correcte des fichiers PDF après lecture [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833).
- Création d'une image "playground" privée pour une utilisation sécurisée [#835](https://github.com/etalab-ia/OpenGateLLM/issues/835).
- Correction d'une erreur dans le playground concernant la longueur maximale du mot de passe [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809).
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en" [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807).

### Évolutions techniques
- Refactoring important des modèles de configuration pour une architecture plus propre [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823).
- Refactoring des endpoints liés aux rôles d'administration vers une architecture plus propre [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808).
- Refactoring du `BaseModeProvider` pour une architecture plus propre [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796).
- Réduction du nombre de shards Elasticsearch par défaut de 24 à 12 pour optimiser les performances [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829).
- Amélioration du monitoring en remplaçant les URLs dans les timeseries Prometheus par des patterns de routes [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824).
- Correction de l'affichage des valeurs non-affichées dans les formulaires du playground (provider, router, user) [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802).
- Correction d'un bug dans le playground lié à une mise à niveau Reflex [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828).

### Autres changements
- Mise à jour de la documentation et des versions générées [#838](https://github.com/etalab-ia/OpenGateLLM/issues/838).
- Correction du workflow de documentation [#837](https://github.com/etalab-ia/OpenGateLLM/issues/837), [#836](https://github.com/etalab-ia/OpenGateLLM/issues/836).
- Suppression de préfixes inutiles dans les messages d'erreur [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826).
- Suppression d'imports inutiles dans le domaine des modèles init [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822).
- Correction des versions des packages [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830).
- Support de l'initialisation du bootstrap admin [#827](https://github.com/etalab-ia/OpenGateLLM/issues/827).
