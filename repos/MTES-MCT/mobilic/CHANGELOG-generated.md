## Changelog : mobilic (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur l'interface d'administration de Mobilic, avec des améliorations significatives dans la gestion et l'affichage des statuts des missions, ainsi que des corrections de bugs et des optimisations de l'expérience utilisateur. Des corrections ont également été apportées à la gestion des contrôles et des redirections de l'application Agent Connect.

### Évolutions fonctionnelles
- Amélioration de l'affichage des statuts des missions dans l'interface d'administration, avec l'ajout de tags visuels pour identifier les missions validées et leur statut. [#834](https://github.com/MTES-MCT/mobilic/pull/834)
- Ajout de la possibilité de naviguer directement vers les détails d'une mission depuis le tableau d'administration en cliquant sur une ligne dédiée. [#834](https://github.com/MTES-MCT/mobilic/pull/834)
- Correction du comportement de l'application Agent Connect après une mise à niveau de Flask, assurant le bon fonctionnement des URL de redirection. [#824](https://github.com/MTES-MCT/mobilic/pull/824)
- Correction d'un bug empêchant la réinitialisation correcte des contrôles après une action spécifique. [#825](https://github.com/MTES-MCT/mobilic/pull/825)
- Amélioration de l'affichage des missions en attente de validation, avec des tooltips plus clairs.
- Correction de l'affichage des infractions lorsque plusieurs missions d'une même journée sont en attente de validation.

### Évolutions techniques
- Refactorisation du code de validation pour améliorer la déduplication des employés dans le filtre de validation. [#831](https://github.com/MTES-MCT/mobilic/pull/831)
- Extraction des labels de statut des missions dans une utilitaire partagée pour une meilleure maintenabilité.
- Optimisation du code de la table de temps de travail pour corriger des problèmes identifiés par SonarCloud.
- Amélioration de la validation des props des composants d'administration.
- Standardisation des labels de statut des missions dans l'interface d'administration.
- Correction de l'importation d'un composant dans le composant `MissionStatusTagBtn`.

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur dans l'interface d'administration (couleurs, tailles, espacements).
- Nettoyage du code et suppression de code obsolète dans la table de temps de travail.
- Correction de la logique d'affichage des missions supprimées dans l'interface d'administration.
- Correction d'un problème lié au remounting du composant `MissionDetails` lors du changement de mission.
- Correction d'un bug empêchant l'ouverture du drawer de détails de mission en cliquant sur le tag de statut.
