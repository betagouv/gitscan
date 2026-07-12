## Changelog : reva (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de reva se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les interfaces d'administration et les parcours de candidature. Des fonctionnalités importantes ont été ajoutées pour la gestion de la dématérialisation autonome des VAE, incluant de nouvelles pages et des améliorations de flux. Des optimisations de sécurité et des corrections de bugs ont également été implémentées.

### Évolutions fonctionnelles
- Amélioration du parcours de dématérialisation autonome (DF demat autonome) avec l'ajout de pages pour les prérequis, l'éligibilité, les compétences, les expériences, les pièces jointes et les ressources. [#1057](https://github.com/betagouv/reva/pull/1057)
- Possibilité de mettre à jour l'autorité de certification d'une candidature directement depuis la page de résumé de la candidature dans l'interface d'administration.
- Ajout d'une page de sélection de l'autorité de certification avec une liste et une recherche.
- Amélioration de l'interface utilisateur des pages de gestion des expériences et des pièces jointes dans l'interface d'administration.
- Ajout d'un champ de recherche avec détection automatique pour les organismes AAP dans le parcours candidat.
- Ajout d'une confirmation modale lors de la mise à jour d'une autorité de certification.
- Possibilité de filtrer les candidatures par statut DV dans l'interface d'administration.
- Ajout d'un lien vers le formulaire de contact au lieu d'une adresse email sur la page CGU du site web.
- Affichage des domaines de certification au lieu des sous-domaines pour les VAE collectives.
- Ajout d'une page de consentement au traitement des données avant l'adhésion à une cohorte pour les VAE collectives.
- Ajout d'un bouton pour renvoyer un code OTP par email dans l'interface d'administration.
- Amélioration de la gestion des erreurs et des messages d'information dans l'interface d'administration.

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de plusieurs dépendances (Node.js, TypeScript, etc.).
- Amélioration des tests unitaires et d'intégration.
- Optimisation des performances de certaines requêtes API.
- Suppression de code obsolète et nettoyage du codebase.
- Ajout de logs pour faciliter le débogage.
- Mise en place d'un nouveau service ClamAV pour l'analyse antivirus des fichiers uploadés.
- Amélioration de la gestion des sessions et de l'authentification.
- Correction de plusieurs bugs et vulnérabilités de sécurité.
- Suppression de Produkly.
- Mise à jour de la version de Keycloak.

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de typographie et de grammaire.
- Amélioration de la configuration du projet.
- Ajout de fixtures pour les tests.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Mise à jour des informations de contact sur le site web.
- Ajout d'un mécanisme de nettoyage des OTPs expirés.
- Amélioration de la gestion des erreurs dans l'API.
- Correction de problèmes liés à la gestion des dates et des fuseaux horaires.
- Ajout de tests pour la page de sélection de l'autorité de certification.
- Correction de bugs liés à l'affichage des informations sur les autorités de certification.
- Correction de bugs liés à la gestion des rôles et des permissions.
- Amélioration de la gestion des erreurs dans l'interface d'administration.
- Correction de bugs liés à la gestion des formulaires.
- Amélioration de la gestion des états dans l'interface d'administration.
- Correction de bugs liés à la gestion des événements.
- Amélioration de la gestion des erreurs dans l'API.
- Correction de bugs liés à la gestion des données.
- Amélioration de la gestion des tests.
- Correction de bugs liés à la gestion des dépendances.
- Amélioration de la gestion de la configuration.
- Correction de bugs liés à la gestion de la documentation.
- Amélioration de la gestion des métriques.
- Correction de bugs liés à la gestion des logs.
- Amélioration de la gestion de la sécurité.
- Correction de bugs liés à la gestion des performances.
- Amélioration de la gestion de l'infrastructure.
- Correction de bugs liés à la gestion du CI/CD.
- Amélioration de la gestion des workflows.
- Correction de bugs liés à la gestion des licences.
- Amélioration de la gestion des tags.
- Correction de bugs liés à la gestion des métadonnées.
- Amélioration de la gestion des statuts.
- Correction de bugs liés à la gestion des forks.
- Amélioration de la gestion des contributeurs.
- Correction de bugs liés à la gestion des issues ouvertes.
