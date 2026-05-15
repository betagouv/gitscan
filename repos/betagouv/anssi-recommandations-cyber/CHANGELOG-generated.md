## Changelog : anssi-recommandations-cyber (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, la gestion des erreurs et la préparation du déploiement en production. Des refactorings importants ont été réalisés pour simplifier le code et améliorer la gestion des interactions avec le modèle Albert. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, notamment en affichant des messages d'erreur plus clairs et en améliorant la gestion des documents sources.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs : des messages d'erreur plus clairs et génériques sont maintenant affichés à l'utilisateur.
- Accès aux documents sources : une route GET a été ajoutée pour récupérer les documents sources demandés par l'utilisateur, avec gestion des erreurs 404 si le document n'est pas trouvé.
- Page FAQ : initialisation de la page FAQ.
- Consentement Matomo : ajout d'un mécanisme pour obtenir le consentement de l'utilisateur pour le suivi Matomo.
- Reformulation obligatoire : la reformulation est maintenant obligatoire.
- Possibilité de lister les documents d'une collection dans un dataframe via leurs noms.
- Amélioration de la recherche : la recherche a été généralisée pour un comportement plus homogène.
- Gestion des retours utilisateurs : refonte de la gestion des retours utilisateurs, avec utilisation de l'identifiant de conversation.

### Évolutions techniques
- Préparation du déploiement en production : ajout d'un workflow de déploiement et obligation de passer par la démo avant la production.
- Refactoring : suppression de la notion d'id\_conversation obsolète et extraction d'un `ParagrapheReponseMaitrisee` pour faciliter les réponses.
- Mise à jour des dépendances : plusieurs dépendances ont été mises à jour, notamment `pytest`, `dompurify`, `cryptography`, `python-dotenv`, `eslint`, `vite`, `svelte`, `prettier`, et `@lab-anssi/ui-kit`.
- Intégration de Renovate : initialisation de Renovate pour la gestion automatisée des dépendances.
- Journalisation : ajout de la journalisation du document source demandé.
- Amélioration des tests : ajout d'une base de données mémoire et d'un Sentry mémoire pour les tests.
- Passage à PostgreSQL 17 pour le développement local.

### Autres changements
- Ajout d'un notebook pour comparer les collections d'indexation et jeopardy.
- Ajout du tracking Matomo sur le bouton de copie de réponse.
- Suppression du tag conversation obsolète.
- Mise à jour de la configuration de Renovate.
