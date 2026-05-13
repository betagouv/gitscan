## Changelog : anssi-recommandations-cyber (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, la gestion des erreurs et l'ajout de nouvelles fonctionnalités de recherche et de gestion des documents. Des efforts importants ont été faits pour la maintenance et la sécurité, avec des mises à jour régulières des dépendances et l'implémentation d'un mode maintenance. L'intégration de la collection "Jeopardy" pour la recherche est également une nouveauté majeure.

### Évolutions fonctionnelles
- Ajout d'une page FAQ.
- Implémentation d'une recherche sur la collection "Jeopardy" permettant d'accéder aux chunks originaux.
- Possibilité de lister les documents d'une collection dans un dataframe via leurs noms.
- Amélioration des messages d'erreur pour une meilleure clarté.
- Ajout d'un tracking Matomo sur le bouton de copie de réponse pour l'analyse de l'utilisation.
- Obligation de la reformulation pour améliorer la qualité des réponses.
- Génération de l'URL d'accès aux documents sources pour faciliter la consultation.
- Ajout d'un notebook pour comparer les collections d’indexation et jeopardy.

### Évolutions techniques
- Mise en place d'un mode maintenance avec une page statique 503.
- Implémentation d'un cooldown d'une semaine pour l'installation des dépendances afin d'améliorer la stabilité.
- Refactorisation de la gestion des conversations, suppression de l'identifiant obsolète et utilisation de la conversation pour les retours utilisateurs.
- Amélioration de la gestion des erreurs et remontée des messages d'erreur originaux.
- Mise à jour de la version de PostgreSQL à 17 pour le développement local.
- Mise à jour de plusieurs dépendances (cryptography, dompurify, pytest, etc.) pour corriger des vulnérabilités de sécurité et améliorer la performance.
- Initialisation de Renovate pour la gestion automatisée des dépendances.
- Ajout de workflows de déploiement sur l'environnement de production et obligation du déploiement en démo avant la production.
- Configuration de Sentry et d'un journal en mémoire pour les tests.

### Autres changements
- Mise à jour de la documentation et du wording sur l'interface utilisateur.
- Correction de typos et amélioration de la qualité du code.
- Ajout d'un fichier de configuration pour Renovate.
- Ajout d'une configuration pour la collection "jeopardy".
- Obtention du consentement pour le suivi Matomo.
