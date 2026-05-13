## Changelog : mobilic (30 derniers jours, au 08 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface administrateur, notamment avec l'ajout d'une page d'accueil dédiée et la refonte de la gestion des véhicules. L'intégration de Brevo Live Chat remplace Crisp pour le support utilisateur, et des corrections ont été apportées pour améliorer la stabilité et la performance de l'application. Des améliorations ont également été apportées à la gestion des activités et des missions.

### Évolutions fonctionnelles
- **Interface Administrateur :** Nouvelle page d'accueil pour les administrateurs avec un tableau de bord et un aperçu des infractions. [#826](https://github.com/MTES-MCT/mobilic/pulls/826)
- **Gestion des Véhicules :** Ajout d'une fonctionnalité d'importation massive de véhicules. [#837](https://github.com/MTES-MCT/mobilic/pulls/837)
- **Gestion des Missions :** Ajout d'étiquettes de statut pour les missions dans l'onglet "Activités", facilitant leur identification. [#834](https://github.com/MTES-MCT/mobilic/pulls/834), [#829](https://github.com/MTES-MCT/mobilic/pulls/829)
- **Support Utilisateur :** Remplacement de Crisp par Brevo Live Chat pour une assistance en direct. [#832](https://github.com/MTES-MCT/mobilic/pulls/832)
- **Impersonation :** Ajout de la fonctionnalité d'impersonation d'utilisateurs pour le support, avec recherche, menu et authentification à deux facteurs (TOTP). [#840](https://github.com/MTES-MCT/mobilic/pulls/840)
- **Recherche Natinf :** Intégration de la recherche Natinf. [#842](https://github.com/MTES-MCT/mobilic/pulls/842)
- **Affichage des Activités :** Correction pour afficher les activités passées, même si la mission est antérieure à 31 jours. [#841](https://github.com/MTES-MCT/mobilic/pulls/841)

### Évolutions techniques
- **Refactoring :** Extraction de constantes réutilisables pour la gestion des couleurs et des dates.
- **Performances :** Mise en cache des données du tableau de bord administrateur pour améliorer la performance. [#848](https://github.com/MTES-MCT/mobilic/pulls/848)
- **Validation :** Amélioration de la validation des numéros d'immatriculation des véhicules.
- **Composants :** Introduction d'un nouveau composant `WarningBadge`.
- **Authentification :** Ajout du support TOTP pour l'authentification à deux facteurs.
- **DSFR :** Utilisation d'icônes DSFR dans les actions d'édition de tableau.
- **Suppression de dépendances :** Suppression de la dépendance à `crisp-sdk-web`.

### Autres changements
- **Documentation :** Mise à jour de la politique de confidentialité pour refléter l'utilisation de Brevo.
- **Nettoyage de code :** Suppression de code inutilisé et correction de problèmes identifiés par SonarCloud.
- **Configuration :** Mise à jour de la configuration du live chat.
- **Assets :** Ajout de l'icône Mobilic au widget Brevo Live Chat.
- **Tests :** Ajout de tests pour la nouvelle fonctionnalité d'impersonation.
