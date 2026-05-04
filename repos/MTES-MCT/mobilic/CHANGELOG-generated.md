## Changelog : mobilic (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration, notamment la gestion des validations et l'affichage des informations relatives aux missions et aux temps de travail. L'intégration de Brevo Conversations remplace Crisp pour le support client via chat en direct. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Administration :** Amélioration de l'affichage et de la logique des états de validation des missions et des temps de travail, avec des indications plus claires sur les validations en attente. [#830](https://github.com/MTES-MCT/mobilic/pull/830)
- **Administration :** Correction de l'affichage des entrées de temps de travail pour les missions dont la date est en dehors de la période de 31 jours. [#839](https://github.com/MTES-MCT/mobilic/pull/839)
- **Administration :** Ajout d'étiquettes d'état pour les missions dans l'onglet d'activité, facilitant leur identification et leur gestion. [#835](https://github.com/MTES-MCT/mobilic/pull/835) et [#829](https://github.com/MTES-MCT/mobilic/pull/829)
- **Support Client :** Remplacement de Crisp par Brevo Conversations pour le chat en direct, avec une intégration améliorée et une meilleure gestion de l'affichage sur différentes pages. [#832](https://github.com/MTES-MCT/mobilic/pull/832)
- **Administration :** Correction d'un problème d'ouverture du tiroir de détails de mission lors du clic sur une étiquette d'état. [#834](https://github.com/MTES-MCT/mobilic/pull/834)

### Évolutions techniques
- **Refactoring :** Simplification de la logique de déduplication des employés dans le filtre de validation. [#831](https://github.com/MTES-MCT/mobilic/pull/831) et [#833](https://github.com/MTES-MCT/mobilic/pull/833)
- **Dépendances :** Suppression de la dépendance à `crisp-sdk-web` suite au remplacement de Crisp par Brevo Conversations.
- **Accessibilité :** Correction de problèmes d'accessibilité détectés par SonarCloud dans le widget de chat en direct Brevo.
- **Conformité DSFR :** Utilisation des tokens DSFR pour l'alignement des couleurs dans les tableaux de l'administration.
- **Amélioration du code :** Ajout de validations de props et de chaînage optionnel pour améliorer la robustesse du code.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo et modifier les informations sur le ministère.
- **Nettoyage du code :** Suppression de code inutilisé et de commentaires obsolètes.
- **Corrections de style :** Amélioration de la lisibilité du code avec l'ajout de points-virgules manquants et la correction d'imports inutiles.
