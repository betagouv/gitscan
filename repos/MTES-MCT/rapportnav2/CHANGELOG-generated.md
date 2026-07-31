## Changelog : rapportnav2 (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant l'intégration de SATI, notamment au niveau de l'interface utilisateur et du traitement des données. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions sur l'administration des missions et des infractions.

### Évolutions fonctionnelles
- **SATI :** Intégration et amélioration de l'interface utilisateur pour SATI, avec de nouveaux composants et la gestion des perspectives d'inspecteur.
- **Formulaire M1 :** Amélioration du formulaire M1 via la PR [#1444](https://github.com/MTES-MCT/rapportnav2/pulls/1444).
- **Administration :** Ajout de fonctionnalités de recherche par ID et ID interne dans l'interface d'administration.
- **Missions :** Intégration des missions dans l'interface d'administration.
- **Données pays :** Mise à jour de la source des données pays via une API.
- **Gestion des infractions :** Amélioration de la suppression des infractions sur l'interface Fish Controls.
- **Gestion des actions :** Ajout d'actions à l'interface d'administration.

### Évolutions techniques
- **React Router :** Mise à jour vers la version 8 de la librairie React Router.
- **Spring Boot :** Mise à jour vers la version 4.1.0 de Spring Boot.
- **Refactoring :** Nettoyage et refactoring du code backend, notamment la suppression de données obsolètes et la correction de l'intégrité des données.
- **Performance :** Amélioration des performances en évitant la récupération répétée des dates de mission.
- **Tests :** Utilisation de mocks dans les tests.
- **Dépendances :** Mise à jour de certaines dépendances frontend.

### Autres changements
- Configuration des services SATI activés.
- Correction de bugs mineurs et améliorations diverses.
- Mise à jour de la documentation.
- Correction de la gestion des valeurs nulles pour le principal inspector et les types d'infraction.
- Correction d'un problème de suppression des cibles.
- Correction d'un problème de pagination dans l'administration.
