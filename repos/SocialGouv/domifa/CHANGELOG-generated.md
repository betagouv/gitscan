## Changelog : domifa (30 derniers jours, au 15 avril 2026)

### Résumé
Cette version apporte des améliorations de sécurité, des corrections de données et des optimisations de performance, notamment grâce à l'ajout d'un système de limitation de requêtes (throttling). Des corrections ont également été apportées à l'interface utilisateur et aux processus de publication.

### Évolutions fonctionnelles
- Ajout d'un système de limitation de requêtes (throttling) pour améliorer la stabilité et la performance de l'API.
- Correction de la validation des champs de formulaire, notamment pour limiter le nombre de caractères.
- Amélioration de la gestion des données des contacts et des référents.
- Intégration de la fonctionnalité SMS Mondomifa.

### Évolutions techniques
- Ajout de logs pour faciliter le débogage et le suivi des performances.
- Mise en place de règles de sécurité renforcées.
- Correction de problèmes liés au build et aux migrations de la base de données.
- Amélioration de la gestion des DTO (Data Transfer Objects) pour garantir la cohérence des données.
- Optimisation du processus de publication avec l'ajout d'une branche dédiée au "fix-enforce-safety".

### Autres changements
- Correction du message de commit pour le processus de publication automatique (semantic-release) afin d'éviter des erreurs de CI.
- Ajout de tests pour le système de limitation de requêtes.
- Amélioration de la documentation interne.
