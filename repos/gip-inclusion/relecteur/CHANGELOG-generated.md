## Changelog : relecteur (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois-ci, relecteur a franchi une étape importante dans son automatisation et sa robustesse. L'outil est désormais capable de gérer de manière beaucoup plus fluide les interruptions (nouveaux commits, limites de débit de l'IA) et s'intègre plus profondément dans les workflows de développement via GitHub Actions. L'expérience utilisateur est également améliorée par une meilleure présentation des résultats et un support natif du français.

### Évolutions fonctionnelles
- **Amélioration de l'expérience de revue** : Les résultats sont désormais présentés de manière plus lisible dans les Pull Requests, avec des résumés par revue et un système de repliement du code cité pour faciliter la lecture des défauts.
- **Localisation** : Les commentaires de revue sont désormais rédigés en français par défaut (configurable dans les paramètres).
- **Gestion intelligente des interruptions** : Le processus de revue peut désormais reprendre automatiquement en cas de nouveau push sur une PR, de timeout ou de limitation de débit (rate limit) de l'API.
- **Personnalisation accrue** : Possibilité de sélectionner précisément les fichiers à réviser via le fichier `.relecteur/config.toml` et de configurer le modèle d'IA ainsi que le "juge" directement dans le dépôt.
- **Compatibilité étendue** : Support de la revue des dépôts privés en utilisant des jetons d'accès sécurisés.

### Évolutions techniques
- **Intégration CI/CD** : Mise en place d'une GitHub Action permettant d'exécuter les revues directement en CI, y compris pour tester l'outil sur ses propres Pull Requests.
- **Métriques de performance** : Ajout de statistiques détaillées dans les rapports d'évaluation, incluant le temps moyen et la consommation de tokens par revue.
- **Robustesse et erreurs** : Amélioration de la gestion des erreurs réseau et des erreurs de service (503) pour une meilleure distinction entre les problèmes d'infrastructure et les problèmes de permissions.
- **Refactorisation** : Optimisation interne des classes de défaillance et des statuts du moteur pour une meilleure maintenance.
- **Connectivité** : Support de l'API Anthropic pour les évaluations.

### Autres changements
- **Documentation** : Refonte complète du README en français, incluant un guide de démarrage rapide plus clair et des pages dédiées selon le profil de l'utilisateur (développeur, décideur, etc.).
- **Comparatifs** : Ajout d'une section comparative avec d'autres outils du marché (Claude Code Review, CodeRabbit, Greptile) pour aider au choix de la solution.
