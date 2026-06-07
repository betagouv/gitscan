## Changelog : apistration (30 derniers jours, au 2026-06-05)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'audit et la sécurité, avec l'ajout d'un suivi des activités des administrateurs et le renforcement de la gestion des accès. Des améliorations significatives ont également été apportées à l'API Particulier, notamment en termes de documentation des scopes et de gestion des accès via FranceConnect. Enfin, des améliorations ont été apportées aux tableaux de bord d'administration et à la documentation.

### Évolutions fonctionnelles
- **API Particulier :** Ajout de la documentation des scopes (périmètres d'accès) pour chaque endpoint et chaque attribut de réponse, facilitant l'intégration pour les développeurs.
- **API Particulier :**  Possibilité d'expliquer les scopes disponibles pour une meilleure compréhension.
- **API Particulier :**  Restriction de l'accès à l'endpoint ANTS identite_particulier à son scope dédié.
- **Tableaux de bord d'administration :** Ajout d'un tableau de bord global pour les fournisseurs, permettant de suivre l'évolution des consommateurs et des habilitations.
- **Tableaux de bord d'administration :** Ajout de graphiques d'évolution cumulée des consommateurs et des habilitations.
- **Tableaux de bord d'administration :** Ajout de séries temporelles pour les consommateurs et les habilitations.
- **Tableaux de bord d'administration :**  Affichage des statistiques agrégées des endpoints legacy sous leur version actuelle.
- **Tableaux de bord d'administration :** Ajout d'une section "Maintenance & Incidents" à la newsletter de l'API Particulier.
- **Tableaux de bord d'administration :** Ajout d'une section "Nouveautés / changelog" dans le footer et le titre des pages.
- **CNAV :**  Possibilité de spécifier le lieu de naissance (commune) lors des requêtes.
- **Scholarship API:** Ajout de nouvelles données pour les bourses scolaires.
- **API Editeur:** Ajout d'une API pour la gestion des délégations d'éditeur.

### Évolutions techniques
- **Audit :** Implémentation d'un suivi complet des activités des administrateurs (création de tokens, interdictions, modifications, impersonations).
- **Sécurité :** Renforcement de la validation des paramètres de civilité pour éviter les injections.
- **Sécurité :**  Exigence du token FranceConnect pour les endpoints V3+ nécessitant FranceConnect.
- **Refactoring :** Extraction de la logique de "transcogage" dans un module dédié.
- **Tests :** Amélioration des tests et de la documentation des tests.
- **Documentation :** Clarification de la documentation concernant le périmètre du quotient familial.
- **Node.js SDK :** Ajout d'un SDK Node.js (TypeScript) pour les API Entreprise et Particulier.
- **CI/CD :** Mise à jour des dépendances et des actions GitHub.

### Autres changements
- Correction de bugs mineurs liés à l'affichage et à la gestion des liens.
- Mise à jour des dépendances Ruby et JavaScript.
- Amélioration de la structure du code et de la lisibilité.
- Ajout de commentaires et de documentation pour faciliter la maintenance.
- Correction de problèmes de CORS pour l'OpenAPI.
- Suppression de code obsolète.
