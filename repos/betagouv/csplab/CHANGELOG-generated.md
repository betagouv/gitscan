## Changelog : csplab (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la sécurité, de la performance et de l'expérience utilisateur de csplab. Des améliorations ont été apportées à la gestion des offres d'emploi et des CV, notamment en matière d'ingestion, de traitement et de recherche. L'interface utilisateur a également été peaufinée, avec l'ajout de fonctionnalités de feedback et de gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'un mécanisme de feedback utilisateur pour les résultats de CV, permettant de signaler les correspondances pertinentes ou non. [#260](https://github.com/betagouv/csplab/issues/260), [#261](https://github.com/betagouv/csplab/issues/261)
- Amélioration de la page de traitement des CV avec de nouveaux styles. [#223](https://github.com/betagouv/csplab/issues/223) et [#219](https://github.com/betagouv/csplab/issues/219)
- Ajout de pages d'erreur statiques pour une meilleure gestion des cas d'erreur. [#228](https://github.com/betagouv/csplab/issues/228)
- Ajout de "drawers" (fenêtres contextuelles) pour afficher les détails des opportunités. [#254](https://github.com/betagouv/csplab/issues/254)
- Possibilité d'ajouter un domaine personnalisé pour les environnements de développement. [#206](https://github.com/betagouv/csplab/issues/206)
- Amélioration de l'affichage des cartes concours. [#231](https://github.com/betagouv/csplab/issues/231)
- Ajout d'informations de débogage en cas d'erreur de parsing JSON. [#217](https://github.com/betagouv/csplab/issues/217)
- Ajout d'un formulaire Tally pour recueillir les retours utilisateurs dans les cas où aucun résultat n'est trouvé. [#245](https://github.com/betagouv/csplab/issues/245)
- Masquage des actions d'en-tête inactives. [#288](https://github.com/betagouv/csplab/issues/288)

### Évolutions techniques
- Mise en place de politiques de sécurité de contenu (CSP) pour renforcer la sécurité de l'application. [#247](https://github.com/betagouv/csplab/issues/247)
- Amélioration de la sécurité avec la mise à jour de pypdf et la configuration de politiques de sécurité supplémentaires (COOP, HSTS, cookies sécurisés). [#248](https://github.com/betagouv/csplab/issues/248), [#249](https://github.com/betagouv/csplab/issues/249)
- Optimisation des requêtes pour supprimer les doublons et améliorer la performance. [#271](https://github.com/betagouv/csplab/issues/271)
- Ajout d'un index Hnsw pour accélérer la recherche vectorielle. [#269](https://github.com/betagouv/csplab/issues/269)
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité. [#262](https://github.com/betagouv/csplab/issues/262), [#212](https://github.com/betagouv/csplab/issues/212), [#184](https://github.com/betagouv/csplab/issues/184)
- Vectorisation uniquement des documents en attente. [#204](https://github.com/betagouv/csplab/issues/204)
- Refactorisation de la gestion des identifiants des entités, passage à des UUID. [#201](https://github.com/betagouv/csplab/issues/201)
- Mise à jour de Django en version 6.0.3. [#284](https://github.com/betagouv/csplab/issues/284)
- Ajout du champ `updated_at` lors de la mise à jour des documents. [#286](https://github.com/betagouv/csplab/issues/286)
- Ajout d'un champ dans l'admin pour les documents bruts afin de faciliter la manipulation des données. [#285](https://github.com/betagouv/csplab/issues/285)

### Autres changements
- Amélioration de la configuration pour les environnements de développement (ajout de la Django Debug Toolbar, gestion des variables d'environnement). [#186](https://github.com/betagouv/csplab/issues/186), [#188](https://github.com/betagouv/csplab/issues/188)
- Mise à jour des dépendances. [#243](https://github.com/betagouv/csplab/issues/243)
- Correction d'un bug dans l'implémentation d'Albert OCR. [#246](https://github.com/betagouv/csplab/issues/246)
- Correction d'un bug lié à la référence de la variable "opportunity" dans un composant. [#270](https://github.com/betagouv/csplab/issues/270)
- Correction d'une erreur Htmx sur la transition poll-to-results. [#264](https://github.com/betagouv/csplab/issues/264)
- Correction d'un problème de CSP nonces. [#265](https://github.com/betagouv/csplab/issues/265), [#267](https://github.com/betagouv/csplab/issues/267)
- Correction d'un problème avec les props de la carte concours. [#231](https://github.com/betagouv/csplab/issues/231)
- Correction d'un problème d'unicité dans le modèle VectorizedDocumentModel. [#233](https://github.com/betagouv/csplab/issues/233)
- Ajout de APHP dans FPH verse. [#234](https://github.com/betagouv/csplab/issues/234)
- Correction d'un problème de formatage partiel. [#244](https://github.com/betagouv/csplab/issues/244)
- Amélioration de la configuration des hooks git. [#221](https://github.com/betagouv/csplab/issues/221), [#222](https://github.com/betagouv/csplab/issues/222)
- Mise à jour des styles de la page de résultats et de la logique de filtrage. [#196](https://github.com/betagouv/csplab/issues/196)
