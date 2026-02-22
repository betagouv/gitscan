## Changelog : ComparIA (30 derniers jours)

### Résumé
Ce mois-ci, ComparIA a connu une refonte majeure de son architecture backend, avec une migration vers FastAPI et une amélioration significative de la gestion des modèles, des données et des sessions. De nouveaux modèles de langage ont été ajoutés et les données de classement ont été mises à jour. L'interface utilisateur a également été améliorée, notamment avec une meilleure gestion des erreurs et l'ajout de liens vers la Matrice d'impact.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les modèles par portail pays (#301).
- Ajout des modèles de langage Qwen 3.5 397B et MiniMax M2.5, et archivage des modèles plus anciens (#302).
- Ajout du modèle Arcee Trinity Large et mise à jour des informations concernant Kimi K2.5 (#287).
- Ajout du modèle Qwen3-Coder-Next (#302).
- Correction de l'URL du modèle Kimi 2.5 (#291).
- Ajout d'un lien vers le tableau de bord de la Matrice d'impact dans le pied de page (#310, #309).
- Mise à jour de l'objectif de votes en français à 300 000 (#311).
- Ajout d'un popup Tally pour recueillir des commentaires sur les pages françaises (#307).
- Amélioration de la gestion des erreurs et affichage des erreurs globales dans l'interface utilisateur.
- Correction de l'affichage des modèles dans le composant de sélection personnalisé.

### Évolutions techniques
- Refonte complète du backend avec migration vers FastAPI.
- Amélioration de la gestion des sessions et des données de conversation.
- Utilisation de Pydantic pour la validation des données et la sérialisation.
- Mise en place d'un système de journalisation plus robuste avec Sentry.
- Amélioration de la gestion des dépendances et du processus de construction avec Docker.
- Mise à jour et optimisation des scripts de construction et de déploiement.
- Amélioration de la gestion des modèles de langage et de leurs métadonnées.
- Utilisation de Redis pour la mise en cache et la gestion des sessions.
- Ajout de tests unitaires et d'intégration.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances et des bibliothèques.

### Autres changements
- Mise à jour de la documentation et des fichiers de contribution.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Mise à jour des données de classement des modèles de langage.
- Amélioration des messages de journalisation et de débogage.
- Ajout de commentaires et de documentation au code.
- Corrections de traductions via Weblate (#247).
