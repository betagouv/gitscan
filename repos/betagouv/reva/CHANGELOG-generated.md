## Changelog : reva (30 derniers jours, au 17 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'intégration FranceConnect, avec notamment la gestion des cas où les informations de l'utilisateur ne correspondent pas, et la possibilité de révoquer une décision de validation. Des efforts ont également été déployés pour améliorer la gestion des blocs de compétences et des résultats de jury dans l'interface d'administration, ainsi que pour la maintenance et la sécurisation du code (suppression de feature flags obsolètes, mises à jour de dépendances).

### Évolutions fonctionnelles
- **FranceConnect :** Amélioration de l'intégration FranceConnect avec gestion des erreurs et des cas de non-correspondance des données. Possibilité pour les utilisateurs de délier leur compte FranceConnect.
- **Gestion des décisions de jury :** Les administrateurs peuvent désormais révoquer une décision de validation (COMPLETE/INCOMPLETE) sur les dossiers de faisabilité.
- **Gestion des blocs de compétences :** Amélioration de l'affichage et de la gestion des blocs de compétences dans l'interface d'administration, notamment lors de la validation des résultats de jury.
- **Interface d'administration :** Ajout d'une page pour la gestion des compléments d'expérience.
- **Informations candidat :** Possibilité pour les administrateurs de modifier le nom et prénom des comptes d'autorité de certification.
- **Notifications :** Envoi d'un email à la nouvelle AAP lors de la mise à jour d'une candidature par un administrateur.
- **VAE Collective :** Amélioration de l'affichage des informations sur la page d'accueil.
- **Formulaire d'inscription :** Amélioration de l'UX et de la clarté des formulaires d'informations civiles et de typologie/convention collective.

### Évolutions techniques
- **Refactoring :** Suppression de nombreux *feature flags* obsolètes pour simplifier le code.
- **Tests :** Migration de nombreux tests Cypress vers Playwright pour améliorer la stabilité et la performance. Ajout de tests unitaires et d'intégration.
- **Sécurité :** Mise à jour de nombreuses dépendances pour corriger des vulnérabilités de sécurité.
- **Architecture :** Rework de la gestion des index dans la base de données pour optimiser les requêtes.
- **Keycloak :** Ajout d'un thème et d'une configuration spécifique pour la page de connexion.
- **API :** Amélioration de la gestion des erreurs et des logs.
- **Strapi :** Mise à jour et sécurisation de l'infrastructure Strapi.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la gestion des variables d'environnement.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression de code mort.
- Amélioration des messages d'erreur.
- Modification de certains libellés dans l'interface d'administration.
