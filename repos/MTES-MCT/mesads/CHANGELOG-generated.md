## Changelog : mesads (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, l'application mesads a bénéficié d'améliorations significatives concernant la gestion des véhicules relais et des registres de transactions, avec l'ajout d'un historique des véhicules et la possibilité de consultation publique des registres. Des corrections et améliorations ont également été apportées à la gestion des listes d'attente, à la recherche d'ADS et à l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout d'un historique des véhicules relais accessible aux inspecteurs et aux préfectures. [#164](https://github.com/MTES-MCT/mesads/pull/164)
- Possibilité de consulter publiquement les registres des transactions. [#164](https://github.com/MTES-MCT/mesads/pull/164)
- Ajout de la fonctionnalité de gestion des transactions.
- Affichage du nombre d'inscriptions à la liste d'attente sur la page d'une administration. [#158](https://github.com/MTES-MCT/mesads/pull/158)
- Possibilité de désarchiver une inscription archivée à la liste d'attente. [#158](https://github.com/MTES-MCT/mesads/pull/158)
- Amélioration de la recherche sur les Autorisations de Stationnement (ADS). [#157](https://github.com/MTES-MCT/mesads/pull/157)
- Ajout d'un filtre par préfecture sur les demandes d'accès gestionnaire dans l'interface d'administration. [#154](https://github.com/MTES-MCT/mesads/pull/154)

### Évolutions techniques
- Amélioration de la mixin ADSManager et son utilisation dans d'autres vues.
- Corrections et ajouts de tests pour le registre.
- Génération d'arrêté de changement de titulaire.
- Corrections sur le registre : ajout du type de contact, utilisation du SIREN, suppression de certaines pièces.

### Autres changements
- Modifications visuelles sur la page des modèles d'arrêtés. [#157](https://github.com/MTES-MCT/mesads/pull/157)
- Correction pour empêcher la saisie d'une date future pour les inscriptions à la liste d'attente. [#157](https://github.com/MTES-MCT/mesads/pull/157)
- Modification du mail de notification de doublon de liste d'attente. [#157](https://github.com/MTES-MCT/mesads/pull/157)
- Corrections de coquilles et assouplissement de la recherche publique.
- Suppression d'avertissements (warnings). [#152](https://github.com/MTES-MCT/mesads/pull/152)
- Application de règles de formatage de code avec `ruff`.
