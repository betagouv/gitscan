## Changelog : vizeau (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'application Vizeau a bénéficié d'améliorations significatives en termes de fonctionnalités et d'expérience utilisateur, notamment autour de la gestion des exploitations agricoles, de la visualisation des données et de la gestion des territoires. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de composants pour le module "Point de prélèvement" [#381](https://github.com/MTES-MCT/vizeau/issues/381).
- Implémentation de l'export des exploitations agricoles [#375](https://github.com/MTES-MCT/vizeau/issues/375) et [#372](https://github.com/MTES-MCT/vizeau/issues/372).
- Ajout de la possibilité d'exporter le journal de bord d'une exploitation.
- Implémentation du filtrage des AAC (Analyse Agricole et Culturelle) sur la carte de visualisation.
- Ajout d'un résumé des AAC sur la page de visualisation, avec recentrage de la carte sur l'AAC sélectionnée.
- Amélioration de l'affichage des AACs et ajout d'une fonctionnalité de recherche.
- Ajout d'un graphique d'évolution des cultures.
- Ajout d'une indication de RPG (Rendement Potentiel en Grain) sur les fiches AAC.
- Ajout de la récupération et de l'affichage des analyses d'eau sous forme de tableau.
- Ajout de nouvelles couches sur la carte de visualisation [#366](https://github.com/MTES-MCT/vizeau/issues/366).
- Traduction des codes NAF (Nomenclature d'Activités Française) en libellés [#370](https://github.com/MTES-MCT/vizeau/issues/370).
- Correction de l'affichage du journal de bord sur la page d'accueil.
- Ajout d'une commande CLI pour assigner facilement des territoires aux utilisateurs [#358](https://github.com/MTES-MCT/vizeau/issues/358).
- Implémentation des permissions par territoire.
- Correction du texte affiché dans la popup des parcelles non assignées [#340](https://github.com/MTES-MCT/vizeau/issues/340).
- Correction du délai de réponse de la recherche par raison sociale [#339](https://github.com/MTES-MCT/vizeau/issues/339).
- Ajout du champ "évolution cultures".

### Évolutions techniques
- Implémentation de Bouncer pour la gestion des autorisations.
- Amélioration de la gestion des dépendances et des types dans plusieurs composants.
- Mise à jour de diverses dépendances npm et yarn.
- Correction de bugs et optimisations diverses pour améliorer la stabilité et la performance de l'application.

### Autres changements
- Correction de la transparence des résultats dans le composant d'auto-complétion [#378](https://github.com/MTES-MCT/vizeau/issues/378).
- Correction d'un crash lors de la visualisation de données de culture manquantes [#347](https://github.com/MTES-MCT/vizeau/issues/347).
- Correction de la gestion inter-formulaires et de la suppression du dernier contact supplémentaire.
- Amélioration de la réactivité de l'interface utilisateur.
- Ajout de bbox sur les fiches AAC [#354](https://github.com/MTES-MCT/vizeau/issues/354).
- Correction de l'icône de priorité dans le composant AacCaptages.
- Amélioration du design de la page AAC et de l'onglet AAC.
- Mise à jour des composants de l'interface utilisateur.
