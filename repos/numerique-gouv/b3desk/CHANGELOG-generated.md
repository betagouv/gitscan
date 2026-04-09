## Changelog : b3desk (30 derniers jours, au 9 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées à b3desk au cours du dernier mois. Les principales évolutions concernent la délégation de réunions, des corrections d'interface utilisateur pour une meilleure expérience, et des améliorations de la documentation. Des corrections ont également été apportées pour assurer la compatibilité avec Keycloak et éviter les liens statiques.

### Évolutions fonctionnelles
- **Délégation de réunions :** Implémentation de la fonctionnalité permettant la délégation de réunions. [#241](https://github.com/numerique-gouv/b3desk/pull/241)
- **Modification du nom de l'utilisateur :** Les utilisateurs authentifiés peuvent maintenant modifier leur nom sur la page de participation à une réunion. [#318](https://github.com/numerique-gouv/b3desk/issues/318)
- **Affichage du logo :** Correction pour éviter que le titre ne recouvre le logo. [#319](https://github.com/numerique-gouv/b3desk/issues/319)

### Évolutions techniques
- **Compatibilité Keycloak :** Correction pour assurer la compatibilité avec Keycloak dans le pipeline CI. [#317](https://github.com/numerique-gouv/b3desk/issues/317)
- **Liens statiques :** Suppression des liens statiques pour une meilleure maintenabilité. [#322](https://github.com/numerique-gouv/b3desk/issues/322)
- **Documentation :** Ajout de documentation concernant la transcription des réunions BigBlueButton. [#321](https://github.com/numerique-gouv/b3desk/issues/321)

### Autres changements
- Mise à jour de la version principale vers 1.6.1dev et 1.5.9dev.
- Mises à jour de dépendances : `cryptography`, `pygments`, `requests`, `authlib`. (Ces mises à jour sont automatiques et ne nécessitent pas d'action particulière.)
