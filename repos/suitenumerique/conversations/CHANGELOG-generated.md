## Changelog : conversations (30 derniers jours, au 2 septembre 2026)

### Résumé
Ce mois a été marqué par des changements structurels majeurs, notamment la migration du frontend vers Vite et la mise à jour des outils d'intelligence artificielle. L'expérience de discussion a été considérablement fluidifiée pour l'utilisateur, tandis que la sécurité et la robustesse du système ont été renforcées par l'introduction de limitations de débit et une optimisation des processus de test.

### Évolutions fonctionnelles
- **Amélioration de l'expérience de chat** : gestion plus fluide du streaming des réponses, prévention des doubles envois de messages et meilleure gestion des erreurs lors du chargement de l'historique.
- **Nouvelles interfaces** : ajout d'un panneau de sources pour les réponses et amélioration de l'interface d'administration (affichage de la taille des conversations et augmentation de la liste à 200 éléments par page).
- **Optimisation de l'assistant** : mise à jour des instructions de l'agent pour une meilleure pertinence avec l'écosystème DINUM.
- **Simplification de l'accès** : suppression de la page et de la barrière du code d'activation.
- **Suivi et métriques** : intégration du suivi des projets, des exports de documents, des résumés et de l'empreinte carbone.
- **Interface utilisateur** : corrections visuelles (icônes) et déplacement des paramètres d'analyse vers la section générale.

### Évolutions techniques
- **Migration majeure du frontend** : passage de Next.js vers Vite et React Router pour plus de légèreté et de flexibilité.
- **Mise à jour de la stack IA** : migration vers Pydantic-AI 2.x et Vercel AI SDK v5.
- **Sécurité et stabilité** : mise en place de limitations de débit (*throttling*) pour la création de conversations et de projets, et sécurisation de la chaîne d'approvisionnement (pinning des actions GitHub).
- **Refactorisation** : unification du client HTTP autour de `httpx` et restructuration du module de configuration par domaines.
- **Optimisation CI/CD** : parallélisation des tests E2E entre les navigateurs et optimisation de la construction des images de test.
- **Nettoyage** : suppression des outils de recherche web inutilisés (Tavily et Albert).

### Autres changements
- **Documentation** : ajout de la documentation concernant les réglages de limitation de débit de l'API.
- **Internationalisation** : mise à jour des chaînes de caractères traduites.
