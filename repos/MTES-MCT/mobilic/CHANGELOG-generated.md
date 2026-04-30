## Changelog : mobilic (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface d'administration de Mobilic, notamment sur la gestion des validations et l'affichage des statuts des missions. L'intégration de Brevo Conversations remplace Crisp pour le support client, offrant une nouvelle expérience de chat en direct. Des corrections et optimisations diverses ont également été apportées pour améliorer la stabilité et la clarté de l'application.

### Évolutions fonctionnelles
- **Administration :** Amélioration de l'affichage et de la gestion des validations des temps de travail, avec des indications claires sur les missions validées et les infractions potentielles. [#830](https://github.com/MTES-MCT/mobilic/pull/830)
- **Administration :** Ajout d'un tag "mission validée" et désactivation des liens vers les missions pour les jours entièrement validés, facilitant l'identification des données traitées. [#829](https://github.com/MTES-MCT/mobilic/pull/829)
- **Support client :** Remplacement de Crisp par Brevo Conversations pour le chat en direct, avec une intégration spécifique pour les contrôleurs et une meilleure gestion de l'affichage. [#832](https://github.com/MTES-MCT/mobilic/pull/832)
- **Statuts des missions :** Ajout de tags de statut pour les missions dans l'onglet d'activité, améliorant la visibilité et la navigation. [#835](https://github.com/MTES-MCT/mobilic/pull/835)
- **Affichage des infractions :** Clarification de la logique d'affichage des infractions et gestion des cas où plusieurs missions non validées coexistent sur la même journée.
- **Historique d'activité :** Correction pour afficher les entrées de temps de travail même lorsque les missions sont en dehors de la fenêtre des 31 jours. [#839](https://github.com/MTES-MCT/mobilic/pull/839)

### Évolutions techniques
- **Refactoring :** Simplification de la logique de déduplication des employés dans le filtre de validation. [#831](https://github.com/MTES-MCT/mobilic/pull/831)
- **Suppression de dépendances :** Suppression du package `crisp-sdk-web` suite au remplacement de Crisp par Brevo Conversations.
- **Améliorations diverses :** Correction de plusieurs problèmes identifiés par SonarCloud concernant l'accessibilité, la gestion des props et des objets globaux.
- **Typage :** Ajout de validations de props et utilisation de chaînes optionnelles pour améliorer la robustesse du code.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo et les changements de nom de l'organisme.
- **Style :** Alignement des couleurs des lignes de tableau dans l'interface d'administration avec les tokens DSFR.
- **Nettoyage de code :** Suppression de commentaires obsolètes et d'imports inutilisés.
