## Changelog : communs-de-la-transition-ecologique-des-collectivites (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent principalement sur l'amélioration du tableau de bord de la transition écologique (Dashboard TE) avec de nouvelles options de filtrage et d'agrégation des données. Des améliorations significatives ont également été apportées à la fonctionnalité de recherche d'aides, notamment en termes de matching et de pondération des critères. Enfin, des corrections et optimisations diverses ont été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Dashboard TE :** Ajout de filtres multi-valeurs pour les communes, départements et sources de données [#1234](https://github.com/betagouv/communs-de-la-transition-ecologique-des-collectivites/issues/1234).
- **Dashboard TE :** Possibilité de filtrer les projets par EPCI (Établissement Public de Coopération Intercommunale).
- **Dashboard TE :** Classification scorée des projets pour une meilleure analyse.
- **Dashboard TE :** Affichage des communes (code INSEE) associées à chaque projet dans le détail.
- **Dashboard TE :** Ajout d'un paramètre pour inclure ou exclure les projets de la DGCL (Direction Générale des Collectivités Locales).
- **Dashboard TE :** Affichage des millésimes des projets dans le résumé.
- **Dashboard TE :** Ajout d'un endpoint `/projets/summary` pour obtenir un résumé des projets.
- **Dashboard TE :**  Possibilité de trier la liste des projets et de plafonner les montants aberrants à 100 M€.
- **Recherche d'aides :** Recherche d'aides par classification et par communes.
- **Recherche d'aides :** Amélioration du matching entre les aides et les projets, avec pondération des axes thématique et textuel.
- **Recherche d'aides :** Ajout de paramètres `cutoff` et seuils de confiance pour affiner les résultats.
- **Recherche d'aides :**  Amélioration du matching textuel avec l'utilisation de BM25.
- **Statistiques nationales :** Ajout d'un flag `inclure_tet` pour agréger les fiches d'action TE.
- **Probabilité de transition écologique :** Exposition de la probabilité de TE par projet et ajout de filtres et d'une synthèse par probabilité.

### Évolutions techniques
- **API :** Amélioration du typage OpenAPI pour les endpoints `/aides/feedback`.
- **CI/CD :** Séparation des jobs de release et de déploiement pour une meilleure résilience.
- **Classification :** Utilisation d'un prompt system dédié pour la classification des aides.
- **Financements :** Correction de la liaison entre les financements et les projets via une table de jointure.
- **Correction de bugs :** Correction de filtres sur les montants et les financements.

### Autres changements
- **Documentation :** Masquage des détails d'implémentation dans le Swagger de l'API aides.
- **Scripts :** Ajout de scripts de diagnostic pour la qualité des données des aides (géo, thématique, textuel).
- **Scripts :** Ajout d'un script de requalification du catalogue d'aides.
- **Tests :** Alignement des mocks pour les tests de l'API aides.
- **Correction de bugs :** Correction du fallback pour la récupération des données des aides.
