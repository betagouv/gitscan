## Changelog : domifa (30 derniers jours, au 20 avril 2026)

### Résumé
Cette version apporte des améliorations de sécurité et de robustesse à la plateforme DomiFa. Des corrections de DTO (Data Transfer Object) ont été implémentées pour renforcer la validation des données, et un système de limitation de requêtes (throttling) a été ajouté pour protéger le backend contre les abus. Des corrections de bugs et des ajustements divers améliorent également la stabilité et la qualité du code.

### Évolutions fonctionnelles
- Ajout d'un système de limitation de requêtes (throttling) pour améliorer la sécurité et la disponibilité du backend.
- Correction de la validation des données pour les décisions, les contacts et les référents.
- Correction du nombre de caractères acceptés dans un champ du frontend.

### Évolutions techniques
- Mise en place de logs pour le système de limitation de requêtes afin de faciliter le débogage et le monitoring.
- Désactivation du throttling pour les requêtes de health check afin d'assurer la disponibilité du service.
- Amélioration des tests unitaires.
- Renforcement des règles de sécurité.

### Autres changements
- Ajout d'une branche `fix-enforce-safety` au workflow de release pour faciliter les corrections de sécurité.
- Ajout de la balise `[skip ci]` aux messages de commit de semantic-release pour éviter des exécutions CI inutiles.
- Correction de la configuration de semantic-release.
