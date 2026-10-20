## Changelog : ds-api-client (30 derniers jours, au 07/10/2026)

### Résumé
Cette période a été marquée par une mise à jour majeure du client pour intégrer les nouveaux schémas GraphQL (versions de janvier et septembre 2026). L'ajout d'un module de gestion locale du schéma et le renforcement des processus d'automatisation (CI/CD) permettent une meilleure stabilité et une facilité d'utilisation accrue pour les développeurs.

### Évolutions fonctionnelles
- **Mise à jour du schéma GraphQL** : Intégration des nouveaux schémas et des nouveaux types pour les versions du 26/01/2026 et du 08/09/2026.
- **Gestion du schéma** : Ajout d'un nouveau module permettant de télécharger et de mettre à jour le schéma GraphQL localement.
- **Corrections GraphQL** : Résolution d'erreurs dans les fragments et mise à jour des liens du schéma.

### Évolutions techniques
- **Amélioration de la CI/CD** : 
    - Mise en place de workflows pour la publication sur GitHub.
    - Utilisation de "trusted publishers" pour sécuriser les déploiements.
    - Ajout de "hosted runners" pour l'exécution des tâches.
- **Fiabilisation des tests** : Mise à jour des tests de bout en bout (E2E) et corrections des tests automatisés au sein de la CI.
- **Déploiement** : Correction des packages de déploiement.

### Autres changements
- **Nettoyage** : Suppression de logs de console (`console.log`) et correction de la terminologie dans le fichier `package.json`.
