## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'introduction de la personnalisation des listes de dossiers, permettant aux utilisateurs de choisir les informations qu'ils souhaitent voir apparaître. Nous avons également amélioré la génération de documents PDF, notamment par la possibilité d'exporter des dossiers vides pour faciliter l'instruction, et l'intégration de cartes statiques dans les exports. Enfin, d'importantes optimisations de performance et de sécurité ont été réalisées pour garantir la fluidité et la robustesse du service.

### Évolutions fonctionnelles
- **Personnalisation de l'affichage** : Les utilisateurs peuvent désormais personnaliser leurs listes de dossiers en choisissant les colonnes à afficher, en les regroupant par sections et en consultant des aides contextuelles directement dans les menus de sélection [#13373](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13373).
- **Gestion des dossiers vides** : Possibilité de générer un export PDF d'un dossier vide (via WeasyPrint) pour accompagner les agents dans la compréhension des démarches à venir [#13587](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13587).
- **Amélioration des exports PDF** : Les cartes géographiques sont désormais intégrées sous forme d'images statiques dans les exports PDF des dossiers pour une meilleure lisibilité [#13597](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13597).
- **Recherche et filtrage** : Amélioration de la précision des recherches et ajout de filtres booléens plus performants (notamment pour les statuts FranceConnect ou les établissements) [#13653](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13715).
- **Administration et API** : Intégration de nouveaux points d'accès et de données spécifiques pour l'intégration avec les services de l'ARS (Agence Régionale de Santé) [#13573](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13573).
- **Expérience utilisateur** : Amélioration des messages d'erreur lors du téléchargement de fichiers et meilleure visibilité des indicateurs de modification sur les champs des dossiers.

### Évolutions techniques
- **Refonte de l'architecture des champs** : Migration massive du système de gestion des types de champs (`TypeDeChamp`) vers un modèle de polymorphisme (STI) pour une meilleure maintenabilité et une gestion plus fine des comportements par type [#13662](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13662).
- **Optimisation des performances** : 
    - Amélioration de la recherche plein texte via l'utilisation de vecteurs de recherche (`tsvectors`) stockés en base de données [#13567](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13567).
    - Optimisation des requêtes GraphQL grâce au préchargement (preloading) de données pour réduire le nombre d'appels à la base de données [#13567](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13567).
- **Sécurité et robustesse** :
    - Renforcement du traitement des images avec `libvips` pour prévenir les vulnérabilités liées aux décodeurs [#13687](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13687).
    - Protection contre les attaques par traversée de chemin (path traversal) lors de la génération d'exports ZIP [#13669](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13669).
- **Nettoyage de l'infrastructure** : Suppression de la gestion des tâches via `delayed_job` au profit de solutions plus modernes et suppression de nombreuses colonnes de base de données obsolètes [#13682](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13682), [#13695](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13695).
- **Internationalisation (i18n)** : Refonte de la gestion des traductions pour utiliser des fichiers "sidecar" par composant, rendant le code plus propre et plus facile à maintenir [#13650](https://github.com/demarche-numerique/demarche.numerique.gouv.fr/pull/13650).

### Autres changements
- **Migration de templates** : Migration importante de nombreux composants de HAML vers ERB pour standardiser le rendu des vues.
- **Documentation** : Mise à jour de la documentation de l'administrateur et de la FAQ pour refléter les nouveaux termes et fonctionnalités.
- **Qualité du code** : Nettoyage de nombreuses méthodes d'aide (helpers) et de fichiers de vues inutilisés.
