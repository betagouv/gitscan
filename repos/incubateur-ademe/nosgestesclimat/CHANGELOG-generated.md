## Changelog : nosgestesclimat (30 derniers jours, au 07/08/2026)

### Résumé
Ce mois-ci, le projet a enrichi ses règles de calcul avec de nouvelles données concernant le transport aérien et l'empreinte des véhicules. Des corrections importantes ont été apportées pour éviter les erreurs de double comptage sur certains terminaux numériques. L'expérience utilisateur est également évoluée avec l'introduction de notifications basées sur l'intelligence artificielle. En parallèle, un travail conséquent a été réalisé pour stabiliser et nettoyer les processus de déploiement automatique (CI/CD).

### Évolutions fonctionnelles
- **Transport & Mobilité** : Ajout de nouvelles actions liées au secteur aérien et amélioration du script de calcul de l'empreinte carbone pour les véhicules.
- **Intelligence Artificielle** : Introduction de nouvelles notifications basées sur l'IA [#2792](https://github.com/incubateur-ademe/nosgestesclimat/pull/2792).
- **Corrections** : Résolution d'un problème de double comptage concernant les terminaux numériques [#2795](https://github.com/incubateur-ademe/nosgestesclimat/pull/2795).

### Évolutions techniques
- **CI/CD & Automatisation** : 
    - Nettoyage et optimisation des workflows GitHub Actions (suppression d'actions non conformes et ajout de nouveaux jobs de validation lors des releases du modèle).
    - Optimisation de la configuration de Dependabot.
    - Mise en place de Husky pour la gestion des hooks Git.
- **Architecture & Code** :
    - Refactorisation de la logique d'envoi des messages (dispatch) pour qu'elle soit uniquement pilotée par le modèle.
    - Organisation des icônes via l'utilisation de namespaces [#2796](https://github.com/incubateur-ademe/nosgestesclimat/pull/2796).
- **Releases** : Déploiement des versions 4.14.1, 4.14.2 et 4.14.3.

### Autres changements
- **Gestion de projet** : Nettoyage de l'infrastructure de branches avec la suppression de la branche `preprod`.
