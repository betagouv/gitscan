## Changelog : mon-aide-cyber (30 derniers jours, au 08/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration du suivi analytique des parcours utilisateurs et sur la consolidation de la chaîne de développement. Le projet bénéficie d'une meilleure automatisation de la gestion des dépendances et d'une optimisation de la construction des environnements de production (Docker).

### Évolutions fonctionnelles
- **Suivi et analytique** : Intégration d'un pixel de suivi (via Brevo) pour analyser le parcours des nouveaux aidants et des utilisateurs inscrits.
- **Interface** : Suppression de la page de statistiques.

### Évolutions techniques
- **Infrastructure et CI/CD** :
    - Optimisation de la construction des images Docker pour garantir l'utilisation des modules Node.js corrects.
    - Automatisation de la gestion et de la sécurité des dépendances via la configuration de Renovate.
- **Qualité du code et Workflow** :
    - Amélioration du processus de formatage automatique du code avec Prettier.
    - Correction et stabilisation des fichiers de verrouillage des dépendances (`pnpm-lock.json`).
