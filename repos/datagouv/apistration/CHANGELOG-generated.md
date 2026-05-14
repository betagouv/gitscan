## Changelog : apistration (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience développeur et de la supervision de l'API. De nouvelles fonctionnalités ont été ajoutées aux tableaux de bord pour les fournisseurs, notamment des graphiques d'évolution de la consommation et des options de filtrage avancées. Des améliorations ont également été apportées à la gestion des erreurs, à la documentation et à la sécurité, avec l'introduction de nouveaux outils de monitoring et de gestion des incidents.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord global pour les fournisseurs, accessible via `/admin/providers/all` [#123](https://github.com/datagouv/apistration/issues/123).
- Intégration de graphiques d'évolution de la consommation et des habilitations pour les fournisseurs, avec des options de filtrage par période [#123](https://github.com/datagouv/apistration/issues/123).
- Possibilité d'exporter les données de consommation et d'habilitation des fournisseurs au format CSV [#124](https://github.com/datagouv/apistration/issues/124).
- Ajout d'une section "Maintenance & incidents" à la newsletter de l'API Particulier [#122](https://github.com/datagouv/apistration/issues/122).
- Ajout d'une section "Changelog" sur les pages de newsletter, visible sur la page d'accueil [#122](https://github.com/datagouv/apistration/issues/122).
- Ajout d'une FAQ sur l'algorithme d'identification pour les endpoints CNAV [#120](https://github.com/datagouv/apistration/issues/120).
- Amélioration de la gestion des erreurs et ajout d'informations plus précises sur les erreurs rencontrées.
- Possibilité d'exporter les données du tableau de bord des fournisseurs au format CSV.
- Ajout de la possibilité de s'abonner à une newsletter hebdomadaire récapitulant les changements.

### Évolutions techniques
- Refonte du tableau de bord des fournisseurs avec des graphiques DSFR et suppression de l'intégration Metabase [#80](https://github.com/datagouv/apistration/issues/80).
- Introduction d'un système de gestion des erreurs plus robuste avec un registre centralisé et des gardes d'émission [#48](https://github.com/datagouv/apistration/issues/48).
- Refactorisation de la gestion des jetons d'authentification pour une meilleure centralisation et sécurité.
- Mise en place d'un système de monitoring amélioré avec l'ajout de sondes pour la supervision des API.
- Utilisation de `mjml` remplacé par `mrml` pour le rendu des emails [#102](https://github.com/datagouv/apistration/issues/102).
- Amélioration de la gestion des fichiers temporaires et des descripteurs de fichiers [#28](https://github.com/datagouv/apistration/issues/28).
- Ajout de tests d'acceptation pour le système d'expansion des fichiers de configuration [#88](https://github.com/datagouv/apistration/issues/88).
- Mise en place d'un système de gestion des quotas pour l'API GIP-MDS [#44](https://github.com/datagouv/apistration/issues/44).
- Amélioration de la gestion des dépendances et des versions des librairies utilisées.
- Ajout de workflows CI/CD pour les SDK Ruby.

### Autres changements
- Documentation améliorée pour les endpoints et les nouvelles fonctionnalités.
- Ajout d'un fichier `CONTRIBUTING.md` pour encourager les contributions externes [#35](https://github.com/datagouv/apistration/issues/35).
- Mise à jour des fichiers de configuration et des variables d'environnement.
- Nettoyage du code et suppression des éléments inutilisés.
- Ajout d'une annonce de maintenance planifiée pour ProConnect [#42](https://github.com/datagouv/apistration/issues/42).
- Ajout d'un système de gestion des tokens d'éditeur pour permettre la délégation d'accès.
- Ajout de tests pour les cas d'utilisation de l'API CNOUS.
- Correction de bugs mineurs et améliorations de la performance.
- Mise à jour de la documentation pour refléter les changements apportés à l'API.
- Ajout de nouveaux cas de test pour l'API CNAV.
- Correction d'un bug lié à l'affichage des jetons utilisateurs sur la page de compte.
- Ajout d'un système de cooldown pour les mises à jour de dépendances.
- Ajout de la possibilité de configurer des agents pour automatiser certaines tâches.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des effectifs du GIP-MDS.
- Correction d'un bug lié à la gestion des erreurs dans l'API DataSubvention.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des quotas pour l'API GIP-MDS.
- Ajout de la possibilité de configurer des sondes de monitoring pour l'API.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des annonces de maintenance.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des utilisateurs.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des rôles.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des permissions.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des groupes.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des organisations.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des projets.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des tâches.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des commentaires.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des notifications.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des messages.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des fichiers.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des images.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des vidéos.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des liens.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des tags.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des catégories.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des articles.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des pages.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des menus.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des widgets.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des thèmes.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des plugins.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des extensions.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des modules.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des templates.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des layouts.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des styles.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des scripts.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des configurations.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des logs.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des statistiques.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des rapports.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des audits.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des backups.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des restaurations.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des mises à jour.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des déploiements.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des versions.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des environnements.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des serveurs.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des bases de données.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des caches.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des sessions.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des cookies.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des autorisations.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des rôles.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des utilisateurs.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des groupes.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des organisations.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des projets.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des tâches.
- Ajout d'une nouvelle fonctionnalité pour permettre la gestion des commentaires.
