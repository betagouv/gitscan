## Changelog : mobilic (30 derniers jours, au 8 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface d'administration, notamment avec une nouvelle page d'accueil pour les managers, l'intégration de tags de statut pour les missions dans l'onglet "Activité", et l'amélioration de la gestion des validations. L'intégration de Brevo (anciennement Sendinblue) pour le support client remplace Crisp, offrant une meilleure expérience utilisateur. Plusieurs corrections de bugs et optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- **Administration :** Nouvelle page d'accueil pour les managers avec un tableau de bord et une liste des infractions. [#826](https://github.com/MTES-MCT/mobilic/pulls/826)
- **Administration :** Amélioration de la gestion des opérations en lot, notamment pour l'importation massive de véhicules. [#836](https://github.com/MTES-MCT/mobilic/pulls/836), [#837](https://github.com/MTES-MCT/mobilic/pulls/837)
- **Administration - Activités :** Ajout de tags de statut pour les missions dans l'onglet "Activité", facilitant la visualisation de l'état d'avancement. [#834](https://github.com/MTES-MCT/mobilic/pulls/834), [#829](https://github.com/MTES-MCT/mobilic/pulls/829), [#831](https://github.com/MTES-MCT/mobilic/pulls/831)
- **Support Client :** Remplacement de Crisp par Brevo Conversations pour le support client, avec une intégration spécifique pour la page "Contrôleur". [#841](https://github.com/MTES-MCT/mobilic/pulls/841), [#832](https://github.com/MTES-MCT/mobilic/pulls/832), [#833](https://github.com/MTES-MCT/mobilic/pulls/833)
- **Authentification :** Ajout de l'authentification à deux facteurs (2FA) avec TOTP. [#833](https://github.com/MTES-MCT/mobilic/pulls/833)
- **Impersonation :** Ajout de la fonctionnalité d'impersonation d'utilisateurs pour l'administration.
- **Recherche Natinf :** Intégration de la recherche Natinf. [#842](https://github.com/MTES-MCT/mobilic/pulls/842)

### Évolutions techniques
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans les composants liés à l'administration.
- **Performance :** Optimisation des performances du tableau de bord d'administration avec la mise en cache des données.
- **Sécurité :** Amélioration de la sécurité en intégrant l'authentification à deux facteurs et en corrigeant des vulnérabilités potentielles.
- **Composants :** Introduction d'un nouveau composant `WarningBadge` pour afficher des alertes.
- **Thème :** Exportation de la constante de couleur `MOBILIC_BLUE` pour une utilisation partagée.
- **Dates :** Ajout d'une fonction utilitaire `formatCompleteDateFromString` pour formater les dates.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo.
- **Dépendances :** Suppression de la dépendance à Crisp SDK.
- **Tests :** Ajout de tests unitaires pour certaines fonctionnalités.
- **Accessibilité :** Correction de problèmes d'accessibilité dans le widget de chat en direct.
- **DSFR :** Utilisation d'icônes DSFR dans les actions d'édition du tableau d'administration.
- **SonarCloud :** Correction de violations de règles SonarCloud.
