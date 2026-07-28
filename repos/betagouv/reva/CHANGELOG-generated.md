## Changelog : reva (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur l'expérience utilisateur, notamment dans le cadre de la dématérialisation de la VAE (DF demat autonome). De nouvelles fonctionnalités ont été ajoutées pour gérer les candidatures, les pièces jointes, les compétences et les certifications. Des corrections et des optimisations ont également été apportées à l'API et à l'administration. Enfin, des améliorations de sécurité et de maintenance ont été effectuées.

### Évolutions fonctionnelles
- Ajout de composants pour la sélection de formacodes v2 dans l'administration [#1082](https://github.com/betagouv/reva/issues/1082).
- Amélioration de l'interface utilisateur et de l'expérience utilisateur pour la page de soumission de pièces justificatives pour la DF demat autonome.
- Ajout de la possibilité de mettre à jour l'autorité de certification d'une candidature depuis la page de détails de l'autorité de certification.
- Ajout d'une page pour la sélection de plusieurs autorités de certification.
- Ajout d'une étape pour l'acceptation des conditions générales d'utilisation pour les candidatures collectives.
- Amélioration de l'affichage des informations sur les organismes financeurs.
- Ajout d'un lien vers le centre d'aide Crisp sur différentes pages (contact, Keycloak, etc.).
- Ajout d'une fonctionnalité permettant de supprimer les comptes d'administration "maison mère".
- Amélioration de la gestion des erreurs et des messages d'alerte.
- Ajout d'une fonctionnalité permettant de rafraîchir les informations de l'autorité de certification des candidatures.

### Évolutions techniques
- Refactorisation de l'architecture de l'interopérabilité avec des tests unitaires et HTTP.
- Mise à jour de plusieurs dépendances (axios, js-yaml, postcss, etc.).
- Amélioration de la sécurité avec l'ajout de contrôles d'accès et de validation.
- Optimisation des performances de l'API.
- Mise en place d'un système d'autorisation basé sur des politiques.
- Suppression de code obsolète et simplification de la base de code.
- Amélioration de la gestion des erreurs et de la journalisation.
- Correction de plusieurs bugs et vulnérabilités de sécurité.
- Mise à jour de la version de Keycloak.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la couverture de test.
- Correction de problèmes de compatibilité avec différents navigateurs.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la configuration du projet.
- Nettoyage du code et suppression de code mort.
- Correction de problèmes de linting.
- Mise à jour des fichiers de configuration de CI/CD.
- Correction de problèmes de typage.
- Amélioration de la gestion des secrets.
- Mise à jour des dépendances de développement.
