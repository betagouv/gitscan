## Changelog : ecobalyse (30 derniers jours, au 11 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux matériaux et processus (batteries, emballages, verre feuilleté, transport), ainsi que sur l'amélioration de la précision des calculs et de la robustesse de l'application. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer l'expérience utilisateur et la performance globale.

### Évolutions fonctionnelles
- Ajout de composants de batterie pour les véhicules ([#2366](https://github.com/MTES-MCT/ecobalyse/issues/2366)).
- Ajout de nouveaux matériaux : polyester non tissé ([#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421)), verre feuilleté ([#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403)).
- Ajout de nouveaux processus : fabrication de pneus ([#2415](https://github.com/MTES-MCT/ecobalyse/issues/2415)), cuisson de céréales et légumineuses ([#2402](https://github.com/MTES-MCT/ecobalyse/issues/2402)).
- Ajout de transports routiers depuis le Maroc ([#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)).
- Amélioration de l'affichage des alias dans l'explorateur ([#2444](https://github.com/MTES-MCT/ecobalyse/issues/2444)).
- Ajout d'un champ "recyclable" ([#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)).
- Ajout de la prise en compte du CFF dans les processus d'emballage alimentaire ([#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)).
- Publication de la section réglementaire pour l'alimentation ([#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)).

### Évolutions techniques
- Refactorisation pour permettre l'absence de clés d'impact, avec une valeur par défaut de zéro ([#2417](https://github.com/MTES-MCT/ecobalyse/issues/2417)).
- Amélioration de la fiabilité des tests E2E en supprimant les tentatives ([#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)).
- Utilisation de JSON pour stocker les composants ([#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)).
- Mise à jour des dépendances npm et Python ([#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389), [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)).
- Amélioration de la gestion des distances pour les transports ([#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347), [#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259)).
- Correction de la gestion des transports aériens ([#2398](https://github.com/MTES-MCT/ecobalyse/issues/2398), [#2377](https://github.com/MTES-MCT/ecobalyse/issues/2377)).
- Amélioration de la précision des calculs en réduisant la précision ([#2303](https://github.com/MTES-MCT/ecobalyse/issues/2303)).

### Autres changements
- Ajout d'un ADR pour la gestion de la localisation des composants ([#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)).
- Correction de l'affichage du nom des processus d'assemblage de batteries ([#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)).
- Suppression de processus obsolètes ([#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)).
- Correction du type de matériau du recyclage de fibres PET ([#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)).
- Ajout de gaz à la cuisson ([#2211](https://github.com/MTES-MCT/ecobalyse/issues/2211)).
- Suppression du dossier "data" de l'image Scalingo ([#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)).
- Correction des avertissements Dependabot ([#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)).
- Synchronisation avec le dépôt de données ([#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)).
