## Changelog : potentiel (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de gestion des erreurs, de navigation et de correction de données (SIRET, coordonnées). Des corrections ont également été apportées pour gérer plus efficacement les projets en abandon ou avec Procédure de Permis de Construire Accélérée (PPA). Enfin, des améliorations techniques ont été réalisées sur la gestion des données et des flux, ainsi que sur la sécurité et la conformité.

### Évolutions fonctionnelles
- Correction d'une redirection après achèvement pour les projets non soumis [#4364](https://github.com/MTES-MCT/potentiel/issues/4364).
- Formatage des coordonnées géodésiques en français [#4363](https://github.com/MTES-MCT/potentiel/issues/4363).
- Enregistrement du rapport associé lors de l'existence d'une attestation de conformité [#4360](https://github.com/MTES-MCT/potentiel/issues/4360).
- Correction de l'affichage du raccordement PTF [#4359](https://github.com/MTES-MCT/potentiel/issues/4359).
- Redirection après invitation à un projet éliminé [#4357](https://github.com/MTES-MCT/potentiel/issues/4357).
- Amélioration des liens d'évitement pour l'accessibilité [#4350](https://github.com/MTES-MCT/potentiel/issues/4350).
- Possibilité pour les agents DREAL/Admin de modifier les garanties financières [#4345](https://github.com/MTES-MCT/potentiel/issues/4345).
- Correction d'un lien vers le détail d'un projet éliminé après recours [#4325](https://github.com/MTES-MCT/potentiel/issues/4325).
- Ajout de la technologie aux exports lauréat et éliminés [#4323](https://github.com/MTES-MCT/potentiel/issues/4323).
- Affichage du motif de refus de garantie financière en attente sur la page projet [#4320](https://github.com/MTES-MCT/potentiel/issues/4320).
- Ajout de l'opérateur `BETWEEN` pour les requêtes [#4349](https://github.com/MTES-MCT/potentiel/issues/4349).
- Amélioration de la navigation au clavier du composant Multiselect [#4346](https://github.com/MTES-MCT/potentiel/issues/4346).
- Ajout d'une tâche à la notification si le numéro d'identification est vide [#4332](https://github.com/MTES-MCT/potentiel/issues/4332).
- Possibilité pour le porteur de projet de corriger son numéro SIRET/SIREN [#4322](https://github.com/MTES-MCT/potentiel/issues/4322).
- Ajout de la possibilité de forcer l'utilisation de Proconnect pour CRE et ADEME [#4327](https://github.com/MTES-MCT/potentiel/issues/4327).
- Ajout de la possibilité pour les PP de corriger le numéro d'identification [#4317](https://github.com/MTES-MCT/potentiel/issues/4317).
- Ajout de l'instruction d'abandon avec choix PPA [#4260](https://github.com/MTES-MCT/potentiel/issues/4260).
- Notification de modification d'achèvement [#4252](https://github.com/MTES-MCT/potentiel/issues/4252).
- Formulaire de correction du SIRET/SIREN [#4222](https://github.com/MTES-MCT/potentiel/issues/4222).

### Évolutions techniques
- Intégration des dernières modifications de la version 3.82 [#4367](https://github.com/MTES-MCT/potentiel/issues/4367).
- Intégration des modifications de la release 3.82 [#4361](https://github.com/MTES-MCT/potentiel/issues/4361).
- Intégration des modifications de la release 3.82 [#4358](https://github.com/MTES-MCT/potentiel/issues/4358).
- Suppression de l'adapter projets éligibles recandidature [#4354](https://github.com/MTES-MCT/potentiel/issues/4354).
- Correction de la valeur "false" dans les filtres [#4355](https://github.com/MTES-MCT/potentiel/issues/4355).
- Amélioration de la hiérarchie des titres pour l'accessibilité [#4348](https://github.com/MTES-MCT/potentiel/issues/4348).
- Simplification des readable stream [#4321](https://github.com/MTES-MCT/potentiel/issues/4321).
- Mise à jour de la sécurité de la librairie `shell-quote` [#4324](https://github.com/MTES-MCT/potentiel/issues/4324).
- Suppression de scripts de migration inutiles [#4337](https://github.com/MTES-MCT/potentiel/issues/4337).
- Suppression de schémas et extensions PostGIS inutiles [#4294](https://github.com/MTES-MCT/potentiel/issues/4294).
- Suppression de l'adapter `getIdentifiantProjetFromLegacyId` et de la page de redirection legacy [#4338](https://github.com/MTES-MCT/potentiel/issues/4338).
- Suppression du script de migration des détails de candidature [#4337](https://github.com/MTES-MCT/potentiel/issues/4337).
- Suppression de l'adapter projets éligibles recandidature [#4354](https://github.com/MTES-MCT/potentiel/issues/4354).
- Suppression de l'adapter `getIdentifiantProjetFromLegacyId` et de la page de redirection legacy [#4338](https://github.com/MTES-MCT/potentiel/issues/4338).

### Autres changements
- Amélioration de la gestion des projets PPA et abandon.
- Correction de divers bugs et améliorations de la stabilité.
- Mise à jour des dépendances (hors mises à jour automatiques).
- Amélioration de la documentation et des tests.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de code obsolète.
- Ajout de types pour le fournisseur PV [#4290](https://github.com/MTES-MCT/potentiel/issues/4290).
- Ajout d'AO Petit PV [#4329](https://github.com/MTES-MCT/potentiel/issues/4329).
- Correction d'un flaky dans `corrigerCandidature` [#4319](https://github.com/MTES-MCT/potentiel/issues/4319).
- Amélioration de la gestion des projections GFS.
- Correction de divers problèmes d'affichage et de navigation.
