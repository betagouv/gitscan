## Changelog : idp-status-monitoring (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation de la production des données de statut des IDP. La diffusion des résultats pour `/idp/internet` est désormais plus réactive, en transmettant les informations au fur et à mesure de leur disponibilité. De plus, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations de sécurité.

### Évolutions fonctionnelles
- Amélioration de la réactivité du producteur : les résultats pour l'endpoint `/idp/internet` sont désormais diffusés en continu au fur et à mesure de leur réception, plutôt qu'en attente de la fin du traitement. [#99](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/99)

### Évolutions techniques
- Mise à jour de Hono (framework web) de la version 4.12.10 à la version 4.12.16.
- Mise à jour de Zod (validation de données) de la version 4.3.6 à la version 4.4.1.
- Mise à jour de UUID (génération d'identifiants uniques) de la version 13.0.0 à la version 14.0.0.
- Mise à jour de Bun (runtime JavaScript) de la version 1.3.11-alpine à la version 1.3.13-alpine.
- Mise à jour des types pour Bun (@types/bun) de la version 1.3.11 à la version 1.3.13.
- Mise à jour de l'action Docker/build-push de la version 7.0.0 à la version 7.1.0.
- Mise à jour de Prettier (formateur de code) de la version 3.8.1 à la version 3.8.3.
- Mise à jour de TypeScript de la version 6.0.2 à la version 6.0.3.
- Mise à jour de l'action d'upload d'artefacts (actions/upload-artifact) de la version 7.0.0 à la version 7.0.1.

### Autres changements
- Aucune information supplémentaire à signaler.
