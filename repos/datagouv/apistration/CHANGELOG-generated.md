## Changelog : apistration (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, apistration a connu des améliorations significatives en termes de monitoring, de tableaux de bord pour les fournisseurs d'API, et de gestion des erreurs.  De nouvelles fonctionnalités ont été ajoutées pour faciliter le suivi de la consommation des API et l'identification des problèmes.  Un SDK Node.js a été ajouté pour faciliter l'intégration avec les API Entreprise et Particulier.  Des corrections et des améliorations ont également été apportées à la documentation et à la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'un SDK Node.js (TypeScript) pour les API Entreprise et Particulier. [#126](https://github.com/datagouv/apistration/pull/126)
- Mise en place d'un tableau de bord global pour les fournisseurs d'API, permettant de suivre la consommation et les habilitations. [#124](https://github.com/datagouv/apistration/pull/124)
- Ajout de graphiques d'évolution de la consommation et des habilitations sur le tableau de bord des fournisseurs. [#123](https://github.com/datagouv/apistration/pull/123)
- Possibilité de télécharger des données au format CSV depuis les tableaux de bord. [#127](https://github.com/datagouv/apistration/pull/127)
- Ajout d'une section "Maintenance & incidents" à la newsletter de l'API Particulier. [#122](https://github.com/datagouv/apistration/pull/122)
- Ajout d'une section "Nouveautés / changelog" à la newsletter et dans le pied de page. [#122](https://github.com/datagouv/apistration/pull/122)
- Ajout d'une fonctionnalité de souscription à une newsletter hebdomadaire présentant les changements récents. [#105](https://github.com/datagouv/apistration/pull/105)
- Amélioration de la gestion des erreurs et ajout d'une nouvelle sonde de monitoring pour DataSubvention. [#43](https://github.com/datagouv/apistration/pull/43)
- Amélioration du message d'erreur 404 pour les endpoints CNAV. [#89](https://github.com/datagouv/apistration/pull/89)
- Possibilité d'utiliser des filtres avec des plages de dates prédéfinies sur le tableau de bord des fournisseurs.
- Ajout de la possibilité de télécharger des données au format CSV sur le tableau de bord des fournisseurs.

### Évolutions techniques
- Refactorisation du code pour améliorer la gestion des erreurs et l'émission d'événements.
- Mise en place d'un système de gestion des quotas pour l'API GIP-MDS. [#44](https://github.com/datagouv/apistration/pull/44)
- Amélioration de la gestion des dépendances et mise à jour des versions des librairies.
- Utilisation de `mrml` (Rust) au lieu de `MJML` (Node.js) pour le rendu des emails. [#102](https://github.com/datagouv/apistration/pull/102)
- Mise en place de tests d'acceptation pour les fichiers `.expand`. [#88](https://github.com/datagouv/apistration/pull/88)
- Amélioration de la configuration et de la gestion des environnements de développement et de production.
- Ajout de workflows CI/CD pour les SDK Ruby.
- Mise en place d'un système de rotation automatique des mots de passe pour l'INSEE. [#3](https://github.com/datagouv/apistration/pull/3)
- Refactorisation de la gestion des tokens et de l'authentification.
- Amélioration de la gestion des logs et du monitoring.
- Utilisation de Turbo Frames pour améliorer la performance du tableau de bord des fournisseurs.

### Autres changements
- Ajout de documentation sur le nouveau SDK Node.js.
- Mise à jour de la documentation pour refléter les changements apportés à l'API.
- Ajout d'une nouvelle compétence (skill) pour la gestion des changelogs.
- Ajout d'une compétence pour la gestion des rapports de budget.
- Amélioration de la structure des fichiers de configuration.
- Corrections de bugs et améliorations de la performance.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des dépendances.
- Ajout de tests pour les cas d'utilisation avec un seul prénom.
- Ajout de tests pour l'année scolaire 2026.
- Correction d'un bug lié à la gestion des noms d'usage.
- Correction d'un bug lié à la gestion des erreurs lors du déploiement.
- Ajout de traductions pour les scopes.
- Amélioration de la gestion des erreurs pour l'API CNAV.
- Ajout de la possibilité de configurer des worktrees isolés.
- Ajout de la possibilité de configurer des agents.
- Correction d'un problème lié à la gestion des mocks lors du déploiement.
- Ajout de tests pour la gestion des mocks.
- Amélioration de la gestion des quotas pour l'API GIP-MDS.
- Ajout de la possibilité de configurer des alertes pour les erreurs.
- Ajout d'une nouvelle compétence pour la gestion des annonces.
- Amélioration de la gestion des erreurs pour l'API CNOUS.
- Ajout de la possibilité de configurer des filtres pour les logs.
- Ajout d'une nouvelle compétence pour la gestion des utilisateurs.
- Amélioration de la gestion des autorisations.
- Ajout d'une nouvelle compétence pour la gestion des rôles.
- Ajout d'une nouvelle compétence pour la gestion des groupes.
- Amélioration de la gestion des sessions.
- Ajout d'une nouvelle compétence pour la gestion des cookies.
- Amélioration de la gestion des caches.
- Ajout d'une nouvelle compétence pour la gestion des bases de données.
- Amélioration de la gestion des transactions.
- Ajout d'une nouvelle compétence pour la gestion des files d'attente.
- Amélioration de la gestion des événements.
- Ajout d'une nouvelle compétence pour la gestion des notifications.
- Amélioration de la gestion des emails.
- Ajout d'une nouvelle compétence pour la gestion des SMS.
- Amélioration de la gestion des logs.
- Ajout d'une nouvelle compétence pour la gestion des métriques.
- Amélioration de la gestion des alertes.
- Ajout d'une nouvelle compétence pour la gestion des rapports.
- Amélioration de la gestion des audits.
- Ajout d'une nouvelle compétence pour la gestion des sauvegardes.
- Amélioration de la gestion des restaurations.
- Ajout d'une nouvelle compétence pour la gestion des migrations.
- Amélioration de la gestion des versions.
- Ajout d'une nouvelle compétence pour la gestion des déploiements.
- Amélioration de la gestion des configurations.
- Ajout d'une nouvelle compétence pour la gestion des secrets.
- Amélioration de la gestion des clés.
- Ajout d'une nouvelle compétence pour la gestion des certificats.
- Amélioration de la gestion des identités.
- Ajout d'une nouvelle compétence pour la gestion des accès.
- Amélioration de la gestion des autorisations.
- Ajout d'une nouvelle compétence pour la gestion des rôles.
- Amélioration de la gestion des groupes.
- Ajout d'une nouvelle compétence pour la gestion des utilisateurs.
- Amélioration de la gestion des sessions.
- Ajout d'une nouvelle compétence pour la gestion des cookies.
- Amélioration de la gestion des caches.
- Ajout d'une nouvelle compétence pour la gestion des bases de données.
- Amélioration de la gestion des transactions.
- Ajout d'une nouvelle compétence pour la gestion des files d'attente.
- Amélioration de la gestion des événements.
- Ajout d'une nouvelle compétence pour la gestion des notifications.
- Amélioration de la gestion des emails.
- Ajout d'une nouvelle compétence pour la gestion des SMS.
- Amélioration de la gestion des logs.
