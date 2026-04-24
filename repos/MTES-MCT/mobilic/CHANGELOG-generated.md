## Changelog : mobilic (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration, notamment la gestion des statuts des missions et l'affichage des validations. L'intégration de Brevo Conversations remplace Crisp pour le support client via chat en direct. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Administration des missions :** Ajout d'un tag "Validé" pour les missions validées, désactivation des liens vers les missions pour les jours déjà validés, et amélioration de l'affichage des statuts des missions. [#835](https://github.com/MTES-MCT/mobilic/issues/835)
- **Chat en direct :** Remplacement de Crisp par Brevo Conversations pour le support client, avec une intégration spécifique pour l'environnement de contrôle. [#832](https://github.com/MTES-MCT/mobilic/issues/832)
- **Amélioration de l'affichage des validations :** Clarification de la logique d'affichage des validations en attente et gestion des cas où plusieurs missions d'un même jour sont en attente de validation.
- **Agent Connect :** Correction de l'URL de redirection après une mise à jour de Flask. [#824](https://github.com/MTES-MCT/mobilic/issues/824)

### Évolutions techniques
- **Refactoring des validations :** Déduplication du code de filtrage des validations pour améliorer la maintenabilité. [#833](https://github.com/MTES-MCT/mobilic/issues/833), [#831](https://github.com/MTES-MCT/mobilic/issues/831)
- **Suppression de Crisp :** Suppression du SDK Crisp et des références associées dans le code et la documentation.
- **Optimisations diverses :** Correction de plusieurs issues SonarCloud concernant l'accessibilité, la gestion des props et des objets globaux.
- **Amélioration du code admin :** Nettoyage et correction de bugs dans les composants de l'interface d'administration, notamment la table des temps de travail et les tags de statut des missions.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo et le changement de nom du ministère.
- **Suppression de code obsolète :** Suppression d'imports inutilisés et de commentaires obsolètes.
- **Styling :** Alignement des couleurs de la table augmentée avec les tokens DSFR.
