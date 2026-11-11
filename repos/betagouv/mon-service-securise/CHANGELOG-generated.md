## Changelog : mon-service-securise (30 derniers jours, au 10 novembre 2026)

### Résumé
Ce mois-ci, le service a franchi des étapes majeures avec l'introduction de la génération automatique de présentations PowerPoint pour les commissions et une refonte de la gestion des risques. L'organisation des services est simplifiée grâce à la gestion par groupes d'entités, tandis que l'administration bénéficie de nouveaux outils de reporting et d'une synchronisation automatisée des données clés avec le CRM.

### Évolutions fonctionnelles
- **Génération de supports de commission (PPTX) :** Création automatique de présentations PowerPoint incluant le sommaire, la composition de la commission, la liste des pièces du dossier et les avis écrits.
- **Gestion des risques et conformité :** 
    - Déploiement d'une nouvelle interface de gestion des risques (V2).
    - Intégration détaillée des vecteurs et objectifs visés de l'ANSSI dans le suivi des risques.
    - Possibilité de créer des risques spécifiques basés sur le référentiel.
- **Organisation et administration :**
    - Mise en place de la gestion par groupes d'entités pour mieux structurer les services.
    - Introduction du rôle de "superviseur" avec des droits et des vues spécifiques.
    - Nouveau système de reporting mensuel pour les administrateurs et superviseurs.
- **Expérience utilisateur (UI/UX) :**
    - Amélioration du système de notifications (toasts) et des modales.
    - Mise à jour du tiroir de téléchargement et de l'affichage des actions sur les pages de service.
    - Ajout de notifications de nouveautés pour les fonctionnalités clés (API publique, groupes de services).

### Évolutions techniques
- **Intégration CRM et automatisation :** 
    - Synchronisation automatique des indicateurs clés (nombre d'utilisateurs, de services et d'homologations) vers le CRM (Twenty).
    - Mise en place de tâches planifiées (CRON) pour le reporting et la maintenance des données.
- **Architecture et refactoring :**
    - Refonte des adaptateurs (PowerPoint, CRM) et des clients HTTP pour une meilleure modularité.
    - Optimisation de la gestion des erreurs et du monitoring via Sentry.
    - Amélioration de la gestion des permissions et des abonnés (event bus).
- **Infrastructure et environnement :**
    - Mise à jour des environnements vers Node.js 26 LTS et PostgreSQL 18.
    - Passage à la version 12 de pnpm.

### Autres changements
- **Tests :** Ajout de tests d'intégration pour la visite guidée et l'affichage des risques.
- **Nettoyage :** Refactorisation de composants UI (accordéons, tableaux d'entités) et suppression de code obsolète.
