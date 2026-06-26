## Changelog : rdv-service-public (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la migration vers un nouveau nom de domaine (rdv.numerique.gouv.fr), l'amélioration de la synchronisation CalDAV, et des corrections de bugs pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées, notamment pour la gestion des motifs et des services, ainsi que pour la robustesse de l'application.

### Évolutions fonctionnelles
- **Nouveau nom de domaine:** Le service a été adapté pour fonctionner avec le nouveau nom de domaine rdv.numerique.gouv.fr. Cela inclut des mises à jour de la documentation, des redirections et des ajustements de l'interface utilisateur. [#6484](https://github.com/betagouv/rdv-service-public/issues/6484), [#6481](https://github.com/betagouv/rdv-service-public/issues/6481), [#6480](https://github.com/betagouv/rdv-service-public/issues/6480), [#6479](https://github.com/betagouv/rdv-service-public/issues/6479)
- **Synchronisation CalDAV:** Amélioration de la synchronisation CalDAV avec Zimbra et correction de bugs liés à l'activation des données personnelles. [#6416](https://github.com/betagouv/rdv-service-public/issues/6416), [#6417](https://github.com/betagouv/rdv-service-public/issues/6417)
- **Gestion des motifs:** Possibilité pour les administrateurs d'espace de créer un nouveau service. Création massive des motifs France Service en un clic dans la super-admin. [#6455](https://github.com/betagouv/rdv-service-public/issues/6455), [#6406](https://github.com/betagouv/rdv-service-public/issues/6406)
- **Interface utilisateur:**
    - Amélioration de l'interface de recherche de créneaux pour les agents avec l'utilisation de cartes DSFR. [#6437](https://github.com/betagouv/rdv-service-public/issues/6437)
    - Utilisation de composants DSFR (badges, boutons, accordéon) pour une meilleure cohérence visuelle. [#6467](https://github.com/betagouv/rdv-service-public/issues/6467), [#6468](https://github.com/betagouv/rdv-service-public/issues/6468), [#6434](https://github.com/betagouv/rdv-service-public/issues/6434)
    - Affichage du nom de l'usager connecté. [#6452](https://github.com/betagouv/rdv-service-public/issues/6452)
- **Prescription externe:** Correction d'un bug sur la bannière de prescription externe. [#6398](https://github.com/betagouv/rdv-service-public/issues/6398)
- **Numéros de téléphone:** Permet désormais les numéros de téléphone des DROM pour les organisations. [#6400](https://github.com/betagouv/rdv-service-public/issues/6400)
- **FranceConnect:** Permet d'utiliser des FS FranceConnect différents par domaine. [#6401](https://github.com/betagouv/rdv-service-public/issues/6401)

### Évolutions techniques
- **Refactoring CSS:** Réduction de la dépendance à Bootstrap pour une meilleure maintenabilité. [#6457](https://github.com/betagouv/rdv-service-public/issues/6457)
- **Mise à jour de Puma:** Mise à jour de la version de Puma à 7.2.1. [#6425](https://github.com/betagouv/rdv-service-public/issues/6425)
- **GoodJob:** Correction d'un problème lié à la gestion des jobs GoodJob. [#6408](https://github.com/betagouv/rdv-service-public/issues/6408)
- **ActionCable:** Correction de tests flaky liés à ActionCable. [#6426](https://github.com/betagouv/rdv-service-public/issues/6426)
- **Suppression de code obsolète:** Suppression de formulaires et de code inutilisé. [#6465](https://github.com/betagouv/rdv-service-public/issues/6465)
- **Amélioration des tests:** Amélioration des tests unitaires et d'intégration. [#6453](https://github.com/betagouv/rdv-service-public/issues/6453), [#6445](https://github.com/betagouv/rdv-service-public/issues/6445), [#6411](https://github.com/betagouv/rdv-service-public/issues/6411)

### Autres changements
- **Documentation:** Mise à jour de la documentation pour refléter les changements récents. [#6476](https://github.com/betagouv/rdv-service-public/issues/6476)
- **Configuration:** Ajout d'une variable d'environnement pour afficher les login codes sur les review apps. [#6454](https://github.com/betagouv/rdv-service-public/issues/6454)
- **Sécurité:** Fixer par hash les versions des GitHub Actions pour améliorer la sécurité. [#6412](https://github.com/betagouv/rdv-service-public/issues/6412)
- **Correction de bugs mineurs:** Correction de divers bugs et améliorations de la stabilité. [#6478](https://github.com/betagouv/rdv-service-public/issues/6478), [#6477](https://github.com/betagouv/rdv-service-public/issues/6477), [#6475](https://github.com/betagouv/rdv-service-public/issues/6475), [#6471](https://github.com/betagouv/rdv-service-public/issues/6471), [#6469](https://github.com/betagouv/rdv-service-public/issues/6469), [#6470](https://github.com/betagouv/rdv-service-public/issues/6470)
