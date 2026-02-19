## Changelog : helm-dev-backend (30 derniers jours)

### Résumé
Ce backend de développement Helm a été mis à jour pour offrir plus de flexibilité lors du déploiement d'applications sur Kubernetes. Les utilisateurs peuvent désormais configurer plus finement les ressources allouées et le nombre de réplicas pour le composant `dsproxy`, permettant une meilleure adaptation aux besoins spécifiques de leurs environnements. Une nouvelle version du chart Helm a également été publiée.

### Évolutions fonctionnelles
- Possibilité de configurer les ressources (CPU, mémoire) allouées au déploiement `dsproxy` (#cb9b129).
- Possibilité de configurer le nombre de réplicas pour le déploiement `dsproxy` (#db68879).

### Évolutions techniques
- Publication de la version 0.0.8 du chart Helm (#52b02b6).
- Publication de la version 0.0.7 du chart Helm (#6c0791e).
