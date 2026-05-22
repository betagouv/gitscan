## Changelog : ComparIA (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de modèles de langage supportés, avec l'ajout de GPT-5.5, DeepSeek V4 et Gemini 3.5 Flash. Des efforts importants ont été consacrés à la maintenance de la plateforme, notamment la correction de bugs liés à la détection de spam, l'amélioration de la gestion des données et la simplification de l'infrastructure de déploiement. Une nouvelle fonctionnalité de gestion des modèles archivés a également été introduite.

### Évolutions fonctionnelles
- Ajout des modèles de langage GPT-5.5 et GPT-5.5 Pro. [#456](https://github.com/betagouv/ComparIA/pull/456)
- Ajout du modèle de langage DeepSeek V4 Pro et Flash. [#455](https://github.com/betagouv/ComparIA/pull/455)
- Ajout du modèle de langage Gemini 3.5 Flash et Grok 4.3, et archivage de 6 modèles. [#480](https://github.com/betagouv/ComparIA/pull/480)
- Amélioration de la détection de spam en bloquant des motifs d'injection de code et des tentatives de "roleplay". [#473](https://github.com/betagouv/ComparIA/pull/473), [#468](https://github.com/betagouv/ComparIA/pull/468), [#467](https://github.com/betagouv/ComparIA/pull/467)
- Correction d'un bug empêchant le calcul correct des intervalles de confiance pour le classement des modèles. [#470](https://github.com/betagouv/ComparIA/pull/470)
- Suppression du tag "nouveau" des modèles de plus de deux mois. [#430](https://github.com/betagouv/ComparIA/pull/430)
- Mise à jour du lien vers le formulaire du kit facilitateur. [#459](https://github.com/betagouv/ComparIA/pull/459)

### Évolutions techniques
- Refactorisation de l'infrastructure de déploiement pour supporter plusieurs instances (fr et da) avec une configuration simplifiée. [#481](https://github.com/betagouv/ComparIA/pull/481)
- Suppression de l'utilisation de Vertex AI pour l'analyse des LLM, au profit d'OpenRouter.
- Amélioration de la gestion des clés API via un coffre-fort (Keepass).
- Simplification de la configuration de la base de données pour chaque instance.
- Nettoyage et simplification du code, notamment dans les scripts de déploiement.
- Ajout d'un outil en ligne de commande (CLI) pour la gestion de la base de données (archivage, nettoyage, analyse).
- Amélioration de la gestion des logs et ajout de logs plus détaillés pour le débogage.
- Refactorisation des requêtes SQL et amélioration des performances.
- Suppression de code obsolète et de dépendances inutiles.
- Correction de problèmes de typage dans les tests.

### Autres changements
- Mise à jour de la documentation et du fichier README.
- Corrections de traductions dans Weblate (Italien, Norvégien Bokmål, Norvégien Nynorsk, Anglais).
- Mise à jour des dépendances (npm et pip).
- Corrections mineures de style et de formatage du code.
