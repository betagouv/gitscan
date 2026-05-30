## Changelog : depenses-eclairees (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'extraction d'informations des documents financiers, en particulier pour les avenants et les documents DC4. Des améliorations ont été apportées aux prompts utilisés par l'IA, aux post-traitements des données extraites et aux tests de bout en bout pour garantir une meilleure qualité et précision. Des métriques de qualité ont également été ajoutées pour évaluer la performance du système.

### Évolutions fonctionnelles
- Ajout d'un front-end pour la gestion des avenants [#132](https://github.com/betagouv/depenses-eclairees/issues/132).
- Amélioration de l'extraction d'informations des avenants, incluant des post-traitements et des tests qualité sur Grist [#131](https://github.com/betagouv/depenses-eclairees/issues/131).
- Ajout du champ `external_created_at` aux engagements et mise à jour de la logique de synchronisation [#133](https://github.com/betagouv/depenses-eclairees/issues/133).
- Amélioration de l'extraction des numéros de compte (AE, DC4) et de la logique de post-traitement des RIB [#129](https://github.com/betagouv/depenses-eclairees/issues/129), [#186d898](https://github.com/betagouv/depenses-eclairees/commit/186d898).
- Correction du schéma du DC4 [#125](https://github.com/betagouv/depenses-eclairees/issues/125).
- Amélioration des prompts d'extraction pour les actes d'engagement, les CCAP, les devis et les DC4 [#126](https://github.com/betagouv/depenses-eclairees/issues/126).
- Ajout de fonctions pour lister les erreurs de différents types (faux positifs, faux négatifs) [#124](https://github.com/betagouv/depenses-eclairees/issues/124).

### Évolutions techniques
- Ajout du suivi des modèles utilisés pour l'OCR, la classification et l'analyse de contenu [#134](https://github.com/betagouv/depenses-eclairees/issues/134).
- Refactorisation de la définition des schémas de données [#120](https://github.com/betagouv/depenses-eclairees/issues/120).
- Amélioration de la gestion des erreurs de décodage JSON dans le client LLM avec une logique de nouvelle tentative [#123](https://github.com/betagouv/depenses-eclairees/issues/123).
- Ajout de métriques pour évaluer la détection, la précision et les hallucinations [#110](https://github.com/betagouv/depenses-eclairees/issues/110).
- Amélioration des tests de bout en bout avec des métriques de rappel et de précision [#110](https://github.com/betagouv/depenses-eclairees/issues/110).
- Simplification du code pour un process unitaire par engagement sans pandas.
- Une seule requête à la base de données pour tous les engagements/contrats.
- Ajout d'un pipeline de synthèse et d'un script d'exécution de tests de bout en bout.
- Refactorisation des prompts pour les champs communs.
- Ajout de métriques pour évaluer la qualité des données extraites.
- Suppression de la dépendance à Jupyter.

### Autres changements
- Correction de l'import de Grist.
- Amélioration de la gestion des fichiers ZIP (ignorance des dossiers `__MACOSX`).
- Ajout de la possibilité d'utiliser `ipython` pour des commandes shell améliorées.
- Mise à jour de la documentation et des commentaires pour une meilleure clarté.
- Paramétrisation de la sérialisation JSON pour plus de rigueur.
- Correction de la date de dernière signature dans les prompts DC4.
- Alignement du schéma RIB pour les sous-traitants avec celui des mandataires.
- Suppression d'importations inutiles (numpy).
- Ajout de la dépendance `pyxlsb`.
