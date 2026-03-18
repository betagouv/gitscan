## Changelog : ComparIA (30 derniers jours, au 17 mars 2026)

### Résumé
Ce mois-ci, ComparIA a connu des améliorations significatives en termes de performance, de stabilité et de fonctionnalités. L'accent a été mis sur l'optimisation du calcul des classements, l'ajout de nouveaux modèles de langage (Mistral Small 4, GPT-5.4, Gemini 3.1 Flash Lite, etc.), et l'amélioration de l'expérience utilisateur, notamment en matière de gestion des erreurs et de filtrage anti-spam. Des efforts importants ont également été consacrés à la mise en place d'une infrastructure de déploiement plus robuste et automatisée.

### Évolutions fonctionnelles
- Ajout du modèle Mistral Small 4 (119B MoE) [#392](https://github.com/betagouv/ComparIA/pull/392).
- Ajout du modèle GPT-5.4 [#374](https://github.com/betagouv/ComparIA/pull/374).
- Ajout du modèle Gemini 3.1 Flash Lite [#386](https://github.com/betagouv/ComparIA/pull/386).
- Ajout du modèle Claude Sonnet 4.6.
- Ajout des modèles Qwen 3.5 397B & MiniMax M2.5.
- Ajout des modèles Ordbogen Odin (odin-large, odin-medium) pour le portail danois.
- Mise en place d'un système de cache probabiliste des réponses pour les premiers tours de conversation, améliorant la réactivité.
- Amélioration de l'affichage des données de consommation énergétique et de leur équivalence avec des impacts environnementaux (fonte des glaces arctiques, etc.).
- Ajout d'un lien vers le tableau de bord "Matrice d'impact" dans le pied de page.
- Ajout d'un popup Tally pour recueillir les commentaires des utilisateurs sur les pages françaises.
- Possibilité d'ouvrir un modèle à partir d'une URL avec un hash.
- Mise à jour des descriptions des modèles Apertus pour refléter leur nature open source.

### Évolutions techniques
- Refonte du calcul des classements : calcul en application et stockage en cache Redis au lieu de fichiers statiques [#390](https://github.com/betagouv/ComparIA/pull/390).
- Optimisation des requêtes SQL et utilisation d'helpers pour la gestion de la base de données.
- Refactorisation du code pour améliorer la modularité et la maintenabilité.
- Mise en place d'une infrastructure CI/CD plus robuste avec des pipelines de déploiement pour les environnements de développement, de staging et de production.
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Mise à jour des dépendances (ecologits, fastapi, litellm, etc.).
- Suppression de code obsolète et nettoyage du code.
- Implémentation d'un filtre anti-spam basé sur des expressions régulières pour bloquer les injections de prompts et les attaques JSON.
- Amélioration de la gestion des timeouts et des erreurs lors des appels aux modèles de langage.
- Utilisation de variables d'environnement pour la configuration.

### Autres changements
- Mise à jour des traductions dans plusieurs langues (Danois, Norvégien Bokmål, Anglais) grâce à Weblate.
- Mise à jour de la documentation et du fichier README.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de la licence MIT.
- Archivage des modèles Cohere Command A, GPT 5.1, et GLM 4.6.
- Suppression de pgAdmin de l'infrastructure.
- Correction de problèmes liés à l'environnement Sentry.
