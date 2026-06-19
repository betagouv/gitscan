## Changelog : ComparIA (30 derniers jours, au 2026-06-15)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de performance, de robustesse et de fonctionnalités. L'export de données a été optimisé pour gérer de plus gros volumes, et des corrections ont été apportées pour améliorer la fiabilité des données. De nouveaux modèles de langage ont été ajoutés et la détection de contenu indésirable (spam, jailbreak) a été renforcée. L'interface utilisateur a également été améliorée avec l'ajout de nouvelles fonctionnalités et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout du modèle de langage MiniMax M3 au catalogue [#531](https://github.com/betagouv/ComparIA/pull/531).
- Ajout du modèle de langage IBM Granite 4.1 8B avec traductions en anglais et danois [#517](https://github.com/betagouv/ComparIA/pull/517).
- Ajout du modèle Gemini 3.5 Flash [#480](https://github.com/betagouv/ComparIA/pull/480).
- Amélioration de l'interface utilisateur avec l'ajout de boutons de vote animés et un retour visuel plus clair lors des votes [#526](https://github.com/betagouv/ComparIA/pull/526).
- Ajout de liens vers les résultats de recherche web dans l'interface utilisateur [#447](https://github.com/betagouv/ComparIA/pull/447).
- Implémentation d'un système de blocage de schémas de "roleplay" et de "jailbreak" pour améliorer la sécurité et la qualité des interactions [#481](https://github.com/betagouv/ComparIA/pull/481).
- Ajout d'un toggle pour activer/désactiver la recherche web.
- Ajout de la traduction danoise pour les nouveaux modèles Gemini et Grok.

### Évolutions techniques
- Optimisation de l'export des données en utilisant un cache basé sur des fichiers Parquet pour accélérer le processus [#524](https://github.com/betagouv/ComparIA/pull/524).
- Amélioration de la gestion des erreurs et des logs, notamment pour la connexion à Loki.
- Refactorisation importante de la base de données et des modèles de données, incluant l'utilisation de UUIDs et une meilleure organisation des tables.
- Mise en place d'un système de migrations de base de données plus robuste et incrémental.
- Utilisation de SQLModel pour une meilleure gestion des modèles de base de données.
- Amélioration de la gestion du streaming des réponses des modèles de langage.
- Correction de bugs liés à la gestion des comparaisons archivées et des données manquantes.
- Suppression du modèle Grok en raison de problèmes de qualité et d'utilisation [#512](https://github.com/betagouv/ComparIA/pull/512).
- Mise à jour des dépendances (protobufjs, pip, npm).

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur.
- Amélioration de la documentation et des commentaires dans le code.
- Nettoyage du code et suppression de code obsolète.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des traductions italiennes via Weblate.
- Correction de bugs liés à la sélection de la langue.
- Ajout de variables d'environnement pour la configuration.
- Suppression de fichiers de configuration inutiles.
- Ajout de logs pour faciliter le débogage.
