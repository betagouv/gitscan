## Changelog : approbiom (30 derniers jours, au 02/09/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes dans l'automatisation et la visualisation des données. L'ajout de nouvelles fonctionnalités cartographiques, l'automatisation de l'importation de fichiers externes (BCIB/BCIAT) et une refonte de l'interface utilisateur permettent une navigation plus intuitive et une exploitation plus efficace des plans d'approvisionnement.

### Évolutions fonctionnelles
- **Nouveaux outils** : Introduction du widget "Concurrence" [#17](https://github.com/betagouv/approbiom/issues/17).
- **Enrichissement du widget Accueil** : 
    - Ajout de filtres multicritères (fournisseurs, programmes d'aide, départements et régions).
    - Ajout d'un onglet "Ressources" et gestion des pièces jointes [#21](https://github.com/betagouv/approbiom/issues/21).
    - Amélioration de la clarté avec l'affichage des noms de plans plutôt que des départements.
- **Visualisation cartographique** : Intégration de cartes affichant des polygones de provenance et des marqueurs d'installation.
- **Optimisation de l'interface (UI)** : 
    - Remplacement des tags par des badges pour la chronologie.
    - Organisation des tableaux de ventilation sous forme d'onglets.
    - Changement de terminologie pour plus de cohérence (remplacement de "Dossier" par "Plan").
- **Performance** : Accélération du temps de mise à jour des données dans l'onglet Accueil.

### Évolutions techniques
- **Automatisation des imports** : Développement d'un script Python permettant l'extraction, la transformation et l'exportation automatisée des données depuis les fichiers Excel (BCIB/BCIAT) vers le format CSV.
- **Refonte architecturale** : Application de l'architecture hexagonale aux widgets "Accueil" et "Ressource" [#18](https://github.com/betagouv/approbiom/issues/18), [#19](https://github.com/betagouv/approbiom/issues/19).
- **Qualité et structure du code** : 
    - Refactorisation globale de la structure du code [#16](https://github.com/betagouv/approbiom/issues/16).
    - Création d'un environnement de développement ("playground") dédié aux composants cartographiques [#18](https://github.com/betagouv/approbiom/issues/18).
    - Implémentation d'une fonction de nettoyage et de standardisation des données de provenance [#19](https://github.com/betagouv/approbiom/issues/19).
- **Maintenance CI/CD** : Correction des scripts de déploiement et de la configuration de formatage (Prettier).

### Autres changements
- Mise à jour de la documentation relative aux décisions d'architecture.
- Nettoyage général du dépôt (suppression de fichiers inutilisés et réorganisation des dossiers).
