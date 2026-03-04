## Changelog : csplab (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'ingestion et du traitement des offres d'emploi et des CV, ainsi que sur l'amélioration de l'interface utilisateur pour la recherche et l'affichage des CV. Des refactorings importants ont été réalisés pour préparer le terrain à de nouvelles fonctionnalités et améliorer la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration du processus de vectorisation des documents en attente d'ingestion [#204](https://github.com/betagouv/csplab/issues/204).
- Correction d'un bug dans l'implémentation de l'OCR Albert [#246](https://github.com/betagouv/csplab/issues/246).
- Ajout de la prise en charge d'APHP dans la source FPH [#234](https://github.com/betagouv/csplab/issues/234).
- Correction d'un problème d'affichage des cartes de concours [#231](https://github.com/betagouv/csplab/issues/231).
- Amélioration du style de la page de traitement des CV [#219](https://github.com/betagouv/csplab/issues/219) et [#223](https://github.com/betagouv/csplab/issues/223).
- Ajout d'informations de débogage en cas d'erreur de parsing JSON lors du traitement des candidatures [#217](https://github.com/betagouv/csplab/issues/217).
- Implémentation d'un système de correspondance entre les CV et les offres d'emploi [#167](https://github.com/betagouv/csplab/issues/167).
- Ajout d'un système de polling pour la mise à jour des résultats de recherche de CV [#162](https://github.com/betagouv/csplab/issues/162).
- Création d'une page de résultats de recherche de CV avec filtrage basique [#180](https://github.com/betagouv/csplab/issues/180), [#182](https://github.com/betagouv/csplab/issues/182) et [#178](https://github.com/betagouv/csplab/issues/178).
- Mise en place d'une authentification JWT pour toutes les API [#159](https://github.com/betagouv/csplab/issues/159).

### Évolutions techniques
- Refactoring de la gestion des documents et création de repositories dédiés [#212](https://github.com/betagouv/csplab/issues/212).
- Refactoring de la configuration pour une meilleure gestion des environnements [#215](https://github.com/betagouv/csplab/issues/215).
- Mise à jour de Django en version 6.0.1 [#143](https://github.com/betagouv/csplab/issues/143).
- Mise à jour de psycopg en version 3.3.2 [#144](https://github.com/betagouv/csplab/issues/144).
- Amélioration de la verbosité des tests [#199](https://github.com/betagouv/csplab/issues/199).
- Ajout de la Django Debug Toolbar en mode développement [#186](https://github.com/betagouv/csplab/issues/186).
- Refactoring des administrateurs Django pour rendre certains champs en lecture seule [#184](https://github.com/betagouv/csplab/issues/184).
- Utilisation d'UUID pour l'identification des entités [#201](https://github.com/betagouv/csplab/issues/201).
- Ajout d'un hook Git pour vérifier le format des commits [#222](https://github.com/betagouv/csplab/issues/222) et [#221](https://github.com/betagouv/csplab/issues/221).
- Configuration de Sentry [#192](https://github.com/betagouv/csplab/issues/192).
- Ajout d'un domaine personnalisé autorisé en mode développement [#206](https://github.com/betagouv/csplab/issues/206).

### Autres changements
- Nettoyage du code et des configurations [#211](https://github.com/betagouv/csplab/issues/211).
- Mise à jour du fichier CHANGELOG.md [#185](https://github.com/betagouv/csplab/issues/185) et [#131](https://github.com/betagouv/csplab/issues/131).
- Correction de la contrainte d'unicité sur le modèle VectorizedDocumentModel [#233](https://github.com/betagouv/csplab/issues/233).
- Correction d'un bug lié au swapping de contenu lors du polling [#165](https://github.com/betagouv/csplab/issues/165).
- Gestion des erreurs lors du traitement des CV [#164](https://github.com/betagouv/csplab/issues/164).
- Amélioration de l'ingestion des offres d'emploi [#171](https://github.com/betagouv/csplab/issues/171) et [#152](https://github.com/betagouv/csplab/issues/152).
- Correction de bugs liés à la localisation et au nettoyage des références [#154](https://github.com/betagouv/csplab/issues/154).
- Correction d'un bug de configuration dans l'environnement Tycho [#151](https://github.com/betagouv/csplab/issues/151).
