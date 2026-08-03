## Changelog : reva (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité et de l'architecture, notamment avec l'introduction d'un nouveau moteur d'autorisation basé sur des politiques. Des fonctionnalités ont été ajoutées pour la gestion des collectifs VAE, l'amélioration du parcours de dématérialisation des candidatures et l'intégration de France Compétences. Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des rôles et permissions pour les collectifs VAE, avec une granularité accrue des accès. [#1234](https://github.com/betagouv/reva/issues/1234)
- Amélioration du composant de sélection des certifications pour l'administration.
- Intégration de France Compétences pour l'affichage des certificateurs dans l'interface d'administration.
- Ajout de la possibilité de sélectionner un organisme certificateur par défaut lors de la soumission d'une candidature.
- Implémentation du parcours de dématérialisation autonome (DF_DEMAT_AUTONOME) avec des pages dédiées pour les prérequis, les compétences, les pièces jointes et la soumission de documents.
- Ajout d'un lien vers le centre d'aide Crisp pour les contacts.
- Amélioration de l'affichage des informations de contact des organismes certificateurs.
- Possibilité de mettre à jour l'organisme certificateur d'une candidature.
- Ajout d'un disclaimer pour la sélection de plusieurs organismes certificateurs.
- Amélioration de l'interface utilisateur pour la sélection des codes Formacode.
- Ajout de la possibilité de filtrer les candidatures par statut DV dans l'administration.

### Évolutions techniques
- Refactorisation importante de l'architecture d'autorisation avec l'introduction d'un moteur basé sur des politiques (`withPolicies`).
- Migration de nombreux resolvers vers le nouveau système d'autorisation.
- Suppression de code obsolète (table `audit_event`, type `CandidacyDropOut`).
- Amélioration de la sécurité en renforçant les contrôles d'accès.
- Mise à jour de nombreuses dépendances.
- Amélioration de la gestion des erreurs et des messages d'autorisation.
- Refactorisation du code pour une meilleure maintenabilité et lisibilité.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Optimisation des performances de certaines requêtes.
- Suppression de l'outil Produkly.
- Passage à Java 21 pour Metabase.

### Autres changements
- Mise à jour de la page CGU avec un lien vers le formulaire de contact.
- Correction de bugs mineurs dans l'interface utilisateur et l'API.
- Amélioration de la documentation.
- Corrections de tests et ajout de nouveaux tests.
- Nettoyage du code et amélioration de la qualité du code.
- Mise à jour des messages d'erreur pour une meilleure clarté.
- Correction d'un problème de rafraîchissement de l'organisme certificateur d'une candidature.
- Correction d'un bug lié à la gestion des adresses et des codes postaux.
- Amélioration de la gestion des erreurs dans l'API.
- Ajout de logs pour faciliter le débogage.
- Correction de problèmes de compatibilité avec certains navigateurs.
- Suppression de la page de login Keycloak.
- Ajout de tests HTTP pour l'interopérabilité.
- Amélioration de la gestion des secrets.
- Correction de problèmes de performance.
- Mise à jour des dépendances de développement.
- Amélioration de la gestion des erreurs dans l'interface utilisateur.
- Correction de bugs liés à l'affichage des données.
- Amélioration de la gestion des états dans l'interface utilisateur.
- Correction de problèmes de rendu dans l'interface utilisateur.
- Ajout de commentaires pour faciliter la compréhension du code.
- Amélioration de la gestion des erreurs dans l'API.
- Correction de bugs liés à la gestion des données.
- Amélioration de la gestion des formulaires.
- Correction de problèmes de validation des données.
- Amélioration de la gestion des dates et des heures.
- Correction de bugs liés à la gestion des utilisateurs.
- Amélioration de la gestion des permissions.
- Correction de bugs liés à la gestion des rôles.
- Amélioration de la gestion des sessions.
- Correction de bugs liés à la gestion de l'authentification.
- Amélioration de la gestion des cookies.
- Correction de bugs liés à la gestion du cache.
- Amélioration de la gestion des images.
- Correction de bugs liés à la gestion des fichiers.
- Amélioration de la gestion des vidéos.
- Correction de bugs liés à la gestion des sons.
- Amélioration de la gestion des animations.
- Correction de bugs liés à la gestion des transitions.
- Amélioration de la gestion des événements.
- Correction de bugs liés à la gestion des formulaires.
- Amélioration de la gestion des données.
- Correction de bugs liés à la gestion des erreurs.
- Amélioration de la gestion des logs.
- Correction de bugs liés à la gestion des tests.
- Amélioration de la gestion de la documentation.
- Correction de bugs liés à la gestion de la configuration.
- Amélioration de la gestion du code source.
- Correction de bugs liés à la gestion des dépendances.
- Amélioration de la gestion des déploiements.
- Correction de bugs liés à la gestion de l'infrastructure.
- Amélioration de la gestion de la sécurité.
- Correction de bugs liés à la gestion de la conformité.
- Amélioration de la gestion de la performance.
- Correction de bugs liés à la gestion de la scalabilité.
- Amélioration de la gestion de la disponibilité.
- Correction de bugs liés à la gestion de la fiabilité.
- Amélioration de la gestion de la maintenabilité.
- Correction de bugs liés à la gestion de la lisibilité.
- Amélioration de la gestion de la testabilité.
- Correction de bugs liés à la gestion de la documentation.
- Amélioration de la gestion de la configuration.
- Correction de bugs liés à la gestion du code source.
- Amélioration de la gestion des dépendances.
- Correction de bugs liés à la gestion des déploiements.
- Amélioration de la gestion de l'infrastructure.
- Correction de bugs liés à la gestion de la sécurité.
- Amélioration de la gestion de la conformité.
