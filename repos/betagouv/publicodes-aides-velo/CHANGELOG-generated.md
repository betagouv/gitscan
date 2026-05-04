## Changelog : publicodes-aides-velo (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les mises à jour se concentrent sur la correction de données d'aides vélo, notamment des ajustements de montants, de dates de validité et de liens. Des améliorations techniques ont également été apportées, incluant le passage à Prettier pour le formatage du code et des optimisations du workflow de publication.

### Évolutions fonctionnelles
- Mise à jour des aides vélo pour le Luxembourg et Monaco.
- Correction de la question relative au "revenu de référence" dans le formulaire de simulation.
- Synchronisation du nombre de parts et du nombre de personnes pour un calcul plus précis des aides.
- Correction et mise à jour de plusieurs aides locales (Oullins-Pierre-Bénite, Gap, Dunkerque, Saint-Alban-Leysse) pour refléter les informations les plus récentes.
- Ajout des aides vélo des communautés de communes Vie et Boulogne, CCVO et suppression des aides dépassées.

### Évolutions techniques
- Remplacement de l'outil de formatage de code Dprint par Prettier pour une meilleure cohérence et intégration avec les outils de développement.
- Mise à jour de la dépendance `@etalab/decoupage-administratif` vers la version 6.0.0.
- Amélioration du workflow de publication des packages.
- Ajout d'un script pour trier les aides par type de collectivité et date d'obsolescence.
- Restauration de la logique de génération du fichier `communes.json`.

### Autres changements
- Correction de liens cassés dans les données des aides vélo.
- Amélioration de l'organisation et de la lisibilité des fichiers Publicodes grâce au formatage avec Prettier.
- Correction de doublons dans les données de l'aide "cc loue-lison".
