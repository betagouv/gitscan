## Changelog : trackdechets-data (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à la plateforme trackdechets-data. Les modifications se concentrent principalement sur l'enrichissement et la correction des modèles de données utilisés pour le suivi des déchets, notamment au niveau des registres et des ICPE, afin d'améliorer la qualité et la clarté des informations disponibles.

### Évolutions fonctionnelles
- Ajout de modèles enrichis pour les registres entrants et sortants, permettant un suivi plus précis des déchets (#65).
- Correction des noms de colonnes dans le modèle `dnd_sortant_observatoires` pour une meilleure lisibilité (#64).
- Filtrage des versions annulées et anciennes des registres pour ne conserver que les données pertinentes (#63).
- Ajout de la colonne `ecoOrganismePartnersIds` au modèle `Company` pour inclure l'information sur les partenaires des éco-organismes (#62).

### Évolutions techniques
- Modification de la stratégie de matérialisation de plusieurs modèles Trackdéchets de "incremental" à "table" dans dbt pour optimiser les performances et la cohérence des données (#65).
- Ajout de descriptions aux modèles `cartographie_icpe` pour une meilleure documentation et compréhension du code (#62).
