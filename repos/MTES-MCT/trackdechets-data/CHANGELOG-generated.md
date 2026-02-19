## Changelog : trackdechets-data (30 derniers jours)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de la qualité et de la clarté des données traitées par la plateforme, notamment au niveau des modèles dbt. Des corrections ont été apportées pour filtrer les données obsolètes et améliorer la lisibilité des schémas de données.

### Évolutions fonctionnelles
- Correction d'un bug dans le modèle `dnd_sortant_observatoires` pour corriger les noms de colonnes et améliorer la clarté (#64).
- Amélioration du filtrage des données du registre pour exclure les entrées annulées et les versions anciennes (#63).
- Ajout de la colonne `ecoOrganismePartnersIds` au modèle `Company` pour enrichir les informations sur les entreprises (#62).

### Évolutions techniques
- Ajout de descriptions aux modèles `cartographie_icpe` pour une meilleure documentation et compréhension du schéma de données (#62).
