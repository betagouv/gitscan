## Changelog : mobilic (30 derniers jours, au 08 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface d'administration, notamment avec la refonte de la page d'accueil et l'ajout d'un tableau de bord. Des améliorations ont également été apportées à la gestion des véhicules et des missions, ainsi qu'à la sécurité avec l'implémentation de l'authentification à deux facteurs (TOTP). L'intégration d'un nouveau service de chat en direct (Brevo) a également été finalisée.

### Évolutions fonctionnelles
- **Administration :** Refonte complète de la page d'accueil de l'administration avec un nouveau tableau de bord présentant des informations clés et des infractions. [#826](https://github.com/MTES-MCT/mobilic/pulls/826)
- **Administration :** Ajout de badges d'état pour les missions dans l'onglet "Activités", permettant d'identifier rapidement leur statut. [#834](https://github.com/MTES-MCT/mobilic/pulls/834)
- **Administration :** Amélioration de la gestion des véhicules avec la possibilité d'importer en masse et une interface plus conviviale. [#836](https://github.com/MTES-MCT/mobilic/pulls/836), [#837](https://github.com/MTES-MCT/mobilic/pulls/837)
- **Authentification :** Implémentation de l'authentification à deux facteurs (TOTP) pour une sécurité renforcée. [#840](https://github.com/MTES-MCT/mobilic/pulls/840)
- **Support :** Intégration d'un widget de chat en direct (Brevo) pour faciliter le support aux utilisateurs. [#832](https://github.com/MTES-MCT/mobilic/pulls/832)
- **Contrôle :** Ajout de la recherche d'articles natinf pour les contrôles. [#842](https://github.com/MTES-MCT/mobilic/pulls/842)
- **Missions :** Possibilité de voir les missions même si elles sont plus anciennes que 31 jours. [#839](https://github.com/MTES-MCT/mobilic/pulls/839)

### Évolutions techniques
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans les composants liés à l'administration.
- **Performances :** Mise en cache des données du tableau de bord pour améliorer les performances. [#848](https://github.com/MTES-MCT/mobilic/pulls/848)
- **Composants :** Introduction d'un nouveau composant `WarningBadge` pour afficher des alertes.
- **Thème :** Exportation de la constante de couleur `MOBILIC_BLUE` pour une utilisation partagée.
- **Validation :** Amélioration de la validation des numéros d'immatriculation des véhicules.
- **Gestion des erreurs :** Amélioration de la gestion des erreurs et des messages d'erreur affichés à l'utilisateur.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter les changements liés à l'intégration de Brevo.
- **Dépendances :** Suppression de l'ancienne librairie de chat Crisp.
- **Accessibilité :** Correction de problèmes d'accessibilité dans le widget de chat en direct.
- **Tests :** Ajout de tests unitaires pour certains composants.
- **CI/CD :** Mise à jour de la configuration de CircleCI.
