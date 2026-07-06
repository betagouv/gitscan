## Changelog : doctorat-gouv (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'intégration de la recherche vectorielle Scaleway, offrant une nouvelle façon de trouver des sujets de thèse. De nombreuses améliorations ont été apportées à l'interface utilisateur pour rendre cette fonctionnalité plus intuitive et informative, notamment l'ajout de badges de score, de filtres et d'une meilleure présentation des résultats. Des corrections d'accessibilité (RGAA) ont également été implémentées.

### Évolutions fonctionnelles
- Intégration de la recherche vectorielle Scaleway, permettant une recherche plus performante et sémantique des sujets de thèse.
- Ajout de badges de score vectoriel et de niveau de pertinence sur les cartes de résultats Scaleway pour aider les utilisateurs à évaluer rapidement la pertinence des sujets.
- Implémentation de filtres Scaleway (localisation, financement et autres) pour affiner les résultats de recherche.
- Affichage des résultats Scaleway en deux sections : "Meilleurs résultats" et "Autres résultats".
- Amélioration de l'affichage des messages d'aide et d'ambiguïté pour la recherche vectorielle.
- Ajout d'un badge "En cours d'expérimentation" pour indiquer que la recherche Scaleway est en version bêta.
- Possibilité de sélectionner plusieurs intentions (localisation et financement) pour la recherche Scaleway.
- Remplacement d'Albert par un toggle Scaleway avec barre de recherche et aide NLP.
- Correction de l'affichage des filtres après navigation vers le détail d'un sujet.
- Amélioration de la distinction visuelle des sections de résultats.

### Évolutions techniques
- Mise à jour des versions pour la release 0.3.6.
- Correction du mapping Hibernate pour le type vectoriel (3584) avec `@JdbcTypeCode(SqlTypes.VECTOR)`.
- Ajout d'un log des requêtes vectorielles en base de données (avec flag d'activation).
- Suppression du cap à 85% du score composite Scaleway.
- Ajout d'une whitelist `FRENCH_LOCATIONS` pour valider les intentions de localisation.
- Refactor de la détection des intentions de localisation et de financement.
- Suppression du scheduler d'indexation Albert via une propriété de configuration.
- Optimisation de la robustesse du split de la requête de recherche.
- Augmentation du budget CSS pour la page de recherche.
- Modification du tri des résultats Scaleway par score composite.

### Autres changements
- Améliorations de l'accessibilité (RGAA) :
    - Dynamisation du titre de page selon le contexte.
    - Signalement de l'état actif des boutons switch et tri par `aria-pressed`.
    - Correction de la hiérarchie des titres.
    - Exposition de l'état ouvert/fermé des dropdowns de filtres.
    - Ajout d'un lien d'évitement vers le contenu principal.
    - Ajout de labels accessibles aux champs de recherche des dropdowns.
    - Rendre les liens "Voir le détail" explicites pour les lecteurs d'écran via `aria-label`.
- Mise à jour de l'exemple NLP pour la recherche vectorielle.
- Correction de l'affichage des badges de type de bloc matche Scaleway.
- Amélioration de l'UI de la recherche vectorielle (chargement Scaleway, chips actifs visibles, compteurs, tooltip custom).
- I18n de divers messages et textes.
- Nettoyage et refactoring du code.
- Compactage des cartes de résultat.
- Suppression des compteurs sur les sections Meilleurs résultats et Autres résultats (puis rétablie sur les chips core des intentions).
