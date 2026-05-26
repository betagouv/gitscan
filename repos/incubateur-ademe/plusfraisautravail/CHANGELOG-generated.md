## Changelog : plusfraisautravail (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, le projet plusfraisautravail a connu des avancées significatives, notamment l'ajout d'un mode de démonstration, l'intégration de données de vigilances (alertes météo et écowatt), et une refonte de l'infrastructure de déploiement. Ces améliorations visent à offrir une meilleure expérience utilisateur et à faciliter la maintenance et l'évolution du projet.

### Évolutions fonctionnelles
- Ajout d'un mode de démonstration pour faciliter la présentation et le test de l'application.
- Intégration des alertes météo et des informations Ecowatt (électricité) pour informer les utilisateurs sur les risques liés aux conditions climatiques et à la consommation d'énergie.
- Amélioration de l'affichage des alertes avec des tooltips détaillés et des liens vers les sources d'information.
- Refonte de la vue des phénomènes pour une meilleure lisibilité et une présentation plus claire des informations.

### Évolutions techniques
- Migration de l'infrastructure de déploiement vers Scaleway et OpenTofu, améliorant ainsi la robustesse et l'automatisation du processus.
- Mise en place de pre-commit hooks pour garantir la qualité du code et faciliter les revues.
- Utilisation de l'environnement variable `CORS_ORIGINS` pour configurer les autorisations CORS de l'API.
- Refactoring du code pour améliorer la maintenabilité et la lisibilité.
- Correction de problèmes de linting avec Ruff.
- Amélioration de la gestion des erreurs dans l'API météo, traitant les `KeyError` comme des alertes valides.
- Mise à jour de l'URL de l'application.

### Autres changements
- Ajout de workflows CI/CD pour le déploiement continu sur GitHub Environments.
- Suppression du cache de Vite du `.gitignore`.
- Traduction de certains éléments de l'interface utilisateur.
- Amélioration de l'affichage du lien source dans le widget d'alerte.
- Modification du namespace pour éviter les conflits.
- Ajout de tests pour le mode de démonstration.
