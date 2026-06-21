## Changelog : potentiel (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant la gestion des informations relatives aux producteurs, aux garanties financières et aux attestations de conformité. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la redirection vers la page appropriée après l'achèvement d'un projet non soumis [#4364](https://github.com/MTES-MCT/potentiel/issues/4364).
- Amélioration du formatage des coordonnées géodésiques pour une meilleure lisibilité [#4363](https://github.com/MTES-MCT/potentiel/issues/4363).
- Possibilité d'enregistrer un rapport associé lorsqu'une attestation de conformité existe déjà [#4360](https://github.com/MTES-MCT/potentiel/issues/4360).
- Correction de l'affichage des raccordements PTF [#4359](https://github.com/MTES-MCT/potentiel/issues/4359).
- Redirection après invitation à un projet éliminé [#4357](https://github.com/MTES-MCT/potentiel/issues/4357).
- Ajout de la possibilité pour les administrateurs et les DREAL de modifier les garanties financières en cours en cas de demande de mainlevée [#4345](https://github.com/MTES-MCT/potentiel/issues/4345).
- Amélioration de la navigation au clavier du composant Multiselect [#4346](https://github.com/MTES-MCT/potentiel/issues/4346).
- Ajout de la technologie aux exports des projets lauréats et éliminés [#4323](https://github.com/MTES-MCT/potentiel/issues/4323).
- Ajout de la possibilité pour les PP de corriger le numéro d'identification (SIRET/SIREN) [#4322](https://github.com/MTES-MCT/potentiel/issues/4322).
- Ajout d'une fonctionnalité permettant d'ouvrir un document sans le télécharger [#4068](https://github.com/MTES-MCT/potentiel/issues/4068).
- Ajout d'une instruction pour l'abandon d'un projet avec le choix de l'option PPA [#4260](https://github.com/MTES-MCT/potentiel/issues/4260).
- Possibilité pour le porteur de modifier l'attestation de conformité avec son rapport associé [#4264](https://github.com/MTES-MCT/potentiel/issues/4264).
- Ajout de l'autocomplétion du nom du producteur à partir du SIRET [#4266](https://github.com/MTES-MCT/potentiel/issues/4266).

### Évolutions techniques
- Intégration des dernières modifications de la version 3.82 [#4367](https://github.com/MTES-MCT/potentiel/issues/4367), 3.81 [#4314](https://github.com/MTES-MCT/potentiel/issues/4314) et 3.80 [#4312](https://github.com/MTES-MCT/potentiel/issues/4312).
- Simplification des readable streams [#4321](https://github.com/MTES-MCT/potentiel/issues/4321).
- Suppression de l'adapter projets éligibles recandidature [#4354](https://github.com/MTES-MCT/potentiel/issues/4354).
- Suppression de l'adapter getIdentifiantProjetFromLegacyId et de la page de redirection legacy [#4338](https://github.com/MTES-MCT/potentiel/issues/4338).
- Suppression du script de migration des détails de candidature [#4337](https://github.com/MTES-MCT/potentiel/issues/4337).
- Suppression de schémas et extensions PostgreSQL inutiles [#4336](https://github.com/MTES-MCT/potentiel/issues/4336).
- Mise à jour de la sécurité de la librairie `shell-quote` [#4324](https://github.com/MTES-MCT/potentiel/issues/4324).
- Mise à jour de `better-auth` en version 1.6.11 [#4284](https://github.com/MTES-MCT/potentiel/issues/4284).
- Correction du proxy withAuth [#4283](https://github.com/MTES-MCT/potentiel/issues/4283).

### Autres changements
- Amélioration de l'accessibilité des liens d'évitement [#4350](https://github.com/MTES-MCT/potentiel/issues/4350).
- Amélioration de la hiérarchie des titres pour l'accessibilité [#4348](https://github.com/MTES-MCT/potentiel/issues/4348).
- Correction de l'affichage des valeurs booléennes dans les filtres [#4355](https://github.com/MTES-MCT/potentiel/issues/4355).
- Ajout de types pour le fournisseur PV [#4290](https://github.com/MTES-MCT/potentiel/issues/4290).
- Correction de typos et améliorations diverses de l'interface utilisateur.
- Ajout de l'opérateur `between` pour les requêtes [#4349](https://github.com/MTES-MCT/potentiel/issues/4349).
- Ajout de l'AO Petit PV [#4329](https://github.com/MTES-MCT/potentiel/issues/4329).
- Ajout de la possibilité de forcer l'usage de Proconnect pour CRE et ADEME [#4327](https://github.com/MTES-MCT/potentiel/issues/4327).
- Correction de flaky tests [#4319](https://github.com/MTES-MCT/potentiel/issues/4319) et [#4351](https://github.com/MTES-MCT/potentiel/issues/4351).
