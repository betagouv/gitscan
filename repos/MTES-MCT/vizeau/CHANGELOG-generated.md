## Changelog : vizeau (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'application Vizeau a bénéficié d'améliorations significatives en termes de gestion des exploitations, notamment avec l'ajout de fonctionnalités d'export de données (parcelles, journal de bord).  L'interface utilisateur a également été enrichie avec de nouvelles couches cartographiques et des informations résumées sur les AAC (Autorisations d'aménagement concertées). Des améliorations ont été apportées à la gestion des territoires et des permissions utilisateurs, ainsi qu'à la gestion des contacts.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les parcelles d'une exploitation. [#372](https://github.com/MTES-MCT/vizeau/pull/372)
- Ajout de la possibilité d'exporter le journal de bord d'une exploitation. [#371](https://github.com/MTES-MCT/vizeau/pull/371)
- Ajout de nouvelles couches sur la carte de visualisation. [#366](https://github.com/MTES-MCT/vizeau/pull/366)
- Affichage d'un résumé des informations relatives aux AAC sur la page de visualisation. [#357](https://github.com/MTES-MCT/vizeau/pull/357)
- Possibilité de centrer la carte sur une AAC spécifique.
- Amélioration de la gestion des contacts : correction de la suppression du dernier contact supplémentaire, gestion inter-formulaires, fermeture du tiroir de formulaire au chargement. [#363](https://github.com/MTES-MCT/vizeau/pull/363)
- Ajout d'une indication de RPG (Référentiel Paysager Graphique).
- Redirection vers la page d'une AAC pour consulter ses évolutions.
- Filtrage des AACs dans la page de visualisation. [#364](https://github.com/MTES-MCT/vizeau/pull/364)
- Correction de l'affichage du journal de bord sur la page d'accueil.
- Traduction des codes NAF en libellés. [#370](https://github.com/MTES-MCT/vizeau/pull/370)

### Évolutions techniques
- Implémentation des permissions par territoire, permettant de restreindre l'accès aux données en fonction du territoire de l'utilisateur. [#358](https://github.com/MTES-MCT/vizeau/pull/358)
- Création d'une commande CLI pour assigner facilement des territoires aux utilisateurs. [#359](https://github.com/MTES-MCT/vizeau/pull/359)
- Amélioration du seeding des comptes animateurs avec l'attribution de territoires. [#380](https://github.com/MTES-MCT/vizeau/pull/380)
- Correction d'un crash lié à l'exportation.
- Correction de la transparence des résultats dans le composant autocomplete. [#378](https://github.com/MTES-MCT/vizeau/pull/378)

### Autres changements
- Composants pour le module Point de prélèvement. [#381](https://github.com/MTES-MCT/vizeau/pull/381)
- Correction de l'erreur de redirection vers la page d'erreur des territoires lorsque l'utilisateur n'en a pas.
- Amélioration de la gestion des dépendances dans useEffect pour le contact principal.
- Diverses corrections et optimisations suite aux revues de code Copilot.
