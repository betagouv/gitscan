## Changelog : mobilic (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration, notamment pour la gestion des validations et l'affichage des statuts des missions. L'intégration de Brevo Conversations remplace Crisp pour le support client, et des corrections ont été apportées pour améliorer la stabilité et la conformité du code.

### Évolutions fonctionnelles
- **Administration :** Amélioration de l'affichage des statuts des missions et ajout d'un tag "mission validée" pour une identification rapide. Possibilité d'ouvrir directement la vue d'une mission en cliquant sur son tag de statut (#[835](https://github.com/MTES-MCT/mobilic/issues/835)).
- **Administration :** Clarification de la logique d'affichage des infractions et des jours validés dans le tableau de temps de travail.
- **Support client :** Remplacement de Crisp par Brevo Conversations pour la gestion du support client et l'ajout d'un widget de chat en direct (#[832](https://github.com/MTES-MCT/mobilic/issues/832)). Le widget s'adapte désormais en fonction du contexte (page contrôleur vs autres pages).
- **Validations :** Correction d'un bug empêchant l'affichage correct des missions en attente de validation pour une même journée.
- **Validations :** Déduplication des employés dans le filtre de validation pour une meilleure expérience utilisateur (#[831](https://github.com/MTES-MCT/mobilic/issues/831)).

### Évolutions techniques
- **Refactoring :** Amélioration de la logique de déduplication des validations et simplification du code.
- **Corrections :** Résolution de plusieurs issues identifiées par SonarCloud concernant l'accessibilité, la gestion des props et l'utilisation d'objets globaux.
- **Suppression :** Suppression du package `crisp-sdk-web` et des références associées.
- **Mise à jour :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo.

### Autres changements
- **Documentation :** Mise à jour de la documentation de la politique de confidentialité.
- **Style :** Alignement des couleurs des lignes du tableau augmenté dans l'administration avec les tokens DSFR.
- **Nettoyage :** Suppression d'imports inutilisés et de commentaires obsolètes.
- **Correction :** Correction d'un problème lié au remount des détails de mission dans l'administration.
