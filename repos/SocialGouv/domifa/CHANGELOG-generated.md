## Changelog : domifa (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration de l'interface utilisateur (frontend) avec l'intégration de la bibliothèque DSFR (Design System for Government) et la correction de plusieurs bugs affectant les formulaires, les tests et l'affichage général. Des corrections ont également été apportées au backend, notamment concernant la gestion des SIRET et des référents. Des améliorations de sécurité et de performance ont été implémentées.

### Évolutions fonctionnelles
- Intégration de la bibliothèque DSFR pour une interface utilisateur plus cohérente et accessible.
- Ajout d'une bannière DSFR à l'interface.
- Correction de problèmes liés aux formulaires et à la page RGAA pour une meilleure accessibilité.
- Correction de l'affichage des fiches pratiques.
- Correction de l'assignation des référents.
- Ajout de la documentation claude.md.

### Évolutions techniques
- Correction de bugs et amélioration des tests frontend.
- Correction de bugs et amélioration des tests backend.
- Ajout d'un mécanisme de "throttling" (limitation de débit) pour protéger le backend contre les requêtes excessives.
- Amélioration de la sécurité avec l'application de règles de sécurité renforcées.
- Refactorisation de DTO (Data Transfer Object) pour améliorer la robustesse et la sécurité.
- Ajout de logs pour faciliter le débogage et le suivi des performances.

### Autres changements
- Correction du fichier de configuration pour les releases (ajout de `[skip ci]` pour éviter des exécutions CI inutiles).
- Amélioration du processus de release avec l'ajout d'une branche dédiée à la correction des problèmes de sécurité.
- Mise à jour de la documentation.
