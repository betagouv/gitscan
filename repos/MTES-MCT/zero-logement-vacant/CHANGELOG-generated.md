## Changelog : zero-logement-vacant (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de performance, notamment au niveau de l'importation des données LOVAC et de l'affichage des tableaux de bord. De nouvelles fonctionnalités ont été ajoutées pour améliorer l'analyse des données, avec l'intégration de graphiques DSFR (barres, secteurs, tableaux) et une meilleure gestion des filtres. Des corrections de bugs et des refactorings ont également été effectués pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les établissements par interco (structure DDT/départementale) [#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867).
- La date de naissance des propriétaires est désormais un champ optionnel dans le formulaire d'édition [#1861](https://github.com/MTES-MCT/zero-logement-vacant/issues/1861).
- Amélioration de l'affichage du tableau de bord d'analyse pour l'année 2026 [#1858](https://github.com/MTES-MCT/zero-logement-vacant/issues/1858).
- Ajout d'une colonne "Statut du suivi" pour les destinataires des campagnes [#1820](https://github.com/MTES-MCT/zero-logement-vacant/issues/1820).
- Redirection vers la vue tableau lors du clic sur un groupe depuis la carte [#1821](https://github.com/MTES-MCT/zero-logement-vacant/issues/1821).
- Ajout de graphiques DSFR (barres, secteurs, tableaux) pour une meilleure visualisation des données [#1834](https://github.com/MTES-MCT/zero-logement-vacant/issues/1834).
- Possibilité de lier une campagne à un logement [#1830](https://github.com/MTES-MCT/zero-logement-vacant/issues/1830).
- Correction du filtre de campagne exclusif [#1822](https://github.com/MTES-MCT/zero-logement-vacant/issues/1822).
- Amélioration de l'affichage du bouton de légende de la carte [#1825](https://github.com/MTES-MCT/zero-logement-vacant/issues/1825).

### Évolutions techniques
- Migration vers React Router v7 pour une meilleure performance et une API plus moderne [#1733](https://github.com/MTES-MCT/zero-logement-vacant/issues/1733).
- Refactoring important du code pour supprimer l'ancienne librairie DSFR et utiliser les composants DSFR natifs.
- Mise en place d'un cache pour les réponses de l'API Metabase afin d'améliorer les performances du tableau de bord d'analyse [#1847](https://github.com/MTES-MCT/zero-logement-vacant/issues/1847).
- Amélioration de la gestion des filtres de logement avec l'utilisation d'un contexte React.
- Utilisation de DuckDB pour le prétraitement des données LOVAC, améliorant la performance et la robustesse de l'import.
- Refactorisation du code pour utiliser des factories plus robustes et des tests plus complets.
- Migration vers `tsx` et suppression de `ts-node`.
- Amélioration de la gestion des dépendances et des versions.
- Utilisation de `uuidv5` pour générer des identifiants déterministes.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements techniques.
- Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
- Correction de bugs mineurs et amélioration de la lisibilité du code.
- Ajout d'un script pour backfiller les adresses LOVAC 2026.
- Ajout de nouvelles compétences aux membres de l'équipe.
- Mise à jour des instructions d'installation et de configuration.
- Correction de problèmes liés à l'affichage des apostrophes françaises.
- Amélioration de la gestion des erreurs et des logs.
- Suppression de code obsolète.
- Mise à jour des dépendances.
