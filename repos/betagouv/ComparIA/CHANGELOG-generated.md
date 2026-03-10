## Changelog : ComparIA (30 derniers jours)

### Résumé
Ce mois-ci, ComparIA a connu une refonte majeure de son architecture backend, passant à FastAPI et Pydantic pour une meilleure performance et maintenabilité. De nombreux modèles de langage ont été ajoutés et mis à jour, offrant ainsi plus de choix aux utilisateurs. Des améliorations ont également été apportées à la collecte de données, à la gestion des erreurs et à l'interface utilisateur. L'équipe a également travaillé sur l'amélioration de la documentation et de la configuration du projet.

### Évolutions fonctionnelles
- Ajout des modèles de langage Arcee Trinity Large, Kimi K2.5 [#287](https://github.com/betagouv/ComparIA/pulls/287).
- Ajout du modèle Qwen 3.5 397B et mise à jour des modèles Qwen existants [#302](https://github.com/betagouv/ComparIA/pulls/302).
- Correction de l'URL pour le modèle Kimi [#291](https://github.com/betagouv/ComparIA/pulls/291).
- Ajout des modèles Claude Sonnet 4.6 et Qwen 3.5 35B-A3B.
- Ajout du modèle Gemini 3.1 Flash Lite.
- Ajout des modèles GPT 5.3 et GPT 5.4.
- Ajout des modèles Ordbogen Odin (large et medium) pour le portail danois.
- Ajout d'un lien vers le tableau de bord Matrice d'impact [#311](https://github.com/betagouv/ComparIA/pulls/311).
- Ajout d'un popup Tally pour recueillir des commentaires sur les pages françaises [#310](https://github.com/betagouv/ComparIA/pulls/310).
- Amélioration de la gestion des erreurs et ajout d'un système de journalisation plus robuste.
- Ajout de la possibilité de filtrer les données du dataset par spam.
- Mise à jour des données de classement des modèles.

### Évolutions techniques
- Refonte complète du backend avec FastAPI et Pydantic.
- Migration vers un nouveau système de gestion de session.
- Amélioration de la gestion des erreurs et ajout de la journalisation avec Sentry.
- Optimisation des performances du backend.
- Mise à jour des dépendances du projet.
- Amélioration de la configuration et de l'environnement de développement.
- Utilisation de Docker pour faciliter le déploiement et la reproductibilité.
- Ajout de tests unitaires et d'intégration.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Utilisation de Redis pour la mise en cache.
- Amélioration de la gestion des requêtes streaming.
- Ajout de types et de validations avec Pydantic.
- Ajout de tests et de linters.

### Autres changements
- Mise à jour de la documentation du projet.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Traductions mises à jour pour le danois, le norvégien Bokmål et le norvégien Nynorsk via Weblate.
- Mise à jour des fichiers de licence.
- Nettoyage du code et suppression des dépendances inutiles.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des variables d'environnement.
- Ajout de scripts pour automatiser les tâches de développement et de déploiement.
