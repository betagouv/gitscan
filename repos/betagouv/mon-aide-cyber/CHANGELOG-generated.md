## Changelog : mon-aide-cyber (30 derniers jours, au 18/09/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur le renforcement de la sécurité des comptes utilisateurs, l'amélioration de la clarté des informations fournies lors des diagnostics et la stabilisation de l'environnement de développement et de déploiement.

### Évolutions fonctionnelles
- **Clarté du diagnostic** : Ajout de détails explicatifs pour les réponses du référentiel afin de mieux accompagner l'utilisateur.
- **Suivi statistique** : Intégration d'un pixel de suivi (Brevo) pour analyser le parcours d'inscription des aidants et des utilisateurs.
- **Gestion de compte** : Correction du processus de changement de mot de passe.

### Évolutions techniques
- **Sécurité** : Renforcement de la gestion des mots de passe (hachage lors de l'authentification et script de migration des hashs) et correction de la génération d'IV (vecteur d'initialisation).
- **Infrastructure & CI/CD** : Optimisation de la construction des images Docker et réactivation de la pipeline Storybook.
- **Qualité & Tests** : Stabilisation de la suite de tests suite aux montées de version de Vitest et Storybook, et mise en conformité du code avec les nouvelles règles de linting (ESLint) et de formatage (Prettier).
- **Maintenance** : Nettoyage des dépendances obsolètes et correction des fichiers de verrouillage (pnpm-lock).

### Autres changements
- Configuration de l'outil Renovate pour automatiser et sécuriser la gestion des dépendances.
