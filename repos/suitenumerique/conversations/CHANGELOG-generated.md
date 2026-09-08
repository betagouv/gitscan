## Changelog : conversations (30 derniers jours, au 07/09/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec une refonte majeure de son interface utilisateur et une modernisation profonde de son architecture technique. L'expérience de discussion a été considérablement fluidifiée pour les utilisateurs, tandis que la robustesse et la sécurité du système ont été renforcées pour garantir une utilisation stable et protégée.

### Évolutions fonctionnelles
- **Amélioration de l'expérience de chat** : gestion plus fluide de l'envoi des messages (prévention des doubles envois), maintien des messages en cas d'erreur de connexion et affichage plus naturel des réponses de l'IA.
- **Nouvelles fonctionnalités d'interface** : ajout d'un panneau de sources pour les réponses de l'IA et intégration de nouveaux outils de suivi de l'empreinte carbone.
- **Simplification du parcours utilisateur** : suppression de la page de code d'activation pour un accès plus direct.
- **Optimisation de l'assistant** : mise à jour des instructions de l'agent pour une meilleure pertinence des réponses de l'assistant DINUM.
- **Améliorations de l'administration** : affichage de la taille des conversations et augmentation du nombre de conversations visibles par page (200) pour faciliter les actions groupées.
- **Retour utilisateur** : ajout de messages explicatifs lorsqu'une limite de création est atteinte.

### Évolutions techniques
- **Migration majeure du frontend** : passage de Next.js vers une architecture basée sur Vite et React Router pour plus de légèreté et de rapidité.
- **Modernisation de l'IA** : montée de version vers le Vercel AI SDK v5 et Pydantic-AI 2.x, incluant un nouveau format de stockage et de streaming des messages.
- **Sécurité renforcée** : mise en place de limitations de débit (throttling) pour la création de projets et de conversations, et sécurisation de la chaîne d'approvisionnement en verrouillant les versions des actions GitHub.
- **Optimisation de la CI/CD** : parallélisation des tests E2E (sharding) et optimisation du processus de build des images pour accélérer les déploiements.
- **Refactoring backend** : remplacement de la bibliothèque `requests` par `httpx` et restructuration du module de configuration pour une meilleure modularité.
- **Observabilité** : intégration de PostHog pour le suivi des indicateurs clés (utilisation des projets, exports de documents, résumés).

### Autres changements
- **Documentation** : refonte de la procédure de release et ajout de la documentation concernant les paramètres de limitation de l'API.
- **Internationalisation** : mise à jour des chaînes de traduction [#711](https://github.com/suitenumerique/conversations/pull/711).
