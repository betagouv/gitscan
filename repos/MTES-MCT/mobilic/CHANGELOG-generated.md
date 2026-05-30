## Changelog : mobilic (30 derniers jours, au 27 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'interface d'administration, notamment une refonte de la page d'accueil, l'ajout de fonctionnalités d'importation en masse de véhicules et l'amélioration de la gestion des infractions. Des corrections de bugs et des optimisations de sécurité ont également été apportées, ainsi que l'ajout de la recherche natinf et de la prise en charge de l'authentification à deux facteurs (2FA).

### Évolutions fonctionnelles
- **Administration :** Refonte complète de la page d'accueil avec affichage des infractions multi-employeurs [#836](https://github.com/MTES-MCT/mobilic/pulls/836).
- **Administration :** Ajout de la possibilité d'importer en masse des véhicules [#837](https://github.com/MTES-MCT/mobilic/pulls/837) et [#845](https://github.com/MTES-MCT/mobilic/pulls/845).
- **Administration :** Amélioration de l'affichage et de la gestion des infractions sur la page d'accueil [#851](https://github.com/MTES-MCT/mobilic/pulls/851).
- **Authentification :** Implémentation de l'authentification à deux facteurs (2FA) avec support TOTP [#826](https://github.com/MTES-MCT/mobilic/pulls/826).
- **Administration :** Ajout de la fonctionnalité d'impersonation d'utilisateurs pour le support administratif.
- **Recherche :** Ajout de la recherche natinf [#842](https://github.com/MTES-MCT/mobilic/pulls/842).
- **Correction :** Correction du rafraîchissement des jours travaillés après la validation d'une mission [#854](https://github.com/MTES-MCT/mobilic/pulls/854).
- **Correction :** Correction de l'affichage des missions de plus de 31 jours dans l'historique des activités [#840](https://github.com/MTES-MCT/mobilic/pulls/840).

### Évolutions techniques
- **Refactoring :** Extraction de la configuration du date picker et de la logique de rafraîchissement dans des constantes partagées.
- **Refactoring :** Introduction d'un composant `WarningBadge` réutilisable.
- **Refactoring :** Ajout d'une fonction `formatCompleteDateFromString` pour formater les dates.
- **Refactoring :** Export de la constante `MOBILIC_BLUE` pour une utilisation partagée.
- **Composants :** Utilisation d'icônes DSFR dans les actions d'édition de tableau.
- **Validation :** Renforcement de la validation des numéros d'immatriculation des véhicules.
- **Performance :** Différment de l'analyse des informations d'immatriculation jusqu'à la soumission du formulaire.

### Autres changements
- **Documentation :** Ajout du logo Chaventon Express [#848](https://github.com/MTES-MCT/mobilic/pulls/848).
- **UI :** Suppression des exemples de valeurs par défaut dans le modal des véhicules [#849](https://github.com/MTES-MCT/mobilic/pulls/849).
- **UI :** Mise à jour du texte de la page de sécurité [#850](https://github.com/MTES-MCT/mobilic/pulls/850).
- **Nettoyage :** Suppression de code inutilisé et correction de duplications de code.
- **DSFR :** Remplacement de composants Material-UI par des composants DSFR dans l'interface de contrôle.
- **Tracking :** Ajout du suivi des fichiers `refresh-line.svg` et `delete-bin-line.svg` dans les assets DSFR.
