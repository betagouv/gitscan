## Changelog : OpenGateLLM (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, OpenGateLLM a bénéficié d'améliorations significatives en termes de fonctionnalités, notamment l'ajout du support de la transcription audio diarisée et de l'intégration avec Langfuse pour le suivi de l'utilisation. Des refactorings importants ont été réalisés pour améliorer la qualité du code et l'architecture du projet, en particulier au niveau de la gestion des rôles et des modèles. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout du support de la transcription audio diarisée, permettant d'identifier les différents locuteurs dans un enregistrement audio. [#832](https://github.com/etalab-ia/OpenGateLLM/issues/832)
- Intégration avec Langfuse pour le suivi de l'utilisation des modèles et des routes. [#812](https://github.com/etalab-ia/OpenGateLLM/issues/812)
- Correction d'un bug empêchant la fermeture correcte des fichiers PDF après lecture. [#833](https://github.com/etalab-ia/OpenGateLLM/issues/833)
- Correction d'un problème lié à une erreur de websocket dans le playground suite à une mise à jour de Reflex. [#828](https://github.com/etalab-ia/OpenGateLLM/issues/828)
- Correction d'un bug empêchant la création de mots de passe trop longs dans le playground. [#809](https://github.com/etalab-ia/OpenGateLLM/issues/809)
- Correction du code de langue par défaut pour la transcription audio, passant de "english" à "en". [#807](https://github.com/etalab-ia/OpenGateLLM/issues/807)

### Évolutions techniques
- Refactoring de la gestion des rôles (endpoints `/v1/admin/roles`) pour une architecture plus propre et plus maintenable. [#821](https://github.com/etalab-ia/OpenGateLLM/issues/821), [#817](https://github.com/etalab-ia/OpenGateLLM/issues/817), [#808](https://github.com/etalab-ia/OpenGateLLM/issues/808)
- Refactoring du modèle `BaseModeProvider` pour une architecture plus propre. [#796](https://github.com/etalab-ia/OpenGateLLM/issues/796)
- Refactoring des modèles de configuration pour un code plus propre. [#823](https://github.com/etalab-ia/OpenGateLLM/issues/823)
- Réduction du nombre de shards Elasticsearch par défaut de 24 à 12 pour optimiser les performances. [#829](https://github.com/etalab-ia/OpenGateLLM/issues/829)
- Amélioration de la gestion des URLs dans les métriques Prometheus, en utilisant des patterns de route au lieu d'URLs complètes. [#824](https://github.com/etalab-ia/OpenGateLLM/issues/824)
- Suppression de préfixes inutiles dans les messages d'erreur. [#826](https://github.com/etalab-ia/OpenGateLLM/issues/826)
- Suppression d'imports inutiles dans les modèles. [#822](https://github.com/etalab-ia/OpenGateLLM/issues/822)

### Autres changements
- Mise à jour des versions des packages. [#830](https://github.com/etalab-ia/OpenGateLLM/issues/830)
- Correction d'un cas limite dans le bootstrap admin. [#827](https://github.com/etalab-ia/OpenGateLLM/issues/827)
- Amélioration de l'affichage des valeurs non affichées dans les formulaires du playground (provider, router, user). [#802](https://github.com/etalab-ia/OpenGateLLM/issues/802)
- Correction d'un bug empêchant l'envoi du code de langue par défaut au modèle Whisper. [#819](https://github.com/etalab-ia/OpenGateLLM/issues/819)
