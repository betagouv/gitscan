## Changelog : ComparIA (30 derniers jours)

### Résumé
Ce mois-ci, ComparIA a connu une refonte majeure de son architecture backend, avec une migration vers FastAPI et une amélioration de la gestion des sessions et du streaming. De nouveaux modèles d'IA ont été ajoutés et les données de classement ont été mises à jour. L'interface utilisateur a également été améliorée, notamment avec une meilleure gestion des erreurs et une simplification de l'URL de l'API.

### Évolutions fonctionnelles
- Ajout des modèles d'IA Claude Sonnet 4.6, Qwen 3.5 397B, MiniMax M2.5 et Arcee Trinity Large (#287, #291, #301, #302).
- Mise à jour des données de classement des modèles d'IA.
- Amélioration de la gestion des erreurs et affichage plus clair des erreurs dans l'interface utilisateur.
- Correction d'un problème de troncature de la sortie des modèles.
- Correction d'un problème de timeout lors de la première interaction avec un modèle.
- Correction de l'affichage des modèles disponibles en fonction du pays.
- Correction d'un bug empêchant l'enregistrement des votes.
- Correction d'un problème lié à la récupération de l'URL de l'API.
- Amélioration de la gestion des votes et des réactions.
- Ajout d'une gestion des licences plus précise pour les modèles.
- Correction de l'affichage des modèles archivés.

### Évolutions techniques
- Refonte complète du backend avec migration vers FastAPI.
- Amélioration de la gestion des sessions et du streaming SSE.
- Utilisation de Pydantic pour la validation des données et la sérialisation.
- Mise en place d'une configuration plus robuste avec des variables d'environnement.
- Amélioration de la gestion des logs avec l'ajout d'un logger personnalisé.
- Utilisation de Docker Compose pour faciliter le déploiement et le développement.
- Mise à jour des dépendances et des outils de développement.
- Amélioration de la structure du code et de la documentation.
- Ajout de tests unitaires et d'intégration.
- Utilisation de Redis pour la mise en cache des données.
- Amélioration de la performance et de la scalabilité de l'application.
- Intégration de Sentry pour la surveillance des erreurs.

### Autres changements
- Mise à jour des traductions avec Weblate (#247).
- Nettoyage du code et suppression des fichiers inutiles.
- Mise à jour des fichiers de configuration et des dépendances.
- Amélioration de la documentation et des commentaires.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Ajout de fichiers de configuration pour l'environnement de développement.
- Mise à jour des modèles de données et des schémas JSON.
- Ajout de tests pour valider les données des modèles.
