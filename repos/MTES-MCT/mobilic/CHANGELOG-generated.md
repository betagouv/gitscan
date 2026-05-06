## Changelog : mobilic (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les évolutions de Mobilic se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface d'administration, notamment avec l'ajout de tags d'état pour les missions et une meilleure gestion de l'affichage des validations. L'intégration de Brevo en remplacement de Crisp pour le support client est également une avancée majeure. Des corrections de bugs et des optimisations techniques ont été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Administration :** Ajout de tags d'état pour les missions dans l'onglet "Activités", facilitant l'identification de leur statut ([#835](https://github.com/MTES-MCT/mobilic/pull/835), [#829](https://github.com/MTES-MCT/mobilic/pull/829)).
- **Administration :** Amélioration de l'affichage des missions et des validations, notamment pour les missions antérieures à 31 jours ([#840](https://github.com/MTES-MCT/mobilic/pull/840), [#839](https://github.com/MTES-MCT/mobilic/pull/839)).
- **Authentification :** Implémentation de l'authentification à deux facteurs (2FA) via TOTP ([#833](https://github.com/MTES-MCT/mobilic/pull/833)).
- **Support Client :** Remplacement de Crisp par Brevo Conversations pour le support client, avec une intégration spécifique pour le contrôleur et les autres utilisateurs ([#832](https://github.com/MTES-MCT/mobilic/pull/832)).
- **Recherche :** Ajout de la recherche d'infractions NATINF dans le contrôle ([#842](https://github.com/MTES-MCT/mobilic/pull/842)).
- **Administration :** Possibilité pour un administrateur de se faire passer pour un autre utilisateur ([#826](https://github.com/MTES-MCT/mobilic/pull/826)).

### Évolutions techniques
- **Refactoring :** Refactorisation du code dans l'onglet "Activités" pour améliorer la lisibilité et la maintenabilité.
- **Optimisation :** Optimisation de la gestion des états et du rendu des composants dans l'interface d'administration.
- **Sécurité :** Correction de vulnérabilités potentielles et amélioration de la sécurité de l'authentification.
- **Dépendances :** Suppression de la dépendance à Crisp SDK et mise à jour des dépendances liées à Brevo.
- **DSFR :** Remplacement de composants Material par des composants Design System Français (DSFR) pour une meilleure cohérence visuelle.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo.
- **Corrections :** Correction de divers bugs et améliorations de l'interface utilisateur, notamment des problèmes d'affichage et de comportement des composants.
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **Sonarqube :** Correction des issues soulevées par Sonarqube.
