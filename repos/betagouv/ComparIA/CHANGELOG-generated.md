## Changelog : ComparIA (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à ComparIA au cours des 30 derniers jours. Les principales évolutions concernent une refonte importante de l'architecture backend, l'ajout de nouveaux modèles de langage, des corrections de bugs et des améliorations de la gestion des données. Ces changements visent à améliorer la performance, la stabilité et la richesse de la plateforme.

### Évolutions fonctionnelles
- Ajout des modèles de langage Qwen 3.5 397B et MiniMax M2.5 (#282).
- Ajout du modèle Arcee Trinity Large et mise à jour des informations pour Kimi K2.5 (#281).
- Ajout du modèle Kimi K2.5 (#282).
- Mise à jour des descriptions d'Apertus pour indiquer qu'ils sont open source (#280).
- Amélioration de la gestion des erreurs et affichage des erreurs en front-end (#351).
- Correction du comportement de l'auto-swap de modèle en cas de timeout lors de la première interaction (#351).
- Ajout d'un lien vers le tableau de bord Matrice d'impact (#310, #311).
- Ajout d'un popup Tally pour recueillir des feedbacks sur les pages françaises (#310).
- Mise à jour des modèles de langage disponibles (#266, #350).

### Évolutions techniques
- Refonte majeure de l'architecture backend : migration vers Pydantic, simplification de la gestion des sessions, amélioration de la journalisation et des erreurs, et refactorisation du code pour une meilleure maintenabilité.
- Amélioration de la gestion des données et des modèles de langage, avec une validation plus robuste et une meilleure organisation.
- Mise en place d'un système de journalisation plus performant avec Sentry.
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation des performances et de la stabilité de la plateforme.
- Mise à jour des dépendances et des outils de développement.
- Amélioration des tests et de la couverture de code.
- Utilisation de Docker Compose pour faciliter le déploiement et la configuration de l'environnement de développement.
- Ajout de scripts pour la génération automatique de la documentation des modèles de langage.
- Amélioration de la gestion des variables d'environnement et de la configuration.

### Autres changements
- Mise à jour des traductions pour le norvégien Bokmål et le norvégien Nynorsk (#333).
- Mise à jour des fichiers de licence et de la documentation.
- Nettoyage du code et suppression des fichiers inutilisés.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Mise à jour des données de classement des modèles de langage (#301, #280, #281, #302).
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la documentation et des commentaires.
