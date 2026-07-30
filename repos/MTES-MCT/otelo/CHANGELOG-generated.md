## Changelog : otelo (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour d'otelo se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'introduction d'un mode tutoriel guidé et des améliorations concernant l'export de données et la sélection de territoires. Des corrections de bugs ont également été apportées pour assurer la fiabilité des données et des fonctionnalités.

### Évolutions fonctionnelles
- Ajout d'un mode tutoriel guidé pour accompagner les utilisateurs à travers les 6 étapes de la création de scénarios [#53](https://github.com/MTES-MCT/otelo/pull/53).
- Amélioration de la sélection de territoire dans la planification territoriale [#54](https://github.com/MTES-MCT/otelo/pull/54).
- Ajout du millésime dans le cadrage temporel et correction de l'export Excel Central_H [#54](https://github.com/MTES-MCT/otelo/pull/54).
- Correction du calcul de la disponibilité des logements, qui prend désormais en compte tous les EPCI du bassin d'habitat (intersection) [#51](https://github.com/MTES-MCT/otelo/pull/51).
- Correction de l'affichage des valeurs démographiques nulles [#51](https://github.com/MTES-MCT/otelo/pull/51).
- Correction d'une erreur "pas de données" [#51](https://github.com/MTES-MCT/otelo/pull/51).

### Évolutions techniques
- Refactorisation du registre unique des étapes du parcours de scénario.
- Correction de l'encodage des accents dans les noms de fichiers exportés.
- Limitation de l'horizon de temps des exports à l'année du millésime.
- Correction d'une migration du millésime.

### Autres changements
- Correction d'un problème lié à la valeur `undefined` lors de l'export du nom de fichier.
- Correction de l'export PowerPoint.
